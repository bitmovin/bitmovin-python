# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class StreamDetails(object):
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
            'id': 'str',
            'codec': 'str',
            'duration': 'int',
            'position': 'int'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'codec': 'codec',
            'duration': 'duration',
            'position': 'position'
        }
        return attributes

    def __init__(self, id=None, codec=None, duration=None, position=None, *args, **kwargs):

        self._id = None
        self._codec = None
        self._duration = None
        self._position = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if codec is not None:
            self.codec = codec
        if duration is not None:
            self.duration = duration
        if position is not None:
            self.position = position

    @property
    def id(self):
        """Gets the id of this StreamDetails.


        :return: The id of this StreamDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StreamDetails.


        :param id: The id of this StreamDetails.
        :type: str
        """

        if id is not None:
            if not isinstance(id, str):
                raise TypeError("Invalid type for `id`, type has to be `str`")

            self._id = id


    @property
    def codec(self):
        """Gets the codec of this StreamDetails.


        :return: The codec of this StreamDetails.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this StreamDetails.


        :param codec: The codec of this StreamDetails.
        :type: str
        """

        if codec is not None:
            if not isinstance(codec, str):
                raise TypeError("Invalid type for `codec`, type has to be `str`")

            self._codec = codec


    @property
    def duration(self):
        """Gets the duration of this StreamDetails.


        :return: The duration of this StreamDetails.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this StreamDetails.


        :param duration: The duration of this StreamDetails.
        :type: int
        """

        if duration is not None:
            if not isinstance(duration, int):
                raise TypeError("Invalid type for `duration`, type has to be `int`")

            self._duration = duration


    @property
    def position(self):
        """Gets the position of this StreamDetails.


        :return: The position of this StreamDetails.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this StreamDetails.


        :param position: The position of this StreamDetails.
        :type: int
        """

        if position is not None:
            if not isinstance(position, int):
                raise TypeError("Invalid type for `position`, type has to be `int`")

            self._position = position

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
            if issubclass(StreamDetails, dict):
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
        if not isinstance(other, StreamDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
