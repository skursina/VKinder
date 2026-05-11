from models.candidate import Candidate
from repositories.favorite_repository import FavoriteRepository
from repositories.user_repository import UserRepository 
from repositories.history_repository import ViewHistoryRepository


class FavoriteService:
    def __init__(self, 
                 favorite_repository: FavoriteRepository, 
                 user_repository: UserRepository, 
                 view_history_repository: ViewHistoryRepository
                 ):
        
        self.favorite_repository = favorite_repository
        self.user_repository = user_repository
        self.view_history_repository = view_history_repository

    def add_current_user_to_favorite(self, user_vk_id: int, session_id: str = "default") -> bool:
        user_db = self.user_repository.get_by_vk_id(user_vk_id)
        if not user_db or not user_db.current_candidate_vk_id:
            return False
        
