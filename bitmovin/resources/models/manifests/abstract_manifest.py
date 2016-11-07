from bitmovin.errors import InvalidTypeError
from bitmovin.resources.models import AbstractModel, EncodingOutput
from bitmovin.utils import Serializable


class AbstractManifest(AbstractModel, Serializable):

    def __init__(self, id_, name, outputs, description=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self.name = name
        self.description = description
        self._outputs = None
        if outputs is not None and not isinstance(outputs, list):
            raise InvalidTypeError('outputs must be a list')
        self.outputs = outputs

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        name = json_object['name']
        outputs = json_object['outputs']
        description = json_object.get('description')
        custom_data = json_object.get('customData')
        abstract_manifest = AbstractManifest(
            id_=id_, name=name, outputs=outputs, description=description, custom_data=custom_data)
        return abstract_manifest

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
