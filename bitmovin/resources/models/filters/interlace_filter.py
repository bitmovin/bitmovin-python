from bitmovin.utils import Serializable

from bitmovin.errors import InvalidTypeError

from bitmovin.resources.enums import InterlaceMode, VerticalLowPassFilteringMode
from . import AbstractFilter


class InterlaceFilter(AbstractFilter, Serializable):

    def __init__(self, name=None, mode=None, vertical_low_pass_filtering_mode=None, id_=None, custom_data=None,
                 description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self._mode = None
        self._vertical_low_pass_filtering_mode = None

        self.mode = mode
        self.verticalLowPassFilteringMode = vertical_low_pass_filtering_mode

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, new_value):
        if new_value is None:
            self._mode = None
            return
        if isinstance(new_value, str):
            self._mode = new_value
        elif isinstance(new_value, InterlaceMode):
            self._mode = new_value.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for mode: must be either str or InterlaceMode!'.format(type(new_value)))

    @property
    def vertical_low_pass_filtering_mode(self):
        return self._vertical_low_pass_filtering_mode

    @vertical_low_pass_filtering_mode.setter
    def vertical_low_pass_filtering_mode(self, new_value):
        if new_value is None:
            self._vertical_low_pass_filtering_mode = None
            return
        if isinstance(new_value, str):
            self._vertical_low_pass_filtering_mode = new_value
        elif isinstance(new_value, VerticalLowPassFilteringMode):
            self._vertical_low_pass_filtering_mode = new_value.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for vertical_low_pass_filtering_mode: ' +
                'must be either str or VerticalLowPassFilteringMode!'.format(type(new_value))
            )

    def serialize(self):
        serialized = super().serialize()
        serialized['mode'] = self.mode
        serialized['verticalLowPassFilteringMode'] = self.vertical_low_pass_filtering_mode
        return serialized

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        mode = json_object.get('mode')
        vertical_low_pass_filtering_mode = json_object.get('verticalLowPassFilteringMode')
        name = json_object.get('name')
        description = json_object.get('description')
        interlace_filter = InterlaceFilter(
            mode=mode,
            vertical_low_pass_filtering_mode=vertical_low_pass_filtering_mode,
            id_=id_,
            name=name,
            description=description
        )
        return interlace_filter
