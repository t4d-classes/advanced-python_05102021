""" get rates module """

from concurrent.futures import ThreadPoolExecutor
from datetime import date
import threading

import requests

from rates_demo.business_days import business_days
import rates_demo.rates_orchestrator as ro

def get_rates(base_url: str) -> list[str]:
    """ get rates """

    start_date = date(2021, 1, 1)
    end_date = date(2021, 1, 31)
    rates: list[str] = []

    for business_day in business_days(start_date, end_date):
        rates_url = "".join([base_url, "/api/",
                             business_day.strftime("%Y-%m-%d"),
                             "?base=USD&symbols=EUR"])

        response = requests.request("GET", rates_url)
        rates.append(response.text)

    return rates


def get_rate_task(base_url: str, business_day: date) -> None:
    """ get rate for a single day from the rest api """

    rates_url = "".join([base_url, "/api/",
                             business_day.strftime("%Y-%m-%d"),
                             "?base=USD&symbols=EUR"])

    ro.process_rates_queue.put(requests.request("GET", rates_url).text)


def get_rates_threaded(base_url: str) -> None:
    """ get rates using multiple threads """

    start_date = date(2021, 1, 1)
    end_date = date(2021, 1, 31)
    threads: list[threading.Thread] = []

    for business_day in business_days(start_date, end_date):
        a_thread = threading.Thread(
            target=get_rate_task, args=(base_url, business_day))
        a_thread.start()
        threads.append(a_thread)

    for a_thread in threads:
        a_thread.join()

    ro.get_rates_done.set()


# def get_rates_threadpool(base_url: str) -> list[str]:
#     """ get rates using multiple threads """

#     start_date = date(2021, 1, 1)
#     end_date = date(2021, 1, 31)

#     with ThreadPoolExecutor() as executor:

#         return list(executor.map(
#             lambda params: get_rate_task(*params),
#             [ (base_url, business_day) for business_day
#                 in business_days(start_date, end_date)]
#         ))


