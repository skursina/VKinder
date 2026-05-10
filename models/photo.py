from dataclasses import dataclass


@dataclass(slots=True)
class Photo:
    owner_id: int
    photo_id: int
    likes_count: int = 0

    def to_attachment(self) -> str:
        return f"photo{self.owner_id}_{self.photo_id}"
