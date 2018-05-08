from bitmovin.resources.models import AACCodecConfiguration, HeAACv1CodecConfiguration, HeAACv2CodecConfiguration
from ..rest_service import RestService


class AAC(RestService):
    BASE_ENDPOINT_URL = 'encoding/configurations/audio/aac'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=AACCodecConfiguration)


class HeAACv1(RestService):
    BASE_ENDPOINT_URL = 'encoding/configurations/audio/he-aac-v1'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=HeAACv1CodecConfiguration)


class HeAACv2(RestService):
    BASE_ENDPOINT_URL = 'encoding/configurations/audio/he-aac-v2'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=HeAACv2CodecConfiguration)
