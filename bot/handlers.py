from bot import commands
from bot.keyboards import KeyboardFactory
import logging

logger = logging.getLogger(__name__)

class MessageHandler:
    def __init__(self, search_service, favorite_service, blacklist_service, photo_service, message_api):
        self.search_service = search_service
        self.favorite_service = favorite_service
        self.blacklist_service = blacklist_service
        self.photo_service = photo_service
        self.message_api = message_api

    def handle_message(self, user_id: int, text: str) -> None:
        normalized = text.strip().lower()
        try:
            if normalized in commands.START:
                self.handle_start(user_id)
            elif normalized in commands.HELP:
                self.handle_help(user_id)
            else:
                self.handle_unknown(user_id)
        except Exception as e:
            logger.error(f"Error in handling message for user {user_id}: {e}")
    
    def handle_start(self, user_id: int) -> None:
        self.message_api.send_message(
            user_id,
            "Привет! Я VKinder, Нажми «Найти пару», чтобы начать поиск!",
            KeyboardFactory.main_menu(),
        )
    
    def handle_help(self, user_id: int) -> None:
        self.message_api.send_message(
            user_id,
            "Команды: /search, /next, /favorite, /favorites, /blacklist.",
            KeyboardFactory.main_menu(),
        )    

    def handle_unknown(self, user_id: int) -> None:
        self.message_api.send_message(user_id, "Не понял команду. Нажмите кнопку или используйте /help.", KeyboardFactory.main_menu())
