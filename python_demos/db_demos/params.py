""" db connection demo """

import pyodbc

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

        rates_id = 4

        sql = " ".join([
            "select RatesID, ClosingDate, CurrencySymbol, ExchangeRate",
            "from rates",
            "where RatesID = ?"])

        rates = con.execute(sql, (rates_id,))

        for rate in rates:
            print(rate)


if __name__ == "__main__":
    main()
