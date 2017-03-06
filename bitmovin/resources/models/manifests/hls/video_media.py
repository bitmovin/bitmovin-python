from .abstract_standard_media import AbstractStandardMedia


class VideoMedia(AbstractStandardMedia):

    def __init__(self, name, group_id, segment_path, encoding_id, stream_id, muxing_id, drm_id=None,
                 start_segment_number=None, end_segment_number=None, language=None, assoc_language=None,
                 is_default=None, autoselect=None, characteristics=None, uri=None, id_=None):
        super().__init__(id_=id_, name=name, group_id=group_id, language=language, assoc_language=assoc_language,
                         is_default=is_default, autoselect=autoselect, characteristics=characteristics,
                         segment_path=segment_path, encoding_id=encoding_id, stream_id=stream_id, muxing_id=muxing_id,
                         drm_id=drm_id, start_segment_number=start_segment_number,
                         end_segment_number=end_segment_number)
        self.uri = uri

    @classmethod
    def parse_from_json_object(cls, json_object):
        media = super().parse_from_json_object(json_object=json_object)
        id_ = media.id
        name = media.name
        group_id = media.groupId
        language = media.language
        assoc_language = media.assocLanguage
        is_default = media.isDefault
        autoselect = media.autoselect
        characteristics = media.characteristics
        segment_path = media.segmentPath
        encoding_id = media.encodingId
        stream_id = media.streamId
        muxing_id = media.muxingId
        drm_id = media.drmId
        start_segment_number = media.startSegmentNumber
        end_segment_number = media.endSegmentNumber
        uri = json_object.get('uri')

        video_media = VideoMedia(id_=id_, name=name, group_id=group_id, language=language,
                                 assoc_language=assoc_language,
                                 is_default=is_default, autoselect=autoselect,
                                 characteristics=characteristics, segment_path=segment_path,
                                 encoding_id=encoding_id, stream_id=stream_id,
                                 muxing_id=muxing_id, drm_id=drm_id,
                                 start_segment_number=start_segment_number,
                                 end_segment_number=end_segment_number, uri=uri)
        return video_media
