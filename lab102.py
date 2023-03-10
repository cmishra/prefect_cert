import yfinance as yf
from prefect import flow, task
from datetime import timedelta, datetime


@task(cache_expiration=timedelta(seconds=120), retries=2)
def fetch_data():
    pd = yf.download("GOOG")
    assert pd.shape[0] > 0, "No data was downloaded"
    return pd


@task
def summary_stats(open_data):
    return {"max": open_data.max(), "min": open_data.min()}


@task
def forecast(model):
    n = model.forecast()
    return n


@flow
def analyze_data(pd):
    pd = pd[pd.index > datetime.fromisoformat("2022-12-31")]["Open"]
    summary = summary_stats(pd)
    print("Summary stats", summary)
    return


@flow
def do_analysis():
    res = fetch_data()
    print(res)
    # analyze_data(res)


if __name__ == "__main__":
    do_analysis()
