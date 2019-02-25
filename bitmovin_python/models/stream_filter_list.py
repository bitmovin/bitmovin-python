# coding: utf-8

from bitmovin_python.models.stream_filter import StreamFilter
import pprint
import six
from datetime import datetime
from enum import Enum


class StreamFilterList(object):
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
            'filters': 'list[StreamFilter]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'filters': 'filters'
        }
        return attributes

    def __init__(self, filters=None, *args, **kwargs):

        self._filters = None
        self.discriminator = None

        self.filters = filters

    @property
    def filters(self):
        """Gets the filters of this StreamFilterList.

        List of stream filters

        :return: The filters of this StreamFilterList.
        :rtype: list[StreamFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this StreamFilterList.

        List of stream filters

        :param filters: The filters of this StreamFilterList.
        :type: list[StreamFilter]
        """

        if filters is not None:
            if not isinstance(filters, list):
                raise TypeError("Invalid type for `filters`, type has to be `list[StreamFilter]`")

            self._filters = filters

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
            if issubclass(StreamFilterList, dict):
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
        if not isinstance(other, StreamFilterList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
