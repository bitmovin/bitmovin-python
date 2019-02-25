# coding: utf-8

from bitmovin_python.models.audio_group_configuration import AudioGroupConfiguration
from bitmovin_python.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from enum import Enum


class StreamInfo(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(StreamInfo, self).openapi_types
        types.update({
            'audio': 'str',
            'audio_groups': 'AudioGroupConfiguration',
            'video': 'str',
            'subtitles': 'str',
            'closed_captions': 'str',
            'encoding_id': 'str',
            'stream_id': 'str',
            'muxing_id': 'str',
            'drm_id': 'str',
            'segment_path': 'str',
            'uri': 'str',
            'start_segment_number': 'int',
            'end_segment_number': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(StreamInfo, self).attribute_map
        attributes.update({
            'audio': 'audio',
            'audio_groups': 'audioGroups',
            'video': 'video',
            'subtitles': 'subtitles',
            'closed_captions': 'closedCaptions',
            'encoding_id': 'encodingId',
            'stream_id': 'streamId',
            'muxing_id': 'muxingId',
            'drm_id': 'drmId',
            'segment_path': 'segmentPath',
            'uri': 'uri',
            'start_segment_number': 'startSegmentNumber',
            'end_segment_number': 'endSegmentNumber'
        })
        return attributes

    def __init__(self, audio=None, audio_groups=None, video=None, subtitles=None, closed_captions=None, encoding_id=None, stream_id=None, muxing_id=None, drm_id=None, segment_path=None, uri=None, start_segment_number=None, end_segment_number=None, *args, **kwargs):
        super(StreamInfo, self).__init__(*args, **kwargs)

        self._audio = None
        self._audio_groups = None
        self._video = None
        self._subtitles = None
        self._closed_captions = None
        self._encoding_id = None
        self._stream_id = None
        self._muxing_id = None
        self._drm_id = None
        self._segment_path = None
        self._uri = None
        self._start_segment_number = None
        self._end_segment_number = None
        self.discriminator = None

        if audio is not None:
            self.audio = audio
        if audio_groups is not None:
            self.audio_groups = audio_groups
        if video is not None:
            self.video = video
        if subtitles is not None:
            self.subtitles = subtitles
        self.closed_captions = closed_captions
        self.encoding_id = encoding_id
        self.stream_id = stream_id
        self.muxing_id = muxing_id
        if drm_id is not None:
            self.drm_id = drm_id
        self.segment_path = segment_path
        self.uri = uri
        if start_segment_number is not None:
            self.start_segment_number = start_segment_number
        if end_segment_number is not None:
            self.end_segment_number = end_segment_number

    @property
    def audio(self):
        """Gets the audio of this StreamInfo.

        It MUST match the value of the GROUP-ID attribute of an Audio EXT-X-MEDIA tag elsewhere in the Master Playlist. Either this or `audioGroups` must be set.

        :return: The audio of this StreamInfo.
        :rtype: str
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this StreamInfo.

        It MUST match the value of the GROUP-ID attribute of an Audio EXT-X-MEDIA tag elsewhere in the Master Playlist. Either this or `audioGroups` must be set.

        :param audio: The audio of this StreamInfo.
        :type: str
        """

        if audio is not None:
            if not isinstance(audio, str):
                raise TypeError("Invalid type for `audio`, type has to be `str`")

            self._audio = audio


    @property
    def audio_groups(self):
        """Gets the audio_groups of this StreamInfo.

        HLS Audio Group Configuration. You will want to use this configuration property in case you specify conditions on audio streams. The first matching audio group will be used for the specific variant stream. Either this or `audio` must be set.

        :return: The audio_groups of this StreamInfo.
        :rtype: AudioGroupConfiguration
        """
        return self._audio_groups

    @audio_groups.setter
    def audio_groups(self, audio_groups):
        """Sets the audio_groups of this StreamInfo.

        HLS Audio Group Configuration. You will want to use this configuration property in case you specify conditions on audio streams. The first matching audio group will be used for the specific variant stream. Either this or `audio` must be set.

        :param audio_groups: The audio_groups of this StreamInfo.
        :type: AudioGroupConfiguration
        """

        if audio_groups is not None:
            if not isinstance(audio_groups, AudioGroupConfiguration):
                raise TypeError("Invalid type for `audio_groups`, type has to be `AudioGroupConfiguration`")

            self._audio_groups = audio_groups


    @property
    def video(self):
        """Gets the video of this StreamInfo.

        It MUST match the value of the GROUP-ID attribute of a Video EXT-X-MEDIA tag elsewhere in the Master Playlist

        :return: The video of this StreamInfo.
        :rtype: str
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this StreamInfo.

        It MUST match the value of the GROUP-ID attribute of a Video EXT-X-MEDIA tag elsewhere in the Master Playlist

        :param video: The video of this StreamInfo.
        :type: str
        """

        if video is not None:
            if not isinstance(video, str):
                raise TypeError("Invalid type for `video`, type has to be `str`")

            self._video = video


    @property
    def subtitles(self):
        """Gets the subtitles of this StreamInfo.

        It MUST match the value of the GROUP-ID attribute of a Subtitles EXT-X-MEDIA tag elsewhere in the Master Playlist

        :return: The subtitles of this StreamInfo.
        :rtype: str
        """
        return self._subtitles

    @subtitles.setter
    def subtitles(self, subtitles):
        """Sets the subtitles of this StreamInfo.

        It MUST match the value of the GROUP-ID attribute of a Subtitles EXT-X-MEDIA tag elsewhere in the Master Playlist

        :param subtitles: The subtitles of this StreamInfo.
        :type: str
        """

        if subtitles is not None:
            if not isinstance(subtitles, str):
                raise TypeError("Invalid type for `subtitles`, type has to be `str`")

            self._subtitles = subtitles


    @property
    def closed_captions(self):
        """Gets the closed_captions of this StreamInfo.

        If the value is not 'NONE', it MUST match the value of the GROUP-ID attribute of a Closed Captions EXT-X-MEDIA tag elsewhere in the Playlist

        :return: The closed_captions of this StreamInfo.
        :rtype: str
        """
        return self._closed_captions

    @closed_captions.setter
    def closed_captions(self, closed_captions):
        """Sets the closed_captions of this StreamInfo.

        If the value is not 'NONE', it MUST match the value of the GROUP-ID attribute of a Closed Captions EXT-X-MEDIA tag elsewhere in the Playlist

        :param closed_captions: The closed_captions of this StreamInfo.
        :type: str
        """

        if closed_captions is not None:
            if not isinstance(closed_captions, str):
                raise TypeError("Invalid type for `closed_captions`, type has to be `str`")

            self._closed_captions = closed_captions


    @property
    def encoding_id(self):
        """Gets the encoding_id of this StreamInfo.

        Id of the encoding.

        :return: The encoding_id of this StreamInfo.
        :rtype: str
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        """Sets the encoding_id of this StreamInfo.

        Id of the encoding.

        :param encoding_id: The encoding_id of this StreamInfo.
        :type: str
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, str):
                raise TypeError("Invalid type for `encoding_id`, type has to be `str`")

            self._encoding_id = encoding_id


    @property
    def stream_id(self):
        """Gets the stream_id of this StreamInfo.

        Id of the stream.

        :return: The stream_id of this StreamInfo.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this StreamInfo.

        Id of the stream.

        :param stream_id: The stream_id of this StreamInfo.
        :type: str
        """

        if stream_id is not None:
            if not isinstance(stream_id, str):
                raise TypeError("Invalid type for `stream_id`, type has to be `str`")

            self._stream_id = stream_id


    @property
    def muxing_id(self):
        """Gets the muxing_id of this StreamInfo.

        Id of the muxing.

        :return: The muxing_id of this StreamInfo.
        :rtype: str
        """
        return self._muxing_id

    @muxing_id.setter
    def muxing_id(self, muxing_id):
        """Sets the muxing_id of this StreamInfo.

        Id of the muxing.

        :param muxing_id: The muxing_id of this StreamInfo.
        :type: str
        """

        if muxing_id is not None:
            if not isinstance(muxing_id, str):
                raise TypeError("Invalid type for `muxing_id`, type has to be `str`")

            self._muxing_id = muxing_id


    @property
    def drm_id(self):
        """Gets the drm_id of this StreamInfo.

        Id of the DRM.

        :return: The drm_id of this StreamInfo.
        :rtype: str
        """
        return self._drm_id

    @drm_id.setter
    def drm_id(self, drm_id):
        """Sets the drm_id of this StreamInfo.

        Id of the DRM.

        :param drm_id: The drm_id of this StreamInfo.
        :type: str
        """

        if drm_id is not None:
            if not isinstance(drm_id, str):
                raise TypeError("Invalid type for `drm_id`, type has to be `str`")

            self._drm_id = drm_id


    @property
    def segment_path(self):
        """Gets the segment_path of this StreamInfo.

        Path to segments.

        :return: The segment_path of this StreamInfo.
        :rtype: str
        """
        return self._segment_path

    @segment_path.setter
    def segment_path(self, segment_path):
        """Sets the segment_path of this StreamInfo.

        Path to segments.

        :param segment_path: The segment_path of this StreamInfo.
        :type: str
        """

        if segment_path is not None:
            if not isinstance(segment_path, str):
                raise TypeError("Invalid type for `segment_path`, type has to be `str`")

            self._segment_path = segment_path


    @property
    def uri(self):
        """Gets the uri of this StreamInfo.

        The URI of the playlist file.

        :return: The uri of this StreamInfo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this StreamInfo.

        The URI of the playlist file.

        :param uri: The uri of this StreamInfo.
        :type: str
        """

        if uri is not None:
            if not isinstance(uri, str):
                raise TypeError("Invalid type for `uri`, type has to be `str`")

            self._uri = uri


    @property
    def start_segment_number(self):
        """Gets the start_segment_number of this StreamInfo.

        Number of the first segment. Default is 0.

        :return: The start_segment_number of this StreamInfo.
        :rtype: int
        """
        return self._start_segment_number

    @start_segment_number.setter
    def start_segment_number(self, start_segment_number):
        """Sets the start_segment_number of this StreamInfo.

        Number of the first segment. Default is 0.

        :param start_segment_number: The start_segment_number of this StreamInfo.
        :type: int
        """

        if start_segment_number is not None:
            if not isinstance(start_segment_number, int):
                raise TypeError("Invalid type for `start_segment_number`, type has to be `int`")

            self._start_segment_number = start_segment_number


    @property
    def end_segment_number(self):
        """Gets the end_segment_number of this StreamInfo.

        Number of the last segment. Default is the last one that was encoded.

        :return: The end_segment_number of this StreamInfo.
        :rtype: int
        """
        return self._end_segment_number

    @end_segment_number.setter
    def end_segment_number(self, end_segment_number):
        """Sets the end_segment_number of this StreamInfo.

        Number of the last segment. Default is the last one that was encoded.

        :param end_segment_number: The end_segment_number of this StreamInfo.
        :type: int
        """

        if end_segment_number is not None:
            if not isinstance(end_segment_number, int):
                raise TypeError("Invalid type for `end_segment_number`, type has to be `int`")

            self._end_segment_number = end_segment_number

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(StreamInfo, self).to_dict()

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
            if issubclass(StreamInfo, dict):
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
        if not isinstance(other, StreamInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
