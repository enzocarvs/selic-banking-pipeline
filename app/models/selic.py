from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Selic(Base):
    __tablename__ = "selic"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    month: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )


    day: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    tax_value: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

