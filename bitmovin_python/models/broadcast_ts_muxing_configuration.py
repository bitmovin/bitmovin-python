# coding: utf-8

from bitmovin_python.models.broadcast_ts_audio_input_stream_configuration import BroadcastTsAudioInputStreamConfiguration
from bitmovin_python.models.broadcast_ts_program_configuration import BroadcastTsProgramConfiguration
from bitmovin_python.models.broadcast_ts_transport_configuration import BroadcastTsTransportConfiguration
from bitmovin_python.models.broadcast_ts_video_input_stream_configuration import BroadcastTsVideoInputStreamConfiguration
import pprint
import six
from datetime import datetime
from enum import Enum


class BroadcastTsMuxingConfiguration(object):
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
            'transport': 'BroadcastTsTransportConfiguration',
            'program': 'BroadcastTsProgramConfiguration',
            'video_streams': 'list[BroadcastTsVideoInputStreamConfiguration]',
            'audio_streams': 'list[BroadcastTsAudioInputStreamConfiguration]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'transport': 'transport',
            'program': 'program',
            'video_streams': 'videoStreams',
            'audio_streams': 'audioStreams'
        }
        return attributes

    def __init__(self, transport=None, program=None, video_streams=None, audio_streams=None, *args, **kwargs):

        self._transport = None
        self._program = None
        self._video_streams = None
        self._audio_streams = None
        self.discriminator = None

        if transport is not None:
            self.transport = transport
        if program is not None:
            self.program = program
        if video_streams is not None:
            self.video_streams = video_streams
        if audio_streams is not None:
            self.audio_streams = audio_streams

    @property
    def transport(self):
        """Gets the transport of this BroadcastTsMuxingConfiguration.

        Transport configuration details for the Broadcast TS muxing.

        :return: The transport of this BroadcastTsMuxingConfiguration.
        :rtype: BroadcastTsTransportConfiguration
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        """Sets the transport of this BroadcastTsMuxingConfiguration.

        Transport configuration details for the Broadcast TS muxing.

        :param transport: The transport of this BroadcastTsMuxingConfiguration.
        :type: BroadcastTsTransportConfiguration
        """

        if transport is not None:
            if not isinstance(transport, BroadcastTsTransportConfiguration):
                raise TypeError("Invalid type for `transport`, type has to be `BroadcastTsTransportConfiguration`")

            self._transport = transport


    @property
    def program(self):
        """Gets the program of this BroadcastTsMuxingConfiguration.

        Program configuration details for the Broadcast TS muxing.

        :return: The program of this BroadcastTsMuxingConfiguration.
        :rtype: BroadcastTsProgramConfiguration
        """
        return self._program

    @program.setter
    def program(self, program):
        """Sets the program of this BroadcastTsMuxingConfiguration.

        Program configuration details for the Broadcast TS muxing.

        :param program: The program of this BroadcastTsMuxingConfiguration.
        :type: BroadcastTsProgramConfiguration
        """

        if program is not None:
            if not isinstance(program, BroadcastTsProgramConfiguration):
                raise TypeError("Invalid type for `program`, type has to be `BroadcastTsProgramConfiguration`")

            self._program = program


    @property
    def video_streams(self):
        """Gets the video_streams of this BroadcastTsMuxingConfiguration.


        :return: The video_streams of this BroadcastTsMuxingConfiguration.
        :rtype: list[BroadcastTsVideoInputStreamConfiguration]
        """
        return self._video_streams

    @video_streams.setter
    def video_streams(self, video_streams):
        """Sets the video_streams of this BroadcastTsMuxingConfiguration.


        :param video_streams: The video_streams of this BroadcastTsMuxingConfiguration.
        :type: list[BroadcastTsVideoInputStreamConfiguration]
        """

        if video_streams is not None:
            if not isinstance(video_streams, list):
                raise TypeError("Invalid type for `video_streams`, type has to be `list[BroadcastTsVideoInputStreamConfiguration]`")

            self._video_streams = video_streams


    @property
    def audio_streams(self):
        """Gets the audio_streams of this BroadcastTsMuxingConfiguration.


        :return: The audio_streams of this BroadcastTsMuxingConfiguration.
        :rtype: list[BroadcastTsAudioInputStreamConfiguration]
        """
        return self._audio_streams

    @audio_streams.setter
    def audio_streams(self, audio_streams):
        """Sets the audio_streams of this BroadcastTsMuxingConfiguration.


        :param audio_streams: The audio_streams of this BroadcastTsMuxingConfiguration.
        :type: list[BroadcastTsAudioInputStreamConfiguration]
        """

        if audio_streams is not None:
            if not isinstance(audio_streams, list):
                raise TypeError("Invalid type for `audio_streams`, type has to be `list[BroadcastTsAudioInputStreamConfiguration]`")

            self._audio_streams = audio_streams

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
            if issubclass(BroadcastTsMuxingConfiguration, dict):
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
        if not isinstance(other, BroadcastTsMuxingConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
