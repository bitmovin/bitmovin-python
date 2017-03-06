from .abstract_media import AbstractMedia


class AbstractStandardMedia(AbstractMedia):

    def __init__(self, name, group_id, segment_path, encoding_id, stream_id, muxing_id, drm_id=None,
                 start_segment_number=None, end_segment_number=None, language=None, assoc_language=None,
                 is_default=None, autoselect=None, characteristics=None, id_=None):
        super().__init__(id_=id_, name=name, group_id=group_id, language=language, assoc_language=assoc_language,
                         is_default=is_default, autoselect=autoselect, characteristics=characteristics)
        self.segmentPath = segment_path
        self.encodingId = encoding_id
        self.streamId = stream_id
        self.muxingId = muxing_id
        self.drmId = drm_id
        self.startSegmentNumber = start_segment_number
        self.endSegmentNumber = end_segment_number

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

        segment_path = json_object.get('segmentPath')
        encoding_id = json_object.get('encodingId')
        stream_id = json_object.get('streamId')
        muxing_id = json_object.get('muxingId')
        drm_id = json_object.get('drmId')
        start_segment_number = json_object.get('startSegmentNumber')
        end_segment_number = json_object.get('endSegmentNumber')

        abstract_standard_media = AbstractStandardMedia(id_=id_, name=name, group_id=group_id, language=language,
                                                        assoc_language=assoc_language,
                                                        is_default=is_default, autoselect=autoselect,
                                                        characteristics=characteristics, segment_path=segment_path,
                                                        encoding_id=encoding_id, stream_id=stream_id,
                                                        muxing_id=muxing_id, drm_id=drm_id,
                                                        start_segment_number=start_segment_number,
                                                        end_segment_number=end_segment_number)
        return abstract_standard_media
