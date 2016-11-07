from bitmovin.resources.models import WatermarkFilter
from ..rest_service import RestService


class Watermark(RestService):
    BASE_ENDPOINT_URL = 'encoding/filters/watermark'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=WatermarkFilter)
