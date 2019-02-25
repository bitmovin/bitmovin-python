# coding: utf-8

from bitmovin_python.models.source_channel import SourceChannel
import pprint
import six
from datetime import datetime
from enum import Enum


class AudioMixChannel(object):
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
            'channel_number': 'int',
            'source_channels': 'list[SourceChannel]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'channel_number': 'channelNumber',
            'source_channels': 'sourceChannels'
        }
        return attributes

    def __init__(self, channel_number=None, source_channels=None, *args, **kwargs):

        self._channel_number = None
        self._source_channels = None
        self.discriminator = None

        self.channel_number = channel_number
        self.source_channels = source_channels

    @property
    def channel_number(self):
        """Gets the channel_number of this AudioMixChannel.

        Channel number of this mix (starting with 0)

        :return: The channel_number of this AudioMixChannel.
        :rtype: int
        """
        return self._channel_number

    @channel_number.setter
    def channel_number(self, channel_number):
        """Sets the channel_number of this AudioMixChannel.

        Channel number of this mix (starting with 0)

        :param channel_number: The channel_number of this AudioMixChannel.
        :type: int
        """

        if channel_number is not None:
            if not isinstance(channel_number, int):
                raise TypeError("Invalid type for `channel_number`, type has to be `int`")

            self._channel_number = channel_number


    @property
    def source_channels(self):
        """Gets the source_channels of this AudioMixChannel.

        List of source channels to be mixed

        :return: The source_channels of this AudioMixChannel.
        :rtype: list[SourceChannel]
        """
        return self._source_channels

    @source_channels.setter
    def source_channels(self, source_channels):
        """Sets the source_channels of this AudioMixChannel.

        List of source channels to be mixed

        :param source_channels: The source_channels of this AudioMixChannel.
        :type: list[SourceChannel]
        """

        if source_channels is not None:
            if not isinstance(source_channels, list):
                raise TypeError("Invalid type for `source_channels`, type has to be `list[SourceChannel]`")

            self._source_channels = source_channels

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
            if issubclass(AudioMixChannel, dict):
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
        if not isinstance(other, AudioMixChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
