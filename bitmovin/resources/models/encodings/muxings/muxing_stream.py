from bitmovin.resources import AbstractIdResource


class MuxingStream(AbstractIdResource):

    def __init__(self, stream_id, id_=None):
        super().__init__(id_=id_)
        self.streamId = stream_id

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        stream_id = json_object['streamId']

        encoding_status = MuxingStream(stream_id=stream_id, id_=id_)
        return encoding_status
