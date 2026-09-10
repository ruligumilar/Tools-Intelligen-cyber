from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Personel(Base):
    __tablename__ = "personel"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    nrp: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
        index=True
    )

    nama: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    pangkat: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    korps: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    jabatan: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True
    )

    kompi: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="aktif"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    role: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="viewer"
    )

    is_active: Mapped[bool] = mapped_column(
        default=True,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )