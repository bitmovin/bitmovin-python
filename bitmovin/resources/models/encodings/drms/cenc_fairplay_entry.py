from bitmovin.utils import Serializable


class CENCFairPlayEntry(Serializable):

    def __init__(self, iv, uri):
        super().__init__()
        self.iv = iv
        self.uri = uri

    @classmethod
    def parse_from_json_object(cls, json_object):
        iv = json_object.get('iv')
        uri = json_object.get('uri')
        cenc_fairplay_entry = CENCFairPlayEntry(iv=iv, uri=uri)

        return cenc_fairplay_entry
