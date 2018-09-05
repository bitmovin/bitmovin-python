from .abstract_mp4_representation import AbstractMP4Representation


class MP4Representation(AbstractMP4Representation):

    def __init__(self, encoding_id, muxing_id, media_file, language=None, track_name=None, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data, encoding_id=encoding_id, muxing_id=muxing_id,
                         media_file=media_file, language=language, track_name=track_name)

    @classmethod
    def parse_from_json_object(cls, json_object):
        representation = AbstractMP4Representation.parse_from_json_object(json_object=json_object)
        id_ = representation.id
        custom_data = representation.customData
        encoding_id = representation.encodingId
        muxing_id = representation.muxingId
        media_file = representation.mediaFile
        language = representation.language
        track_name = representation.trackName

        mp4_representation = MP4Representation(id_=id_, custom_data=custom_data, encoding_id=encoding_id,
                                                 muxing_id=muxing_id, media_file=media_file,
                                                 language=language, track_name=track_name)
        return mp4_representation
