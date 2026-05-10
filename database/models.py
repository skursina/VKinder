"""
ORM-модели для БД.
"""

from datetime import datetime, date
from sqlalchemy import Integer, String, BigInteger, Text, DateTime, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column

from database.db import Base

class UserDB(Base):
    """Пользователь VK, который начал диалог с ботом."""
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    vk_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, index=True)
    first_name: Mapped[str | None] = mapped_column(String(100))
    last_name: Mapped[str | None] = mapped_column(String(100))
    sex: Mapped[int | None] = mapped_column(Integer)
    city_id: Mapped[int | None] = mapped_column(Integer)
    birth_date: Mapped[date | None] = mapped_column(Date)

    # Состояние текущего диалога: последний показанный кандидат.
    current_candidate_vk_id: Mapped[int | None] = mapped_column(BigInteger)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class FavoriteDB(Base):
    """Кандидаты, которых пользователь добавил в избранное."""

    __tablename__ = "favorites"
    __table_args__ = (
        UniqueConstraint("user_vk_id", "candidate_vk_id", name="uq_favorite_user_candidate"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_vk_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True)
    candidate_vk_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True)
    first_name: Mapped[str | None] = mapped_column(String(100))
    last_name: Mapped[str | None] = mapped_column(String(100))
    profile_url: Mapped[str | None] = mapped_column(Text)
    age: Mapped[int | None] = mapped_column(Integer)
    city_id: Mapped[int | None] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class BlacklistDB(Base):
    """Кандидаты, которые были показаны пользователю, но не выбраны в избранное."""

    __tablename__ = "blacklist"
    __table_args__ = (
        UniqueConstraint("user_vk_id", "candidate_vk_id", name="uq_blacklist_user_candidate"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_vk_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True)
    candidate_vk_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True)
    first_name: Mapped[str | None] = mapped_column(String(100))
    last_name: Mapped[str | None] = mapped_column(String(100))
    profile_url: Mapped[str | None] = mapped_column(Text)
    age: Mapped[int | None] = mapped_column(Integer)
    city_id: Mapped[int | None] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class ViewHistoryDB(Base):
    """История кандидатов, показанных пользователю в рамках сессии поиска."""

    __tablename__ = "view_history"
    __table_args__ = (
        UniqueConstraint("user_vk_id", "candidate_vk_id", "session_id", name="uq_view_user_candidate_session"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_vk_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True)
    candidate_vk_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True)
    session_id: Mapped[str] = mapped_column(String(64), nullable=False, default="default", index=True)
    first_name: Mapped[str | None] = mapped_column(String(100))
    last_name: Mapped[str | None] = mapped_column(String(100))
    profile_url: Mapped[str | None] = mapped_column(Text)
    age: Mapped[int | None] = mapped_column(Integer)
    city_id: Mapped[int | None] = mapped_column(Integer)
    viewed_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)    