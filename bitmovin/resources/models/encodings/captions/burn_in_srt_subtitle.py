from bitmovin.errors import InvalidTypeError
from bitmovin.resources import AbstractNameDescriptionResource, CaptionCharacterEncoding
from bitmovin.resources.models import AbstractModel
from bitmovin.utils import Serializable
from bitmovin.resources.models.encodings.encoding_input import EncodingInput


class BurnInSrtSubtitle(AbstractNameDescriptionResource, AbstractModel, Serializable):

    def __init__(self, input=None, id_=None, custom_data=None,
                 name=None, description=None, character_encoding=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)

        self._input = None
        self._character_encoding = None
        self.input = input
        self.characterEncoding = character_encoding

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

    @property
    def characterEncoding(self):
        return self._character_encoding

    @characterEncoding.setter
    def characterEncoding(self, new_character_encoding):
        if new_character_encoding is None:
            self._character_encoding = None
        elif isinstance(new_character_encoding, CaptionCharacterEncoding):
            self._character_encoding = new_character_encoding.value
        elif isinstance(new_character_encoding, str):
            self._character_encoding = new_character_encoding
        else:
            raise InvalidTypeError('characterEncoding has to be of type CaptionCharacterEncoding or str')

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        custom_data = json_object.get('customData')
        name = json_object.get('name')
        description = json_object.get('description')
        input = json_object.get('input')
        character_encoding = json_object.get('characterEncoding')

        burn_in_srt_subtitle = BurnInSrtSubtitle(input=input, name=name, description=description,
                                                 custom_data=custom_data, id_=id_,
                                                 character_encoding=character_encoding)

        return burn_in_srt_subtitle

    def serialize(self):
        serialized = super().serialize()
        serialized['input'] = self.input
        serialized['characterEncoding'] = self.characterEncoding
        return serialized
