from bitmovin.resources import AbstractNameDescriptionResource
from bitmovin.resources.models import AbstractModel
from bitmovin.utils import Serializable


class AbstractTrimmingInputStream(AbstractNameDescriptionResource, AbstractModel, Serializable):

    def __init__(self, input_stream_id, id_=None, custom_data=None, name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.inputStreamId = input_stream_id

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        custom_data = json_object.get('customData')
        name = json_object.get('name')
        description = json_object.get('description')
        input_stream_id = json_object.get('inputStreamId')

        trimming_input_stream = AbstractTrimmingInputStream(
            input_stream_id=input_stream_id,
            id_=id_,
            custom_data=custom_data,
            name=name,
            description=description
        )

        return trimming_input_stream

    def serialize(self):
        serialized = super().serialize()
        return serialized
