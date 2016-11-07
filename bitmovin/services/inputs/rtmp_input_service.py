from bitmovin.errors import FunctionalityNotAvailableError
from bitmovin.resources.models import RTMPInput
from ..rest_service import RestService


class RTMP(RestService):
    BASE_ENDPOINT_URL = 'encoding/inputs/rtmp'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=RTMPInput)

    def create(self, object_):
        raise FunctionalityNotAvailableError('functionality "create" is not available for RTMP inputs')

    def delete(self, id_):
        raise FunctionalityNotAvailableError('functionality "delete" is not available for RTMP inputs')

    def retrieve_custom_data(self, id_):
        raise FunctionalityNotAvailableError('functionality "retrieve_custom_data" is not available for RTMP inputs')

