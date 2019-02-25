# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class Statistics(object):
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
            'bytes_encoded_total': 'int',
            'time_encoded_total': 'int'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'bytes_encoded_total': 'bytesEncodedTotal',
            'time_encoded_total': 'timeEncodedTotal'
        }
        return attributes

    def __init__(self, bytes_encoded_total=None, time_encoded_total=None, *args, **kwargs):

        self._bytes_encoded_total = None
        self._time_encoded_total = None
        self.discriminator = None

        self.bytes_encoded_total = bytes_encoded_total
        self.time_encoded_total = time_encoded_total

    @property
    def bytes_encoded_total(self):
        """Gets the bytes_encoded_total of this Statistics.

        Bytes encoded total.

        :return: The bytes_encoded_total of this Statistics.
        :rtype: int
        """
        return self._bytes_encoded_total

    @bytes_encoded_total.setter
    def bytes_encoded_total(self, bytes_encoded_total):
        """Sets the bytes_encoded_total of this Statistics.

        Bytes encoded total.

        :param bytes_encoded_total: The bytes_encoded_total of this Statistics.
        :type: int
        """

        if bytes_encoded_total is not None:
            if not isinstance(bytes_encoded_total, int):
                raise TypeError("Invalid type for `bytes_encoded_total`, type has to be `int`")

            self._bytes_encoded_total = bytes_encoded_total


    @property
    def time_encoded_total(self):
        """Gets the time_encoded_total of this Statistics.

        Time in seconds encoded for all contained daily statistics.

        :return: The time_encoded_total of this Statistics.
        :rtype: int
        """
        return self._time_encoded_total

    @time_encoded_total.setter
    def time_encoded_total(self, time_encoded_total):
        """Sets the time_encoded_total of this Statistics.

        Time in seconds encoded for all contained daily statistics.

        :param time_encoded_total: The time_encoded_total of this Statistics.
        :type: int
        """

        if time_encoded_total is not None:
            if not isinstance(time_encoded_total, int):
                raise TypeError("Invalid type for `time_encoded_total`, type has to be `int`")

            self._time_encoded_total = time_encoded_total

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
            if issubclass(Statistics, dict):
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
        if not isinstance(other, Statistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
