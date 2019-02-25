# coding: utf-8

from bitmovin_python.models.convert_scc_position_mode import ConvertSccPositionMode
import pprint
import six
from datetime import datetime
from enum import Enum


class ConvertSccCaptionWebVttSettings(object):
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
            'position_mode': 'ConvertSccPositionMode',
            'remove_flash': 'bool',
            'remove_color': 'bool'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'position_mode': 'positionMode',
            'remove_flash': 'removeFlash',
            'remove_color': 'removeColor'
        }
        return attributes

    def __init__(self, position_mode=None, remove_flash=None, remove_color=None, *args, **kwargs):

        self._position_mode = None
        self._remove_flash = None
        self._remove_color = None
        self.discriminator = None

        if position_mode is not None:
            self.position_mode = position_mode
        if remove_flash is not None:
            self.remove_flash = remove_flash
        if remove_color is not None:
            self.remove_color = remove_color

    @property
    def position_mode(self):
        """Gets the position_mode of this ConvertSccCaptionWebVttSettings.


        :return: The position_mode of this ConvertSccCaptionWebVttSettings.
        :rtype: ConvertSccPositionMode
        """
        return self._position_mode

    @position_mode.setter
    def position_mode(self, position_mode):
        """Sets the position_mode of this ConvertSccCaptionWebVttSettings.


        :param position_mode: The position_mode of this ConvertSccCaptionWebVttSettings.
        :type: ConvertSccPositionMode
        """

        if position_mode is not None:
            if not isinstance(position_mode, ConvertSccPositionMode):
                raise TypeError("Invalid type for `position_mode`, type has to be `ConvertSccPositionMode`")

            self._position_mode = position_mode


    @property
    def remove_flash(self):
        """Gets the remove_flash of this ConvertSccCaptionWebVttSettings.

        Remove flash (blinking) information when converting SCC to WebVTT

        :return: The remove_flash of this ConvertSccCaptionWebVttSettings.
        :rtype: bool
        """
        return self._remove_flash

    @remove_flash.setter
    def remove_flash(self, remove_flash):
        """Sets the remove_flash of this ConvertSccCaptionWebVttSettings.

        Remove flash (blinking) information when converting SCC to WebVTT

        :param remove_flash: The remove_flash of this ConvertSccCaptionWebVttSettings.
        :type: bool
        """

        if remove_flash is not None:
            if not isinstance(remove_flash, bool):
                raise TypeError("Invalid type for `remove_flash`, type has to be `bool`")

            self._remove_flash = remove_flash


    @property
    def remove_color(self):
        """Gets the remove_color of this ConvertSccCaptionWebVttSettings.

        Remove color information when converting SCC to WebVTT

        :return: The remove_color of this ConvertSccCaptionWebVttSettings.
        :rtype: bool
        """
        return self._remove_color

    @remove_color.setter
    def remove_color(self, remove_color):
        """Sets the remove_color of this ConvertSccCaptionWebVttSettings.

        Remove color information when converting SCC to WebVTT

        :param remove_color: The remove_color of this ConvertSccCaptionWebVttSettings.
        :type: bool
        """

        if remove_color is not None:
            if not isinstance(remove_color, bool):
                raise TypeError("Invalid type for `remove_color`, type has to be `bool`")

            self._remove_color = remove_color

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
            if issubclass(ConvertSccCaptionWebVttSettings, dict):
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
        if not isinstance(other, ConvertSccCaptionWebVttSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
