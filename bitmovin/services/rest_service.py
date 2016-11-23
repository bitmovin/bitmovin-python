from bitmovin.bitmovin_object import BitmovinObject
from bitmovin.errors import BitmovinApiError, InvalidStatusError, InvalidTypeError
from bitmovin.resources import ResourceResponse, Status, Response
from bitmovin.resources.models import CustomData
from bitmovin.rest import BitmovinHttpClient
from .parsing_utils import ParsingUtils


class RestService(BitmovinObject):

    def __init__(self, http_client, relative_url, class_):
        super().__init__(http_client, relative_url)
        self.DEFAULT_LIST_OFFSET_PARAM = 0
        self.DEFAULT_LIST_LIMIT_PARAM = 100
        self.http_client = http_client  # type: BitmovinHttpClient
        self.relative_url = relative_url
        self.class_ = class_
        self.parsing_utils = ParsingUtils()

    def create(self, object_):
        if not isinstance(object_, self.class_):
            raise InvalidTypeError('object_ has to be an instance of {}'.format(self.class_.__name__))

        response = self.http_client.post(self.relative_url, object_)  # type: Response

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful: {}'.format(response.raw_response), response)

        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=self.class_)
            return ResourceResponse(response=response, resource=created_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def retrieve(self, id_):
        self.parsing_utils.check_arg_valid_uuid(argument=id_)
        url = '{}/{}'.format(self.relative_url, id_)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            retrieved_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=self.class_)
            return ResourceResponse(response=response, resource=retrieved_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def delete(self, id_):
        self.parsing_utils.check_arg_valid_uuid(argument=id_)
        url = '{}/{}'.format(self.relative_url, id_)
        response = self.http_client.delete(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            retrieved_resource = self.parsing_utils.parse_bitmovin_minimal_model_from_response(
                response=response)
            return ResourceResponse(response=response, resource=retrieved_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def list(self, offset=None, limit=None):
        if not offset:
            offset = self.DEFAULT_LIST_OFFSET_PARAM
        if not limit:
            limit = self.DEFAULT_LIST_LIMIT_PARAM
        url = '{}?offset={}&limit={}'.format(self.relative_url, offset, limit)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            minimal_models = self.parsing_utils.parse_bitmovin_resource_list_from_response(
                response=response, class_=self.class_)

            return ResourceResponse(response=response, resource=minimal_models)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def retrieve_custom_data(self, id_):
        self.parsing_utils.check_arg_valid_uuid(argument=id_)
        url = '{}/{}/customData'.format(self.relative_url, id_)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            retrieved_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=CustomData)

            return ResourceResponse(response=response, resource=retrieved_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))
