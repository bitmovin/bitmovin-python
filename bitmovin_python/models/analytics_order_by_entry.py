# coding: utf-8

from bitmovin_python.models.analytics_order import AnalyticsOrder
import pprint
import six
from datetime import datetime
from enum import Enum


class AnalyticsOrderByEntry(object):
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
            'order': 'AnalyticsOrder'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'name': 'name',
            'order': 'order'
        }
        return attributes

    def __init__(self, name=None, order=None, *args, **kwargs):

        self._name = None
        self._order = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.order = order

    @property
    def name(self):
        """Gets the name of this AnalyticsOrderByEntry.


        :return: The name of this AnalyticsOrderByEntry.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnalyticsOrderByEntry.


        :param name: The name of this AnalyticsOrderByEntry.
        :type: str
        """

        if name is not None:
            if not isinstance(name, str):
                raise TypeError("Invalid type for `name`, type has to be `str`")

            self._name = name


    @property
    def order(self):
        """Gets the order of this AnalyticsOrderByEntry.


        :return: The order of this AnalyticsOrderByEntry.
        :rtype: AnalyticsOrder
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this AnalyticsOrderByEntry.


        :param order: The order of this AnalyticsOrderByEntry.
        :type: AnalyticsOrder
        """

        if order is not None:
            if not isinstance(order, AnalyticsOrder):
                raise TypeError("Invalid type for `order`, type has to be `AnalyticsOrder`")

            self._order = order

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
            if issubclass(AnalyticsOrderByEntry, dict):
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
        if not isinstance(other, AnalyticsOrderByEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
