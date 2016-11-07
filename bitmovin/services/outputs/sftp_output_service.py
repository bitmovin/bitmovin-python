from bitmovin.resources.models import SFTPOutput
from ..rest_service import RestService


class SFTP(RestService):
    BASE_ENDPOINT_URL = 'encoding/outputs/sftp'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=SFTPOutput)
