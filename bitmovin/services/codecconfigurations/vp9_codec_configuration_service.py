from bitmovin.resources.models import VP9CodecConfiguration
from ..rest_service import RestService


class VP9(RestService):
    BASE_ENDPOINT_URL = 'encoding/configurations/video/vp9'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=VP9CodecConfiguration)
