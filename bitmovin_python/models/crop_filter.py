# coding: utf-8

from bitmovin_python.models.filter import Filter
from bitmovin_python.models.filter_type import FilterType
from bitmovin_python.models.position_unit import PositionUnit
import pprint
import six
from datetime import datetime
from enum import Enum


class CropFilter(Filter):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(CropFilter, self).openapi_types
        types.update({
            'left': 'int',
            'right': 'int',
            'top': 'int',
            'bottom': 'int',
            'unit': 'PositionUnit'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(CropFilter, self).attribute_map
        attributes.update({
            'left': 'left',
            'right': 'right',
            'top': 'top',
            'bottom': 'bottom',
            'unit': 'unit'
        })
        return attributes

    def __init__(self, left=None, right=None, top=None, bottom=None, unit=None, *args, **kwargs):
        super(CropFilter, self).__init__(*args, **kwargs)

        self._left = None
        self._right = None
        self._top = None
        self._bottom = None
        self._unit = None
        self.discriminator = None

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
    def left(self):
        """Gets the left of this CropFilter.

        Amount of pixels which will be cropped of the input video from the left side.

        :return: The left of this CropFilter.
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this CropFilter.

        Amount of pixels which will be cropped of the input video from the left side.

        :param left: The left of this CropFilter.
        :type: int
        """

        if left is not None:
            if not isinstance(left, int):
                raise TypeError("Invalid type for `left`, type has to be `int`")

            self._left = left


    @property
    def right(self):
        """Gets the right of this CropFilter.

        Amount of pixels which will be cropped of the input video from the right side.

        :return: The right of this CropFilter.
        :rtype: int
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this CropFilter.

        Amount of pixels which will be cropped of the input video from the right side.

        :param right: The right of this CropFilter.
        :type: int
        """

        if right is not None:
            if not isinstance(right, int):
                raise TypeError("Invalid type for `right`, type has to be `int`")

            self._right = right


    @property
    def top(self):
        """Gets the top of this CropFilter.

        Amount of pixels which will be cropped of the input video from the top.

        :return: The top of this CropFilter.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this CropFilter.

        Amount of pixels which will be cropped of the input video from the top.

        :param top: The top of this CropFilter.
        :type: int
        """

        if top is not None:
            if not isinstance(top, int):
                raise TypeError("Invalid type for `top`, type has to be `int`")

            self._top = top


    @property
    def bottom(self):
        """Gets the bottom of this CropFilter.

        Amount of pixels which will be cropped of the input video from the bottom.

        :return: The bottom of this CropFilter.
        :rtype: int
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """Sets the bottom of this CropFilter.

        Amount of pixels which will be cropped of the input video from the bottom.

        :param bottom: The bottom of this CropFilter.
        :type: int
        """

        if bottom is not None:
            if not isinstance(bottom, int):
                raise TypeError("Invalid type for `bottom`, type has to be `int`")

            self._bottom = bottom


    @property
    def unit(self):
        """Gets the unit of this CropFilter.


        :return: The unit of this CropFilter.
        :rtype: PositionUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this CropFilter.


        :param unit: The unit of this CropFilter.
        :type: PositionUnit
        """

        if unit is not None:
            if not isinstance(unit, PositionUnit):
                raise TypeError("Invalid type for `unit`, type has to be `PositionUnit`")

            self._unit = unit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(CropFilter, self).to_dict()

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
            if issubclass(CropFilter, dict):
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
        if not isinstance(other, CropFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
