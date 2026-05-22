import yfinance as yf
import pandas as pd
from datetime import datetime


def fetch_stocks(tickers, data_inicio, data_fim):
    df = yf.download(tickers, start=data_inicio, end=data_fim)
    df = df['Close']
    df = df.reset_index()
    return df


if __name__ == '__main__':
    TICKERS = ['ITUB4.SA', 'BBDC4.SA', 'BBAS3.SA']

    data_inicio = '2020-01-01'
    data_fim = datetime.today().strftime('%Y-%m-%d')

    print('Buscando ações...')
    stocks = fetch_stocks(TICKERS, data_inicio, data_fim)
    print(stocks.head())