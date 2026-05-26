import requests
import pandas as pd
from datetime import datetime

def fetch_bcb_series(codigo:int, nome:str, data_inicio:str, data_fim:str): 
    """
    Essa função busca uma série temporal na API do Banco Central, transforma a resposta JSON em um DataFrame do pandas, converte
    a coluna de data para datetime, converte os valores para número e retorna a tabela pronta para análise.

    Args:
        codigo: Código SGS da série.
        nome: Nome da coluna no DataFrame.
        data_inicio: Data inicial no formato dd/mm/yyyy.
        data_fim: Data final no formato dd/mm/yyyy.

    Returns:
        pandas.DataFrame: DataFrame contendo datas e valores da série.
    
    """
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