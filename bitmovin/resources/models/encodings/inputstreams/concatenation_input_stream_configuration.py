from bitmovin.utils import Serializable
from bitmovin.resources import Resource


class ConcatenationInputStreamConfiguration(Resource, Serializable):

    def __init__(self, input_stream_id, is_main, position=None):
        super().__init__()
        self.inputStreamId = input_stream_id
        self.isMain = is_main
        self.position = position

    @classmethod
    def parse_from_json_object(cls, json_object):
        input_stream_id = json_object.get('inputStreamId')
        is_main = json_object.get('isMain')
        position = json_object.get('position')

        concatentation_input_stream_configuration = ConcatenationInputStreamConfiguration(
            input_stream_id=input_stream_id,
            is_main=is_main,
            position=position
        )

        return concatentation_input_stream_configuration

    def serialize(self):
        serialized = super().serialize()
        return serialized
