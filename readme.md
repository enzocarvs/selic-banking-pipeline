# Selic Banking Pipeline

## Requirements

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

Basic expected structure:

```txt
.
├── app/
│   ├── __init__.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── connection.py
│   └── models/
│       ├── __init__.py
│       └── selic.py
├── alembic/
│   ├── env.py
│   └── versions/
├── alembic.ini
└── README.md
```
## Creating a Migration

After creating or changing a model, generate a migration with:

```bash
alembic revision --autogenerate -m "create selic table"
```

Alembic will create a new file inside:

```txt
alembic/versions/
```

Always review the generated migration before applying it.

## Applying Migrations

To apply all pending migrations, run:

```bash
alembic upgrade head
```

This creates or updates the SQLite database schema.

## Checking Current Migration Version

```bash
alembic current
```

## Viewing Migration History

```bash
alembic history
```## Creating a Migration

After creating or changing a model, generate a migration with:

```bash
alembic revision --autogenerate -m "create selic table"
```

Alembic will create a new file inside:

```txt
alembic/versions/
```

Always review the generated migration before applying it.

## Applying Migrations

To apply all pending migrations, run:

```bash
alembic upgrade head
```

This creates or updates the SQLite database schema.

## Checking Current Migration Version

```bash
alembic current
```

## Viewing Migration History

```bash
alembic history
```
