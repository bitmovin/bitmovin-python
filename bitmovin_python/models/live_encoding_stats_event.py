# coding: utf-8

from bitmovin_python.models.live_encoding_stats_event_details import LiveEncodingStatsEventDetails
import pprint
import six
from datetime import datetime
from enum import Enum


class LiveEncodingStatsEvent(object):
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
            'time': 'datetime',
            'details': 'LiveEncodingStatsEventDetails'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'time': 'time',
            'details': 'details'
        }
        return attributes

    def __init__(self, time=None, details=None, *args, **kwargs):

        self._time = None
        self._details = None
        self.discriminator = None

        self.time = time
        self.details = details

    @property
    def time(self):
        """Gets the time of this LiveEncodingStatsEvent.

        Timestamp of the event expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :return: The time of this LiveEncodingStatsEvent.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this LiveEncodingStatsEvent.

        Timestamp of the event expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :param time: The time of this LiveEncodingStatsEvent.
        :type: datetime
        """

        if time is not None:
            if not isinstance(time, datetime):
                raise TypeError("Invalid type for `time`, type has to be `datetime`")

            self._time = time


    @property
    def details(self):
        """Gets the details of this LiveEncodingStatsEvent.


        :return: The details of this LiveEncodingStatsEvent.
        :rtype: LiveEncodingStatsEventDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this LiveEncodingStatsEvent.


        :param details: The details of this LiveEncodingStatsEvent.
        :type: LiveEncodingStatsEventDetails
        """

        if details is not None:
            if not isinstance(details, LiveEncodingStatsEventDetails):
                raise TypeError("Invalid type for `details`, type has to be `LiveEncodingStatsEventDetails`")

            self._details = details

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
            if issubclass(LiveEncodingStatsEvent, dict):
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
        if not isinstance(other, LiveEncodingStatsEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
