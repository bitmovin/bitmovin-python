from bitmovin.errors import InvalidTypeError
from bitmovin.resources.models import AbstractModel, EncodingOutput
from bitmovin.resources import AbstractNameDescriptionResource
from bitmovin.utils import Serializable


class AbstractManifest(AbstractNameDescriptionResource, AbstractModel, Serializable):

    def __init__(self, id_, manifest_name, outputs, name=None, description=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.manifestName = manifest_name
        self._outputs = None
        if outputs is not None and not isinstance(outputs, list):
            raise InvalidTypeError('outputs must be a list')
        self.outputs = outputs

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        manifest_name = json_object.get('manifestName')
        outputs = json_object.get('outputs')
        name = json_object.get('name')
        description = json_object.get('description')
        custom_data = json_object.get('customData')
        abstract_manifest = AbstractManifest(
            id_=id_, manifest_name=manifest_name, outputs=outputs, custom_data=custom_data,
            name=name, description=description)
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
