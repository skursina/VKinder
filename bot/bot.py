"""
Основной модуль для работы бота.

"""
import logging
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


logger = logging.getLogger(__name__)


class VKBot:
    def __init__(self, group_token: str, message_handler):
        self.group_token = group_token
        self.message_handler = message_handler

    def run(self):
        pass
    
