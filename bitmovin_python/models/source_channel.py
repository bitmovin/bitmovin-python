# coding: utf-8

from bitmovin_python.models.source_channel_type import SourceChannelType
import pprint
import six
from datetime import datetime
from enum import Enum


class SourceChannel(object):
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
            'gain': 'float',
            'type': 'SourceChannelType',
            'channel_number': 'int'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'gain': 'gain',
            'type': 'type',
            'channel_number': 'channelNumber'
        }
        return attributes

    def __init__(self, gain=None, type=None, channel_number=None, *args, **kwargs):

        self._gain = None
        self._type = None
        self._channel_number = None
        self.discriminator = None

        if gain is not None:
            self.gain = gain
        self.type = type
        if channel_number is not None:
            self.channel_number = channel_number

    @property
    def gain(self):
        """Gets the gain of this SourceChannel.

        Gain for this source channel. Default is 1.0.

        :return: The gain of this SourceChannel.
        :rtype: float
        """
        return self._gain

    @gain.setter
    def gain(self, gain):
        """Sets the gain of this SourceChannel.

        Gain for this source channel. Default is 1.0.

        :param gain: The gain of this SourceChannel.
        :type: float
        """

        if gain is not None:
            if not isinstance(gain, float):
                raise TypeError("Invalid type for `gain`, type has to be `float`")

            self._gain = gain


    @property
    def type(self):
        """Gets the type of this SourceChannel.


        :return: The type of this SourceChannel.
        :rtype: SourceChannelType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SourceChannel.


        :param type: The type of this SourceChannel.
        :type: SourceChannelType
        """

        if type is not None:
            if not isinstance(type, SourceChannelType):
                raise TypeError("Invalid type for `type`, type has to be `SourceChannelType`")

            self._type = type


    @property
    def channel_number(self):
        """Gets the channel_number of this SourceChannel.

        Number of this source channel. If type is 'CHANNEL_NUMBER', this must be set.

        :return: The channel_number of this SourceChannel.
        :rtype: int
        """
        return self._channel_number

    @channel_number.setter
    def channel_number(self, channel_number):
        """Sets the channel_number of this SourceChannel.

        Number of this source channel. If type is 'CHANNEL_NUMBER', this must be set.

        :param channel_number: The channel_number of this SourceChannel.
        :type: int
        """

        if channel_number is not None:
            if not isinstance(channel_number, int):
                raise TypeError("Invalid type for `channel_number`, type has to be `int`")

            self._channel_number = channel_number

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
            if issubclass(SourceChannel, dict):
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
        if not isinstance(other, SourceChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
