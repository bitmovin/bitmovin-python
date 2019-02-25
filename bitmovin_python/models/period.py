# coding: utf-8

from bitmovin_python.models.bitmovin_response import BitmovinResponse
import pprint
import six
from datetime import datetime
from enum import Enum


class Period(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Period, self).openapi_types
        types.update({
            'start': 'float',
            'duration': 'float'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Period, self).attribute_map
        attributes.update({
            'start': 'start',
            'duration': 'duration'
        })
        return attributes

    def __init__(self, start=None, duration=None, *args, **kwargs):
        super(Period, self).__init__(*args, **kwargs)

        self._start = None
        self._duration = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if duration is not None:
            self.duration = duration

    @property
    def start(self):
        """Gets the start of this Period.

        Starting time in seconds

        :return: The start of this Period.
        :rtype: float
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this Period.

        Starting time in seconds

        :param start: The start of this Period.
        :type: float
        """

        if start is not None:
            if not isinstance(start, float):
                raise TypeError("Invalid type for `start`, type has to be `float`")

            self._start = start


    @property
    def duration(self):
        """Gets the duration of this Period.

        Duration in seconds

        :return: The duration of this Period.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Period.

        Duration in seconds

        :param duration: The duration of this Period.
        :type: float
        """

        if duration is not None:
            if not isinstance(duration, float):
                raise TypeError("Invalid type for `duration`, type has to be `float`")

            self._duration = duration

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Period, self).to_dict()

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
            if issubclass(Period, dict):
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
        if not isinstance(other, Period):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
