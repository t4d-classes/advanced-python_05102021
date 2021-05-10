""" date format module """

from datetime import date, datetime

independence_day = date(1776, 7, 4)

print(independence_day)
print(type(independence_day))

print(datetime.now())
print(datetime.now().strftime("%B %A"))

TAX_DAY_STR = "2021-05-17"

tax_day = datetime.strptime(TAX_DAY_STR, "%Y-%m-%d")

print(tax_day)
print(type(tax_day))
