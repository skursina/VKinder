from models.photo import Photo
from api.photo_api import VKPhotoAPI


class PhotoService:
    def __init__(self, photo_api: VKPhotoAPI):
        self.photo_api = photo_api