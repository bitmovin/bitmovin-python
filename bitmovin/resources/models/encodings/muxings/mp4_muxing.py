from .muxing import Muxing


class MP4Muxing(Muxing):

    def __init__(self, streams, name=None, outputs=None, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data, streams=streams, outputs=outputs)
        self.name = name

    @classmethod
    def parse_from_json_object(cls, json_object):
        muxing = super().parse_from_json_object(json_object=json_object)
        id_ = muxing.id
        custom_data = muxing.customData
        streams = muxing.streams
        outputs = muxing.outputs
        name = json_object['name']
        mp4_muxing = MP4Muxing(streams=streams, name=name, outputs=outputs, id_=id_, custom_data=custom_data)
        return mp4_muxing
