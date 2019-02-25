# coding: utf-8

from bitmovin_python.models.audio_mix_channel import AudioMixChannel
from bitmovin_python.models.audio_mix_channel_layout import AudioMixChannelLayout
from bitmovin_python.models.filter import Filter
from bitmovin_python.models.filter_type import FilterType
import pprint
import six
from datetime import datetime
from enum import Enum


class AudioMixFilter(Filter):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AudioMixFilter, self).openapi_types
        types.update({
            'channel_layout': 'AudioMixChannelLayout',
            'audio_mix_channels': 'list[AudioMixChannel]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AudioMixFilter, self).attribute_map
        attributes.update({
            'channel_layout': 'channelLayout',
            'audio_mix_channels': 'audioMixChannels'
        })
        return attributes

    def __init__(self, channel_layout=None, audio_mix_channels=None, *args, **kwargs):
        super(AudioMixFilter, self).__init__(*args, **kwargs)

        self._channel_layout = None
        self._audio_mix_channels = None
        self.discriminator = None

        self.channel_layout = channel_layout
        self.audio_mix_channels = audio_mix_channels

    @property
    def channel_layout(self):
        """Gets the channel_layout of this AudioMixFilter.

        Channel layout of the audio codec configuration

        :return: The channel_layout of this AudioMixFilter.
        :rtype: AudioMixChannelLayout
        """
        return self._channel_layout

    @channel_layout.setter
    def channel_layout(self, channel_layout):
        """Sets the channel_layout of this AudioMixFilter.

        Channel layout of the audio codec configuration

        :param channel_layout: The channel_layout of this AudioMixFilter.
        :type: AudioMixChannelLayout
        """

        if channel_layout is not None:
            if not isinstance(channel_layout, AudioMixChannelLayout):
                raise TypeError("Invalid type for `channel_layout`, type has to be `AudioMixChannelLayout`")

            self._channel_layout = channel_layout


    @property
    def audio_mix_channels(self):
        """Gets the audio_mix_channels of this AudioMixFilter.

        List of mixed channels that matches the channel layout

        :return: The audio_mix_channels of this AudioMixFilter.
        :rtype: list[AudioMixChannel]
        """
        return self._audio_mix_channels

    @audio_mix_channels.setter
    def audio_mix_channels(self, audio_mix_channels):
        """Sets the audio_mix_channels of this AudioMixFilter.

        List of mixed channels that matches the channel layout

        :param audio_mix_channels: The audio_mix_channels of this AudioMixFilter.
        :type: list[AudioMixChannel]
        """

        if audio_mix_channels is not None:
            if not isinstance(audio_mix_channels, list):
                raise TypeError("Invalid type for `audio_mix_channels`, type has to be `list[AudioMixChannel]`")

            self._audio_mix_channels = audio_mix_channels

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AudioMixFilter, self).to_dict()

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
            if issubclass(AudioMixFilter, dict):
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
        if not isinstance(other, AudioMixFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
