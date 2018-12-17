from bitmovin.errors import InvalidTypeError
from bitmovin.resources import AbstractNameDescriptionResource
from bitmovin.resources.models import AbstractModel
from bitmovin.utils import Serializable
from .concatenation_input_stream_configuration import ConcatenationInputStreamConfiguration

class ConcatenationInputStream(AbstractNameDescriptionResource, AbstractModel, Serializable):

    def __init__(self, concatenation, id_=None, custom_data=None, name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self._concatenation = None
        if concatenation is not None and not isinstance(concatenation, list):
            raise InvalidTypeError('input_streams must be a list')
        self.concatenation = concatenation

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        custom_data = json_object.get('customData')
        name = json_object.get('name')
        description = json_object.get('description')
        concatenation = json_object.get('concatenation')

        concatenation_input_stream = ConcatenationInputStream(concatenation=concatenation, 
                        id_=id_, custom_data=custom_data, name=name, description=description)

        return concatenation_input_stream

    # @concatenation.setter
    # def concatenation(self, new_concatenations):
    #     if new_concatenations is None:
    #         return

    #     if not isinstance(new_concatenations, list):
    #         raise InvalidTypeError('new_concatenation has to be a list of ConcatenationInputStreamConfiguration objects')

    #     if all(isinstance(concatenation, ConcatenationInputStreamConfiguration) for concatenation in new_concatenations):
    #         self._concatenation = new_concatenations
    #     else:
    #         concatenations = []
    #         for json_object in new_concatenations:
    #             concatenation = ConcatenationInputStreamConfiguration.parse_from_json_object(json_object)
    #             concatenations.append(concatenation)
    #         self._concatenation = concatenations

    def serialize(self):
        serialized = super().serialize()
        serialized['concatenation'] = self.concatenation
        return serialized
