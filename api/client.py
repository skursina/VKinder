import logging
import requests

logger = logging.getLogger(__name__)


class VKClient:
    API_URL = "https://api.vk.com/method/"
    
    def __init__(self, token: str, api_version: str):
        self.token = token
        self.api_version = api_version

    def call_method(self, method: str, params: dict) -> dict:
        payload = params.copy() if params else {}
        payload.update({"access_token": self.token, "v": self.api_version})
        response = requests.get(f"{self.API_URL}{method}", params=payload, timeout=15)
        response.raise_for_status()
        data = response.json()
        if "error" in data:
            logger.error("VK API error: %s", data["error"])
#            raise VKApiError(data["error"].get("error_msg", "VK API error"))

        return data.get("response", {})        