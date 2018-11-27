from bitmovin.resources import ResourceResponse, Status
from bitmovin.errors import MissingArgumentError, BitmovinApiError, InvalidStatusError
from bitmovin.services.rest_service import RestService


class GenericManifestService(RestService):
    BASE_ENDPOINT_URL = 'encoding/manifests/{manifest_type}'

    def __init__(self, http_client, manifest_type, resource_class):
        if not manifest_type:
            raise MissingArgumentError('manifest_type must be given')
        if not resource_class:
            raise MissingArgumentError('resource_class must be given')
        self.manifest_type = manifest_type
        self.resource_class = resource_class
        self.relative_url = self.BASE_ENDPOINT_URL.replace('{manifest_type}', manifest_type)
        super().__init__(http_client=http_client, relative_url=self.relative_url, class_=resource_class)

    def filter_by_encoding_id(self, encoding_id, offset=None, limit=None):
        if not offset:
            offset = self.DEFAULT_LIST_OFFSET_PARAM
        if not limit:
            limit = self.DEFAULT_LIST_LIMIT_PARAM
        url = '{}?encodingId={}&offset={}&limit={}'.format(self.relative_url, encoding_id, offset, limit)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            minimal_models = self.parsing_utils.parse_bitmovin_resource_list_from_response(
                response=response, class_=self.class_)

            return ResourceResponse(response=response, resource=minimal_models)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))
