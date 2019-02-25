# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class AnalyticsQueryTimeframe(object):
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
            'start': 'datetime',
            'end': 'datetime'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'start': 'start',
            'end': 'end'
        }
        return attributes

    def __init__(self, start=None, end=None, *args, **kwargs):

        self._start = None
        self._end = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if end is not None:
            self.end = end

    @property
    def start(self):
        """Gets the start of this AnalyticsQueryTimeframe.

        Start of timeframe which is queried

        :return: The start of this AnalyticsQueryTimeframe.
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this AnalyticsQueryTimeframe.

        Start of timeframe which is queried

        :param start: The start of this AnalyticsQueryTimeframe.
        :type: datetime
        """

        if start is not None:
            if not isinstance(start, datetime):
                raise TypeError("Invalid type for `start`, type has to be `datetime`")

            self._start = start


    @property
    def end(self):
        """Gets the end of this AnalyticsQueryTimeframe.

        End of timeframe which is queried

        :return: The end of this AnalyticsQueryTimeframe.
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this AnalyticsQueryTimeframe.

        End of timeframe which is queried

        :param end: The end of this AnalyticsQueryTimeframe.
        :type: datetime
        """

        if end is not None:
            if not isinstance(end, datetime):
                raise TypeError("Invalid type for `end`, type has to be `datetime`")

            self._end = end

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
            if issubclass(AnalyticsQueryTimeframe, dict):
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
        if not isinstance(other, AnalyticsQueryTimeframe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
