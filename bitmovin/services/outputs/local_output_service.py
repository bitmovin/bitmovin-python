from bitmovin.resources.models import LocalOutput
from ..rest_service import RestService


class Local(RestService):
    BASE_ENDPOINT_URL = 'encoding/outputs/local'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=LocalOutput)
