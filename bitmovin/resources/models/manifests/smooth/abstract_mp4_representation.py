from bitmovin.resources.models import AbstractModel
from bitmovin.utils import Serializable


class AbstractMP4Representation(AbstractModel, Serializable):

    def __init__(self, encoding_id, muxing_id, media_file, language=None,
                 track_name=None, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self.encodingId = encoding_id
        self.muxingId = muxing_id
        self.mediaFile = media_file
        self.language = language
        self.trackName = track_name

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        custom_data = json_object.get('customData')
        encoding_id = json_object.get('encodingId')
        muxing_id = json_object.get('muxingId')
        media_file = json_object.get('mediaFile')
        language = json_object.get('language')
        track_name = json_object.get('trackName')

        abstract_mp4_representation = AbstractMP4Representation(
            id_=id_, custom_data=custom_data, encoding_id=encoding_id, muxing_id=muxing_id,
            media_file=media_file, language=language, track_name=track_name)

        return abstract_mp4_representation
