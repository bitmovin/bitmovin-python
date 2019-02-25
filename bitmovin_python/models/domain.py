# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from enum import Enum


class Domain(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Domain, self).openapi_types
        types.update({
            'url': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Domain, self).attribute_map
        attributes.update({
            'url': 'url'
        })
        return attributes

    def __init__(self, url=None, *args, **kwargs):
        super(Domain, self).__init__(*args, **kwargs)

        self._url = None
        self.discriminator = None

        self.url = url

    @property
    def url(self):
        """Gets the url of this Domain.

        Host where the player is allowed to play

        :return: The url of this Domain.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Domain.

        Host where the player is allowed to play

        :param url: The url of this Domain.
        :type: str
        """

        if url is not None:
            if not isinstance(url, str):
                raise TypeError("Invalid type for `url`, type has to be `str`")

            self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Domain, self).to_dict()

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
            if issubclass(Domain, dict):
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
        if not isinstance(other, Domain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
