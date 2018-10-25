from bitmovin.resources.models import AbstractModel
from bitmovin.utils import Serializable


class AbstractDashMP4Representation(AbstractModel, Serializable):

    def __init__(self, encoding_id, muxing_id, file_path, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self.encodingId = encoding_id
        self.muxingId = muxing_id
        self.filePath = file_path

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        custom_data = json_object.get('customData')
        encoding_id = json_object.get('encodingId')
        muxing_id = json_object.get('muxingId')
        file_path = json_object.get('filePath')
        abstract_mp4_representation = AbstractDashMP4Representation(
            id_=id_, custom_data=custom_data, encoding_id=encoding_id, muxing_id=muxing_id, file_path=file_path)
        return abstract_mp4_representation
