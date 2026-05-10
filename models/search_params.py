from dataclasses import dataclass


@dataclass(slots=True)
class SearchParams:
    sex: int
    age_from: int
    age_to: int
    city_id: int | None = None
    count: int = 30
    offset: int = 0
