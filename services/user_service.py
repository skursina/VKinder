from models.user import User
from repositories.user_repository import UserRepository
from api.user_api import VKUserAPI


class UserService:
    def __init__(self, user_api: VKUserAPI, user_repository: UserRepository):
        self.user_api = user_api
        self.user_repository = user_repository