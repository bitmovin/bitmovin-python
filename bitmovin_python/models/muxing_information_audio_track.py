# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class MuxingInformationAudioTrack(object):
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
            'index': 'int',
            'codec': 'str',
            'codec_iso': 'str',
            'bit_rate': 'int',
            'rate': 'int',
            'sample_rate': 'int',
            'channels': 'int',
            'duration': 'float'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'index': 'index',
            'codec': 'codec',
            'codec_iso': 'codecIso',
            'bit_rate': 'bitRate',
            'rate': 'rate',
            'sample_rate': 'sampleRate',
            'channels': 'channels',
            'duration': 'duration'
        }
        return attributes

    def __init__(self, index=None, codec=None, codec_iso=None, bit_rate=None, rate=None, sample_rate=None, channels=None, duration=None, *args, **kwargs):

        self._index = None
        self._codec = None
        self._codec_iso = None
        self._bit_rate = None
        self._rate = None
        self._sample_rate = None
        self._channels = None
        self._duration = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if codec is not None:
            self.codec = codec
        if codec_iso is not None:
            self.codec_iso = codec_iso
        if bit_rate is not None:
            self.bit_rate = bit_rate
        if rate is not None:
            self.rate = rate
        if sample_rate is not None:
            self.sample_rate = sample_rate
        if channels is not None:
            self.channels = channels
        if duration is not None:
            self.duration = duration

    @property
    def index(self):
        """Gets the index of this MuxingInformationAudioTrack.

        The stream index in the container

        :return: The index of this MuxingInformationAudioTrack.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this MuxingInformationAudioTrack.

        The stream index in the container

        :param index: The index of this MuxingInformationAudioTrack.
        :type: int
        """

        if index is not None:
            if not isinstance(index, int):
                raise TypeError("Invalid type for `index`, type has to be `int`")

            self._index = index


    @property
    def codec(self):
        """Gets the codec of this MuxingInformationAudioTrack.

        The codec used for the track

        :return: The codec of this MuxingInformationAudioTrack.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this MuxingInformationAudioTrack.

        The codec used for the track

        :param codec: The codec of this MuxingInformationAudioTrack.
        :type: str
        """

        if codec is not None:
            if not isinstance(codec, str):
                raise TypeError("Invalid type for `codec`, type has to be `str`")

            self._codec = codec


    @property
    def codec_iso(self):
        """Gets the codec_iso of this MuxingInformationAudioTrack.

        The codec string of the track

        :return: The codec_iso of this MuxingInformationAudioTrack.
        :rtype: str
        """
        return self._codec_iso

    @codec_iso.setter
    def codec_iso(self, codec_iso):
        """Sets the codec_iso of this MuxingInformationAudioTrack.

        The codec string of the track

        :param codec_iso: The codec_iso of this MuxingInformationAudioTrack.
        :type: str
        """

        if codec_iso is not None:
            if not isinstance(codec_iso, str):
                raise TypeError("Invalid type for `codec_iso`, type has to be `str`")

            self._codec_iso = codec_iso


    @property
    def bit_rate(self):
        """Gets the bit_rate of this MuxingInformationAudioTrack.

        The bitrate of the audio track

        :return: The bit_rate of this MuxingInformationAudioTrack.
        :rtype: int
        """
        return self._bit_rate

    @bit_rate.setter
    def bit_rate(self, bit_rate):
        """Sets the bit_rate of this MuxingInformationAudioTrack.

        The bitrate of the audio track

        :param bit_rate: The bit_rate of this MuxingInformationAudioTrack.
        :type: int
        """

        if bit_rate is not None:
            if not isinstance(bit_rate, int):
                raise TypeError("Invalid type for `bit_rate`, type has to be `int`")

            self._bit_rate = bit_rate


    @property
    def rate(self):
        """Gets the rate of this MuxingInformationAudioTrack.


        :return: The rate of this MuxingInformationAudioTrack.
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this MuxingInformationAudioTrack.


        :param rate: The rate of this MuxingInformationAudioTrack.
        :type: int
        """

        if rate is not None:
            if not isinstance(rate, int):
                raise TypeError("Invalid type for `rate`, type has to be `int`")

            self._rate = rate


    @property
    def sample_rate(self):
        """Gets the sample_rate of this MuxingInformationAudioTrack.

        The sampling rate of the audio stream

        :return: The sample_rate of this MuxingInformationAudioTrack.
        :rtype: int
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this MuxingInformationAudioTrack.

        The sampling rate of the audio stream

        :param sample_rate: The sample_rate of this MuxingInformationAudioTrack.
        :type: int
        """

        if sample_rate is not None:
            if not isinstance(sample_rate, int):
                raise TypeError("Invalid type for `sample_rate`, type has to be `int`")

            self._sample_rate = sample_rate


    @property
    def channels(self):
        """Gets the channels of this MuxingInformationAudioTrack.

        The number of channels in this audio stream

        :return: The channels of this MuxingInformationAudioTrack.
        :rtype: int
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this MuxingInformationAudioTrack.

        The number of channels in this audio stream

        :param channels: The channels of this MuxingInformationAudioTrack.
        :type: int
        """

        if channels is not None:
            if not isinstance(channels, int):
                raise TypeError("Invalid type for `channels`, type has to be `int`")

            self._channels = channels


    @property
    def duration(self):
        """Gets the duration of this MuxingInformationAudioTrack.

        TODO add description

        :return: The duration of this MuxingInformationAudioTrack.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this MuxingInformationAudioTrack.

        TODO add description

        :param duration: The duration of this MuxingInformationAudioTrack.
        :type: float
        """

        if duration is not None:
            if not isinstance(duration, float):
                raise TypeError("Invalid type for `duration`, type has to be `float`")

            self._duration = duration

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
            if issubclass(MuxingInformationAudioTrack, dict):
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
        if not isinstance(other, MuxingInformationAudioTrack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
