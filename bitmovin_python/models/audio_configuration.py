# coding: utf-8

from bitmovin_python.models.codec_config_type import CodecConfigType
from bitmovin_python.models.codec_configuration import CodecConfiguration
import pprint
import six
from datetime import datetime
from enum import Enum


class AudioConfiguration(CodecConfiguration):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AudioConfiguration, self).openapi_types
        types.update({
            'bitrate': 'int',
            'rate': 'float'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AudioConfiguration, self).attribute_map
        attributes.update({
            'bitrate': 'bitrate',
            'rate': 'rate'
        })
        return attributes

    def __init__(self, bitrate=None, rate=None, *args, **kwargs):
        super(AudioConfiguration, self).__init__(*args, **kwargs)

        self._bitrate = None
        self._rate = None
        self.discriminator = None

        self.bitrate = bitrate
        if rate is not None:
            self.rate = rate

    @property
    def bitrate(self):
        """Gets the bitrate of this AudioConfiguration.

        Target bitrate for the encoded audio in bps

        :return: The bitrate of this AudioConfiguration.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this AudioConfiguration.

        Target bitrate for the encoded audio in bps

        :param bitrate: The bitrate of this AudioConfiguration.
        :type: int
        """

        if bitrate is not None:
            if not isinstance(bitrate, int):
                raise TypeError("Invalid type for `bitrate`, type has to be `int`")

            self._bitrate = bitrate


    @property
    def rate(self):
        """Gets the rate of this AudioConfiguration.

        Audio sampling rate Hz

        :return: The rate of this AudioConfiguration.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this AudioConfiguration.

        Audio sampling rate Hz

        :param rate: The rate of this AudioConfiguration.
        :type: float
        """

        if rate is not None:
            if not isinstance(rate, float):
                raise TypeError("Invalid type for `rate`, type has to be `float`")

            self._rate = rate

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AudioConfiguration, self).to_dict()

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
            if issubclass(AudioConfiguration, dict):
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
        if not isinstance(other, AudioConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
