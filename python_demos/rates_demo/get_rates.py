""" get rates module """

from concurrent.futures import ThreadPoolExecutor
from datetime import date

import requests

from rates_demo.business_days import business_days

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

def get_rate_task(base_url: str, business_day: date, rates: list[str]) -> None:
    """ get rate for a single day from the rest api """

    rates_url = "".join([base_url, "/api/",
                             business_day.strftime("%Y-%m-%d"),
                             "?base=USD&symbols=EUR"])

    response = requests.request("GET", rates_url)
    rates.append(response.text)

def get_rates_threaded(base_url: str) -> list[str]:
    """ get rates using multiple threads """

    start_date = date(2021, 1, 1)
    end_date = date(2021, 1, 31)
    rates: list[str] = []

    with ThreadPoolExecutor() as executor:

        executor.map(
            lambda params: get_rate_task(*params),
            [ (base_url, business_day, rates) for business_day
                in business_days(start_date, end_date)]
        )

    return rates
