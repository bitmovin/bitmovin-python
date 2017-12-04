from .muxing import Muxing


class ProgressiveTSMuxing(Muxing):

    def __init__(self, streams, segment_length, filename, outputs=None, id_=None, custom_data=None,
                 name=None, description=None, ignored_by=None):
        super().__init__(id_=id_, custom_data=custom_data, streams=streams, outputs=outputs,
                         name=name, description=description, ignored_by=ignored_by)
        self.segmentLength = segment_length
        self.filename = filename

    @classmethod
    def parse_from_json_object(cls, json_object):
        muxing = super().parse_from_json_object(json_object=json_object)

        id_ = muxing.id
        custom_data = muxing.customData
        streams = muxing.streams
        outputs = muxing.outputs
        name = muxing.name
        description = muxing.description
        ignored_by = muxing.ignored_by

        segment_length = json_object.get('segmentLength')
        filename = json_object.get('filename')

        progressive_ts_muxing = ProgressiveTSMuxing(streams=streams, segment_length=segment_length, filename=filename,
                                                    outputs=outputs, id_=id_, custom_data=custom_data,
                                                    name=name, description=description, ignored_by=ignored_by)

        return progressive_ts_muxing
