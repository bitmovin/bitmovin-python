from bitmovin.utils import Serializable


class StreamFilter(Serializable):
    def __init__(self, id=None, position=None):
        super().__init__()
        self.id = id
        self.position = position

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        position = json_object.get('position')

        sprite = StreamFilter(id=id_, position=position)
        return sprite
