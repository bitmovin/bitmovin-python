from .muxing import Muxing


class MP4Muxing(Muxing):

    def __init__(self, streams, filename=None, outputs=None, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data, streams=streams, outputs=outputs)
        self.filename = filename

    @classmethod
    def parse_from_json_object(cls, json_object):
        muxing = super().parse_from_json_object(json_object=json_object)
        id_ = muxing.id
        custom_data = muxing.customData
        streams = muxing.streams
        outputs = muxing.outputs
        filename = json_object['filename']
        mp4_muxing = MP4Muxing(streams=streams, filename=filename, outputs=outputs, id_=id_, custom_data=custom_data)
        return mp4_muxing
