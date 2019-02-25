# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.encoding_output import EncodingOutput
from bitmovin_python.models.ignoring import Ignoring
from bitmovin_python.models.muxing_stream import MuxingStream
from bitmovin_python.models.muxing_type import MuxingType
from bitmovin_python.models.stream_conditions_mode import StreamConditionsMode
import pprint
import six
from datetime import datetime
from enum import Enum


class Muxing(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Muxing, self).openapi_types
        types.update({
            'streams': 'list[MuxingStream]',
            'outputs': 'list[EncodingOutput]',
            'type': 'MuxingType',
            'avg_bitrate': 'int',
            'min_bitrate': 'int',
            'max_bitrate': 'int',
            'ignored_by': 'list[Ignoring]',
            'stream_conditions_mode': 'StreamConditionsMode'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Muxing, self).attribute_map
        attributes.update({
            'streams': 'streams',
            'outputs': 'outputs',
            'type': 'type',
            'avg_bitrate': 'avgBitrate',
            'min_bitrate': 'minBitrate',
            'max_bitrate': 'maxBitrate',
            'ignored_by': 'ignoredBy',
            'stream_conditions_mode': 'streamConditionsMode'
        })
        return attributes

    discriminator_value_class_map = {
        'FMP4': 'Fmp4Muxing',
        'MP4': 'Mp4Muxing',
        'TS': 'TsMuxing',
        'WEBM': 'WebmMuxing',
        'MP3': 'Mp3Muxing',
        'PROGRESSIVE_WEBM': 'ProgressiveWebmMuxing',
        'PROGRESSIVE_MOV': 'ProgressiveMovMuxing',
        'PROGRESSIVE_TS': 'ProgressiveTsMuxing',
        'BROADCAST_TS': 'BroadcastTsMuxing'
    }

    def __init__(self, streams=None, outputs=None, type=None, avg_bitrate=None, min_bitrate=None, max_bitrate=None, ignored_by=None, stream_conditions_mode=None, *args, **kwargs):
        super(Muxing, self).__init__(*args, **kwargs)

        self._streams = None
        self._outputs = None
        self._type = None
        self._avg_bitrate = None
        self._min_bitrate = None
        self._max_bitrate = None
        self._ignored_by = None
        self._stream_conditions_mode = None
        self.discriminator = 'type'

        self.streams = streams
        if outputs is not None:
            self.outputs = outputs
        if type is not None:
            self.type = type
        if avg_bitrate is not None:
            self.avg_bitrate = avg_bitrate
        if min_bitrate is not None:
            self.min_bitrate = min_bitrate
        if max_bitrate is not None:
            self.max_bitrate = max_bitrate
        if ignored_by is not None:
            self.ignored_by = ignored_by
        if stream_conditions_mode is not None:
            self.stream_conditions_mode = stream_conditions_mode

    @property
    def streams(self):
        """Gets the streams of this Muxing.


        :return: The streams of this Muxing.
        :rtype: list[MuxingStream]
        """
        return self._streams

    @streams.setter
    def streams(self, streams):
        """Sets the streams of this Muxing.


        :param streams: The streams of this Muxing.
        :type: list[MuxingStream]
        """

        if streams is not None:
            if not isinstance(streams, list):
                raise TypeError("Invalid type for `streams`, type has to be `list[MuxingStream]`")

            self._streams = streams


    @property
    def outputs(self):
        """Gets the outputs of this Muxing.


        :return: The outputs of this Muxing.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this Muxing.


        :param outputs: The outputs of this Muxing.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

            self._outputs = outputs


    @property
    def type(self):
        """Gets the type of this Muxing.

        Type of the muxing

        :return: The type of this Muxing.
        :rtype: MuxingType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Muxing.

        Type of the muxing

        :param type: The type of this Muxing.
        :type: MuxingType
        """

        if type is not None:
            if not isinstance(type, MuxingType):
                raise TypeError("Invalid type for `type`, type has to be `MuxingType`")

            self._type = type


    @property
    def avg_bitrate(self):
        """Gets the avg_bitrate of this Muxing.

        Average bitrate. Available after encoding finishes.

        :return: The avg_bitrate of this Muxing.
        :rtype: int
        """
        return self._avg_bitrate

    @avg_bitrate.setter
    def avg_bitrate(self, avg_bitrate):
        """Sets the avg_bitrate of this Muxing.

        Average bitrate. Available after encoding finishes.

        :param avg_bitrate: The avg_bitrate of this Muxing.
        :type: int
        """

        if avg_bitrate is not None:
            if not isinstance(avg_bitrate, int):
                raise TypeError("Invalid type for `avg_bitrate`, type has to be `int`")

            self._avg_bitrate = avg_bitrate


    @property
    def min_bitrate(self):
        """Gets the min_bitrate of this Muxing.

        Min bitrate. Available after encoding finishes.

        :return: The min_bitrate of this Muxing.
        :rtype: int
        """
        return self._min_bitrate

    @min_bitrate.setter
    def min_bitrate(self, min_bitrate):
        """Sets the min_bitrate of this Muxing.

        Min bitrate. Available after encoding finishes.

        :param min_bitrate: The min_bitrate of this Muxing.
        :type: int
        """

        if min_bitrate is not None:
            if not isinstance(min_bitrate, int):
                raise TypeError("Invalid type for `min_bitrate`, type has to be `int`")

            self._min_bitrate = min_bitrate


    @property
    def max_bitrate(self):
        """Gets the max_bitrate of this Muxing.

        Max bitrate. Available after encoding finishes.

        :return: The max_bitrate of this Muxing.
        :rtype: int
        """
        return self._max_bitrate

    @max_bitrate.setter
    def max_bitrate(self, max_bitrate):
        """Sets the max_bitrate of this Muxing.

        Max bitrate. Available after encoding finishes.

        :param max_bitrate: The max_bitrate of this Muxing.
        :type: int
        """

        if max_bitrate is not None:
            if not isinstance(max_bitrate, int):
                raise TypeError("Invalid type for `max_bitrate`, type has to be `int`")

            self._max_bitrate = max_bitrate


    @property
    def ignored_by(self):
        """Gets the ignored_by of this Muxing.

        If this is set and contains objects, then this muxing has been ignored during the encoding process

        :return: The ignored_by of this Muxing.
        :rtype: list[Ignoring]
        """
        return self._ignored_by

    @ignored_by.setter
    def ignored_by(self, ignored_by):
        """Sets the ignored_by of this Muxing.

        If this is set and contains objects, then this muxing has been ignored during the encoding process

        :param ignored_by: The ignored_by of this Muxing.
        :type: list[Ignoring]
        """

        if ignored_by is not None:
            if not isinstance(ignored_by, list):
                raise TypeError("Invalid type for `ignored_by`, type has to be `list[Ignoring]`")

            self._ignored_by = ignored_by


    @property
    def stream_conditions_mode(self):
        """Gets the stream_conditions_mode of this Muxing.

        Specifies how to handle streams that don't fulfill stream conditions

        :return: The stream_conditions_mode of this Muxing.
        :rtype: StreamConditionsMode
        """
        return self._stream_conditions_mode

    @stream_conditions_mode.setter
    def stream_conditions_mode(self, stream_conditions_mode):
        """Sets the stream_conditions_mode of this Muxing.

        Specifies how to handle streams that don't fulfill stream conditions

        :param stream_conditions_mode: The stream_conditions_mode of this Muxing.
        :type: StreamConditionsMode
        """

        if stream_conditions_mode is not None:
            if not isinstance(stream_conditions_mode, StreamConditionsMode):
                raise TypeError("Invalid type for `stream_conditions_mode`, type has to be `StreamConditionsMode`")

            self._stream_conditions_mode = stream_conditions_mode

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator]
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Muxing, self).to_dict()

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
            if issubclass(Muxing, dict):
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
        if not isinstance(other, Muxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
