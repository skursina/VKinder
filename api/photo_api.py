from models.photo import Photo
from api.client import VKClient

class VKPhotoAPI:
    def __init__(self, client: VKClient):
        self.client = client

    def get_profile_photos(self, user_id: int) -> list[Photo]:
        # Здесь должна быть реализация получения фотографий пользователя из VK API
        pass

