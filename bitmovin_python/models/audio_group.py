# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class AudioGroup(object):
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
            'name': 'str',
            'priority': 'int'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'name': 'name',
            'priority': 'priority'
        }
        return attributes

    def __init__(self, name=None, priority=None, *args, **kwargs):

        self._name = None
        self._priority = None
        self.discriminator = None

        self.name = name
        self.priority = priority

    @property
    def name(self):
        """Gets the name of this AudioGroup.

        Name of the audio group

        :return: The name of this AudioGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AudioGroup.

        Name of the audio group

        :param name: The name of this AudioGroup.
        :type: str
        """

        if name is not None:
            if not isinstance(name, str):
                raise TypeError("Invalid type for `name`, type has to be `str`")

            self._name = name


    @property
    def priority(self):
        """Gets the priority of this AudioGroup.

        Priority of the audio group

        :return: The priority of this AudioGroup.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this AudioGroup.

        Priority of the audio group

        :param priority: The priority of this AudioGroup.
        :type: int
        """

        if priority is not None:
            if priority is not None and priority > 100:
                raise ValueError("Invalid value for `priority`, must be a value less than or equal to `100`")
            if priority is not None and priority < 0:
                raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `0`")
            if not isinstance(priority, int):
                raise TypeError("Invalid type for `priority`, type has to be `int`")

            self._priority = priority

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
            if issubclass(AudioGroup, dict):
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
        if not isinstance(other, AudioGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
