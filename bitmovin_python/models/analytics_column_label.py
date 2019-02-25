# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class AnalyticsColumnLabel(object):
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
            'key': 'str',
            'label': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'key': 'key',
            'label': 'label'
        }
        return attributes

    def __init__(self, key=None, label=None, *args, **kwargs):

        self._key = None
        self._label = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if label is not None:
            self.label = label

    @property
    def key(self):
        """Gets the key of this AnalyticsColumnLabel.


        :return: The key of this AnalyticsColumnLabel.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AnalyticsColumnLabel.


        :param key: The key of this AnalyticsColumnLabel.
        :type: str
        """

        if key is not None:
            if not isinstance(key, str):
                raise TypeError("Invalid type for `key`, type has to be `str`")

            self._key = key


    @property
    def label(self):
        """Gets the label of this AnalyticsColumnLabel.


        :return: The label of this AnalyticsColumnLabel.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this AnalyticsColumnLabel.


        :param label: The label of this AnalyticsColumnLabel.
        :type: str
        """

        if label is not None:
            if not isinstance(label, str):
                raise TypeError("Invalid type for `label`, type has to be `str`")

            self._label = label

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
            if issubclass(AnalyticsColumnLabel, dict):
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
        if not isinstance(other, AnalyticsColumnLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
