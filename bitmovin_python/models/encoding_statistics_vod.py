# coding: utf-8

from bitmovin_python.models.encoding_statistics import EncodingStatistics
import pprint
import six
from datetime import datetime
from enum import Enum


class EncodingStatisticsVod(EncodingStatistics):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(EncodingStatisticsVod, self).openapi_types
        types.update({
            'time_enqueued': 'int',
            'real_time_factor': 'float'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(EncodingStatisticsVod, self).attribute_map
        attributes.update({
            'time_enqueued': 'timeEnqueued',
            'real_time_factor': 'realTimeFactor'
        })
        return attributes

    def __init__(self, time_enqueued=None, real_time_factor=None, *args, **kwargs):
        super(EncodingStatisticsVod, self).__init__(*args, **kwargs)

        self._time_enqueued = None
        self._real_time_factor = None
        self.discriminator = None

        self.time_enqueued = time_enqueued
        self.real_time_factor = real_time_factor

    @property
    def time_enqueued(self):
        """Gets the time_enqueued of this EncodingStatisticsVod.

        Time in seconds encoded for this encoding.

        :return: The time_enqueued of this EncodingStatisticsVod.
        :rtype: int
        """
        return self._time_enqueued

    @time_enqueued.setter
    def time_enqueued(self, time_enqueued):
        """Sets the time_enqueued of this EncodingStatisticsVod.

        Time in seconds encoded for this encoding.

        :param time_enqueued: The time_enqueued of this EncodingStatisticsVod.
        :type: int
        """

        if time_enqueued is not None:
            if not isinstance(time_enqueued, int):
                raise TypeError("Invalid type for `time_enqueued`, type has to be `int`")

            self._time_enqueued = time_enqueued


    @property
    def real_time_factor(self):
        """Gets the real_time_factor of this EncodingStatisticsVod.

        The realtime factor.

        :return: The real_time_factor of this EncodingStatisticsVod.
        :rtype: float
        """
        return self._real_time_factor

    @real_time_factor.setter
    def real_time_factor(self, real_time_factor):
        """Sets the real_time_factor of this EncodingStatisticsVod.

        The realtime factor.

        :param real_time_factor: The real_time_factor of this EncodingStatisticsVod.
        :type: float
        """

        if real_time_factor is not None:
            if not isinstance(real_time_factor, float):
                raise TypeError("Invalid type for `real_time_factor`, type has to be `float`")

            self._real_time_factor = real_time_factor

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(EncodingStatisticsVod, self).to_dict()

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
            if issubclass(EncodingStatisticsVod, dict):
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
        if not isinstance(other, EncodingStatisticsVod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
