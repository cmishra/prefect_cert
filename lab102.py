import yfinance as yf

import yfinance as yf
from prefect import flow, task
from datetime import timedelta, datetime
from statsmodels.tsa.arima.model import ARIMA


@task(cache_expiration=timedelta(seconds=120), retries=2)
def fetch_data():
    pd = yf.download("GOOG")
    assert pd.shape[0] > 0, "No data was downloaded"
    return pd


@task
def summary_stats(open_data):
    return {"max": open_data.max(), "min": open_data.min()}


@task
def arima_model(open_data):
    model = ARIMA(open_data)
    model_fitted = model.fit()
    return model_fitted


@task
def forecast(model):
    n = model.forecast()
    return n


@flow
def analyze_data(pd):
    pd = pd[pd.index > datetime.fromisoformat("2022-12-31")]["Open"]
    summary = summary_stats(pd)
    print("Summary stats", summary)
    model = arima_model(pd)
    n = forecast(model)
    print("Next forecast", n)
    return


@flow
def do_analysis():
    res = fetch_data()
    print(res)
    analyze_data(res)


if __name__ == "__main__":
    do_analysis()
