import yfinance as yf
import pandas as pd

from datetime import datetime

def fetch_stocks(tickers, data_inicio, data_fim):
    df = yf.download(tickers, start=data_inicio, end=data_fim)
    df = df['Close']