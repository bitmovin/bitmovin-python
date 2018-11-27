from bitmovin.resources import AbstractNameDescriptionResource
from bitmovin.resources.models import AbstractModel
from bitmovin.utils import Serializable
from bitmovin.resources.models.encodings.encoding_input import EncodingInput


class BurnInSrtSubtitle(AbstractNameDescriptionResource, AbstractModel, Serializable):

    def __init__(self, input=None, id_=None, custom_data=None,
                 name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)

        self._input = None
        self.input = input

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, new_input):
        if new_input is None:
            self._input = None
            return

        if isinstance(new_input, EncodingInput):
            self._input = new_input
        else:
            new_input_parsed = EncodingInput.parse_from_json_object(new_input)
            self._input = new_input_parsed

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        custom_data = json_object.get('customData')
        name = json_object.get('name')
        description = json_object.get('description')
        input = json_object.get('input')

        burn_in_srt_subtitle = BurnInSrtSubtitle(input=input, name=name, description=description,
                                                 custom_data=custom_data, id_=id_)

        return burn_in_srt_subtitle

    def serialize(self):
        serialized = super().serialize()
        serialized['input'] = self.input
        return serialized
