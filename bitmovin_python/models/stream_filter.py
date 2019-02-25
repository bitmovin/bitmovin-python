# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class StreamFilter(object):
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
            'position': 'int'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'position': 'position'
        }
        return attributes

    def __init__(self, id=None, position=None, *args, **kwargs):

        self._id = None
        self._position = None
        self.discriminator = None

        self.id = id
        self.position = position

    @property
    def id(self):
        """Gets the id of this StreamFilter.

        The id of the filter that should be used in the stream

        :return: The id of this StreamFilter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StreamFilter.

        The id of the filter that should be used in the stream

        :param id: The id of this StreamFilter.
        :type: str
        """

        if id is not None:
            if not isinstance(id, str):
                raise TypeError("Invalid type for `id`, type has to be `str`")

            self._id = id


    @property
    def position(self):
        """Gets the position of this StreamFilter.

        Defines the order in which filters are applied. Filters are applied in ascending order.

        :return: The position of this StreamFilter.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this StreamFilter.

        Defines the order in which filters are applied. Filters are applied in ascending order.

        :param position: The position of this StreamFilter.
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
            if issubclass(StreamFilter, dict):
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
        if not isinstance(other, StreamFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
