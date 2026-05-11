from models.user import User
from repositories.user_repository import UserRepository
from api.user_api import VKUserAPI


class UserService:
    def __init__(self, user_api: VKUserAPI, user_repository: UserRepository):
        self.user_api = user_api
        self.user_repository = user_repository

    def get_or_create_user(self, user_vk_id: int) -> User:
        db_user = self.user_repository.get_by_vk_id(user_vk_id)
        if db_user:
            return db_user
        
        user = self.user_api.get_user_info(user_vk_id)
        self.user_repository.create(user) # Защитить от ошибки при сохранении в БД
        
        return user
    
    def load_user_info(self, user_vk_id: int) -> User:
        return self.user_api.get_user_info(user_vk_id)