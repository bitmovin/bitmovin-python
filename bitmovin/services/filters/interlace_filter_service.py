from bitmovin.resources.models import InterlaceFilter
from ..rest_service import RestService


class Interlace(RestService):
    BASE_ENDPOINT_URL = 'encoding/filters/interlace'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=InterlaceFilter)
