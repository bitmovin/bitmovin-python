# coding: utf-8

from bitmovin_python.models.audio_stream import AudioStream
from bitmovin_python.models.media_stream import MediaStream
from bitmovin_python.models.subtitle_stream import SubtitleStream
from bitmovin_python.models.video_stream import VideoStream
import pprint
import six
from datetime import datetime
from enum import Enum


class EncodingStreamInputDetails(object):
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
            'format_name': 'str',
            'start_time': 'float',
            'duration': 'float',
            'size': 'int',
            'bitrate': 'int',
            'tags': 'list[str]',
            'video_streams': 'list[VideoStream]',
            'audio_streams': 'list[AudioStream]',
            'meta_streams': 'list[MediaStream]',
            'subtitle_streams': 'list[SubtitleStream]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'format_name': 'formatName',
            'start_time': 'startTime',
            'duration': 'duration',
            'size': 'size',
            'bitrate': 'bitrate',
            'tags': 'tags',
            'video_streams': 'videoStreams',
            'audio_streams': 'audioStreams',
            'meta_streams': 'metaStreams',
            'subtitle_streams': 'subtitleStreams'
        }
        return attributes

    def __init__(self, format_name=None, start_time=None, duration=None, size=None, bitrate=None, tags=None, video_streams=None, audio_streams=None, meta_streams=None, subtitle_streams=None, *args, **kwargs):

        self._format_name = None
        self._start_time = None
        self._duration = None
        self._size = None
        self._bitrate = None
        self._tags = None
        self._video_streams = None
        self._audio_streams = None
        self._meta_streams = None
        self._subtitle_streams = None
        self.discriminator = None

        if format_name is not None:
            self.format_name = format_name
        if start_time is not None:
            self.start_time = start_time
        if duration is not None:
            self.duration = duration
        if size is not None:
            self.size = size
        if bitrate is not None:
            self.bitrate = bitrate
        if tags is not None:
            self.tags = tags
        if video_streams is not None:
            self.video_streams = video_streams
        if audio_streams is not None:
            self.audio_streams = audio_streams
        if meta_streams is not None:
            self.meta_streams = meta_streams
        if subtitle_streams is not None:
            self.subtitle_streams = subtitle_streams

    @property
    def format_name(self):
        """Gets the format_name of this EncodingStreamInputDetails.

        Format name

        :return: The format_name of this EncodingStreamInputDetails.
        :rtype: str
        """
        return self._format_name

    @format_name.setter
    def format_name(self, format_name):
        """Sets the format_name of this EncodingStreamInputDetails.

        Format name

        :param format_name: The format_name of this EncodingStreamInputDetails.
        :type: str
        """

        if format_name is not None:
            if not isinstance(format_name, str):
                raise TypeError("Invalid type for `format_name`, type has to be `str`")

            self._format_name = format_name


    @property
    def start_time(self):
        """Gets the start_time of this EncodingStreamInputDetails.

        The start time in seconds

        :return: The start_time of this EncodingStreamInputDetails.
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this EncodingStreamInputDetails.

        The start time in seconds

        :param start_time: The start_time of this EncodingStreamInputDetails.
        :type: float
        """

        if start_time is not None:
            if not isinstance(start_time, float):
                raise TypeError("Invalid type for `start_time`, type has to be `float`")

            self._start_time = start_time


    @property
    def duration(self):
        """Gets the duration of this EncodingStreamInputDetails.

        Duration in seconds

        :return: The duration of this EncodingStreamInputDetails.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this EncodingStreamInputDetails.

        Duration in seconds

        :param duration: The duration of this EncodingStreamInputDetails.
        :type: float
        """

        if duration is not None:
            if not isinstance(duration, float):
                raise TypeError("Invalid type for `duration`, type has to be `float`")

            self._duration = duration


    @property
    def size(self):
        """Gets the size of this EncodingStreamInputDetails.

        Input file size in bytes

        :return: The size of this EncodingStreamInputDetails.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this EncodingStreamInputDetails.

        Input file size in bytes

        :param size: The size of this EncodingStreamInputDetails.
        :type: int
        """

        if size is not None:
            if not isinstance(size, int):
                raise TypeError("Invalid type for `size`, type has to be `int`")

            self._size = size


    @property
    def bitrate(self):
        """Gets the bitrate of this EncodingStreamInputDetails.

        Bitrate in bps

        :return: The bitrate of this EncodingStreamInputDetails.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this EncodingStreamInputDetails.

        Bitrate in bps

        :param bitrate: The bitrate of this EncodingStreamInputDetails.
        :type: int
        """

        if bitrate is not None:
            if not isinstance(bitrate, int):
                raise TypeError("Invalid type for `bitrate`, type has to be `int`")

            self._bitrate = bitrate


    @property
    def tags(self):
        """Gets the tags of this EncodingStreamInputDetails.

        Additional metadata saved in the input file

        :return: The tags of this EncodingStreamInputDetails.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this EncodingStreamInputDetails.

        Additional metadata saved in the input file

        :param tags: The tags of this EncodingStreamInputDetails.
        :type: list[str]
        """

        if tags is not None:
            if not isinstance(tags, list):
                raise TypeError("Invalid type for `tags`, type has to be `list[str]`")

            self._tags = tags


    @property
    def video_streams(self):
        """Gets the video_streams of this EncodingStreamInputDetails.

        Video streams in the input file

        :return: The video_streams of this EncodingStreamInputDetails.
        :rtype: list[VideoStream]
        """
        return self._video_streams

    @video_streams.setter
    def video_streams(self, video_streams):
        """Sets the video_streams of this EncodingStreamInputDetails.

        Video streams in the input file

        :param video_streams: The video_streams of this EncodingStreamInputDetails.
        :type: list[VideoStream]
        """

        if video_streams is not None:
            if not isinstance(video_streams, list):
                raise TypeError("Invalid type for `video_streams`, type has to be `list[VideoStream]`")

            self._video_streams = video_streams


    @property
    def audio_streams(self):
        """Gets the audio_streams of this EncodingStreamInputDetails.

        Audio stream in the input file

        :return: The audio_streams of this EncodingStreamInputDetails.
        :rtype: list[AudioStream]
        """
        return self._audio_streams

    @audio_streams.setter
    def audio_streams(self, audio_streams):
        """Sets the audio_streams of this EncodingStreamInputDetails.

        Audio stream in the input file

        :param audio_streams: The audio_streams of this EncodingStreamInputDetails.
        :type: list[AudioStream]
        """

        if audio_streams is not None:
            if not isinstance(audio_streams, list):
                raise TypeError("Invalid type for `audio_streams`, type has to be `list[AudioStream]`")

            self._audio_streams = audio_streams


    @property
    def meta_streams(self):
        """Gets the meta_streams of this EncodingStreamInputDetails.

        Meta data streams in the input file

        :return: The meta_streams of this EncodingStreamInputDetails.
        :rtype: list[MediaStream]
        """
        return self._meta_streams

    @meta_streams.setter
    def meta_streams(self, meta_streams):
        """Sets the meta_streams of this EncodingStreamInputDetails.

        Meta data streams in the input file

        :param meta_streams: The meta_streams of this EncodingStreamInputDetails.
        :type: list[MediaStream]
        """

        if meta_streams is not None:
            if not isinstance(meta_streams, list):
                raise TypeError("Invalid type for `meta_streams`, type has to be `list[MediaStream]`")

            self._meta_streams = meta_streams


    @property
    def subtitle_streams(self):
        """Gets the subtitle_streams of this EncodingStreamInputDetails.

        Subtitle streams in the input file

        :return: The subtitle_streams of this EncodingStreamInputDetails.
        :rtype: list[SubtitleStream]
        """
        return self._subtitle_streams

    @subtitle_streams.setter
    def subtitle_streams(self, subtitle_streams):
        """Sets the subtitle_streams of this EncodingStreamInputDetails.

        Subtitle streams in the input file

        :param subtitle_streams: The subtitle_streams of this EncodingStreamInputDetails.
        :type: list[SubtitleStream]
        """

        if subtitle_streams is not None:
            if not isinstance(subtitle_streams, list):
                raise TypeError("Invalid type for `subtitle_streams`, type has to be `list[SubtitleStream]`")

            self._subtitle_streams = subtitle_streams

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
            if issubclass(EncodingStreamInputDetails, dict):
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
        if not isinstance(other, EncodingStreamInputDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
