# coding: utf-8

from bitmovin_python.models.encoding_output import EncodingOutput
from bitmovin_python.models.fragmented_mp4_muxing_manifest_type import FragmentedMp4MuxingManifestType
from bitmovin_python.models.ignoring import Ignoring
from bitmovin_python.models.internal_chunk_length import InternalChunkLength
from bitmovin_python.models.muxing import Muxing
from bitmovin_python.models.muxing_stream import MuxingStream
from bitmovin_python.models.muxing_type import MuxingType
from bitmovin_python.models.stream_conditions_mode import StreamConditionsMode
from bitmovin_python.models.time_code import TimeCode
import pprint
import six
from datetime import datetime
from enum import Enum


class Mp4Muxing(Muxing):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Mp4Muxing, self).openapi_types
        types.update({
            'filename': 'str',
            'fragment_duration': 'int',
            'time_code': 'TimeCode',
            'fragmented_mp4_muxing_manifest_type': 'FragmentedMp4MuxingManifestType',
            'internal_chunk_length': 'InternalChunkLength'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Mp4Muxing, self).attribute_map
        attributes.update({
            'filename': 'filename',
            'fragment_duration': 'fragmentDuration',
            'time_code': 'timeCode',
            'fragmented_mp4_muxing_manifest_type': 'fragmentedMP4MuxingManifestType',
            'internal_chunk_length': 'internalChunkLength'
        })
        return attributes

    def __init__(self, filename=None, fragment_duration=None, time_code=None, fragmented_mp4_muxing_manifest_type=None, internal_chunk_length=None, *args, **kwargs):
        super(Mp4Muxing, self).__init__(*args, **kwargs)

        self._filename = None
        self._fragment_duration = None
        self._time_code = None
        self._fragmented_mp4_muxing_manifest_type = None
        self._internal_chunk_length = None
        self.discriminator = None

        if filename is not None:
            self.filename = filename
        if fragment_duration is not None:
            self.fragment_duration = fragment_duration
        if time_code is not None:
            self.time_code = time_code
        if fragmented_mp4_muxing_manifest_type is not None:
            self.fragmented_mp4_muxing_manifest_type = fragmented_mp4_muxing_manifest_type
        if internal_chunk_length is not None:
            self.internal_chunk_length = internal_chunk_length

    @property
    def filename(self):
        """Gets the filename of this Mp4Muxing.

        Name of the new Video

        :return: The filename of this Mp4Muxing.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Mp4Muxing.

        Name of the new Video

        :param filename: The filename of this Mp4Muxing.
        :type: str
        """

        if filename is not None:
            if not isinstance(filename, str):
                raise TypeError("Invalid type for `filename`, type has to be `str`")

            self._filename = filename


    @property
    def fragment_duration(self):
        """Gets the fragment_duration of this Mp4Muxing.

         Duration of fragments in milliseconds. Required for Fragmented MP4 Muxing (for Smooth Streaming or DASH On-Demand). Not setting this will result in unfragmented mp4.

        :return: The fragment_duration of this Mp4Muxing.
        :rtype: int
        """
        return self._fragment_duration

    @fragment_duration.setter
    def fragment_duration(self, fragment_duration):
        """Sets the fragment_duration of this Mp4Muxing.

         Duration of fragments in milliseconds. Required for Fragmented MP4 Muxing (for Smooth Streaming or DASH On-Demand). Not setting this will result in unfragmented mp4.

        :param fragment_duration: The fragment_duration of this Mp4Muxing.
        :type: int
        """

        if fragment_duration is not None:
            if not isinstance(fragment_duration, int):
                raise TypeError("Invalid type for `fragment_duration`, type has to be `int`")

            self._fragment_duration = fragment_duration


    @property
    def time_code(self):
        """Gets the time_code of this Mp4Muxing.


        :return: The time_code of this Mp4Muxing.
        :rtype: TimeCode
        """
        return self._time_code

    @time_code.setter
    def time_code(self, time_code):
        """Sets the time_code of this Mp4Muxing.


        :param time_code: The time_code of this Mp4Muxing.
        :type: TimeCode
        """

        if time_code is not None:
            if not isinstance(time_code, TimeCode):
                raise TypeError("Invalid type for `time_code`, type has to be `TimeCode`")

            self._time_code = time_code


    @property
    def fragmented_mp4_muxing_manifest_type(self):
        """Gets the fragmented_mp4_muxing_manifest_type of this Mp4Muxing.


        :return: The fragmented_mp4_muxing_manifest_type of this Mp4Muxing.
        :rtype: FragmentedMp4MuxingManifestType
        """
        return self._fragmented_mp4_muxing_manifest_type

    @fragmented_mp4_muxing_manifest_type.setter
    def fragmented_mp4_muxing_manifest_type(self, fragmented_mp4_muxing_manifest_type):
        """Sets the fragmented_mp4_muxing_manifest_type of this Mp4Muxing.


        :param fragmented_mp4_muxing_manifest_type: The fragmented_mp4_muxing_manifest_type of this Mp4Muxing.
        :type: FragmentedMp4MuxingManifestType
        """

        if fragmented_mp4_muxing_manifest_type is not None:
            if not isinstance(fragmented_mp4_muxing_manifest_type, FragmentedMp4MuxingManifestType):
                raise TypeError("Invalid type for `fragmented_mp4_muxing_manifest_type`, type has to be `FragmentedMp4MuxingManifestType`")

            self._fragmented_mp4_muxing_manifest_type = fragmented_mp4_muxing_manifest_type


    @property
    def internal_chunk_length(self):
        """Gets the internal_chunk_length of this Mp4Muxing.

        Modifies the internal chunk length used for chunked encoding

        :return: The internal_chunk_length of this Mp4Muxing.
        :rtype: InternalChunkLength
        """
        return self._internal_chunk_length

    @internal_chunk_length.setter
    def internal_chunk_length(self, internal_chunk_length):
        """Sets the internal_chunk_length of this Mp4Muxing.

        Modifies the internal chunk length used for chunked encoding

        :param internal_chunk_length: The internal_chunk_length of this Mp4Muxing.
        :type: InternalChunkLength
        """

        if internal_chunk_length is not None:
            if not isinstance(internal_chunk_length, InternalChunkLength):
                raise TypeError("Invalid type for `internal_chunk_length`, type has to be `InternalChunkLength`")

            self._internal_chunk_length = internal_chunk_length

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Mp4Muxing, self).to_dict()

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
            if issubclass(Mp4Muxing, dict):
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
        if not isinstance(other, Mp4Muxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
