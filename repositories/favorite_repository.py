from database.models import FavoriteDB
from models.candidate import Candidate
from repositories.base import BaseRepository


class FavoriteRepository(BaseRepository):
    def add(self, user_vk_id: int, candidate: Candidate) -> None:
        self.session.add(FavoriteDB(
            user_vk_id=user_vk_id, 
            candidate_vk_id=candidate.vk_id,
            first_name=candidate.first_name,
            last_name=candidate.last_name,
            profile_url=candidate.profile_url,
            age=candidate.age,
            city_id=candidate.city_id,
        ))
        try:
            self.session.commit()
        except Exception:
            self.session.rollback()
            
    def get_all_by_user(self, user_vk_id: int) -> list[FavoriteDB]:
        return self.session.query(FavoriteDB).filter_by(user_vk_id=user_vk_id).all()
    
    def is_favorite(self, user_vk_id: int, candidate_vk_id: int) -> bool:
        return self.session.query(FavoriteDB).filter_by(
            user_vk_id=user_vk_id, 
            candidate_vk_id=candidate_vk_id
        ).one_or_none() is not None