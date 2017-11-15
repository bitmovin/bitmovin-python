from bitmovin.resources import Resource


class ByteRange(Resource):

    def __init__(self, segment_number, start_bytes, end_bytes, duration, **kwargs):
        super().__init__(**kwargs)

        self.segment_number = segment_number
        self.start_bytes = start_bytes
        self.end_bytes = end_bytes
        self.duration = duration

    @classmethod
    def parse_from_json_object(cls, json_object):
        segment_number = json_object.get('segmentNumber')
        start_bytes = json_object.get('startBytes')
        end_bytes = json_object.get('endBytes')
        duration = json_object.get('duration')

        byte_range = ByteRange(segment_number=segment_number, start_bytes=start_bytes, end_bytes=end_bytes,
                               duration=duration)
        return byte_range
