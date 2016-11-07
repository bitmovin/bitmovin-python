from . import AbstractInput


class RTMPInput(AbstractInput):

    def __init__(self, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        custom_data = json_object.get('customData')
        rtmp_input = RTMPInput(id_=id_, custom_data=custom_data)
        return rtmp_input
