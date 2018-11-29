from bitmovin.resources.models import OpusCodecConfiguration
from ..rest_service import RestService


class Opus(RestService):
    BASE_ENDPOINT_URL = 'encoding/configurations/audio/opus'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=OpusCodecConfiguration)
