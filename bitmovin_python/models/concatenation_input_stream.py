# coding: utf-8

from bitmovin_python.models.basic_input_stream import BasicInputStream
from bitmovin_python.models.concatenation_input_configuration import ConcatenationInputConfiguration
from bitmovin_python.models.input_stream_type import InputStreamType
import pprint
import six
from datetime import datetime
from enum import Enum


class ConcatenationInputStream(BasicInputStream):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(ConcatenationInputStream, self).openapi_types
        types.update({
            'concatenation': 'list[ConcatenationInputConfiguration]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(ConcatenationInputStream, self).attribute_map
        attributes.update({
            'concatenation': 'concatenation'
        })
        return attributes

    def __init__(self, concatenation=None, *args, **kwargs):
        super(ConcatenationInputStream, self).__init__(*args, **kwargs)

        self._concatenation = None
        self.discriminator = None

        if concatenation is not None:
            self.concatenation = concatenation

    @property
    def concatenation(self):
        """Gets the concatenation of this ConcatenationInputStream.

        Concatenation configuration for the output of this stream

        :return: The concatenation of this ConcatenationInputStream.
        :rtype: list[ConcatenationInputConfiguration]
        """
        return self._concatenation

    @concatenation.setter
    def concatenation(self, concatenation):
        """Sets the concatenation of this ConcatenationInputStream.

        Concatenation configuration for the output of this stream

        :param concatenation: The concatenation of this ConcatenationInputStream.
        :type: list[ConcatenationInputConfiguration]
        """

        if concatenation is not None:
            if not isinstance(concatenation, list):
                raise TypeError("Invalid type for `concatenation`, type has to be `list[ConcatenationInputConfiguration]`")

            self._concatenation = concatenation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(ConcatenationInputStream, self).to_dict()

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
            if issubclass(ConcatenationInputStream, dict):
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
        if not isinstance(other, ConcatenationInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
