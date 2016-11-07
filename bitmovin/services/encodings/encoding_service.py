from bitmovin.resources.models import Encoding as EncodingResource
from .encoding_control_service import EncodingControlService
from ..rest_service import RestService


class Encoding(RestService, EncodingControlService):
    BASE_ENDPOINT_URL = 'encoding/encodings'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=EncodingResource)

    def list(self, offset=None, limit=None):
        raise NotImplementedError('\'List all Encodings\' call is not implemented yet!')

    def retrieve_live(self, id_):
        raise NotImplementedError('\'Live Encoding Details\' call is not implemented yet!')
