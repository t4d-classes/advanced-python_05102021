""" rates api module """

from flask import Flask

app = Flask(__name__)

@app.route("/check")
def check() -> str:
    """ health check route function """
    return "READY"


def start_rates_api() -> None:
    """ start rates api rest server """

    app.run()

if __name__ == "__main__":
    start_rates_api()
