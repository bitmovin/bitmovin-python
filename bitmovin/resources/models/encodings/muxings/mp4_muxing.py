from .muxing import Muxing


class MP4Muxing(Muxing):

    def __init__(self, streams, filename=None, outputs=None, id_=None, custom_data=None, name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, streams=streams, outputs=outputs,
                         name=name, description=description)
        self.filename = filename

    @classmethod
    def parse_from_json_object(cls, json_object):
        muxing = super().parse_from_json_object(json_object=json_object)
        id_ = muxing.id
        custom_data = muxing.customData
        streams = muxing.streams
        outputs = muxing.outputs
        name = muxing.name
        description = muxing.description
        filename = json_object['filename']
        mp4_muxing = MP4Muxing(streams=streams, filename=filename, outputs=outputs, id_=id_, custom_data=custom_data,
                               name=name, description=description)
        return mp4_muxing
