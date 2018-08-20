from bitmovin.resources.models import UnsharpFilter
from ..rest_service import RestService


class Unsharp(RestService):
    BASE_ENDPOINT_URL = 'encoding/filters/unsharp'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=UnsharpFilter)
