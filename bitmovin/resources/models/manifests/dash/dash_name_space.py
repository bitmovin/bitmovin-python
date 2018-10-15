from bitmovin.utils import Serializable


class DASHNamespace(Serializable):

    def __init__(self, prefix, uri):
        super().__init__()
        self.prefix = prefix
        self.uri = uri

    @classmethod
    def parse_from_json_object(cls, json_object):
        prefix = json_object.get('prefix')
        uri = json_object.get('uri')
        namespace = DASHNamespace(prefix=prefix, uri=uri)
        return namespace

    def serialize(self):
        serialized = super().serialize()
        serialized['prefix'] = self.prefix
        serialized['uri'] = self.uri
        return serialized
