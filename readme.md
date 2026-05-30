# Selic Banking Pipeline

Pipeline de dados que responde à pergunta: **como variações na Selic, IPCA e câmbio impactam o desempenho das principais ações bancárias brasileiras?**

Os dados são coletados automaticamente, transformados e armazenados em um banco PostgreSQL, prontos para análise e visualização.

---

## Visão Geral

Esse projeto implementa um pipeline ETL completo voltado ao mercado financeiro brasileiro:

- **Extract** — coleta indicadores macroeconômicos do Banco Central do Brasil (BCB) e cotações históricas de ações via yfinance
- **Transform** — limpa, agrega mensalmente e cruza os dados em um único DataFrame
- **Load** — salva os dados transformados em um banco PostgreSQL

### Indicadores coletados

| Fonte | Dados |
|-------|-------|
| BCB (API pública) | Taxa Selic, IPCA, Câmbio USD/BRL |
| yfinance | ITUB4.SA, BBDC4.SA, BBAS3.SA |

Período: janeiro de 2020 até a data de execução.

---

## Estrutura do Projeto

```
selic-banking-pipeline/
├── src/
│   ├── extract/
│   │   ├── bcb.py          # Coleta dados do Banco Central
│   │   └── stocks.py       # Coleta cotações via yfinance
│   ├── transform/
│   │   └── transform.py    # Limpeza, agregação mensal e merge
│   └── load/
│       └── load.py         # Salva os dados no PostgreSQL
├── notebooks/              # Análises exploratórias
├── tests/                  # Testes automatizados
├── main.py                 # Orquestrador do pipeline
├── .env.example            # Modelo de variáveis de ambiente
├── requirements.txt
└── README.md
```

---

## Pré-requisitos

- Python 3.11+
- PostgreSQL 18+
- Conda (recomendado)

---

## Instalação

**1. Clone o repositório**

```bash
git clone https://github.com/enzocarvs/selic-banking-pipeline.git
cd selic-banking-pipeline
```

**2. Crie e ative o ambiente**

```bash
conda create -n banking-pipeline python=3.11
conda activate banking-pipeline
```

**3. Instale as dependências**

```bash
pip install -r requirements.txt
```

**4. Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

```
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
DB_NAME=selic_banking
```

**5. Crie o banco de dados**

No PostgreSQL, crie um banco chamado `selic_banking`. Isso pode ser feito via pgAdmin ou pelo terminal:

```bash
psql -U postgres -c "CREATE DATABASE selic_banking;"
```

---

## Executando o Pipeline

Com o ambiente ativado e o banco configurado, rode:

```bash
python main.py
```

O pipeline vai:
1. Buscar os dados do BCB e do yfinance
2. Agregar e cruzar os indicadores mensalmente
3. Salvar a tabela `indicadores_mensais` no PostgreSQL

Exemplo de saída esperada:

```
Iniciando pipeline...
Executando transform...
3 of 3 completed
Carregando dados no PostgreSQL...
Tabela carregada com sucesso - 76 linhas.
Pipeline concluído com sucesso.
```

---

## Tecnologias

- **Python 3.11**
- **pandas** — manipulação e transformação de dados
- **requests** — chamadas à API do BCB
- **yfinance** — dados históricos de ações
- **SQLAlchemy** — conexão e escrita no PostgreSQL
- **psycopg2** — driver PostgreSQL
- **python-dotenv** — gerenciamento de variáveis de ambiente
- **PostgreSQL 18** — armazenamento dos dados transformados