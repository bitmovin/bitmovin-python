# coding: utf-8

from bitmovin_python.models.bitmovin_response import BitmovinResponse
import pprint
import six
from datetime import datetime
from enum import Enum


class CustomXmlElement(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(CustomXmlElement, self).openapi_types
        types.update({
            'data': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(CustomXmlElement, self).attribute_map
        attributes.update({
            'data': 'data'
        })
        return attributes

    def __init__(self, data=None, *args, **kwargs):
        super(CustomXmlElement, self).__init__(*args, **kwargs)

        self._data = None
        self.discriminator = None

        self.data = data

    @property
    def data(self):
        """Gets the data of this CustomXmlElement.

        String representation of the XML element

        :return: The data of this CustomXmlElement.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CustomXmlElement.

        String representation of the XML element

        :param data: The data of this CustomXmlElement.
        :type: str
        """

        if data is not None:
            if not isinstance(data, str):
                raise TypeError("Invalid type for `data`, type has to be `str`")

            self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(CustomXmlElement, self).to_dict()

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
            if issubclass(CustomXmlElement, dict):
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
        if not isinstance(other, CustomXmlElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
