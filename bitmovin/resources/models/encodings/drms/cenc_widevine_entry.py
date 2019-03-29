from bitmovin.utils import Serializable


class CENCWidevineEntry(Serializable):

    def __init__(self, pssh):
        super().__init__()
        self.pssh = pssh

    @classmethod
    def parse_from_json_object(cls, json_object):
        pssh = json_object.get('pssh')
        cenc_widevine_entry = CENCWidevineEntry(pssh)
        return cenc_widevine_entry
    
    def serialize(self):
        serialized = super().serialize()
        serialized['pssh'] = self.pssh
        return serialized
