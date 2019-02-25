# coding: utf-8

from bitmovin_python.models.codec_config_type import CodecConfigType
from bitmovin_python.models.codec_configuration import CodecConfiguration
from bitmovin_python.models.color_config import ColorConfig
from bitmovin_python.models.encoding_mode import EncodingMode
from bitmovin_python.models.pixel_format import PixelFormat
import pprint
import six
from datetime import datetime
from enum import Enum


class VideoConfiguration(CodecConfiguration):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(VideoConfiguration, self).openapi_types
        types.update({
            'width': 'int',
            'height': 'int',
            'bitrate': 'int',
            'rate': 'float',
            'pixel_format': 'PixelFormat',
            'color_config': 'ColorConfig',
            'sample_aspect_ratio_numerator': 'int',
            'sample_aspect_ratio_denominator': 'int',
            'encoding_mode': 'EncodingMode'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(VideoConfiguration, self).attribute_map
        attributes.update({
            'width': 'width',
            'height': 'height',
            'bitrate': 'bitrate',
            'rate': 'rate',
            'pixel_format': 'pixelFormat',
            'color_config': 'colorConfig',
            'sample_aspect_ratio_numerator': 'sampleAspectRatioNumerator',
            'sample_aspect_ratio_denominator': 'sampleAspectRatioDenominator',
            'encoding_mode': 'encodingMode'
        })
        return attributes

    def __init__(self, width=None, height=None, bitrate=None, rate=None, pixel_format=None, color_config=None, sample_aspect_ratio_numerator=None, sample_aspect_ratio_denominator=None, encoding_mode=None, *args, **kwargs):
        super(VideoConfiguration, self).__init__(*args, **kwargs)

        self._width = None
        self._height = None
        self._bitrate = None
        self._rate = None
        self._pixel_format = None
        self._color_config = None
        self._sample_aspect_ratio_numerator = None
        self._sample_aspect_ratio_denominator = None
        self._encoding_mode = None
        self.discriminator = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if bitrate is not None:
            self.bitrate = bitrate
        if rate is not None:
            self.rate = rate
        if pixel_format is not None:
            self.pixel_format = pixel_format
        if color_config is not None:
            self.color_config = color_config
        if sample_aspect_ratio_numerator is not None:
            self.sample_aspect_ratio_numerator = sample_aspect_ratio_numerator
        if sample_aspect_ratio_denominator is not None:
            self.sample_aspect_ratio_denominator = sample_aspect_ratio_denominator
        if encoding_mode is not None:
            self.encoding_mode = encoding_mode

    @property
    def width(self):
        """Gets the width of this VideoConfiguration.

        Width of the encoded video in pixels

        :return: The width of this VideoConfiguration.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this VideoConfiguration.

        Width of the encoded video in pixels

        :param width: The width of this VideoConfiguration.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

            self._width = width


    @property
    def height(self):
        """Gets the height of this VideoConfiguration.

        Height of the encoded video in pixels

        :return: The height of this VideoConfiguration.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this VideoConfiguration.

        Height of the encoded video in pixels

        :param height: The height of this VideoConfiguration.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

            self._height = height


    @property
    def bitrate(self):
        """Gets the bitrate of this VideoConfiguration.

        Target bitrate for the encoded video in bps. Either bitrate or crf is required.

        :return: The bitrate of this VideoConfiguration.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this VideoConfiguration.

        Target bitrate for the encoded video in bps. Either bitrate or crf is required.

        :param bitrate: The bitrate of this VideoConfiguration.
        :type: int
        """

        if bitrate is not None:
            if not isinstance(bitrate, int):
                raise TypeError("Invalid type for `bitrate`, type has to be `int`")

            self._bitrate = bitrate


    @property
    def rate(self):
        """Gets the rate of this VideoConfiguration.

        Target frame rate of the encoded video. Must be set for live encodings

        :return: The rate of this VideoConfiguration.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this VideoConfiguration.

        Target frame rate of the encoded video. Must be set for live encodings

        :param rate: The rate of this VideoConfiguration.
        :type: float
        """

        if rate is not None:
            if not isinstance(rate, float):
                raise TypeError("Invalid type for `rate`, type has to be `float`")

            self._rate = rate


    @property
    def pixel_format(self):
        """Gets the pixel_format of this VideoConfiguration.


        :return: The pixel_format of this VideoConfiguration.
        :rtype: PixelFormat
        """
        return self._pixel_format

    @pixel_format.setter
    def pixel_format(self, pixel_format):
        """Sets the pixel_format of this VideoConfiguration.


        :param pixel_format: The pixel_format of this VideoConfiguration.
        :type: PixelFormat
        """

        if pixel_format is not None:
            if not isinstance(pixel_format, PixelFormat):
                raise TypeError("Invalid type for `pixel_format`, type has to be `PixelFormat`")

            self._pixel_format = pixel_format


    @property
    def color_config(self):
        """Gets the color_config of this VideoConfiguration.


        :return: The color_config of this VideoConfiguration.
        :rtype: ColorConfig
        """
        return self._color_config

    @color_config.setter
    def color_config(self, color_config):
        """Sets the color_config of this VideoConfiguration.


        :param color_config: The color_config of this VideoConfiguration.
        :type: ColorConfig
        """

        if color_config is not None:
            if not isinstance(color_config, ColorConfig):
                raise TypeError("Invalid type for `color_config`, type has to be `ColorConfig`")

            self._color_config = color_config


    @property
    def sample_aspect_ratio_numerator(self):
        """Gets the sample_aspect_ratio_numerator of this VideoConfiguration.

        The numerator of the sample aspect ratio (also known as pixel aspect ratio). Must be set if sampleAspectRatioDenominator is set.

        :return: The sample_aspect_ratio_numerator of this VideoConfiguration.
        :rtype: int
        """
        return self._sample_aspect_ratio_numerator

    @sample_aspect_ratio_numerator.setter
    def sample_aspect_ratio_numerator(self, sample_aspect_ratio_numerator):
        """Sets the sample_aspect_ratio_numerator of this VideoConfiguration.

        The numerator of the sample aspect ratio (also known as pixel aspect ratio). Must be set if sampleAspectRatioDenominator is set.

        :param sample_aspect_ratio_numerator: The sample_aspect_ratio_numerator of this VideoConfiguration.
        :type: int
        """

        if sample_aspect_ratio_numerator is not None:
            if not isinstance(sample_aspect_ratio_numerator, int):
                raise TypeError("Invalid type for `sample_aspect_ratio_numerator`, type has to be `int`")

            self._sample_aspect_ratio_numerator = sample_aspect_ratio_numerator


    @property
    def sample_aspect_ratio_denominator(self):
        """Gets the sample_aspect_ratio_denominator of this VideoConfiguration.

        The denominator of the sample aspect ratio (also known as pixel aspect ratio). Must be set if sampleAspectRatioNumerator is set.

        :return: The sample_aspect_ratio_denominator of this VideoConfiguration.
        :rtype: int
        """
        return self._sample_aspect_ratio_denominator

    @sample_aspect_ratio_denominator.setter
    def sample_aspect_ratio_denominator(self, sample_aspect_ratio_denominator):
        """Sets the sample_aspect_ratio_denominator of this VideoConfiguration.

        The denominator of the sample aspect ratio (also known as pixel aspect ratio). Must be set if sampleAspectRatioNumerator is set.

        :param sample_aspect_ratio_denominator: The sample_aspect_ratio_denominator of this VideoConfiguration.
        :type: int
        """

        if sample_aspect_ratio_denominator is not None:
            if not isinstance(sample_aspect_ratio_denominator, int):
                raise TypeError("Invalid type for `sample_aspect_ratio_denominator`, type has to be `int`")

            self._sample_aspect_ratio_denominator = sample_aspect_ratio_denominator


    @property
    def encoding_mode(self):
        """Gets the encoding_mode of this VideoConfiguration.

        The mode of the encoding

        :return: The encoding_mode of this VideoConfiguration.
        :rtype: EncodingMode
        """
        return self._encoding_mode

    @encoding_mode.setter
    def encoding_mode(self, encoding_mode):
        """Sets the encoding_mode of this VideoConfiguration.

        The mode of the encoding

        :param encoding_mode: The encoding_mode of this VideoConfiguration.
        :type: EncodingMode
        """

        if encoding_mode is not None:
            if not isinstance(encoding_mode, EncodingMode):
                raise TypeError("Invalid type for `encoding_mode`, type has to be `EncodingMode`")

            self._encoding_mode = encoding_mode

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(VideoConfiguration, self).to_dict()

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
            if issubclass(VideoConfiguration, dict):
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
        if not isinstance(other, VideoConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
