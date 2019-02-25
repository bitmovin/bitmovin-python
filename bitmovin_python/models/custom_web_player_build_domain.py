# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from enum import Enum


class CustomWebPlayerBuildDomain(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(CustomWebPlayerBuildDomain, self).openapi_types
        types.update({
            'domain': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(CustomWebPlayerBuildDomain, self).attribute_map
        attributes.update({
            'domain': 'domain'
        })
        return attributes

    def __init__(self, domain=None, *args, **kwargs):
        super(CustomWebPlayerBuildDomain, self).__init__(*args, **kwargs)

        self._domain = None
        self.discriminator = None

        self.domain = domain

    @property
    def domain(self):
        """Gets the domain of this CustomWebPlayerBuildDomain.

        Domain where the player is allowed to play

        :return: The domain of this CustomWebPlayerBuildDomain.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CustomWebPlayerBuildDomain.

        Domain where the player is allowed to play

        :param domain: The domain of this CustomWebPlayerBuildDomain.
        :type: str
        """

        if domain is not None:
            if not isinstance(domain, str):
                raise TypeError("Invalid type for `domain`, type has to be `str`")

            self._domain = domain

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(CustomWebPlayerBuildDomain, self).to_dict()

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
            if issubclass(CustomWebPlayerBuildDomain, dict):
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
        if not isinstance(other, CustomWebPlayerBuildDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
