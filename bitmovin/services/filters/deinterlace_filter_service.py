from bitmovin.resources.models import DeinterlaceFilter
from ..rest_service import RestService


class Deinterlace(RestService):
    BASE_ENDPOINT_URL = 'encoding/filters/deinterlace'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=DeinterlaceFilter)
