# coding: utf-8

from bitmovin_python.models.filter import Filter
from bitmovin_python.models.filter_type import FilterType
from bitmovin_python.models.position_unit import PositionUnit
import pprint
import six
from datetime import datetime
from enum import Enum


class EnhancedWatermarkFilter(Filter):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(EnhancedWatermarkFilter, self).openapi_types
        types.update({
            'image': 'str',
            'left': 'float',
            'right': 'float',
            'top': 'float',
            'bottom': 'float',
            'unit': 'PositionUnit'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(EnhancedWatermarkFilter, self).attribute_map
        attributes.update({
            'image': 'image',
            'left': 'left',
            'right': 'right',
            'top': 'top',
            'bottom': 'bottom',
            'unit': 'unit'
        })
        return attributes

    def __init__(self, image=None, left=None, right=None, top=None, bottom=None, unit=None, *args, **kwargs):
        super(EnhancedWatermarkFilter, self).__init__(*args, **kwargs)

        self._image = None
        self._left = None
        self._right = None
        self._top = None
        self._bottom = None
        self._unit = None
        self.discriminator = None

        self.image = image
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
        if top is not None:
            self.top = top
        if bottom is not None:
            self.bottom = bottom
        if unit is not None:
            self.unit = unit

    @property
    def image(self):
        """Gets the image of this EnhancedWatermarkFilter.

        URL of the file to be used as watermark image. Supported image formats: PNG, JPEG, BMP, GIF

        :return: The image of this EnhancedWatermarkFilter.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this EnhancedWatermarkFilter.

        URL of the file to be used as watermark image. Supported image formats: PNG, JPEG, BMP, GIF

        :param image: The image of this EnhancedWatermarkFilter.
        :type: str
        """

        if image is not None:
            if not isinstance(image, str):
                raise TypeError("Invalid type for `image`, type has to be `str`")

            self._image = image


    @property
    def left(self):
        """Gets the left of this EnhancedWatermarkFilter.

        Distance from the left edge of the input video to the left edge of the watermark image. May not be set if 'right' is set.

        :return: The left of this EnhancedWatermarkFilter.
        :rtype: float
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this EnhancedWatermarkFilter.

        Distance from the left edge of the input video to the left edge of the watermark image. May not be set if 'right' is set.

        :param left: The left of this EnhancedWatermarkFilter.
        :type: float
        """

        if left is not None:
            if not isinstance(left, float):
                raise TypeError("Invalid type for `left`, type has to be `float`")

            self._left = left


    @property
    def right(self):
        """Gets the right of this EnhancedWatermarkFilter.

        Distance from the right edge of the input video to the right edge of the watermark image . May not be set if 'left' is set.

        :return: The right of this EnhancedWatermarkFilter.
        :rtype: float
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this EnhancedWatermarkFilter.

        Distance from the right edge of the input video to the right edge of the watermark image . May not be set if 'left' is set.

        :param right: The right of this EnhancedWatermarkFilter.
        :type: float
        """

        if right is not None:
            if not isinstance(right, float):
                raise TypeError("Invalid type for `right`, type has to be `float`")

            self._right = right


    @property
    def top(self):
        """Gets the top of this EnhancedWatermarkFilter.

        Distance from the top edge of the input video to the top edge of the watermark image. May not be set if 'bottom' is set.

        :return: The top of this EnhancedWatermarkFilter.
        :rtype: float
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this EnhancedWatermarkFilter.

        Distance from the top edge of the input video to the top edge of the watermark image. May not be set if 'bottom' is set.

        :param top: The top of this EnhancedWatermarkFilter.
        :type: float
        """

        if top is not None:
            if not isinstance(top, float):
                raise TypeError("Invalid type for `top`, type has to be `float`")

            self._top = top


    @property
    def bottom(self):
        """Gets the bottom of this EnhancedWatermarkFilter.

        Distance from the bottom edge of the input video to the bottom edge of the watermark image. May not be set if 'top' is set.

        :return: The bottom of this EnhancedWatermarkFilter.
        :rtype: float
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """Sets the bottom of this EnhancedWatermarkFilter.

        Distance from the bottom edge of the input video to the bottom edge of the watermark image. May not be set if 'top' is set.

        :param bottom: The bottom of this EnhancedWatermarkFilter.
        :type: float
        """

        if bottom is not None:
            if not isinstance(bottom, float):
                raise TypeError("Invalid type for `bottom`, type has to be `float`")

            self._bottom = bottom


    @property
    def unit(self):
        """Gets the unit of this EnhancedWatermarkFilter.


        :return: The unit of this EnhancedWatermarkFilter.
        :rtype: PositionUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this EnhancedWatermarkFilter.


        :param unit: The unit of this EnhancedWatermarkFilter.
        :type: PositionUnit
        """

        if unit is not None:
            if not isinstance(unit, PositionUnit):
                raise TypeError("Invalid type for `unit`, type has to be `PositionUnit`")

            self._unit = unit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(EnhancedWatermarkFilter, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(EnhancedWatermarkFilter, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EnhancedWatermarkFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
