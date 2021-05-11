""" main module """

from datetime import date

import requests

from rates_demo.business_days import business_days

def get_rates(base_url: str) -> list[str]:
    """ get rates """

    start_date = date(2021, 1, 1)
    end_date = date(2021, 3, 31)
    rates: list[str] = []

    for business_day in business_days(start_date, end_date):
        rates_url = "".join([base_url, "/api/",
                             business_day.strftime("%Y-%m-%d"),
                             "?base=USD&symbols=EUR"])

        response = requests.request("GET", rates_url)
        rates.append(response.text)

    return rates