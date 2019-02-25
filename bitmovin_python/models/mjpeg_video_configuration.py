# coding: utf-8

from bitmovin_python.models.codec_config_type import CodecConfigType
from bitmovin_python.models.codec_configuration import CodecConfiguration
from bitmovin_python.models.pixel_format import PixelFormat
import pprint
import six
from datetime import datetime
from enum import Enum


class MjpegVideoConfiguration(CodecConfiguration):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(MjpegVideoConfiguration, self).openapi_types
        types.update({
            'width': 'int',
            'height': 'int',
            'rate': 'float',
            'q_scale': 'int',
            'pixel_format': 'PixelFormat'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(MjpegVideoConfiguration, self).attribute_map
        attributes.update({
            'width': 'width',
            'height': 'height',
            'rate': 'rate',
            'q_scale': 'qScale',
            'pixel_format': 'pixelFormat'
        })
        return attributes

    def __init__(self, width=None, height=None, rate=None, q_scale=None, pixel_format=None, *args, **kwargs):
        super(MjpegVideoConfiguration, self).__init__(*args, **kwargs)

        self._width = None
        self._height = None
        self._rate = None
        self._q_scale = None
        self._pixel_format = None
        self.discriminator = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        self.rate = rate
        self.q_scale = q_scale
        if pixel_format is not None:
            self.pixel_format = pixel_format

    @property
    def width(self):
        """Gets the width of this MjpegVideoConfiguration.

        Width of the encoded video

        :return: The width of this MjpegVideoConfiguration.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this MjpegVideoConfiguration.

        Width of the encoded video

        :param width: The width of this MjpegVideoConfiguration.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

            self._width = width


    @property
    def height(self):
        """Gets the height of this MjpegVideoConfiguration.

        Height of the encoded video

        :return: The height of this MjpegVideoConfiguration.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this MjpegVideoConfiguration.

        Height of the encoded video

        :param height: The height of this MjpegVideoConfiguration.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

            self._height = height


    @property
    def rate(self):
        """Gets the rate of this MjpegVideoConfiguration.

        Target frame rate of the encoded video!

        :return: The rate of this MjpegVideoConfiguration.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this MjpegVideoConfiguration.

        Target frame rate of the encoded video!

        :param rate: The rate of this MjpegVideoConfiguration.
        :type: float
        """

        if rate is not None:
            if not isinstance(rate, float):
                raise TypeError("Invalid type for `rate`, type has to be `float`")

            self._rate = rate


    @property
    def q_scale(self):
        """Gets the q_scale of this MjpegVideoConfiguration.

        The quality scale parameter

        :return: The q_scale of this MjpegVideoConfiguration.
        :rtype: int
        """
        return self._q_scale

    @q_scale.setter
    def q_scale(self, q_scale):
        """Sets the q_scale of this MjpegVideoConfiguration.

        The quality scale parameter

        :param q_scale: The q_scale of this MjpegVideoConfiguration.
        :type: int
        """

        if q_scale is not None:
            if not isinstance(q_scale, int):
                raise TypeError("Invalid type for `q_scale`, type has to be `int`")

            self._q_scale = q_scale


    @property
    def pixel_format(self):
        """Gets the pixel_format of this MjpegVideoConfiguration.


        :return: The pixel_format of this MjpegVideoConfiguration.
        :rtype: PixelFormat
        """
        return self._pixel_format

    @pixel_format.setter
    def pixel_format(self, pixel_format):
        """Sets the pixel_format of this MjpegVideoConfiguration.


        :param pixel_format: The pixel_format of this MjpegVideoConfiguration.
        :type: PixelFormat
        """

        if pixel_format is not None:
            if not isinstance(pixel_format, PixelFormat):
                raise TypeError("Invalid type for `pixel_format`, type has to be `PixelFormat`")

            self._pixel_format = pixel_format

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(MjpegVideoConfiguration, self).to_dict()

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
            if issubclass(MjpegVideoConfiguration, dict):
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
        if not isinstance(other, MjpegVideoConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
