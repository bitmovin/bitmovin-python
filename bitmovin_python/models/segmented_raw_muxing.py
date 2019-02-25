# coding: utf-8

from bitmovin_python.models.encoding_output import EncodingOutput
from bitmovin_python.models.ignoring import Ignoring
from bitmovin_python.models.muxing import Muxing
from bitmovin_python.models.muxing_stream import MuxingStream
from bitmovin_python.models.muxing_type import MuxingType
from bitmovin_python.models.stream_conditions_mode import StreamConditionsMode
import pprint
import six
from datetime import datetime
from enum import Enum


class SegmentedRawMuxing(Muxing):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(SegmentedRawMuxing, self).openapi_types
        types.update({
            'segment_length': 'float',
            'segment_naming': 'str',
            'segments_muxed': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(SegmentedRawMuxing, self).attribute_map
        attributes.update({
            'segment_length': 'segmentLength',
            'segment_naming': 'segmentNaming',
            'segments_muxed': 'segmentsMuxed'
        })
        return attributes

    def __init__(self, segment_length=None, segment_naming=None, segments_muxed=None, *args, **kwargs):
        super(SegmentedRawMuxing, self).__init__(*args, **kwargs)

        self._segment_length = None
        self._segment_naming = None
        self._segments_muxed = None
        self.discriminator = None

        self.segment_length = segment_length
        self.segment_naming = segment_naming
        if segments_muxed is not None:
            self.segments_muxed = segments_muxed

    @property
    def segment_length(self):
        """Gets the segment_length of this SegmentedRawMuxing.

        Length of the fragments in seconds

        :return: The segment_length of this SegmentedRawMuxing.
        :rtype: float
        """
        return self._segment_length

    @segment_length.setter
    def segment_length(self, segment_length):
        """Sets the segment_length of this SegmentedRawMuxing.

        Length of the fragments in seconds

        :param segment_length: The segment_length of this SegmentedRawMuxing.
        :type: float
        """

        if segment_length is not None:
            if not isinstance(segment_length, float):
                raise TypeError("Invalid type for `segment_length`, type has to be `float`")

            self._segment_length = segment_length


    @property
    def segment_naming(self):
        """Gets the segment_naming of this SegmentedRawMuxing.

        Segment naming policy

        :return: The segment_naming of this SegmentedRawMuxing.
        :rtype: str
        """
        return self._segment_naming

    @segment_naming.setter
    def segment_naming(self, segment_naming):
        """Sets the segment_naming of this SegmentedRawMuxing.

        Segment naming policy

        :param segment_naming: The segment_naming of this SegmentedRawMuxing.
        :type: str
        """

        if segment_naming is not None:
            if not isinstance(segment_naming, str):
                raise TypeError("Invalid type for `segment_naming`, type has to be `str`")

            self._segment_naming = segment_naming


    @property
    def segments_muxed(self):
        """Gets the segments_muxed of this SegmentedRawMuxing.

        Number of segments which have been encoded

        :return: The segments_muxed of this SegmentedRawMuxing.
        :rtype: int
        """
        return self._segments_muxed

    @segments_muxed.setter
    def segments_muxed(self, segments_muxed):
        """Sets the segments_muxed of this SegmentedRawMuxing.

        Number of segments which have been encoded

        :param segments_muxed: The segments_muxed of this SegmentedRawMuxing.
        :type: int
        """

        if segments_muxed is not None:
            if not isinstance(segments_muxed, int):
                raise TypeError("Invalid type for `segments_muxed`, type has to be `int`")

            self._segments_muxed = segments_muxed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(SegmentedRawMuxing, self).to_dict()

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
            if issubclass(SegmentedRawMuxing, dict):
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
        if not isinstance(other, SegmentedRawMuxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
