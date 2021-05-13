""" db connection demo """

import pyodbc
from datetime import date

docker_conn_options = [
    "DRIVER={ODBC Driver 17 for SQL Server}",
    "SERVER=localhost,1433",
    "DATABASE=ratesapp",
    "UID=sa",
    "PWD=sqlDbp@ss!",
]

def main() -> None:
    """ main """

    with pyodbc.connect(";".join(docker_conn_options)) as con:

        rates = [
            ('2021-02-23', 'EUR', 1.12,),
            ('2021-02-24', 'EUR', 1.11,),
            ('2021-02-25', 'EUR', 1.13,),
            ('2021-02-26', 'EUR', 1.14,),
        ]

        sql = " ".join([
            "insert into Rates (ClosingDate, CurrencySymbol, ExchangeRate)",
            "values(?, ?, ?)"])

        with con.cursor() as cur:
            cur.executemany(sql, rates)



if __name__ == "__main__":
    main()
