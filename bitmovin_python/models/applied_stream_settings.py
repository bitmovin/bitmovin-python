# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class AppliedStreamSettings(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = {
            'width': 'int',
            'height': 'int'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'width': 'width',
            'height': 'height'
        }
        return attributes

    def __init__(self, width=None, height=None, *args, **kwargs):

        self._width = None
        self._height = None
        self.discriminator = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def width(self):
        """Gets the width of this AppliedStreamSettings.

        The applied width. Useful if the width in the configuration was undefined

        :return: The width of this AppliedStreamSettings.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this AppliedStreamSettings.

        The applied width. Useful if the width in the configuration was undefined

        :param width: The width of this AppliedStreamSettings.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

            self._width = width


    @property
    def height(self):
        """Gets the height of this AppliedStreamSettings.

        The applied height. Useful if the height in the configuration was undefined

        :return: The height of this AppliedStreamSettings.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this AppliedStreamSettings.

        The applied height. Useful if the height in the configuration was undefined

        :param height: The height of this AppliedStreamSettings.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

            self._height = height

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

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
            if issubclass(AppliedStreamSettings, dict):
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
        if not isinstance(other, AppliedStreamSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
