FROM prefecthq/prefect:2-latest

RUN pip install yfinance statsmodels

COPY ./* /opt/prefect/flows/