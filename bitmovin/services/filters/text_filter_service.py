from bitmovin.resources.models import TextFilter
from ..rest_service import RestService


class Text(RestService):
    BASE_ENDPOINT_URL = 'encoding/filters/text'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=TextFilter)
