# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class UtcTiming(object):
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
            'value': 'str',
            'scheme_id_uri': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'value': 'value',
            'scheme_id_uri': 'schemeIdUri'
        }
        return attributes

    def __init__(self, value=None, scheme_id_uri=None, *args, **kwargs):

        self._value = None
        self._scheme_id_uri = None
        self.discriminator = None

        self.value = value
        self.scheme_id_uri = scheme_id_uri

    @property
    def value(self):
        """Gets the value of this UtcTiming.

        The server to get the time from

        :return: The value of this UtcTiming.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UtcTiming.

        The server to get the time from

        :param value: The value of this UtcTiming.
        :type: str
        """

        if value is not None:
            if not isinstance(value, str):
                raise TypeError("Invalid type for `value`, type has to be `str`")

            self._value = value


    @property
    def scheme_id_uri(self):
        """Gets the scheme_id_uri of this UtcTiming.

        The scheme id to use. Please refer to the DASH standard.

        :return: The scheme_id_uri of this UtcTiming.
        :rtype: str
        """
        return self._scheme_id_uri

    @scheme_id_uri.setter
    def scheme_id_uri(self, scheme_id_uri):
        """Sets the scheme_id_uri of this UtcTiming.

        The scheme id to use. Please refer to the DASH standard.

        :param scheme_id_uri: The scheme_id_uri of this UtcTiming.
        :type: str
        """

        if scheme_id_uri is not None:
            if not isinstance(scheme_id_uri, str):
                raise TypeError("Invalid type for `scheme_id_uri`, type has to be `str`")

            self._scheme_id_uri = scheme_id_uri

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
            if issubclass(UtcTiming, dict):
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
        if not isinstance(other, UtcTiming):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
