# coding: utf-8

from bitmovin_python.models.media_stream import MediaStream
import pprint
import six
from datetime import datetime
from enum import Enum


class AudioStream(MediaStream):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AudioStream, self).openapi_types
        types.update({
            'sample_rate': 'int',
            'bitrate': 'int',
            'rate': 'int',
            'channel_format': 'str',
            'language': 'str',
            'hearing_impaired': 'bool'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AudioStream, self).attribute_map
        attributes.update({
            'sample_rate': 'sampleRate',
            'bitrate': 'bitrate',
            'rate': 'rate',
            'channel_format': 'channelFormat',
            'language': 'language',
            'hearing_impaired': 'hearingImpaired'
        })
        return attributes

    def __init__(self, sample_rate=None, bitrate=None, rate=None, channel_format=None, language=None, hearing_impaired=None, *args, **kwargs):
        super(AudioStream, self).__init__(*args, **kwargs)

        self._sample_rate = None
        self._bitrate = None
        self._rate = None
        self._channel_format = None
        self._language = None
        self._hearing_impaired = None
        self.discriminator = None

        if sample_rate is not None:
            self.sample_rate = sample_rate
        if bitrate is not None:
            self.bitrate = bitrate
        if rate is not None:
            self.rate = rate
        if channel_format is not None:
            self.channel_format = channel_format
        if language is not None:
            self.language = language
        if hearing_impaired is not None:
            self.hearing_impaired = hearing_impaired

    @property
    def sample_rate(self):
        """Gets the sample_rate of this AudioStream.

        Audio sampling rate in Hz

        :return: The sample_rate of this AudioStream.
        :rtype: int
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this AudioStream.

        Audio sampling rate in Hz

        :param sample_rate: The sample_rate of this AudioStream.
        :type: int
        """

        if sample_rate is not None:
            if not isinstance(sample_rate, int):
                raise TypeError("Invalid type for `sample_rate`, type has to be `int`")

            self._sample_rate = sample_rate


    @property
    def bitrate(self):
        """Gets the bitrate of this AudioStream.

        Bitrate in bps

        :return: The bitrate of this AudioStream.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this AudioStream.

        Bitrate in bps

        :param bitrate: The bitrate of this AudioStream.
        :type: int
        """

        if bitrate is not None:
            if not isinstance(bitrate, int):
                raise TypeError("Invalid type for `bitrate`, type has to be `int`")

            self._bitrate = bitrate


    @property
    def rate(self):
        """Gets the rate of this AudioStream.

        Bitrate in bps

        :return: The rate of this AudioStream.
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this AudioStream.

        Bitrate in bps

        :param rate: The rate of this AudioStream.
        :type: int
        """

        if rate is not None:
            if not isinstance(rate, int):
                raise TypeError("Invalid type for `rate`, type has to be `int`")

            self._rate = rate


    @property
    def channel_format(self):
        """Gets the channel_format of this AudioStream.

        Audio channel format

        :return: The channel_format of this AudioStream.
        :rtype: str
        """
        return self._channel_format

    @channel_format.setter
    def channel_format(self, channel_format):
        """Sets the channel_format of this AudioStream.

        Audio channel format

        :param channel_format: The channel_format of this AudioStream.
        :type: str
        """

        if channel_format is not None:
            if not isinstance(channel_format, str):
                raise TypeError("Invalid type for `channel_format`, type has to be `str`")

            self._channel_format = channel_format


    @property
    def language(self):
        """Gets the language of this AudioStream.

        Language of the stream

        :return: The language of this AudioStream.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AudioStream.

        Language of the stream

        :param language: The language of this AudioStream.
        :type: str
        """

        if language is not None:
            if not isinstance(language, str):
                raise TypeError("Invalid type for `language`, type has to be `str`")

            self._language = language


    @property
    def hearing_impaired(self):
        """Gets the hearing_impaired of this AudioStream.

        Hearing impaired support

        :return: The hearing_impaired of this AudioStream.
        :rtype: bool
        """
        return self._hearing_impaired

    @hearing_impaired.setter
    def hearing_impaired(self, hearing_impaired):
        """Sets the hearing_impaired of this AudioStream.

        Hearing impaired support

        :param hearing_impaired: The hearing_impaired of this AudioStream.
        :type: bool
        """

        if hearing_impaired is not None:
            if not isinstance(hearing_impaired, bool):
                raise TypeError("Invalid type for `hearing_impaired`, type has to be `bool`")

            self._hearing_impaired = hearing_impaired

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AudioStream, self).to_dict()

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
            if issubclass(AudioStream, dict):
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
        if not isinstance(other, AudioStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
