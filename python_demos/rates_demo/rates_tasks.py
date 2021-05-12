""" rates tasks module """

import json
import queue
import csv
import pathlib

import rates_demo.rates_orchestrator as ro

def process_rate() -> None:
    """ process rate """

    while True:
        try:
            # getting the item off of the queue
            rate_json = ro.process_rates_queue.get(timeout=0.1)

            # processing of the item
            rate = json.loads(rate_json)
            rate_dict = {
                "date": rate["date"],
                "eur":  rate["rates"]["EUR"]
            }

            # putting of the processed item on to the next queue
            ro.save_rates_queue.put(rate_dict)

        except queue.Empty:
            if ro.get_rates_done.is_set():
                ro.process_rates_done.set()
                break
            else:
                continue


def save_rate() -> None:
    """ save rate """

    with open(pathlib.Path("output", "rates.csv"),
        "w", newline="\n") as rates_file:

        rates_csv = csv.writer(rates_file)

        while True:
            try:
                # getting the item off of the queue
                rate_dict = ro.save_rates_queue.get(timeout=0.1)

                # processing of the item
                rates_csv.writerow(rate_dict.values())

            except queue.Empty:
                if ro.process_rates_done.is_set():
                    break
                else:
                    continue
