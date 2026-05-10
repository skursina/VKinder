from dataclasses import dataclass


@dataclass(slots=True)
class Candidate:
    vk_id: int
    first_name: str
    last_name: str
    profile_url: str
    age: int | None = None
    city_id: int | None = None
