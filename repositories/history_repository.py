from database.models import ViewHistoryDB
from models.candidate import Candidate
from repositories.base import BaseRepository

class ViewHistoryRepository(BaseRepository):
    def add(self, user_vk_id: int, candidate: Candidate, session_id: str = 'default') -> None:
        record = ViewHistoryDB(
            user_vk_id=user_vk_id,
            candidate_vk_id=candidate.vk_id,
            session_id=session_id,
            first_name=candidate.first_name,
            last_name=candidate.last_name,
            profile_url=candidate.profile_url,
            age=candidate.age,
            city_id=candidate.city_id,
        )
        self.session.add(record)
        try:
            self.session.commit()
        except Exception:
            self.session.rollback()
