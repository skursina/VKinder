from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class User:
    vk_id: int
    first_name: str
    last_name: str
    sex: int | None = None
    city_id: int | None = None
    birth_date: date | None = None
