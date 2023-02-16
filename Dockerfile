FROM --platform=amd64 prefecthq/prefect:2-latest

RUN pip install yfinance 

COPY ./* /opt/prefect/flows/