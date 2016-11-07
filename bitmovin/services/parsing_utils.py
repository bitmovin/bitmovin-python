from bitmovin.bitmovin_object import BitmovinObject
from bitmovin.errors import MissingArgumentError, InvalidTypeError, BitmovinApiError
from bitmovin.resources import ResponseSuccessData
from bitmovin.resources.models import MinimalModel, CustomData


class ParsingUtils(BitmovinObject):

    def __init__(self):
        super().__init__()

    @classmethod
    def check_arg_valid(cls, argument):
        if not argument:
            raise MissingArgumentError('id_ must be an UUID')
        if not isinstance(argument, str):
            raise InvalidTypeError('argument must be an UUID')

    def parse_bitmovin_resource_from_response(self, response, class_):
        response_data = response.data  # type: ResponseSuccessData
        result = response_data.result
        resource = class_.parse_from_json_object(json_object=result)
        return resource

    def parse_bitmovin_minimal_model_from_response(self, response):
        response_data = response.data  # type: ResponseSuccessData
        result = response_data.result
        resource = MinimalModel.parse_from_json_object(json_object=result)
        return resource

    def parse_bitmovin_resource_list_from_response(self, response, class_):
        response_data = response.data  # type: ResponseSuccessData
        resource_list = response_data.result.get('items')

        if not isinstance(resource_list, list):
            raise BitmovinApiError('Got invalid response from server: \'items\' has to be a list')

        resources = []
        for resource in resource_list:
            parsed_resource = class_.parse_from_json_object(json_object=resource)
            resources.append(parsed_resource)

        self.logger.info('resources[] size: {}'.format(resources.__sizeof__()))

        return resources
