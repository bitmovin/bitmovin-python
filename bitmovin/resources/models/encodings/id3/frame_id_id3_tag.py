from .id3_tag import ID3Tag


class FrameIdID3Tag(ID3Tag):

    def __init__(self, position_mode, frame_id, bytes_, time=None, frame=None, id_=None, custom_data=None, name=None, description=None):

        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description,
                         position_mode=position_mode, time=time, frame=frame)
        self.bytes = bytes_
        self.frameId = frame_id

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
        frame_id = json_object.get('frameId')

        frame_id_id3_tag = FrameIdID3Tag(bytes_=bytes_, frame_id=frame_id,
                                         position_mode=position_mode, time=time, frame=frame,
                                         id_=id_, custom_data=custom_data, name=name, description=description)

        return frame_id_id3_tag
