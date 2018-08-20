from bitmovin.utils import Serializable

from bitmovin.errors import InvalidTypeError

from bitmovin.resources.enums import PictureFieldParity, DeinterlaceMode
from . import AbstractFilter


class DeinterlaceFilter(AbstractFilter, Serializable):

    def __init__(self, name=None, parity=None, mode=None, id_=None, custom_data=None,
                 description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self._parity = None
        self._mode = None

        self.parity = parity
        self.mode = mode

    @property
    def parity(self):
        return self._parity

    @parity.setter
    def parity(self, new_value):
        if new_value is None:
            return
        if isinstance(new_value, str):
            self._parity = new_value
        elif isinstance(new_value, PictureFieldParity):
            self._parity = new_value.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for parity: must be either str or PictureFieldParity!'.format(type(new_value)))

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, new_value):
        if new_value is None:
            return
        if isinstance(new_value, str):
            self._mode = new_value
        elif isinstance(new_value, DeinterlaceMode):
            self._mode = new_value.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for mode: must be either str or DeinterlaceMode!'.format(type(new_value)))

    def serialize(self):
        serialized = super().serialize()
        serialized['mode'] = self.mode
        serialized['parity'] = self.parity
        return serialized

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        parity = json_object.get('parity')
        mode = json_object.get('mode')
        name = json_object.get('name')
        description = json_object.get('description')
        deinterlace_filter = DeinterlaceFilter(parity=parity, mode=mode, id_=id_, name=name, description=description)
        return deinterlace_filter
