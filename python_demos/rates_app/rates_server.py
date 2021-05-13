""" rate server module """

from typing import Optional, Any
from multiprocessing.sharedctypes import Synchronized
import multiprocessing as mp
import sys
import socket
import threading
import re
import json
import requests

# Task 1 - Cache Rate Results

# Upgrade the application to check the database for a given exchange rate
# (year, currency)

# If the exchange rate was previously retrieved and stored in the
# database, then return it

# If the exchange rate is not in the database, then download it, add it to
# the database and return it

# Task 2 - Clear Rate Cache

# Add a command for clearing the rate cache from the server command
# prompt. Name the command "clear".

# Task 3 - Add support for getting multiple rates using the following
# example command structures. Be sure to implement caching.

# GET 2021-04-01 CAD,EUR,RUB
# GET 2021-04-01 CAD;EUR;RUB
# GET 2021-04-01 CAD|EUR|RUB
# GET 2021-04-01 CAD:EUR;RUB
# GET 2021-04-01 CAD|EUR:RUB

# From the examples above, observe how the separator for the symbols can
# be ":", ";", "|", or ",". In any combination. Consider using some of the
# Regex examples we reviewed in class.

# Hint: Public API can be called like this:
# https://api.ratesapi.io/api/2010-01-12?base=USD&symbols=EUR,GBP

# Hint: To add multiple cache entries, consider using the execute many API

# Bonus Challenge: When calling the Public Rates API server, only pass one
# symbol in the URL, if multiple symbols are needed, then call the Rates API
# multiple times using a ThreadPoolExecutor.

# Task 4 - YAML Config Files

# Add server and client yaml configuration files for storing the host
# and port. Both the server and client yaml files should have the same
# structure. The host and port for server config is used for "bind" and
# for the client config is used for "connect". Also, store the database
# connection information in the server yaml configuration file

# Task 5: Client Connection CSV Log

# On the server, on each client connection and disconnection, record
# information about the connection in a CSV log with the following structure.

# The host and the port are the client's host and port

# The addr will contain the client host and port
# conn, addr = socket_server.accept()

# <thread_id>,<date>,<host>,<port>,connect
# <thread_id>,<date>,<host>,<port>,disconnect


CLIENT_COMMAND_PARTS = [
    r"^(?P<name>[A-Z]*) ",
    r"(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2}) ",
    r"(?P<symbol>[A-Z]{3})$",
]

CLIENT_COMMAND_REGEX = re.compile("".join(CLIENT_COMMAND_PARTS))


class ClientConnectionThread(threading.Thread):
    """ client connection thread class """

    def __init__(self, conn: socket.socket, client_count: Synchronized) -> None:
        threading.Thread.__init__(self)
        self.conn = conn
        self.client_count = client_count

    def run(self) -> None:

        with self.client_count.get_lock():
            self.client_count.value += 1

        self.conn.sendall(b"Connected to the Rate Server.")

        try:
            while True:
                data = self.conn.recv(2048)
                if not data:
                    break
                
                client_command_str = data.decode('UTF-8')

                client_command_match = CLIENT_COMMAND_REGEX.match(
                    client_command_str)

                if not client_command_match:
                    self.conn.sendall(b"Invalid Command Format")
                else:
                    self.process_client_command(
                        client_command_match.groupdict())

        except OSError:
            pass

        with self.client_count.get_lock():
            self.client_count.value -= 1


    def process_client_command(self, client_command: dict[str, Any]) -> None:
        """ process client command """

        if client_command["name"] == "GET":

            url = "".join([
                "https://api.ratesapi.io/api/",
                client_command["date"],
                "?base=USD&symbols=",
                client_command["symbol"]
            ])

            response = requests.request("GET", url)
            rate_data = json.loads(response.text)

            self.conn.sendall(
                str(rate_data["rates"][client_command["symbol"]])
                    .encode("UTF_8")
            )

        else:
            self.conn.sendall(b"Unknown Command Name")



def rate_server(client_count: Synchronized) -> None:
    """rate server"""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server:

        socket_server.bind(('127.0.0.1', 5000))
        socket_server.listen()

        while True:

            conn, _ = socket_server.accept()

            client_con_thread = ClientConnectionThread(conn, client_count)
            client_con_thread.start()




class RateServerError(Exception):
    """ rate server error class """


def command_start_server(server_process: Optional[mp.Process],
    client_count: Synchronized) -> mp.Process:
    """ command start server """

    if server_process and server_process.is_alive():
        print("server is already running")
    else:
        server_process = mp.Process(target=rate_server, args=(client_count,))
        server_process.start()
        print("server started")

    return server_process


def command_stop_server(
    server_process: Optional[mp.Process]) -> Optional[mp.Process]:
    """ command stop server """

    if not server_process or not server_process.is_alive():
        print("server is not running")
    else:
        server_process.terminate()
        print("server stopped")

    server_process = None

    return server_process


def command_server_status(server_process: Optional[mp.Process]) -> None:
    """ outputs the status of the server """

    if server_process and server_process.is_alive():
        print("server is running")
    else:
        print("server is stopped")


def command_exit(server_process: Optional[mp.Process]) -> None:
    """ clean up resources for exit """

    if server_process and server_process.is_alive():
        server_process.terminate()

def command_client_count(client_count: int) -> None:
    """ display the current client count """

    print(f"client count: {client_count}")



def main() -> None:
    """Main Function"""

    try:

        client_count: Synchronized = mp.Value('i', 0)
        server_process: Optional[mp.Process] = None

        while True:

            command = input("> ")

            if command == "start":
                server_process = command_start_server(
                    server_process, client_count)
            elif command == "stop":
                server_process = command_stop_server(server_process)
            elif command == "status":
                command_server_status(server_process)
            elif command == "count":
                command_client_count(client_count.value)
            elif command == "exit":
                command_exit(server_process)
                break

    except KeyboardInterrupt:
        command_exit(server_process)

    sys.exit(0)


if __name__ == '__main__':
    main()
