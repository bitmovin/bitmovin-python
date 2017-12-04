from bitmovin.resources.models import MJPEGCodecConfiguration
from ..rest_service import RestService


class MJPEG(RestService):
    BASE_ENDPOINT_URL = 'encoding/configurations/video/mjpeg'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=MJPEGCodecConfiguration)
