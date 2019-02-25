# coding: utf-8

from bitmovin_python.models.broadcast_ts_muxing_configuration import BroadcastTsMuxingConfiguration
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


class BroadcastTsMuxing(Muxing):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(BroadcastTsMuxing, self).openapi_types
        types.update({
            'segment_length': 'float',
            'filename': 'str',
            'configuration': 'BroadcastTsMuxingConfiguration',
            'internal_chunk_length': 'InternalChunkLength'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(BroadcastTsMuxing, self).attribute_map
        attributes.update({
            'segment_length': 'segmentLength',
            'filename': 'filename',
            'configuration': 'configuration',
            'internal_chunk_length': 'internalChunkLength'
        })
        return attributes

    def __init__(self, segment_length=None, filename=None, configuration=None, internal_chunk_length=None, *args, **kwargs):
        super(BroadcastTsMuxing, self).__init__(*args, **kwargs)

        self._segment_length = None
        self._filename = None
        self._configuration = None
        self._internal_chunk_length = None
        self.discriminator = None

        if segment_length is not None:
            self.segment_length = segment_length
        if filename is not None:
            self.filename = filename
        if configuration is not None:
            self.configuration = configuration
        if internal_chunk_length is not None:
            self.internal_chunk_length = internal_chunk_length

    @property
    def segment_length(self):
        """Gets the segment_length of this BroadcastTsMuxing.

        Length of the segments in seconds.

        :return: The segment_length of this BroadcastTsMuxing.
        :rtype: float
        """
        return self._segment_length

    @segment_length.setter
    def segment_length(self, segment_length):
        """Sets the segment_length of this BroadcastTsMuxing.

        Length of the segments in seconds.

        :param segment_length: The segment_length of this BroadcastTsMuxing.
        :type: float
        """

        if segment_length is not None:
            if not isinstance(segment_length, float):
                raise TypeError("Invalid type for `segment_length`, type has to be `float`")

            self._segment_length = segment_length


    @property
    def filename(self):
        """Gets the filename of this BroadcastTsMuxing.

        Name of the new Video

        :return: The filename of this BroadcastTsMuxing.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this BroadcastTsMuxing.

        Name of the new Video

        :param filename: The filename of this BroadcastTsMuxing.
        :type: str
        """

        if filename is not None:
            if not isinstance(filename, str):
                raise TypeError("Invalid type for `filename`, type has to be `str`")

            self._filename = filename


    @property
    def configuration(self):
        """Gets the configuration of this BroadcastTsMuxing.


        :return: The configuration of this BroadcastTsMuxing.
        :rtype: BroadcastTsMuxingConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this BroadcastTsMuxing.


        :param configuration: The configuration of this BroadcastTsMuxing.
        :type: BroadcastTsMuxingConfiguration
        """

        if configuration is not None:
            if not isinstance(configuration, BroadcastTsMuxingConfiguration):
                raise TypeError("Invalid type for `configuration`, type has to be `BroadcastTsMuxingConfiguration`")

            self._configuration = configuration


    @property
    def internal_chunk_length(self):
        """Gets the internal_chunk_length of this BroadcastTsMuxing.

        Modifies the internal chunk length used for chunked encoding

        :return: The internal_chunk_length of this BroadcastTsMuxing.
        :rtype: InternalChunkLength
        """
        return self._internal_chunk_length

    @internal_chunk_length.setter
    def internal_chunk_length(self, internal_chunk_length):
        """Sets the internal_chunk_length of this BroadcastTsMuxing.

        Modifies the internal chunk length used for chunked encoding

        :param internal_chunk_length: The internal_chunk_length of this BroadcastTsMuxing.
        :type: InternalChunkLength
        """

        if internal_chunk_length is not None:
            if not isinstance(internal_chunk_length, InternalChunkLength):
                raise TypeError("Invalid type for `internal_chunk_length`, type has to be `InternalChunkLength`")

            self._internal_chunk_length = internal_chunk_length

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(BroadcastTsMuxing, self).to_dict()

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
            if issubclass(BroadcastTsMuxing, dict):
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
        if not isinstance(other, BroadcastTsMuxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
