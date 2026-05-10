from models.search_params import SearchParams
from repositories.blacklist_repository import BlacklistRepository
from repositories.favorite_repository import FavoriteRepository
from repositories.user_repository import UserRepository
from repositories.history_repository import ViewHistoryRepository
from services.user_service import UserService
from services.photo_service import PhotoService
from api.user_api import VKUserAPI


class SearchService:
    def __init__(self, 
                 user_repository: UserRepository, 
                 blacklist_repository: BlacklistRepository, 
                 favorite_repository: FavoriteRepository, 
                 view_history_repository: ViewHistoryRepository, 
                 user_service: UserService, 
                 photo_service: PhotoService, 
                 user_api: VKUserAPI):
        
        self.user_service = user_service
        self.user_api = user_api
        self.photo_service = photo_service
        self.favorite_repository = favorite_repository
        self.blacklist_repository = blacklist_repository
        self.view_history_repository = view_history_repository
        self.user_repository = user_repository
