"""
Создать подключение к БД. Создать фабрику сессий. Дать другим уровням доступ к сессии БД.
"""

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config.settings import settings


class Base(DeclarativeBase):
    """Базовый класс для всех моделей SQLAlchemy."""
    pass


def build_db_url() -> URL:
    """
    Собирает строку подключения к PostgreSQL из settings.DB_CONFIG.
    """
    settings.validate()

    return URL.create(
        drivername="postgresql+psycopg2",
        username=settings.DB_CONFIG['user'],
        password=settings.DB_CONFIG['password'],
        host=settings.DB_CONFIG['host'],
        port=settings.DB_CONFIG['port'],
        database=settings.DB_CONFIG['database']
    )


engine = create_engine(build_db_url(), echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

def get_session():
    return SessionLocal()