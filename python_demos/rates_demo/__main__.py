""" main module """

import time
from threading import Thread

from rates_demo.get_rates import get_rates_threaded
from rates_demo.rates_api_server import rates_api_server
from rates_demo.rates_tasks import process_rate, save_rate

def display_message(msg: str) -> None:
    """ display a message of hope and love """
    print(msg)


if __name__ == "__main__":

    with rates_api_server():

        start = time.time()
        get_rates_threaded("http://127.0.0.1:5000")

        process_rates_thread = Thread(target=process_rate)
        process_rates_thread.start()

        save_rates_thread = Thread(target=save_rate)
        save_rates_thread.start()

        process_rates_thread.join()
        save_rates_thread.join()

        print(f"execution time: {time.time() - start}")










        # start = time.time()
        # rates = get_rates("https://api.ratesapi.io")
        # print("".join([
        #     "remote api: ",
        #     str(len(rates)),
        #     " requests in ",
        #     str(time.time() - start),
        #     " seconds"]))

        # start = time.time()
        # rates = get_rates_threaded("https://api.ratesapi.io")
        # print("".join([
        #     "remote threaded api: ",
        #     str(len(rates)),
        #     " requests in ",
        #     str(time.time() - start),
        #     " seconds"]))

        # start = time.time()
        # rates = get_rates("http://127.0.0.1:5000")
        # print("".join([
        #     "local api: ",
        #     str(len(rates)),
        #     " requests in ",
        #     str(time.time() - start),
        #     " seconds"]))

