from models.candidate import Candidate
from repositories.blacklist_repository import BlacklistRepository
from repositories.user_repository import UserRepository
from repositories.history_repository import ViewHistoryRepository


class BlacklistService:
    def __init__(self, blacklist_repository: BlacklistRepository, user_repository: UserRepository, view_history_repository: ViewHistoryRepository):
        self.blacklist_repository = blacklist_repository
        self.user_repository = user_repository
        self.view_history_repository = view_history_repository