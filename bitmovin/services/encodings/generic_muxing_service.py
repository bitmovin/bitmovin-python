from bitmovin.errors import MissingArgumentError, BitmovinApiError, InvalidStatusError
from bitmovin.resources import ResourceResponse, Status
from bitmovin.resources.models import EncodingStatus
from bitmovin.services.rest_service import RestService


class GenericMuxingService(RestService):
    BASE_ENDPOINT_URL = 'encoding/encodings/{encoding_id}/muxings/{type}'

    def __init__(self, http_client, type_url, resource_class):
        if not type_url:
            raise MissingArgumentError('type_url must be given')
        if not resource_class:
            raise MissingArgumentError('resource_class must be given')
        self.type_url = type_url
        self.resource_class = resource_class
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=self.resource_class)

    def _get_endpoint_url(self, encoding_id):
        if not encoding_id:
            raise MissingArgumentError('encoding_id must be given')
        return self.BASE_ENDPOINT_URL.replace('{encoding_id}', encoding_id).replace('{type}', self.type_url)

    def create(self, object_, encoding_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id)
        return super().create(object_)

    def delete(self, encoding_id, muxing_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id)
        return super().delete(id_=muxing_id)

    def retrieve(self, encoding_id, muxing_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id)
        return super().retrieve(id_=muxing_id)

    def list(self, encoding_id, offset=None, limit=None):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id)
        return super().list(offset, limit)

    def retrieve_custom_data(self, encoding_id, muxing_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id)
        return super().retrieve_custom_data(id_=muxing_id)

    def retrieve_status(self, encoding_id, muxing_id):
        self.parsing_utils.check_arg_valid_uuid(argument=encoding_id)
        self.parsing_utils.check_arg_valid_uuid(argument=muxing_id)
        url = '{}/{}/status'.format(self._get_endpoint_url(encoding_id=encoding_id), muxing_id)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            retrieved_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=EncodingStatus)

            return ResourceResponse(response=response, resource=retrieved_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))
