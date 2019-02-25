# coding: utf-8

from bitmovin_python.models.bitmovin_response import BitmovinResponse
import pprint
import six
from datetime import datetime
from enum import Enum


class MediaStream(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(MediaStream, self).openapi_types
        types.update({
            'position': 'int',
            'duration': 'int',
            'codec': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(MediaStream, self).attribute_map
        attributes.update({
            'position': 'position',
            'duration': 'duration',
            'codec': 'codec'
        })
        return attributes

    def __init__(self, position=None, duration=None, codec=None, *args, **kwargs):
        super(MediaStream, self).__init__(*args, **kwargs)

        self._position = None
        self._duration = None
        self._codec = None
        self.discriminator = None

        if position is not None:
            self.position = position
        if duration is not None:
            self.duration = duration
        if codec is not None:
            self.codec = codec

    @property
    def position(self):
        """Gets the position of this MediaStream.

        Position starts from 0 and indicates the position of the stream in the media. 0 means that this is the first stream found in the media

        :return: The position of this MediaStream.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this MediaStream.

        Position starts from 0 and indicates the position of the stream in the media. 0 means that this is the first stream found in the media

        :param position: The position of this MediaStream.
        :type: int
        """

        if position is not None:
            if not isinstance(position, int):
                raise TypeError("Invalid type for `position`, type has to be `int`")

            self._position = position


    @property
    def duration(self):
        """Gets the duration of this MediaStream.

        Duration of the stream in seconds

        :return: The duration of this MediaStream.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this MediaStream.

        Duration of the stream in seconds

        :param duration: The duration of this MediaStream.
        :type: int
        """

        if duration is not None:
            if not isinstance(duration, int):
                raise TypeError("Invalid type for `duration`, type has to be `int`")

            self._duration = duration


    @property
    def codec(self):
        """Gets the codec of this MediaStream.

        Codec of the stream

        :return: The codec of this MediaStream.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this MediaStream.

        Codec of the stream

        :param codec: The codec of this MediaStream.
        :type: str
        """

        if codec is not None:
            if not isinstance(codec, str):
                raise TypeError("Invalid type for `codec`, type has to be `str`")

            self._codec = codec

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(MediaStream, self).to_dict()

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
            if issubclass(MediaStream, dict):
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
        if not isinstance(other, MediaStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
