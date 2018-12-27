from .muxing import Muxing


class WebMMuxing(Muxing):

    def __init__(self, streams, segment_length, segment_naming=None, init_segment_name=None, outputs=None,
                 id_=None, custom_data=None, name=None, description=None, ignored_by=None, stream_conditions_mode=None):

        super().__init__(id_=id_, custom_data=custom_data, streams=streams, outputs=outputs,
                         name=name, description=description, ignored_by=ignored_by,
                         stream_conditions_mode=stream_conditions_mode)
        self.segmentLength = segment_length
        self.segmentNaming = segment_naming
        self.initSegmentName = init_segment_name

    @classmethod
    def parse_from_json_object(cls, json_object):
        muxing = super().parse_from_json_object(json_object=json_object)

        segment_length = json_object.get('segmentLength')
        segment_naming = json_object.get('segmentNaming')
        init_segment_name = json_object.get('initSegmentName')

        webm_muxing = WebMMuxing(segment_length=segment_length,
                                 segment_naming=segment_naming,
                                 init_segment_name=init_segment_name,
                                 id_=muxing.id,
                                 streams=muxing.streams,
                                 outputs=muxing.outputs,
                                 custom_data=muxing.customData,
                                 name=muxing.name,
                                 description=muxing.description,
                                 ignored_by=muxing.ignored_by,
                                 stream_conditions_mode=muxing.stream_conditions_mode)

        return webm_muxing
