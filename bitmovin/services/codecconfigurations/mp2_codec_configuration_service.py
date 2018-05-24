from bitmovin.resources.models import MP2CodecConfiguration
from ..rest_service import RestService


class MP2(RestService):
    BASE_ENDPOINT_URL = 'encoding/configurations/audio/mp2'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=MP2CodecConfiguration)
