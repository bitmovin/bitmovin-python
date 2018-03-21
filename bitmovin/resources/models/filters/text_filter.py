from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums.font import Font
from bitmovin.utils import Serializable
from . import AbstractFilter


class TextFilter(AbstractFilter, Serializable):

    def __init__(self, x, y, text=None, timecode=None, shadow_y=None, shadow_x=None, shadow_color=None, alpha=None,
                 font_size=None, font=None, font_color=None, fix_bounds=None, border_width=None, line_spacing=None,
                 box_color=None, box_border_width=None, box=None, id_=None, custom_data=None,
                 name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self._font = None

        self.x = x
        self.y = y
        self.text = text
        self.timecode = timecode
        self.shadowY = shadow_y
        self.shadowX = shadow_x
        self.shadowColor = shadow_color
        self.alpha = alpha
        self.fontSize = font_size
        self.font = font
        self.fontColor = font_color
        self.fixBounds = fix_bounds
        self.borderWidth = border_width
        self.lineSpacing = line_spacing
        self.boxColor = box_color
        self.boxBorderWidth = box_border_width
        self.box = box

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, new_value):
        if new_value is None:
            return
        if isinstance(new_value, str):
            self._font = new_value
        elif isinstance(new_value, Font):
            self._font = new_value.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for font: must be either str or Font!'.format(type(new_value)))

    def serialize(self):
        serialized = super().serialize()
        serialized['font'] = self.font
        return serialized

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        x = json_object['x']
        y = json_object['y']

        text = json_object.get('text')
        timecode = json_object.get('timecode')
        shadow_x = json_object.get('shadowX')
        shadow_y = json_object.get('shadowY')
        shadow_color = json_object.get('shadowColor')
        alpha = json_object.get('alpha')
        font_size = json_object.get('fontSize')
        font = json_object.get('font')
        font_color = json_object.get('fontColor')
        fix_bounds = json_object.get('fixBounds')
        border_width = json_object.get('borderWidth')
        line_spacing = json_object.get('lineSpacing')
        name = json_object.get('name')
        description = json_object.get('description')

        text_filter = TextFilter(id_=id_, x=x, y=y, text=text, timecode=timecode, shadow_x=shadow_x,
                                 shadow_y=shadow_y, shadow_color=shadow_color, alpha=alpha, font_size=font_size,
                                 font=font, font_color=font_color, fix_bounds=fix_bounds,
                                 border_width=border_width, line_spacing=line_spacing, name=name,
                                 description=description)
        return text_filter
