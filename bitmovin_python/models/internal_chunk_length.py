# coding: utf-8

from bitmovin_python.models.chunk_length_mode import ChunkLengthMode
import pprint
import six
from datetime import datetime
from enum import Enum


class InternalChunkLength(object):
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
            'mode': 'ChunkLengthMode',
            'custom_chunk_length': 'float'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'mode': 'mode',
            'custom_chunk_length': 'customChunkLength'
        }
        return attributes

    def __init__(self, mode=None, custom_chunk_length=None, *args, **kwargs):

        self._mode = None
        self._custom_chunk_length = None
        self.discriminator = None

        self.mode = mode
        if custom_chunk_length is not None:
            self.custom_chunk_length = custom_chunk_length

    @property
    def mode(self):
        """Gets the mode of this InternalChunkLength.

        Defines how the internal chunk length for encoding will be determined

        :return: The mode of this InternalChunkLength.
        :rtype: ChunkLengthMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this InternalChunkLength.

        Defines how the internal chunk length for encoding will be determined

        :param mode: The mode of this InternalChunkLength.
        :type: ChunkLengthMode
        """

        if mode is not None:
            if not isinstance(mode, ChunkLengthMode):
                raise TypeError("Invalid type for `mode`, type has to be `ChunkLengthMode`")

            self._mode = mode


    @property
    def custom_chunk_length(self):
        """Gets the custom_chunk_length of this InternalChunkLength.

        Defines a custom internal chunk length in seconds to be used for encoding if mode is set to `CUSTOM`. Valid range is from 1 to 180 seconds

        :return: The custom_chunk_length of this InternalChunkLength.
        :rtype: float
        """
        return self._custom_chunk_length

    @custom_chunk_length.setter
    def custom_chunk_length(self, custom_chunk_length):
        """Sets the custom_chunk_length of this InternalChunkLength.

        Defines a custom internal chunk length in seconds to be used for encoding if mode is set to `CUSTOM`. Valid range is from 1 to 180 seconds

        :param custom_chunk_length: The custom_chunk_length of this InternalChunkLength.
        :type: float
        """

        if custom_chunk_length is not None:
            if custom_chunk_length is not None and custom_chunk_length > 180:
                raise ValueError("Invalid value for `custom_chunk_length`, must be a value less than or equal to `180`")
            if custom_chunk_length is not None and custom_chunk_length < 1:
                raise ValueError("Invalid value for `custom_chunk_length`, must be a value greater than or equal to `1`")
            if not isinstance(custom_chunk_length, float):
                raise TypeError("Invalid type for `custom_chunk_length`, type has to be `float`")

            self._custom_chunk_length = custom_chunk_length

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
            if issubclass(InternalChunkLength, dict):
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
        if not isinstance(other, InternalChunkLength):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
