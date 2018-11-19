from bitmovin.resources.models import VorbisCodecConfiguration
from ..rest_service import RestService


class Vorbis(RestService):
    BASE_ENDPOINT_URL = 'encoding/configurations/audio/vorbis'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=VorbisCodecConfiguration)
