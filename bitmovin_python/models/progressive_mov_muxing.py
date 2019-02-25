# coding: utf-8

from bitmovin_python.models.encoding_output import EncodingOutput
from bitmovin_python.models.ignoring import Ignoring
from bitmovin_python.models.internal_chunk_length import InternalChunkLength
from bitmovin_python.models.muxing import Muxing
from bitmovin_python.models.muxing_stream import MuxingStream
from bitmovin_python.models.muxing_type import MuxingType
from bitmovin_python.models.stream_conditions_mode import StreamConditionsMode
import pprint
import six
from datetime import datetime
from enum import Enum


class ProgressiveMovMuxing(Muxing):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(ProgressiveMovMuxing, self).openapi_types
        types.update({
            'filename': 'str',
            'internal_chunk_length': 'InternalChunkLength'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(ProgressiveMovMuxing, self).attribute_map
        attributes.update({
            'filename': 'filename',
            'internal_chunk_length': 'internalChunkLength'
        })
        return attributes

    def __init__(self, filename=None, internal_chunk_length=None, *args, **kwargs):
        super(ProgressiveMovMuxing, self).__init__(*args, **kwargs)

        self._filename = None
        self._internal_chunk_length = None
        self.discriminator = None

        if filename is not None:
            self.filename = filename
        if internal_chunk_length is not None:
            self.internal_chunk_length = internal_chunk_length

    @property
    def filename(self):
        """Gets the filename of this ProgressiveMovMuxing.

        The output file name

        :return: The filename of this ProgressiveMovMuxing.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this ProgressiveMovMuxing.

        The output file name

        :param filename: The filename of this ProgressiveMovMuxing.
        :type: str
        """

        if filename is not None:
            if not isinstance(filename, str):
                raise TypeError("Invalid type for `filename`, type has to be `str`")

            self._filename = filename


    @property
    def internal_chunk_length(self):
        """Gets the internal_chunk_length of this ProgressiveMovMuxing.

        Modifies the internal chunk length used for chunked encoding

        :return: The internal_chunk_length of this ProgressiveMovMuxing.
        :rtype: InternalChunkLength
        """
        return self._internal_chunk_length

    @internal_chunk_length.setter
    def internal_chunk_length(self, internal_chunk_length):
        """Sets the internal_chunk_length of this ProgressiveMovMuxing.

        Modifies the internal chunk length used for chunked encoding

        :param internal_chunk_length: The internal_chunk_length of this ProgressiveMovMuxing.
        :type: InternalChunkLength
        """

        if internal_chunk_length is not None:
            if not isinstance(internal_chunk_length, InternalChunkLength):
                raise TypeError("Invalid type for `internal_chunk_length`, type has to be `InternalChunkLength`")

            self._internal_chunk_length = internal_chunk_length

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(ProgressiveMovMuxing, self).to_dict()

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
            if issubclass(ProgressiveMovMuxing, dict):
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
        if not isinstance(other, ProgressiveMovMuxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
