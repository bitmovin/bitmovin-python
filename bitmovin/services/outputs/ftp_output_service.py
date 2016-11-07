from bitmovin.resources.models import FTPOutput
from ..rest_service import RestService


class FTP(RestService):
    BASE_ENDPOINT_URL = 'encoding/outputs/ftp'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=FTPOutput)
