import os
from pathlib import Path
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent.parent / '.env')

def get_engine():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    name = os.getenv('DB_NAME')
    url = f'postgresql://{user}:{password}@{host}:{port}/{name}'
    return create_engine(url)

def load_to_postgres(df, tabela='indicadores_mensais'):
    engine = get_engine()
    df = df.copy()
    df['ano_mes'] = df['ano_mes'].astype(str)
    df.to_sql(tabela, engine, if_exists='replace', index=False)
    print(f'Tabela carregada com sucesso - {len(df)} linhas.')
