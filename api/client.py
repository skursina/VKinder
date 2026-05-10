import logging
import requests

logger = logging.getLogger(__name__)


class VKClient:
    API_URL = "https://api.vk.com/method/"
    
    def __init__(self, token: str):
        self.token = token

    def call_method(self, method: str, params: dict) -> dict:
        pass