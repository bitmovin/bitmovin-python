from .id3_tag import ID3Tag


class PlainTextID3Tag(ID3Tag):

    def __init__(self, position_mode, frame_id, text, time=None, frame=None, id_=None, custom_data=None, name=None, description=None):

        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description,
                         position_mode=position_mode, time=time, frame=frame)
        self.text = text
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

        text = json_object.get('text')
        frame_id = json_object.get('frameId')

        plain_text_id3_tag = PlainTextID3Tag(text=text, frame_id=frame_id,
                                             position_mode=position_mode, time=time, frame=frame,
                                             id_=id_, custom_data=custom_data, name=name, description=description)

        return plain_text_id3_tag
