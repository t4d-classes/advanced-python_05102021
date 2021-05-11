""" main module """

import time

from rates_demo.get_rates import get_rates

def display_message(msg: str) -> None:
    """ display a message of hope and love """
    print(msg)


if __name__ == "__main__":

    start = time.time()
    rates = get_rates("https://api.ratesapi.io")
    print("".join([
        "remote api: ",
        str(len(rates)),
        " requests in ",
        str(time.time() - start),
        " seconds"]))

    start = time.time()
    rates = get_rates("http://localhost:5000")
    print("".join([
        "local api: ",
        str(len(rates)),
        " requests in ",
        str(time.time() - start),
        " seconds"]))
