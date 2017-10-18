from .muxing import Muxing


class FMP4Muxing(Muxing):

    def __init__(self, streams, segment_length, segment_naming=None, init_segment_name=None, outputs=None,
                 id_=None, custom_data=None, name=None, description=None, avg_bitrate=None, max_bitrate=None,
                 min_bitrate=None, ignored_by=None):

        super().__init__(id_=id_, custom_data=custom_data, streams=streams, outputs=outputs,
                         name=name, description=description, avg_bitrate=avg_bitrate, max_bitrate=max_bitrate,
                         min_bitrate=min_bitrate, ignored_by=ignored_by)
        self.segmentLength = segment_length
        self.segmentNaming = segment_naming
        self.initSegmentName = init_segment_name

    @classmethod
    def parse_from_json_object(cls, json_object):
        muxing = super().parse_from_json_object(json_object=json_object)
        id_ = muxing.id
        custom_data = muxing.customData
        streams = muxing.streams
        outputs = muxing.outputs
        name = muxing.name
        description = muxing.description
        max_bitrate = muxing.maxBitrate
        min_bitrate = muxing.minBitrate
        avg_bitrate = muxing.avgBitrate
        segment_length = json_object['segmentLength']
        segment_naming = json_object.get('segmentNaming')
        init_segment_name = json_object.get('initSegmentName')
        ignored_by = json_object.get('ignoredBy')

        fmp4_muxing = FMP4Muxing(streams=streams, segment_length=segment_length, segment_naming=segment_naming,
                                 init_segment_name=init_segment_name, outputs=outputs, id_=id_, custom_data=custom_data,
                                 name=name, description=description, max_bitrate=max_bitrate, avg_bitrate=avg_bitrate,
                                 min_bitrate=min_bitrate, ignored_by=ignored_by)

        return fmp4_muxing
