from bitmovin.resources import AbstractIdResource


class VariantStream(AbstractIdResource):

    def __init__(self, encoding_id, stream_id, muxing_id, uri, segment_path,
                 closed_captions='NONE', audio=None, video=None, subtitles=None,
                 drm_id=None, start_segment_number=None, end_segment_number=None, id_=None):
        super().__init__(id_=id_)
        self.encodingId = encoding_id
        self.streamId = stream_id
        self.muxingId = muxing_id
        self.uri = uri
        self.segmentPath = segment_path
        self.closedCaptions = closed_captions
        self.audio = audio
        self.video = video
        self.subtitles = subtitles
        self.drmId = drm_id
        self.startSegmentNumber = start_segment_number
        self.endSegmentNumber = end_segment_number

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        encoding_id = json_object.get('encodingId')
        stream_id = json_object.get('streamId')
        muxing_id = json_object.get('muxingId')
        uri = json_object.get('uri')
        segment_path = json_object.get('segmentPath')
        closed_captions = json_object.get('closedCaptions')
        audio = json_object.get('audio')
        video = json_object.get('video')
        subtitles = json_object.get('subtitles')
        drm_id = json_object.get('drmId')
        start_segment_number = json_object.get('startSegmentNumber')
        end_segment_number = json_object.get('endSegmentNumber')

        variant_stream = VariantStream(id_=id_, encoding_id=encoding_id, stream_id=stream_id, muxing_id=muxing_id,
                                       uri=uri, segment_path=segment_path, closed_captions=closed_captions, audio=audio,
                                       video=video, subtitles=subtitles, drm_id=drm_id,
                                       start_segment_number=start_segment_number, end_segment_number=end_segment_number)

        return variant_stream
