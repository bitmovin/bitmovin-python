from bitmovin.resources.models import RotateFilter
from ..rest_service import RestService


class Rotate(RestService):
    BASE_ENDPOINT_URL = 'encoding/filters/rotate'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=RotateFilter)
