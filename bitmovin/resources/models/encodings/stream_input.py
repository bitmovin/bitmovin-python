from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import SelectionMode
from bitmovin.utils import Serializable
from bitmovin.resources import AbstractIdResource


class StreamInput(AbstractIdResource, Serializable):

    def __init__(self, input_stream_id=None, input_id=None, input_path=None, selection_mode=None, id_=None, position=None):
        super().__init__(id_=id_)

        self.inputStreamId = input_stream_id
        self.inputId = input_id
        self.inputPath = input_path
        self._selectionMode = None
        self.selectionMode = selection_mode
        self.position = position

    @property
    def selectionMode(self):
        return self._selectionMode

    @selectionMode.setter
    def selectionMode(self, new_mode):
        if new_mode is None:
            return
        if isinstance(new_mode, str):
            self._selectionMode = new_mode
        elif isinstance(new_mode, SelectionMode):
            self._selectionMode = new_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for selectionMode: must be either str or SelectionMode!'.format(type(new_mode)))

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        input_stream_id = json_object['inputStreamId']
        input_id = json_object['inputId']
        input_path = json_object['inputPath']
        selection_mode = json_object['selectionMode']
        position = json_object.get('position')

        stream_input = StreamInput(input_stream_id=input_stream_id, input_id=input_id, input_path=input_path, selection_mode=selection_mode, id_=id_,
                                   position=position)

        return stream_input

    def serialize(self):
        serialized = super().serialize()
        serialized['selectionMode'] = self.selectionMode
        return serialized
