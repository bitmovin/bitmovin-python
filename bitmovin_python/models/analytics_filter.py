# coding: utf-8

from bitmovin_python.models.analytics_operator import AnalyticsOperator
import pprint
import six
from datetime import datetime
from enum import Enum


class AnalyticsFilter(object):
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
            'operator': 'AnalyticsOperator',
            'value': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'name': 'name',
            'operator': 'operator',
            'value': 'value'
        }
        return attributes

    def __init__(self, name=None, operator=None, value=None, *args, **kwargs):

        self._name = None
        self._operator = None
        self._value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.operator = operator
        self.value = value

    @property
    def name(self):
        """Gets the name of this AnalyticsFilter.


        :return: The name of this AnalyticsFilter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnalyticsFilter.


        :param name: The name of this AnalyticsFilter.
        :type: str
        """

        if name is not None:
            if not isinstance(name, str):
                raise TypeError("Invalid type for `name`, type has to be `str`")

            self._name = name


    @property
    def operator(self):
        """Gets the operator of this AnalyticsFilter.


        :return: The operator of this AnalyticsFilter.
        :rtype: AnalyticsOperator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this AnalyticsFilter.


        :param operator: The operator of this AnalyticsFilter.
        :type: AnalyticsOperator
        """

        if operator is not None:
            if not isinstance(operator, AnalyticsOperator):
                raise TypeError("Invalid type for `operator`, type has to be `AnalyticsOperator`")

            self._operator = operator


    @property
    def value(self):
        """Gets the value of this AnalyticsFilter.

        The value to compare to the property specified by the name

        :return: The value of this AnalyticsFilter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AnalyticsFilter.

        The value to compare to the property specified by the name

        :param value: The value of this AnalyticsFilter.
        :type: str
        """

        if value is not None:
            if not isinstance(value, str):
                raise TypeError("Invalid type for `value`, type has to be `str`")

            self._value = value

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
            if issubclass(AnalyticsFilter, dict):
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
        if not isinstance(other, AnalyticsFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
