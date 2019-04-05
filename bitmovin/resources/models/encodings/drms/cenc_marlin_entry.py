from bitmovin.utils import Serializable


class CENCMarlinEntry(Serializable):

    def __init__(self):
        super().__init__()

    @classmethod
    def parse_from_json_object(cls, json_object):
        cenc_marlin_entry = CENCMarlinEntry()
        return cenc_marlin_entry
    
    def serialize(self):
        serialized = super().serialize()
        return serialized
