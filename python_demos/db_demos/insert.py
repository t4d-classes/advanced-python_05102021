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

        sql = " ".join([
            "insert into Rates (ClosingDate, CurrencySymbol, ExchangeRate)",
            "values(?, ?, ?)"])

        # con.execute(sql, (date(2021, 2, 23), 'EUR', 1.12,))
        con.execute(sql, ('2021-02-23', 'EUR', 1.12,))



if __name__ == "__main__":
    main()
