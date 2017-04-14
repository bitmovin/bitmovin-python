from bitmovin.resources.models import AbstractModel
from bitmovin.resources import AbstractNameDescriptionResource
from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable
from .encoding_output import EncodingOutput


class Sprite(AbstractNameDescriptionResource, AbstractModel, Serializable):

    def __init__(self, height, width, sprite_name, vtt_name, outputs, distance=None, id_=None, custom_data=None,
                 name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self._outputs = None

        self.height = height
        self.width = width
        self.distance = distance
        self.spriteName = sprite_name
        self.vttName = vtt_name

        if outputs is not None and not isinstance(outputs, list):
            raise InvalidTypeError('outputs must be a list')

        self.outputs = outputs

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        custom_data = json_object.get('customData')
        width = json_object.get('width')
        height = json_object.get('height')
        distance = json_object.get('distance')
        sprite_name = json_object.get('spriteName')
        vtt_name = json_object.get('vttName')
        outputs = json_object.get('outputs')
        name = json_object.get('name')
        description = json_object.get('description')

        sprite = Sprite(id_=id_, custom_data=custom_data, outputs=outputs, name=name, description=description,
                        height=height, width=width, sprite_name=sprite_name, vtt_name=vtt_name, distance=distance)
        return sprite

    @property
    def outputs(self):
        return self._outputs

    @outputs.setter
    def outputs(self, new_outputs):
        if new_outputs is None:
            return

        if not isinstance(new_outputs, list):
            raise InvalidTypeError('new_outputs has to be a list of EncodingOutput objects')

        if all(isinstance(output, EncodingOutput) for output in new_outputs):
            self._outputs = new_outputs
        else:
            outputs = []
            for json_object in new_outputs:
                output = EncodingOutput.parse_from_json_object(json_object)
                outputs.append(output)
            self._outputs = outputs

    def serialize(self):
        serialized = super().serialize()
        serialized['outputs'] = self.outputs
        return serialized
