from .abstract_dash_mp4_representation import AbstractDashMP4Representation


class DashMP4Representation(AbstractDashMP4Representation):

    def __init__(self, encoding_id, muxing_id, file_path, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data, encoding_id=encoding_id, muxing_id=muxing_id,
                         file_path=file_path)

    @classmethod
    def parse_from_json_object(cls, json_object):
        representation = AbstractDashMP4Representation.parse_from_json_object(json_object=json_object)

        id_ = representation.id
        custom_data = representation.customData
        encoding_id = representation.encodingId
        muxing_id = representation.muxingId
        file_path = representation.filePath

        dash_mp4_representation = DashMP4Representation(id_=id_,
                                                        custom_data=custom_data,
                                                        encoding_id=encoding_id,
                                                        muxing_id=muxing_id,
                                                        file_path=file_path)
        return dash_mp4_representation
