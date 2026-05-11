import logging
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


logger = logging.getLogger(__name__)


class VKBot:
    def __init__(self, group_token: str, group_id: str, message_handler):
        self.group_token = group_token
        self.group_id = group_id    
        self.message_handler = message_handler

    def run(self):
        vk_session = vk_api.VkApi(token=self.group_token)
        vk = vk_session.get_api()
        botlongpoll = VkBotLongPoll(vk_session, group_id=self.group_id)
        logger.info("VKinder запущен. Ожидание сообщений...")

        for event in botlongpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
                self.process_event(event)
        
    def process_event(self, event)-> None:
        message = event.obj.message
        user_id = message['from_id']
        text = message['text']
        self.message_handler.handle_message(user_id=user_id, text=text)