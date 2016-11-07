from bitmovin.errors import InvalidTypeError
from bitmovin.resources.models import AbstractModel
from bitmovin.resources.models.encodings.encoding_output import EncodingOutput
from bitmovin.utils import Serializable


class DRM(AbstractModel, Serializable):

    def __init__(self, outputs=None, id_=None, custom_data=None):

        super().__init__(id_=id_, custom_data=custom_data)
        self._outputs = None
        if outputs is not None and not isinstance(outputs, list):
            raise InvalidTypeError('outputs must be a list')
        self.outputs = outputs

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        custom_data = json_object.get('customData')
        outputs = json_object.get('outputs')
        drm = DRM(id_=id_, custom_data=custom_data, outputs=outputs)
        return drm

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
