from bitmovin.resources import Status, ResourceResponse

from bitmovin.errors import BitmovinApiError, InvalidStatusError

from bitmovin.resources.models import MP4Muxing as MP4MuxingResource
from bitmovin.resources.models.encodings.muxings.information import Mp4MuxingInformation
from .generic_muxing_service import GenericMuxingService


class MP4Muxing(GenericMuxingService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client, type_url='mp4', resource_class=MP4MuxingResource)

    def retrieve_information(self, encoding_id, muxing_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id)

        self.parsing_utils.check_arg_valid_uuid(argument=muxing_id)
        url = '{}/{}/information'.format(self.relative_url, muxing_id)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            retrieved_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response,
                class_=Mp4MuxingInformation)
            return ResourceResponse(response=response, resource=retrieved_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))
