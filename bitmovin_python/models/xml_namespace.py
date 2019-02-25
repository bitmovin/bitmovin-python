# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class XmlNamespace(object):
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
            'prefix': 'str',
            'uri': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'prefix': 'prefix',
            'uri': 'uri'
        }
        return attributes

    def __init__(self, prefix=None, uri=None, *args, **kwargs):

        self._prefix = None
        self._uri = None
        self.discriminator = None

        self.prefix = prefix
        self.uri = uri

    @property
    def prefix(self):
        """Gets the prefix of this XmlNamespace.

        Name of the XML Namespace reference

        :return: The prefix of this XmlNamespace.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this XmlNamespace.

        Name of the XML Namespace reference

        :param prefix: The prefix of this XmlNamespace.
        :type: str
        """

        if prefix is not None:
            if not isinstance(prefix, str):
                raise TypeError("Invalid type for `prefix`, type has to be `str`")

            self._prefix = prefix


    @property
    def uri(self):
        """Gets the uri of this XmlNamespace.

        Source of the XML Namespace reference

        :return: The uri of this XmlNamespace.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this XmlNamespace.

        Source of the XML Namespace reference

        :param uri: The uri of this XmlNamespace.
        :type: str
        """

        if uri is not None:
            if not isinstance(uri, str):
                raise TypeError("Invalid type for `uri`, type has to be `str`")

            self._uri = uri

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
            if issubclass(XmlNamespace, dict):
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
        if not isinstance(other, XmlNamespace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
