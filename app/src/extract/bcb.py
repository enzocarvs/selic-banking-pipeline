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
    SELIC = 11
    IPCA = 433
    CAMBIO = 1
    
    data_inicio = '01/01/2020'
    data_fim = datetime.today().strftime('%d/%m/%Y')

    print('Buscando Selic...')
    selic = fetch_bcb_series(SELIC, 'selic', data_inicio, data_fim)
    print(selic.head())

    print('Buscando IPCA...')
    ipca = fetch_bcb_series(IPCA, 'ipca', data_inicio, data_fim)
    print(ipca.head())

    print('Buscando Câmbio...')
    cambio = fetch_bcb_series(CAMBIO, 'cambio_usd', data_inicio, data_fim)
    print(cambio.head())