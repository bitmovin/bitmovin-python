# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class CencWidevine(object):
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
            'pssh': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'pssh': 'pssh'
        }
        return attributes

    def __init__(self, pssh=None, *args, **kwargs):

        self._pssh = None
        self.discriminator = None

        self.pssh = pssh

    @property
    def pssh(self):
        """Gets the pssh of this CencWidevine.

        Base64 encoded pssh payload

        :return: The pssh of this CencWidevine.
        :rtype: str
        """
        return self._pssh

    @pssh.setter
    def pssh(self, pssh):
        """Sets the pssh of this CencWidevine.

        Base64 encoded pssh payload

        :param pssh: The pssh of this CencWidevine.
        :type: str
        """

        if pssh is not None:
            if not isinstance(pssh, str):
                raise TypeError("Invalid type for `pssh`, type has to be `str`")

            self._pssh = pssh

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
            if issubclass(CencWidevine, dict):
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
        if not isinstance(other, CencWidevine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
