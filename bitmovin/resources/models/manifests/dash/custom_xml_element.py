from bitmovin.utils import Serializable


class CustomXMLElement(Serializable):

    def __init__(self, data):
        super().__init__()
        self.data = data

    @classmethod
    def parse_from_json_object(cls, json_object):
        data = json_object.get('data')
        return data

    def serialize(self):
        serialized = super().serialize()
        serialized['data'] = self.data
        return serialized
