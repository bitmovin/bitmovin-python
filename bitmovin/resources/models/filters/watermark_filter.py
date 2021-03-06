from bitmovin.resources.enums import WatermarkUnit
from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable
from . import AbstractFilter


class WatermarkFilter(AbstractFilter, Serializable):

    def __init__(self, image, left=None, right=None, top=None, bottom=None, id_=None, custom_data=None,
                 name=None, description=None, unit=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.image = image
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

        self._unit = None
        self.unit = unit

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, new_unit):
        if new_unit is None:
            self._unit = None
            return
        if isinstance(new_unit, str):
            self._unit = new_unit
        elif isinstance(new_unit, WatermarkUnit):
            self._unit = new_unit.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for unit: must be either str or WatermarkUnit!'.format(type(new_unit)))

    def serialize(self):
        serialized = super().serialize()
        serialized['unit'] = self.unit
        return serialized

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        image = json_object['image']
        left = json_object.get('left')
        right = json_object.get('right')
        top = json_object.get('top')
        bottom = json_object.get('bottom')
        name = json_object.get('name')
        description = json_object.get('description')
        unit = json_object.get('unit')
        watermark_filter = WatermarkFilter(
            image=image, left=left, right=right, top=top, bottom=bottom, id_=id_, name=name, description=description,
            unit=unit)
        return watermark_filter
