from bitmovin.resources.models import AV1CodecConfiguration
from ..rest_service import RestService


class AV1(RestService):
    BASE_ENDPOINT_URL = 'encoding/configurations/video/av1'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=AV1CodecConfiguration)
