from .abstract_fmp4_representation import AbstractFMP4Representation


class DRMFMP4Representation(AbstractFMP4Representation):

    def __init__(self, type, encoding_id, muxing_id, drm_id, segment_path, start_segment_number=None,
                 id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data, type=type, encoding_id=encoding_id, muxing_id=muxing_id,
                         segment_path=segment_path, start_segment_number=start_segment_number)
        self.drmId = drm_id

    @classmethod
    def parse_from_json_object(cls, json_object):
        representation = AbstractFMP4Representation.parse_from_json_object(json_object=json_object)
        id_ = representation.id
        custom_data = representation.customData
        type = representation.type
        encoding_id = representation.encodingId
        muxing_id = representation.muxingId
        segment_path = representation.segmentPath
        start_segment_number = representation.startSegmentNumber
        drm_id = json_object['drmId']

        fmp4_representation = DRMFMP4Representation(id_=id_, custom_data=custom_data, type=type,
                                                    encoding_id=encoding_id, muxing_id=muxing_id, drm_id=drm_id,
                                                    segment_path=segment_path,
                                                    start_segment_number=start_segment_number)
        return fmp4_representation
