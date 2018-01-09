from bitmovin.resources.enums.crop_filter_unit import CropFilterUnit
from bitmovin.utils import Serializable
from bitmovin.errors import InvalidTypeError
from . import AbstractFilter


class CropFilter(AbstractFilter, Serializable):

    def __init__(self, name=None, left=None, right=None, top=None, bottom=None, unit=None, id_=None, custom_data=None,
                 description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self._unit = None

        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.unit = unit

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        left = json_object.get('left')
        right = json_object.get('right')
        top = json_object.get('top')
        bottom = json_object.get('bottom')
        unit = json_object.get('unit')
        name = json_object.get('name')
        description = json_object.get('description')
        crop_filter = CropFilter(
            left=left, right=right, top=top, bottom=bottom, unit=unit, id_=id_, name=name, description=description)
        return crop_filter

    @property
    def unit(self):
        if self._unit is not None:
            return self._unit
        else:
            return None # API sets the default value to PIXELS.

    @unit.setter
    def unit(self, new_unit):
        if new_unit is None:
            return
        if isinstance(new_unit, str):
            self._unit = new_unit
        elif isinstance(new_unit, CropFilterUnit):
            self._unit = new_unit.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for unit: must be either str or CropFilterUnit!'.format(type(new_unit)))

    def serialize(self):
        serialized = super().serialize()
        serialized['unit'] = self.unit
        return serialized
