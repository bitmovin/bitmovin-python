from bitmovin.resources.models import AbstractModel
from bitmovin.resources import AbstractNameDescriptionResource


class AbstractCodecConfiguration(AbstractNameDescriptionResource, AbstractModel):

    def __init__(self, id_, name, description=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        name = json_object.get('name')
        description = json_object.get('description')
        custom_data = json_object.get('customData')
        abstract_codec_configuration = AbstractCodecConfiguration(
            id_=id_, name=name, description=description, custom_data=custom_data)
        return abstract_codec_configuration
