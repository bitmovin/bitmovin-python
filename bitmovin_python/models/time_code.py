# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class TimeCode(object):
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
            'time_code_start': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'time_code_start': 'timeCodeStart'
        }
        return attributes

    def __init__(self, time_code_start=None, *args, **kwargs):

        self._time_code_start = None
        self.discriminator = None

        if time_code_start is not None:
            self.time_code_start = time_code_start

    @property
    def time_code_start(self):
        """Gets the time_code_start of this TimeCode.

        Specify start timecode for writing.

        :return: The time_code_start of this TimeCode.
        :rtype: str
        """
        return self._time_code_start

    @time_code_start.setter
    def time_code_start(self, time_code_start):
        """Sets the time_code_start of this TimeCode.

        Specify start timecode for writing.

        :param time_code_start: The time_code_start of this TimeCode.
        :type: str
        """

        if time_code_start is not None:
            if not isinstance(time_code_start, str):
                raise TypeError("Invalid type for `time_code_start`, type has to be `str`")

            self._time_code_start = time_code_start

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
            if issubclass(TimeCode, dict):
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
        if not isinstance(other, TimeCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
