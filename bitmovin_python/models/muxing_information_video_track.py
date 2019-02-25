# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class MuxingInformationVideoTrack(object):
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
            'index': 'int',
            'codec': 'str',
            'codec_iso': 'str',
            'bit_rate': 'int',
            'rate': 'int',
            'pixel_format': 'str',
            'frame_mode': 'str',
            'frame_width': 'int',
            'frame_height': 'int',
            'frame_rate': 'str',
            'start_time': 'float',
            'duration': 'float',
            'number_of_frames': 'int',
            'aspect_ratio': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'index': 'index',
            'codec': 'codec',
            'codec_iso': 'codecIso',
            'bit_rate': 'bitRate',
            'rate': 'rate',
            'pixel_format': 'pixelFormat',
            'frame_mode': 'frameMode',
            'frame_width': 'frameWidth',
            'frame_height': 'frameHeight',
            'frame_rate': 'frameRate',
            'start_time': 'startTime',
            'duration': 'duration',
            'number_of_frames': 'numberOfFrames',
            'aspect_ratio': 'aspectRatio'
        }
        return attributes

    def __init__(self, index=None, codec=None, codec_iso=None, bit_rate=None, rate=None, pixel_format=None, frame_mode=None, frame_width=None, frame_height=None, frame_rate=None, start_time=None, duration=None, number_of_frames=None, aspect_ratio=None, *args, **kwargs):

        self._index = None
        self._codec = None
        self._codec_iso = None
        self._bit_rate = None
        self._rate = None
        self._pixel_format = None
        self._frame_mode = None
        self._frame_width = None
        self._frame_height = None
        self._frame_rate = None
        self._start_time = None
        self._duration = None
        self._number_of_frames = None
        self._aspect_ratio = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if codec is not None:
            self.codec = codec
        if codec_iso is not None:
            self.codec_iso = codec_iso
        if bit_rate is not None:
            self.bit_rate = bit_rate
        if rate is not None:
            self.rate = rate
        if pixel_format is not None:
            self.pixel_format = pixel_format
        if frame_mode is not None:
            self.frame_mode = frame_mode
        if frame_width is not None:
            self.frame_width = frame_width
        if frame_height is not None:
            self.frame_height = frame_height
        if frame_rate is not None:
            self.frame_rate = frame_rate
        if start_time is not None:
            self.start_time = start_time
        if duration is not None:
            self.duration = duration
        if number_of_frames is not None:
            self.number_of_frames = number_of_frames
        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio

    @property
    def index(self):
        """Gets the index of this MuxingInformationVideoTrack.

        The stream index in the container

        :return: The index of this MuxingInformationVideoTrack.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this MuxingInformationVideoTrack.

        The stream index in the container

        :param index: The index of this MuxingInformationVideoTrack.
        :type: int
        """

        if index is not None:
            if not isinstance(index, int):
                raise TypeError("Invalid type for `index`, type has to be `int`")

            self._index = index


    @property
    def codec(self):
        """Gets the codec of this MuxingInformationVideoTrack.

        The codec used for the track

        :return: The codec of this MuxingInformationVideoTrack.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this MuxingInformationVideoTrack.

        The codec used for the track

        :param codec: The codec of this MuxingInformationVideoTrack.
        :type: str
        """

        if codec is not None:
            if not isinstance(codec, str):
                raise TypeError("Invalid type for `codec`, type has to be `str`")

            self._codec = codec


    @property
    def codec_iso(self):
        """Gets the codec_iso of this MuxingInformationVideoTrack.

        The codec string of the track

        :return: The codec_iso of this MuxingInformationVideoTrack.
        :rtype: str
        """
        return self._codec_iso

    @codec_iso.setter
    def codec_iso(self, codec_iso):
        """Sets the codec_iso of this MuxingInformationVideoTrack.

        The codec string of the track

        :param codec_iso: The codec_iso of this MuxingInformationVideoTrack.
        :type: str
        """

        if codec_iso is not None:
            if not isinstance(codec_iso, str):
                raise TypeError("Invalid type for `codec_iso`, type has to be `str`")

            self._codec_iso = codec_iso


    @property
    def bit_rate(self):
        """Gets the bit_rate of this MuxingInformationVideoTrack.

        The bitrate of the video track

        :return: The bit_rate of this MuxingInformationVideoTrack.
        :rtype: int
        """
        return self._bit_rate

    @bit_rate.setter
    def bit_rate(self, bit_rate):
        """Sets the bit_rate of this MuxingInformationVideoTrack.

        The bitrate of the video track

        :param bit_rate: The bit_rate of this MuxingInformationVideoTrack.
        :type: int
        """

        if bit_rate is not None:
            if not isinstance(bit_rate, int):
                raise TypeError("Invalid type for `bit_rate`, type has to be `int`")

            self._bit_rate = bit_rate


    @property
    def rate(self):
        """Gets the rate of this MuxingInformationVideoTrack.

        TODO add description

        :return: The rate of this MuxingInformationVideoTrack.
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this MuxingInformationVideoTrack.

        TODO add description

        :param rate: The rate of this MuxingInformationVideoTrack.
        :type: int
        """

        if rate is not None:
            if not isinstance(rate, int):
                raise TypeError("Invalid type for `rate`, type has to be `int`")

            self._rate = rate


    @property
    def pixel_format(self):
        """Gets the pixel_format of this MuxingInformationVideoTrack.

        The pixel format used

        :return: The pixel_format of this MuxingInformationVideoTrack.
        :rtype: str
        """
        return self._pixel_format

    @pixel_format.setter
    def pixel_format(self, pixel_format):
        """Sets the pixel_format of this MuxingInformationVideoTrack.

        The pixel format used

        :param pixel_format: The pixel_format of this MuxingInformationVideoTrack.
        :type: str
        """

        if pixel_format is not None:
            if not isinstance(pixel_format, str):
                raise TypeError("Invalid type for `pixel_format`, type has to be `str`")

            self._pixel_format = pixel_format


    @property
    def frame_mode(self):
        """Gets the frame_mode of this MuxingInformationVideoTrack.

        The frame mode (e.g. progressive)

        :return: The frame_mode of this MuxingInformationVideoTrack.
        :rtype: str
        """
        return self._frame_mode

    @frame_mode.setter
    def frame_mode(self, frame_mode):
        """Sets the frame_mode of this MuxingInformationVideoTrack.

        The frame mode (e.g. progressive)

        :param frame_mode: The frame_mode of this MuxingInformationVideoTrack.
        :type: str
        """

        if frame_mode is not None:
            if not isinstance(frame_mode, str):
                raise TypeError("Invalid type for `frame_mode`, type has to be `str`")

            self._frame_mode = frame_mode


    @property
    def frame_width(self):
        """Gets the frame_width of this MuxingInformationVideoTrack.

        The width of the frame in pixel

        :return: The frame_width of this MuxingInformationVideoTrack.
        :rtype: int
        """
        return self._frame_width

    @frame_width.setter
    def frame_width(self, frame_width):
        """Sets the frame_width of this MuxingInformationVideoTrack.

        The width of the frame in pixel

        :param frame_width: The frame_width of this MuxingInformationVideoTrack.
        :type: int
        """

        if frame_width is not None:
            if not isinstance(frame_width, int):
                raise TypeError("Invalid type for `frame_width`, type has to be `int`")

            self._frame_width = frame_width


    @property
    def frame_height(self):
        """Gets the frame_height of this MuxingInformationVideoTrack.

        The height of the frame in pixel

        :return: The frame_height of this MuxingInformationVideoTrack.
        :rtype: int
        """
        return self._frame_height

    @frame_height.setter
    def frame_height(self, frame_height):
        """Sets the frame_height of this MuxingInformationVideoTrack.

        The height of the frame in pixel

        :param frame_height: The frame_height of this MuxingInformationVideoTrack.
        :type: int
        """

        if frame_height is not None:
            if not isinstance(frame_height, int):
                raise TypeError("Invalid type for `frame_height`, type has to be `int`")

            self._frame_height = frame_height


    @property
    def frame_rate(self):
        """Gets the frame_rate of this MuxingInformationVideoTrack.

        The frame rate of the stream in fractional format

        :return: The frame_rate of this MuxingInformationVideoTrack.
        :rtype: str
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this MuxingInformationVideoTrack.

        The frame rate of the stream in fractional format

        :param frame_rate: The frame_rate of this MuxingInformationVideoTrack.
        :type: str
        """

        if frame_rate is not None:
            if not isinstance(frame_rate, str):
                raise TypeError("Invalid type for `frame_rate`, type has to be `str`")

            self._frame_rate = frame_rate


    @property
    def start_time(self):
        """Gets the start_time of this MuxingInformationVideoTrack.

        The start time in seconds

        :return: The start_time of this MuxingInformationVideoTrack.
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this MuxingInformationVideoTrack.

        The start time in seconds

        :param start_time: The start_time of this MuxingInformationVideoTrack.
        :type: float
        """

        if start_time is not None:
            if not isinstance(start_time, float):
                raise TypeError("Invalid type for `start_time`, type has to be `float`")

            self._start_time = start_time


    @property
    def duration(self):
        """Gets the duration of this MuxingInformationVideoTrack.

        The duration in seconds

        :return: The duration of this MuxingInformationVideoTrack.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this MuxingInformationVideoTrack.

        The duration in seconds

        :param duration: The duration of this MuxingInformationVideoTrack.
        :type: float
        """

        if duration is not None:
            if not isinstance(duration, float):
                raise TypeError("Invalid type for `duration`, type has to be `float`")

            self._duration = duration


    @property
    def number_of_frames(self):
        """Gets the number_of_frames of this MuxingInformationVideoTrack.

        The number of frames of that video track

        :return: The number_of_frames of this MuxingInformationVideoTrack.
        :rtype: int
        """
        return self._number_of_frames

    @number_of_frames.setter
    def number_of_frames(self, number_of_frames):
        """Sets the number_of_frames of this MuxingInformationVideoTrack.

        The number of frames of that video track

        :param number_of_frames: The number_of_frames of this MuxingInformationVideoTrack.
        :type: int
        """

        if number_of_frames is not None:
            if not isinstance(number_of_frames, int):
                raise TypeError("Invalid type for `number_of_frames`, type has to be `int`")

            self._number_of_frames = number_of_frames


    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this MuxingInformationVideoTrack.

        The aspect ratio of the stream

        :return: The aspect_ratio of this MuxingInformationVideoTrack.
        :rtype: str
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this MuxingInformationVideoTrack.

        The aspect ratio of the stream

        :param aspect_ratio: The aspect_ratio of this MuxingInformationVideoTrack.
        :type: str
        """

        if aspect_ratio is not None:
            if not isinstance(aspect_ratio, str):
                raise TypeError("Invalid type for `aspect_ratio`, type has to be `str`")

            self._aspect_ratio = aspect_ratio

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
            if issubclass(MuxingInformationVideoTrack, dict):
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
        if not isinstance(other, MuxingInformationVideoTrack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
