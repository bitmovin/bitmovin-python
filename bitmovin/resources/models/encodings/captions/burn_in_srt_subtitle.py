from bitmovin.resources import AbstractIdResource
from bitmovin.utils import Serializable


class BurnInSrtSubtitle(AbstractIdResource, Serializable):

    def __init__(self, input_id, input_path, id_=None):
        super().__init__(id_=id_)

        self.inputId = input_id
        self.inputPath = input_path

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        input_id = json_object['inputId']
        input_path = json_object['inputPath']

        burn_in_srt_subtitle = BurnInSrtSubtitle(input_id=input_id, input_path=input_path, id_=id_)

        return burn_in_srt_subtitle

    def serialize(self):
        serialized = super().serialize()
        return serialized
