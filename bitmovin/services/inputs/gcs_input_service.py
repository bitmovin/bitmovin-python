from bitmovin.resources.models import GCSInput
from ..rest_service import RestService
from .analyse_service import AnalyzeService


class GCS(RestService, AnalyzeService):
    BASE_ENDPOINT_URL = 'encoding/inputs/gcs'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=GCSInput)
