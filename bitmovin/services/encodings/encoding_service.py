from bitmovin.errors import BitmovinApiError, InvalidStatusError
from bitmovin.resources import Status, ResourceResponse
from bitmovin.resources.models import Encoding as EncodingResource
from bitmovin.resources.models import EncodingLiveDetails
from .encoding_control_service import EncodingControlService
from ..rest_service import RestService


class Encoding(RestService, EncodingControlService):
    BASE_ENDPOINT_URL = 'encoding/encodings'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=EncodingResource)

    def list(self, offset=None, limit=None):
        raise NotImplementedError('\'List all Encodings\' call is not implemented yet!')

    def retrieve_live(self, encoding_id):
        self.parsing_utils.check_arg_valid_uuid(encoding_id)
        url = self.relative_url + '/{}/live'.format(encoding_id)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)
        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(response=response,
                                                                                        class_=EncodingLiveDetails)
            return ResourceResponse(response=response, resource=created_resource)
        raise InvalidStatusError('Unknown status {} received'.format(response.status))

