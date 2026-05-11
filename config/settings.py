from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    VK_GROUP_TOKEN = os.getenv("VK_GROUP_TOKEN")
    VK_USER_TOKEN = os.getenv("VK_USER_TOKEN")
    VK_GROUP_ID = os.getenv("VK_GROUP_ID")
    VK_API_VERSION = os.getenv("VK_API_VERSION")
    DB_CONFIG = {
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "database": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
    }

    def validate(self) -> None:
        if not self.VK_GROUP_TOKEN:
            raise ValueError("VK_GROUP_TOKEN не установлен")
        if not self.VK_USER_TOKEN:
            raise ValueError("VK_USER_TOKEN не установлен")
        if not self.VK_GROUP_ID:
            raise ValueError("VK_GROUP_ID не установлен")
        for key, value in self.DB_CONFIG.items():
            if not value:
                raise ValueError(f"Настройка базы данных '{key}' не установлена")


settings = Settings()
