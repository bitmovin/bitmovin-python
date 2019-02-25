# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class EncodingStatistics(object):
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
            'date': 'datetime',
            'bytes_encoded': 'int',
            'time_encoded': 'int'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'date': 'date',
            'bytes_encoded': 'bytesEncoded',
            'time_encoded': 'timeEncoded'
        }
        return attributes

    def __init__(self, date=None, bytes_encoded=None, time_encoded=None, *args, **kwargs):

        self._date = None
        self._bytes_encoded = None
        self._time_encoded = None
        self.discriminator = None

        self.date = date
        self.bytes_encoded = bytes_encoded
        self.time_encoded = time_encoded

    @property
    def date(self):
        """Gets the date of this EncodingStatistics.

        Date, format. yyyy-MM-dd

        :return: The date of this EncodingStatistics.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this EncodingStatistics.

        Date, format. yyyy-MM-dd

        :param date: The date of this EncodingStatistics.
        :type: datetime
        """

        if date is not None:
            if not isinstance(date, datetime):
                raise TypeError("Invalid type for `date`, type has to be `datetime`")

            self._date = date


    @property
    def bytes_encoded(self):
        """Gets the bytes_encoded of this EncodingStatistics.

        Bytes encoded for this encoding.

        :return: The bytes_encoded of this EncodingStatistics.
        :rtype: int
        """
        return self._bytes_encoded

    @bytes_encoded.setter
    def bytes_encoded(self, bytes_encoded):
        """Sets the bytes_encoded of this EncodingStatistics.

        Bytes encoded for this encoding.

        :param bytes_encoded: The bytes_encoded of this EncodingStatistics.
        :type: int
        """

        if bytes_encoded is not None:
            if not isinstance(bytes_encoded, int):
                raise TypeError("Invalid type for `bytes_encoded`, type has to be `int`")

            self._bytes_encoded = bytes_encoded


    @property
    def time_encoded(self):
        """Gets the time_encoded of this EncodingStatistics.

        Time in seconds encoded for this encoding.

        :return: The time_encoded of this EncodingStatistics.
        :rtype: int
        """
        return self._time_encoded

    @time_encoded.setter
    def time_encoded(self, time_encoded):
        """Sets the time_encoded of this EncodingStatistics.

        Time in seconds encoded for this encoding.

        :param time_encoded: The time_encoded of this EncodingStatistics.
        :type: int
        """

        if time_encoded is not None:
            if not isinstance(time_encoded, int):
                raise TypeError("Invalid type for `time_encoded`, type has to be `int`")

            self._time_encoded = time_encoded

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
            if issubclass(EncodingStatistics, dict):
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
        if not isinstance(other, EncodingStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
