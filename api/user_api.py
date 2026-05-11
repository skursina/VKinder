from models.user import User
from models.candidate import Candidate
from models.search_params import SearchParams
from api.client import VKClient


class VKUserAPI:
    def __init__(self, client: VKClient):
        self.client = client

    def get_user_info(self, user_id: int) -> User:
        # Здесь должна быть реализация получения информации о пользователе из VK API
        pass
    
    def search_candidates(self, search_params: SearchParams) -> list[Candidate]:
        # Здесь должна быть реализация поиска кандидатов в VK API на основе переданных параметров
        pass