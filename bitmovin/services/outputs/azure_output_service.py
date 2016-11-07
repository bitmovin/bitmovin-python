from bitmovin.resources.models import AzureOutput
from ..rest_service import RestService


class Azure(RestService):
    BASE_ENDPOINT_URL = 'encoding/outputs/azure'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=AzureOutput)
