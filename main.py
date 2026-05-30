from src.transform.transform import transform
from src.load.load import load_to_postgres

def run_pipeline():
    print('Iniciando pipeline...')
    
    print('Executando transform...')
    df = transform()
    
    print('Carregando dados no PostgreSQL...')
    load_to_postgres(df)
    
    print('Pipeline concluido com sucesso.')

if __name__ == '__main__':
    run_pipeline()
