from bitmovin.resources.models import H264CodecConfiguration
from ..rest_service import RestService


class H264(RestService):
    BASE_ENDPOINT_URL = 'encoding/configurations/video/h264'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=H264CodecConfiguration)
