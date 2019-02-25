# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from enum import Enum


class AccountApiKey(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AccountApiKey, self).openapi_types
        types.update({
            'value': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AccountApiKey, self).attribute_map
        attributes.update({
            'value': 'value'
        })
        return attributes

    def __init__(self, value=None, *args, **kwargs):
        super(AccountApiKey, self).__init__(*args, **kwargs)

        self._value = None
        self.discriminator = None

        self.value = value

    @property
    def value(self):
        """Gets the value of this AccountApiKey.

        Key value for authentication with the Bitmovin API

        :return: The value of this AccountApiKey.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AccountApiKey.

        Key value for authentication with the Bitmovin API

        :param value: The value of this AccountApiKey.
        :type: str
        """

        if value is not None:
            if not isinstance(value, str):
                raise TypeError("Invalid type for `value`, type has to be `str`")

            self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AccountApiKey, self).to_dict()

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
            if issubclass(AccountApiKey, dict):
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
        if not isinstance(other, AccountApiKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
