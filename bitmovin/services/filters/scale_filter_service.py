from bitmovin.resources.models import ScaleFilter
from ..rest_service import RestService


class Scale(RestService):
    BASE_ENDPOINT_URL = 'encoding/filters/scale'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=ScaleFilter)
