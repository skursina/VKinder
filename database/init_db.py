from database.db import Base, engine
from database import models 


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("База данных VKinder инициализирована.")
