from prefect.blocks.system import String
from prefect import task, flow
from prefect.blocks import notifications
import requests

VANTAGE_API_KEY = None


@task
def set_alphavantage_apikey():
    key = String.load("alphavantage")
    assert key != None and key != ""
    global VANTAGE_API_KEY
    VANTAGE_API_KEY = key


@task
def get_stockdata(ticker):
    data = requests.get(
        "https://www.alphavantage.co/query",
        params={
            "function": "TIME_SERIES_INTRADAY",
            "symbol": ticker,
            "interval": "5min",
            "apikey": VANTAGE_API_KEY,
        },
    )
    data = data.json()
    return data


@flow
def lab103_do_analysis(ticker='IBM'):
    set_alphavantage_apikey()
    data = get_stockdata(ticker)
    last_updated = data["Meta Data"]["3. Last Refreshed"]
    print(last_updated)


if __name__ == "__main__":
    lab103_do_analysis()
