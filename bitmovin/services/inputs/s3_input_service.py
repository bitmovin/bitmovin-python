from bitmovin.resources.models import S3Input
from ..rest_service import RestService
from .analyse_service import AnalyzeService


class S3(RestService, AnalyzeService):
    BASE_ENDPOINT_URL = 'encoding/inputs/s3'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=S3Input)
