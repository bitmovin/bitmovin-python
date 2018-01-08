from bitmovin.resources.models import DenoiseHqdn3dFilter
from ..rest_service import RestService


class DenoiseHqdn3d(RestService):
    BASE_ENDPOINT_URL = 'encoding/filters/denoise-hqdn3d'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=DenoiseHqdn3dFilter)
