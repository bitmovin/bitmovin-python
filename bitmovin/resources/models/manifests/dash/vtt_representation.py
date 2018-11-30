from bitmovin.resources.models import AbstractModel
from bitmovin.utils import Serializable


class VttRepresentation(AbstractModel, Serializable):

    def __init__(self, vtt_url, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self.vttUrl = vtt_url

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        custom_data = json_object.get('customData')
        vtt_url = json_object['vttUrl']

        vtt_representation = VttRepresentation(
            id_=id_, custom_data=custom_data, vtt_url=vtt_url)
        return vtt_representation
