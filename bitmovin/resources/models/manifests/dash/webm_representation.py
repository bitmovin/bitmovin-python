from bitmovin.errors import InvalidTypeError
from bitmovin.resources.models import AbstractModel
from bitmovin.resources.enums import FMP4RepresentationType
from bitmovin.utils import Serializable


class WebMRepresentation(AbstractModel, Serializable):

    def __init__(self, type, encoding_id, muxing_id, segment_path, start_segment_number=None,
                 id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self._type = None
        self.type = type
        self.encodingId = encoding_id
        self.muxingId = muxing_id
        self.segmentPath = segment_path
        self.startSegmentNumber = start_segment_number

    @property
    def type(self):
        if self._type is not None:
            return self._type
        else:
            return FMP4RepresentationType.default().value

    @type.setter
    def type(self, new_type):
        if new_type is None:
            return
        if isinstance(new_type, str):
            self._type = new_type
        elif isinstance(new_type, FMP4RepresentationType):
            self._type = new_type.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for \'type\': must be either str or FMP4RepresentationType!'.format(type(new_type)))


    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        custom_data = json_object.get('customData')
        type = json_object['type']
        encoding_id = json_object['encodingId']
        muxing_id = json_object['muxingId']
        segment_path = json_object['segmentPath']
        start_segment_number = json_object.get('startSegmentNumber')
        webm_representation = WebMRepresentation(
            id_=id_, custom_data=custom_data, type=type, encoding_id=encoding_id, muxing_id=muxing_id,
            segment_path=segment_path, start_segment_number=start_segment_number)
        return webm_representation

    def serialize(self):
        serialized = super().serialize()
        serialized['type'] = self.type
        return serialized
