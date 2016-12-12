from . import AbstractInput


class RTMPInput(AbstractInput):

    def __init__(self, id_=None, custom_data=None, name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        custom_data = json_object.get('customData')
        name = json_object.get('name')
        description = json_object.get('description')
        rtmp_input = RTMPInput(id_=id_, custom_data=custom_data, name=name, description=description)
        return rtmp_input
