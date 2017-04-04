from bitmovin.resources.models import GenericS3Input
from ..rest_service import RestService
from .analyse_service import AnalyzeService


class GenericS3(RestService, AnalyzeService):
    BASE_ENDPOINT_URL = 'encoding/inputs/generic-s3'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=GenericS3Input)
