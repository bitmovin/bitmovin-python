from bitmovin.utils import Serializable


class CENCPlayReadyEntry(Serializable):

    def __init__(self, la_url=None, pssh=None):
        super().__init__()
        self.laUrl = la_url
        self.pssh = pssh

    @classmethod
    def parse_from_json_object(cls, json_object):
        pssh = json_object.get('pssh')
        la_url = json_object.get('laUrl')
        cenc_playready_entry = CENCPlayReadyEntry(la_url, pssh)
        return cenc_playready_entry
    
    def serialize(self):
        serialized = super().serialize()
        serialized['pssh'] = self.pssh
        serialized['laUrl'] = self.laUrl
        return serialized
