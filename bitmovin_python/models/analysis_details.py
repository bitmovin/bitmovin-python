# coding: utf-8

from bitmovin_python.models.audio_stream_details import AudioStreamDetails
from bitmovin_python.models.meta_stream_details import MetaStreamDetails
from bitmovin_python.models.subtitle_stream_details import SubtitleStreamDetails
from bitmovin_python.models.video_stream_details import VideoStreamDetails
import pprint
import six
from datetime import datetime
from enum import Enum


class AnalysisDetails(object):
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
            'video_streams': 'list[VideoStreamDetails]',
            'audio_streams': 'list[AudioStreamDetails]',
            'meta_streams': 'list[MetaStreamDetails]',
            'subtitle_streams': 'list[SubtitleStreamDetails]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'video_streams': 'videoStreams',
            'audio_streams': 'audioStreams',
            'meta_streams': 'metaStreams',
            'subtitle_streams': 'subtitleStreams'
        }
        return attributes

    def __init__(self, video_streams=None, audio_streams=None, meta_streams=None, subtitle_streams=None, *args, **kwargs):

        self._video_streams = None
        self._audio_streams = None
        self._meta_streams = None
        self._subtitle_streams = None
        self.discriminator = None

        if video_streams is not None:
            self.video_streams = video_streams
        if audio_streams is not None:
            self.audio_streams = audio_streams
        if meta_streams is not None:
            self.meta_streams = meta_streams
        if subtitle_streams is not None:
            self.subtitle_streams = subtitle_streams

    @property
    def video_streams(self):
        """Gets the video_streams of this AnalysisDetails.


        :return: The video_streams of this AnalysisDetails.
        :rtype: list[VideoStreamDetails]
        """
        return self._video_streams

    @video_streams.setter
    def video_streams(self, video_streams):
        """Sets the video_streams of this AnalysisDetails.


        :param video_streams: The video_streams of this AnalysisDetails.
        :type: list[VideoStreamDetails]
        """

        if video_streams is not None:
            if not isinstance(video_streams, list):
                raise TypeError("Invalid type for `video_streams`, type has to be `list[VideoStreamDetails]`")

            self._video_streams = video_streams


    @property
    def audio_streams(self):
        """Gets the audio_streams of this AnalysisDetails.


        :return: The audio_streams of this AnalysisDetails.
        :rtype: list[AudioStreamDetails]
        """
        return self._audio_streams

    @audio_streams.setter
    def audio_streams(self, audio_streams):
        """Sets the audio_streams of this AnalysisDetails.


        :param audio_streams: The audio_streams of this AnalysisDetails.
        :type: list[AudioStreamDetails]
        """

        if audio_streams is not None:
            if not isinstance(audio_streams, list):
                raise TypeError("Invalid type for `audio_streams`, type has to be `list[AudioStreamDetails]`")

            self._audio_streams = audio_streams


    @property
    def meta_streams(self):
        """Gets the meta_streams of this AnalysisDetails.


        :return: The meta_streams of this AnalysisDetails.
        :rtype: list[MetaStreamDetails]
        """
        return self._meta_streams

    @meta_streams.setter
    def meta_streams(self, meta_streams):
        """Sets the meta_streams of this AnalysisDetails.


        :param meta_streams: The meta_streams of this AnalysisDetails.
        :type: list[MetaStreamDetails]
        """

        if meta_streams is not None:
            if not isinstance(meta_streams, list):
                raise TypeError("Invalid type for `meta_streams`, type has to be `list[MetaStreamDetails]`")

            self._meta_streams = meta_streams


    @property
    def subtitle_streams(self):
        """Gets the subtitle_streams of this AnalysisDetails.


        :return: The subtitle_streams of this AnalysisDetails.
        :rtype: list[SubtitleStreamDetails]
        """
        return self._subtitle_streams

    @subtitle_streams.setter
    def subtitle_streams(self, subtitle_streams):
        """Sets the subtitle_streams of this AnalysisDetails.


        :param subtitle_streams: The subtitle_streams of this AnalysisDetails.
        :type: list[SubtitleStreamDetails]
        """

        if subtitle_streams is not None:
            if not isinstance(subtitle_streams, list):
                raise TypeError("Invalid type for `subtitle_streams`, type has to be `list[SubtitleStreamDetails]`")

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
            if issubclass(AnalysisDetails, dict):
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
        if not isinstance(other, AnalysisDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
