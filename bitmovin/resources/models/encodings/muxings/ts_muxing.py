from .muxing import Muxing


class TSMuxing(Muxing):

    def __init__(self, name, streams, segment_length, segment_naming=None, outputs=None, id_=None, custom_data=None,
                 description=None):
        super().__init__(id_=id_, custom_data=custom_data, streams=streams, outputs=outputs,
                         name=name, description=description)
        self.segmentLength = segment_length
        self.segmentNaming = segment_naming

    @classmethod
    def parse_from_json_object(cls, json_object):
        muxing = super().parse_from_json_object(json_object=json_object)
        id_ = muxing.id
        custom_data = muxing.customData
        streams = muxing.streams
        outputs = muxing.outputs
        name = muxing.name
        description = muxing.description
        segment_length = json_object['segmentLength']
        segment_naming = json_object.get('segmentNaming')

        ts_muxing = TSMuxing(streams=streams, segment_length=segment_length, segment_naming=segment_naming,
                             outputs=outputs, id_=id_, custom_data=custom_data, name=name, description=description)

        return ts_muxing
