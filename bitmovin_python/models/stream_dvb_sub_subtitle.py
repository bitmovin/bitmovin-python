# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.input_stream import InputStream
import pprint
import six
from datetime import datetime
from enum import Enum


class StreamDvbSubSubtitle(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(StreamDvbSubSubtitle, self).openapi_types
        types.update({
            'input_stream': 'InputStream'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(StreamDvbSubSubtitle, self).attribute_map
        attributes.update({
            'input_stream': 'inputStream'
        })
        return attributes

    def __init__(self, input_stream=None, *args, **kwargs):
        super(StreamDvbSubSubtitle, self).__init__(*args, **kwargs)

        self._input_stream = None
        self.discriminator = None

        self.input_stream = input_stream

    @property
    def input_stream(self):
        """Gets the input_stream of this StreamDvbSubSubtitle.

        The input stream to extract the subtitle from

        :return: The input_stream of this StreamDvbSubSubtitle.
        :rtype: InputStream
        """
        return self._input_stream

    @input_stream.setter
    def input_stream(self, input_stream):
        """Sets the input_stream of this StreamDvbSubSubtitle.

        The input stream to extract the subtitle from

        :param input_stream: The input_stream of this StreamDvbSubSubtitle.
        :type: InputStream
        """

        if input_stream is not None:
            if not isinstance(input_stream, InputStream):
                raise TypeError("Invalid type for `input_stream`, type has to be `InputStream`")

            self._input_stream = input_stream

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(StreamDvbSubSubtitle, self).to_dict()

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
            if issubclass(StreamDvbSubSubtitle, dict):
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
        if not isinstance(other, StreamDvbSubSubtitle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
