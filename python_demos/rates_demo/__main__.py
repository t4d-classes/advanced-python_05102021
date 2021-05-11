""" main module """

import time

from rates_demo.get_rates import get_rates, get_rates_threaded
from rates_demo.rates_api_server import rates_api_server

def display_message(msg: str) -> None:
    """ display a message of hope and love """
    print(msg)


if __name__ == "__main__":

    with rates_api_server():

        start = time.time()
        rates = get_rates("https://api.ratesapi.io")
        print("".join([
            "remote api: ",
            str(len(rates)),
            " requests in ",
            str(time.time() - start),
            " seconds"]))

        start = time.time()
        rates = get_rates_threaded("https://api.ratesapi.io")
        print("".join([
            "remote threaded api: ",
            str(len(rates)),
            " requests in ",
            str(time.time() - start),
            " seconds"]))

        start = time.time()
        rates = get_rates("http://127.0.0.1:5000")
        print("".join([
            "local api: ",
            str(len(rates)),
            " requests in ",
            str(time.time() - start),
            " seconds"]))

        start = time.time()
        rates = get_rates_threaded("http://127.0.0.1:5000")
        print("".join([
            "local threaded api: ",
            str(len(rates)),
            " requests in ",
            str(time.time() - start),
            " seconds"]))
