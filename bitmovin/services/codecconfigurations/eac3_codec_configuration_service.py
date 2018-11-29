from bitmovin.resources.models import EAC3CodecConfiguration
from ..rest_service import RestService


class EAC3(RestService):
    BASE_ENDPOINT_URL = 'encoding/configurations/audio/eac3'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=EAC3CodecConfiguration)
