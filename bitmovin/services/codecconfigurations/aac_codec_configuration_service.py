from bitmovin.resources.models import AACCodecConfiguration
from ..rest_service import RestService


class AAC(RestService):
    BASE_ENDPOINT_URL = 'encoding/configurations/audio/aac'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=AACCodecConfiguration)
