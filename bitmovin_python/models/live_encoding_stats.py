# coding: utf-8

from bitmovin_python.models.live_encoding_stats_event import LiveEncodingStatsEvent
from bitmovin_python.models.live_encoding_status import LiveEncodingStatus
from bitmovin_python.models.stream_infos import StreamInfos
import pprint
import six
from datetime import datetime
from enum import Enum


class LiveEncodingStats(object):
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
            'status': 'LiveEncodingStatus',
            'events': 'list[LiveEncodingStatsEvent]',
            'statistics': 'list[StreamInfos]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'status': 'status',
            'events': 'events',
            'statistics': 'statistics'
        }
        return attributes

    def __init__(self, status=None, events=None, statistics=None, *args, **kwargs):

        self._status = None
        self._events = None
        self._statistics = None
        self.discriminator = None

        self.status = status
        if events is not None:
            self.events = events
        if statistics is not None:
            self.statistics = statistics

    @property
    def status(self):
        """Gets the status of this LiveEncodingStats.


        :return: The status of this LiveEncodingStats.
        :rtype: LiveEncodingStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LiveEncodingStats.


        :param status: The status of this LiveEncodingStats.
        :type: LiveEncodingStatus
        """

        if status is not None:
            if not isinstance(status, LiveEncodingStatus):
                raise TypeError("Invalid type for `status`, type has to be `LiveEncodingStatus`")

            self._status = status


    @property
    def events(self):
        """Gets the events of this LiveEncodingStats.

        List of events

        :return: The events of this LiveEncodingStats.
        :rtype: list[LiveEncodingStatsEvent]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this LiveEncodingStats.

        List of events

        :param events: The events of this LiveEncodingStats.
        :type: list[LiveEncodingStatsEvent]
        """

        if events is not None:
            if not isinstance(events, list):
                raise TypeError("Invalid type for `events`, type has to be `list[LiveEncodingStatsEvent]`")

            self._events = events


    @property
    def statistics(self):
        """Gets the statistics of this LiveEncodingStats.

        List of statistics

        :return: The statistics of this LiveEncodingStats.
        :rtype: list[StreamInfos]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this LiveEncodingStats.

        List of statistics

        :param statistics: The statistics of this LiveEncodingStats.
        :type: list[StreamInfos]
        """

        if statistics is not None:
            if not isinstance(statistics, list):
                raise TypeError("Invalid type for `statistics`, type has to be `list[StreamInfos]`")

            self._statistics = statistics

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
            if issubclass(LiveEncodingStats, dict):
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
        if not isinstance(other, LiveEncodingStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
