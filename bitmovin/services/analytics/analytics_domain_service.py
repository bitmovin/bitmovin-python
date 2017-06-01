from bitmovin.resources import ResponseSuccessData, Status, ResourceResponse
from bitmovin.resources.models import AnalyticsDomain, MinimalModel
from bitmovin.errors import MissingArgumentError, FunctionalityNotAvailableError, BitmovinApiError, InvalidStatusError
from ..rest_service import RestService


class AnalyticsDomainService(RestService):
    BASE_ENDPOINT_URL = 'analytics/licenses/{license_id}/domains'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=AnalyticsDomain)

    def list(self, license_id, offset=None, limit=None):
        self.relative_url = self._get_endpoint_url(license_id=license_id)

        if not offset:
            offset = self.DEFAULT_LIST_OFFSET_PARAM
        if not limit:
            limit = self.DEFAULT_LIST_LIMIT_PARAM
        url = '{}?offset={}&limit={}'.format(self.relative_url, offset, limit)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            models = self._parse_bitmovin_resource_list_from_deprecated_response(
                response=response, class_=self.class_)
            return ResourceResponse(response=response, resource=models)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def delete(self, license_id, domain_id):
        self.relative_url = self._get_endpoint_url(license_id=license_id)
        self.parsing_utils.check_arg_valid_uuid(argument=domain_id)
        url = '{}/{}'.format(self.relative_url, domain_id)
        response = self.http_client.delete(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            retrieved_resource = self.parse_bitmovin_minimal_model_from_deprecated_response(response=response)
            return ResourceResponse(response=response, resource=retrieved_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def create(self, object_, license_id):
        self.relative_url = self._get_endpoint_url(license_id=license_id)
        return super().create(object_)

    def retrieve(self, license_id, domain_id):
        raise FunctionalityNotAvailableError()

    def retrieve_custom_data(self, license_id, domain_id):
        raise FunctionalityNotAvailableError()

    def _get_endpoint_url(self, license_id):
        if not license_id:
            raise MissingArgumentError('license_id must be given')
        endpoint_url = self.BASE_ENDPOINT_URL.replace('{license_id}', license_id)
        return endpoint_url

    @staticmethod
    def _parse_bitmovin_resource_list_from_deprecated_response(response, class_):
        response_data = response.data  # type: ResponseSuccessData
        resource_list = response_data.result.get('domains')

        if not isinstance(resource_list, list):
            raise BitmovinApiError('Got invalid response from server: \'result\' has to be a list')

        resources = []
        for resource in resource_list:
            parsed_resource = class_.parse_from_json_object(json_object=resource)
            resources.append(parsed_resource)

        return resources

    @staticmethod
    def parse_bitmovin_minimal_model_from_deprecated_response(response):
        response_data = response.data  # type: ResponseSuccessData
        result = response_data.result
        resource = MinimalModel(id_=result)
        return resource
