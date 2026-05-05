import requests
import pandas as pd
from datetime import datetime

def fetch_bcb_series(codigo, nome, data_inicio, data_fim):
    url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados'
    params = {
    'formato': 'json',
    'dataInicial': data_inicio,
    'dataFinal': data_fim
    }
    response = requests.get(url, params=params)
    df = pd.DataFrame(response.json())
    df.columns = ['data', nome]
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    df[nome] = pd.to_numeric(df[nome])
    return df
    if __name__ == '__main__':