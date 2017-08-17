from bitmovin.resources.models import AbstractModel
from bitmovin.resources import AbstractNameDescriptionResource
from bitmovin.resources.enums import ThumbnailUnit
from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable
from .encoding_output import EncodingOutput


class Thumbnail(AbstractNameDescriptionResource, AbstractModel, Serializable):
    def __init__(self, height, positions, outputs, pattern, unit=None, id_=None, custom_data=None,
                 name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self._outputs = None
        self._positions = None
        self._unit = None

        self.height = height
        self.positions = positions
        self.unit = unit
        self.pattern = pattern
        
        if not isinstance(positions, list):
            raise InvalidTypeError('positions must be a list')

        if outputs is not None and not isinstance(outputs, list):
            raise InvalidTypeError('outputs must be a list')

        self.outputs = outputs
        self.positions = positions

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        custom_data = json_object.get('customData')
        height = json_object.get('height')
        unit = json_object.get('unit')
        pattern = json_object.get('pattern')
        outputs = json_object.get('outputs')
        name = json_object.get('name')
        description = json_object.get('description')
        positions = json_object.get('positions')

        thumbnail = Thumbnail(id_=id_, custom_data=custom_data, outputs=outputs, name=name, description=description,
                              height=height, unit=unit, pattern=pattern, positions=positions)
        return thumbnail

    @property
    def positions(self):
        return self._positions

    @positions.setter
    def positions(self, new_positions):
        if new_positions is None:
            return

        if not isinstance(new_positions, list):
            raise InvalidTypeError('new_positions has to be a list of numeric')

        if all(isinstance(output, EncodingOutput) for output in new_positions):
            self._positions = new_positions
        else:
            positions = []
            for position in new_positions:
                positions.append(position)
            self._positions = positions
            
    @property
    def unit(self):
        if self._unit is not None:
            return self._unit
        else:
            return ThumbnailUnit.default().value

    @unit.setter
    def unit(self, new_unit):
        if new_unit is None:
            return
        if isinstance(new_unit, str):
            self._unit = new_unit
        elif isinstance(new_unit, ThumbnailUnit):
            self._unit = new_unit.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for unit: must be either str or ThumbnailUnit!'.format(type(new_unit)))

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
        serialized['unit'] = self.unit
        serialized['positions'] = self.positions
        return serialized
