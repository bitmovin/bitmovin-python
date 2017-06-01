from .id3_tag import ID3Tag


class RawID3Tag(ID3Tag):

    def __init__(self, position_mode, bytes_, time=None, frame=None, id_=None, custom_data=None, name=None, description=None):

        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description,
                         position_mode=position_mode, time=time, frame=frame)
        self.bytes = bytes_

    @classmethod
    def parse_from_json_object(cls, json_object):
        id3_tag = super().parse_from_json_object(json_object=json_object)

        id_ = id3_tag.id
        custom_data = id3_tag.customData
        name = id3_tag.name
        description = id3_tag.description
        position_mode = id3_tag.positionMode
        time = id3_tag.time
        frame = id3_tag.frame

        bytes_ = json_object.get('bytes')

        raw_id3_tag = RawID3Tag(bytes_=bytes_, position_mode=position_mode, time=time, frame=frame,
                                id_=id_, custom_data=custom_data, name=name, description=description)

        return raw_id3_tag
