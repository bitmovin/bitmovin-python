from .muxing import Muxing


class ProgressiveTSMuxing(Muxing):

    def __init__(self, streams, segment_length, filename, outputs=None, id_=None, custom_data=None,
                 name=None, description=None, ignored_by=None, stream_conditions_mode=None):
        super().__init__(id_=id_, custom_data=custom_data, streams=streams, outputs=outputs,
                         name=name, description=description, ignored_by=ignored_by,
                         stream_conditions_mode=stream_conditions_mode)
        self.segmentLength = segment_length
        self.filename = filename

    @classmethod
    def parse_from_json_object(cls, json_object):
        muxing = super().parse_from_json_object(json_object=json_object)

        segment_length = json_object.get('segmentLength')
        filename = json_object.get('filename')

        progressive_ts_muxing = ProgressiveTSMuxing(segment_length=segment_length,
                                                    filename=filename,
                                                    id_=muxing.id,
                                                    streams=muxing.streams,
                                                    outputs=muxing.outputs,
                                                    custom_data=muxing.customData,
                                                    name=muxing.name,
                                                    description=muxing.description,
                                                    ignored_by=muxing.ignored_by,
                                                    stream_conditions_mode=muxing.stream_conditions_mode)

        return progressive_ts_muxing
