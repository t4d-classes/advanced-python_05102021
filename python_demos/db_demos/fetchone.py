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

        sql = "select * from Rates where ClosingDate = '2021-02-28'"

        with con.cursor() as cur:

            cur.execute(sql)

            rate = cur.fetchone()

            print(rate)



if __name__ == "__main__":
    main()
