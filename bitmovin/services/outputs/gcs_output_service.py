from bitmovin.resources.models import GCSOutput
from ..rest_service import RestService


class GCS(RestService):
    BASE_ENDPOINT_URL = 'encoding/outputs/gcs'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=GCSOutput)
