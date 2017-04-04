from bitmovin.resources.models import GenericS3Output
from ..rest_service import RestService


class GenericS3(RestService):
    BASE_ENDPOINT_URL = 'encoding/outputs/generic-s3'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=GenericS3Output)
