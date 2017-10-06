from bitmovin.errors import InvalidTypeError
from bitmovin.resources import Resource
from .byte_range import ByteRange


class ProgressiveTSInformation(Resource):

    def __init__(self, byte_ranges, **kwargs):
        super().__init__(**kwargs)

        self._byte_ranges = None
        self.byte_ranges = byte_ranges

    @property
    def byte_ranges(self):
        return self._byte_ranges

    @byte_ranges.setter
    def byte_ranges(self, new_value):
        if new_value is None:
            return

        if not isinstance(new_value, list):
            raise InvalidTypeError('byte_ranges has to be a list of ByteRange instances')

        if all(isinstance(output, ByteRange) for output in new_value):
            byte_ranges = []
            for item in new_value:
                byte_ranges.append(item)
            self._byte_ranges = byte_ranges
        else:
            byte_ranges = []
            for item in new_value:
                byte_ranges.append(ByteRange.parse_from_json_object(item))
            self._byte_ranges = byte_ranges

    @classmethod
    def parse_from_json_object(cls, json_object):
        byte_ranges = json_object.get('byteRanges')

        progressive_ts_information = ProgressiveTSInformation(byte_ranges=byte_ranges)
        return progressive_ts_information
