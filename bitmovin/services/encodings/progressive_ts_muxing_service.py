from bitmovin.errors import BitmovinApiError, InvalidStatusError
from bitmovin.resources import ResourceResponse, Status
from bitmovin.resources.models import ProgressiveTSMuxing as ProgressiveTSMuxingResource
from bitmovin.resources.models.encodings.muxings.information.progressive_ts_muxing_information import \
    ProgressiveTsMuxingInformation
from .generic_muxing_service import GenericMuxingService
from .progressive_ts_id3_service import ProgressiveTSID3Service


class ProgressiveTSMuxing(GenericMuxingService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client, type_url='progressive-ts', resource_class=ProgressiveTSMuxingResource)
        self.ID3Tags = ProgressiveTSID3Service(http_client=http_client)

    def information(self, encoding_id, muxing_id):
        self.parsing_utils.check_arg_valid_uuid(argument=muxing_id)
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id)
        url = self.relative_url + '/{}/information'.format(muxing_id)

        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            retrieved_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=ProgressiveTsMuxingInformation)
            return ResourceResponse(response=response, resource=retrieved_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))
