from bitmovin.utils import Serializable
from bitmovin.resources import AbstractIdResource


class ConcatenationInputStreamConfiguration(AbstractIdResource, Serializable):

    def __init__(self, input_stream_id, is_main, id_=None, position=None):
        super().__init__(id_=id_)

        self._position = None
        self.inputStreamId = input_stream_id
        self.isMain = is_main
        self.position = position

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        input_stream_id = json_object['inputStreamId']
        is_main = json_object['isMain']
        position = json_object.get('position')

        concatentation_input_stream_configuration = ConcatenationInputStreamConfiguration(input_stream_id=input_stream_id, is_main=is_main, id_=id_,
                                   position=position)

        return concatentation_input_stream_configuration

    def serialize(self):
        serialized = super().serialize()
        serialized['inputStreamId'] = self.inputStreamId
        serialized['isMain'] = self.isMain
        serialized['position'] = self.position
        return serialized
