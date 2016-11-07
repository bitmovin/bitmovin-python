from bitmovin.errors import BitmovinApiError
from bitmovin.resources import Resource


class AnalysisStream(Resource):

    def __init__(self, id_, position, duration, codec):
        super().__init__()
        self.id = id_
        self.position = position
        self.duration = duration
        self.codec = codec

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        if id_ is None:
            raise BitmovinApiError('Invalid json object: missing field \'id\'')
        position = json_object.get('position')
        duration = json_object.get('duration')
        codec = json_object.get('codec')
        stream = AnalysisStream(id_=id_, position=position, duration=duration, codec=codec)
        return stream
