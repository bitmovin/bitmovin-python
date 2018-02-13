from bitmovin.resources.models import AkamaiNetStorageOutput
from ..rest_service import RestService


class AkamaiNetStorage(RestService):
    BASE_ENDPOINT_URL = 'encoding/outputs/akamai-netstorage'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=AkamaiNetStorageOutput)
