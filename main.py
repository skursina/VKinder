from config.settings import settings
from utils.logging_config import setup_logging

from bot.handlers import MessageHandler
from bot.bot import VKBot
from database.db import get_session
from database.init_db import init_db
from repositories.blacklist_repository import BlacklistRepository
from repositories.favorite_repository import FavoriteRepository
from repositories.history_repository import ViewHistoryRepository
from repositories.user_repository import UserRepository
from services.blacklist_service import BlacklistService
from services.search_service import SearchService
from services.favorite_service import FavoriteService
from services.photo_service import PhotoService
from services.user_service import UserService
from api.client import VKClient
from api.message_api import VKMessageAPI
from api.photo_api import VKPhotoAPI
from api.user_api import VKUserAPI


def build_handler():
    session = get_session()

    group_client = VKClient(settings.VK_GROUP_TOKEN)
    user_client = VKClient(settings.VK_USER_TOKEN)

    user_api = VKUserAPI(user_client)
    photo_api = VKPhotoAPI(user_client)
    message_api = VKMessageAPI(group_client)

    user_repository = UserRepository(session)
    favorite_repository = FavoriteRepository(session)
    blacklist_repository = BlacklistRepository(session)
    view_history_repository = ViewHistoryRepository(session)

    favorite_service = FavoriteService(favorite_repository, user_repository, view_history_repository)
    blacklist_service = BlacklistService(blacklist_repository, favorite_repository, user_repository, view_history_repository)
    user_service = UserService(user_api, user_repository)
    photo_service = PhotoService(photo_api)
    search_service = SearchService(
        user_service=user_service,
        user_api=user_api,
        photo_service=photo_service,
        favorite_repository=favorite_repository,
        blacklist_repository=blacklist_repository,
        view_history_repository=view_history_repository,
        user_repository=user_repository,
    )

    return MessageHandler(
        search_service=search_service,
        favorite_service=favorite_service,
        blacklist_service=blacklist_service,
        photo_service=photo_service,
        message_api=message_api
    )


def main() -> None:
    setup_logging()
    settings.validate()
    init_db()
    handler = build_handler()
    bot = VKBot(settings.VK_GROUP_TOKEN, handler)
    bot.run()


if __name__ == "__main__":
    main()
