from bitmovin.resources.models import MP3CodecConfiguration
from ..rest_service import RestService


class MP3(RestService):
    BASE_ENDPOINT_URL = 'encoding/configurations/audio/mp3'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=MP3CodecConfiguration)
