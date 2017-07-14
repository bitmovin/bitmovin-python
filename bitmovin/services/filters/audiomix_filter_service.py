from bitmovin.resources.models import DeinterlaceFilter, AudioMixFilter
from ..rest_service import RestService


class AudioMix(RestService):
    BASE_ENDPOINT_URL = 'encoding/filters/audio-mix'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=AudioMixFilter)
