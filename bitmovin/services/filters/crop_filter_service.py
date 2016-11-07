from bitmovin.resources.models import CropFilter
from ..rest_service import RestService


class Crop(RestService):
    BASE_ENDPOINT_URL = 'encoding/filters/crop'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=CropFilter)
