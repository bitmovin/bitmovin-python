# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.input_path import InputPath
import pprint
import six
from datetime import datetime
from enum import Enum


class BurnInSubtitleSrt(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(BurnInSubtitleSrt, self).openapi_types
        types.update({
            'input': 'InputPath'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(BurnInSubtitleSrt, self).attribute_map
        attributes.update({
            'input': 'input'
        })
        return attributes

    def __init__(self, input=None, *args, **kwargs):
        super(BurnInSubtitleSrt, self).__init__(*args, **kwargs)

        self._input = None
        self.discriminator = None

        self.input = input

    @property
    def input(self):
        """Gets the input of this BurnInSubtitleSrt.

        The input location to get the SRT file from

        :return: The input of this BurnInSubtitleSrt.
        :rtype: InputPath
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this BurnInSubtitleSrt.

        The input location to get the SRT file from

        :param input: The input of this BurnInSubtitleSrt.
        :type: InputPath
        """

        if input is not None:
            if not isinstance(input, InputPath):
                raise TypeError("Invalid type for `input`, type has to be `InputPath`")

            self._input = input

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(BurnInSubtitleSrt, self).to_dict()

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
            if issubclass(BurnInSubtitleSrt, dict):
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
        if not isinstance(other, BurnInSubtitleSrt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
