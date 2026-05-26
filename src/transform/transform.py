import pandas as pd
from datetime import datetime

from src.extract.bcb import fetch_bcb_series
from src.extract.stocks import fetch_stocks


def transform():
    data_inicio_bcb = '01/01/2020'
    data_fim_bcb = datetime.today().strftime('%d/%m/%Y')
    data_inicio_stocks = '2020-01-01'
    data_fim_stocks = datetime.today().strftime('%Y-%m-%d')

    selic = fetch_bcb_series(11, 'selic', data_inicio_bcb, data_fim_bcb)
    ipca = fetch_bcb_series(433, 'ipca', data_inicio_bcb, data_fim_bcb)
    cambio = fetch_bcb_series(1, 'cambio_usd', data_inicio_bcb, data_fim_bcb)
    stocks = fetch_stocks(['ITUB4.SA', 'BBDC4.SA', 'BBAS3.SA'], data_inicio_stocks, data_fim_stocks)

    selic['ano_mes'] = selic['data'].dt.to_period('M')
    cambio['ano_mes'] = cambio['data'].dt.to_period('M')
    ipca['ano_mes'] = ipca['data'].dt.to_period('M')
    stocks['ano_mes'] = stocks['Date'].dt.to_period('M')

    selic_mensal = selic.groupby('ano_mes')['selic'].mean().reset_index()
    cambio_mensal = cambio.groupby('ano_mes')['cambio_usd'].mean().reset_index()
    ipca_mensal = ipca.groupby('ano_mes')['ipca'].mean().reset_index()
    stocks_mensal = stocks.groupby('ano_mes')[['ITUB4.SA', 'BBDC4.SA', 'BBAS3.SA']].mean().reset_index()

    df = selic_mensal.merge(cambio_mensal, on='ano_mes')
    df = df.merge(ipca_mensal, on='ano_mes')
    df = df.merge(stocks_mensal, on='ano_mes')
    return df


if __name__ == '__main__':
    df = transform()
    print(df.head())