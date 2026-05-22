from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///app.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    from app.models.selic import Selic    

    db = SessionLocal()

    try:
        selic_test = Selic(
                year=2020,
                month=6,
                day=15,
                tax_value=0.54
            )

        db.add(selic_test)
        db.commit()
        db.refresh(selic_test)

        print(selic_test.year, selic_test.tax_value)
    finally:
        db.close()

