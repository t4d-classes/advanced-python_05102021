""" rate client module """
import sys
import socket

try:

    # implement socket client
    # the host and port should be received as parameters into this function

    # - use "AF_INET" for IPv4
    # - use "SOCK_STREAM" for TCP

    # connect to localhost and port 5000 using the context manager

    # print the welcome message from the server

    # display a command prompt, allow the user to enter text

    # send the user entered text to the server, then receive the response
    # and output the response to the console

    # when a connection reset occurs (you may need to look this up),
    # display the following message
    #     "Server connection was closed.""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_client:

        socket_client.connect(('127.0.0.1', 5000))

        welcome_message = socket_client.recv(2048)

        print(welcome_message.decode("UTF-8"))

        while True:

            command = input("> ")

            if command == "exit":
                break
            else:
                socket_client.sendall(command.encode("UTF-8"))
                message = socket_client.recv(2048)
                print(message.decode("UTF-8"))

except ConnectionResetError:
    print("Server connection was closed.")
except KeyboardInterrupt:
    pass

sys.exit(0)
