# coding: utf-8

from bitmovin_python.models.muxing_information_audio_track import MuxingInformationAudioTrack
from bitmovin_python.models.muxing_information_video_track import MuxingInformationVideoTrack
from bitmovin_python.models.progressive_muxing_information import ProgressiveMuxingInformation
from bitmovin_python.models.progressive_ts_muxing_information_byte_ranges import ProgressiveTsMuxingInformationByteRanges
import pprint
import six
from datetime import datetime
from enum import Enum


class ProgressiveTsMuxingInformation(ProgressiveMuxingInformation):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(ProgressiveTsMuxingInformation, self).openapi_types
        types.update({
            'byte_ranges': 'list[ProgressiveTsMuxingInformationByteRanges]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(ProgressiveTsMuxingInformation, self).attribute_map
        attributes.update({
            'byte_ranges': 'byteRanges'
        })
        return attributes

    def __init__(self, byte_ranges=None, *args, **kwargs):
        super(ProgressiveTsMuxingInformation, self).__init__(*args, **kwargs)

        self._byte_ranges = None
        self.discriminator = None

        if byte_ranges is not None:
            self.byte_ranges = byte_ranges

    @property
    def byte_ranges(self):
        """Gets the byte_ranges of this ProgressiveTsMuxingInformation.

        Byte ranges for the segments within the TS file

        :return: The byte_ranges of this ProgressiveTsMuxingInformation.
        :rtype: list[ProgressiveTsMuxingInformationByteRanges]
        """
        return self._byte_ranges

    @byte_ranges.setter
    def byte_ranges(self, byte_ranges):
        """Sets the byte_ranges of this ProgressiveTsMuxingInformation.

        Byte ranges for the segments within the TS file

        :param byte_ranges: The byte_ranges of this ProgressiveTsMuxingInformation.
        :type: list[ProgressiveTsMuxingInformationByteRanges]
        """

        if byte_ranges is not None:
            if not isinstance(byte_ranges, list):
                raise TypeError("Invalid type for `byte_ranges`, type has to be `list[ProgressiveTsMuxingInformationByteRanges]`")

            self._byte_ranges = byte_ranges

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(ProgressiveTsMuxingInformation, self).to_dict()

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
            if issubclass(ProgressiveTsMuxingInformation, dict):
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
        if not isinstance(other, ProgressiveTsMuxingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
