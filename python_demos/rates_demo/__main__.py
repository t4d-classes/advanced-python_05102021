""" main module """

import time

from rates_demo.get_rates import get_rates

def display_message(msg: str) -> None:
    """ display a message of hope and love """
    print(msg)


if __name__ == "__main__":

    start = time.time()
    get_rates("https://api.ratesapi.io")
    print(f"remote api: {time.time() - start}")

    # start = time.time()
    # get_rates("http://localhost:5000")
    # print(f"local api: {time.time() - start}")
