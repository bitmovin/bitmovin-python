from bitmovin.resources.models import AC3CodecConfiguration
from ..rest_service import RestService


class AC3(RestService):
    BASE_ENDPOINT_URL = 'encoding/configurations/audio/ac3'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=AC3CodecConfiguration)
