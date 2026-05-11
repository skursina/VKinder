from database.models import UserDB
from models.user import User
from repositories.base import BaseRepository


class UserRepository(BaseRepository):
    def get_by_vk_id(self, vk_id: int) -> UserDB | None:
        return self.session.query(UserDB).filter(UserDB.vk_id == vk_id).one_or_none()
    
    def create(self, user: User) -> UserDB:
        user_db = UserDB(**user.dict())
        self.session.add(user_db)
        self.session.commit()
        self.session.refresh(user_db)
        return user_db
    
    def set_current_candidate(self, user_vk_id: int, candidate_vk_id: int | None) -> None:
        user_db = self.get_by_vk_id(user_vk_id)
        if user_db:
           user_db.current_candidate_vk_id = candidate_vk_id
           self.session.commit()    