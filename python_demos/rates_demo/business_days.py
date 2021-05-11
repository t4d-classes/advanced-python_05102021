""" business days demo """

from datetime import timedelta, date
from collections.abc import Generator
import holidays

def business_days_list(sdate: date, edate: date) -> list[date]:
    """ get business days for start and end date inclusive """

    days = []

    us_holidays = holidays.UnitedStates()

    for num in range((edate - sdate).days + 1):
        the_date = sdate + timedelta(days=num)
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            days.append(the_date)

    return days

def business_days(sdate: date, edate: date
    ) -> Generator[date, None, None]:
    """ get business days for start and end date inclusive """

    us_holidays = holidays.UnitedStates()

    for num in range((edate - sdate).days + 1):
        the_date = sdate + timedelta(days=num)
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            yield the_date



if __name__ == "__main__":

    start_date = date(2021, 1, 1)
    end_date = date(2021, 3, 31)

    for business_day in business_days(start_date, end_date):
        print("in the loop")
        print(business_day)
