# coding: utf-8

from bitmovin_python.models.live_encoding_codec import LiveEncodingCodec
from bitmovin_python.models.media_type import MediaType
import pprint
import six
from datetime import datetime
from enum import Enum


class StreamInfosDetails(object):
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
            'id': 'int',
            'media_type': 'MediaType',
            'width': 'int',
            'height': 'int',
            'rate': 'int',
            'codec': 'LiveEncodingCodec',
            'samples_read_per_second_min': 'float',
            'samples_read_per_second_max': 'float',
            'samples_read_per_second_avg': 'float',
            'samples_backup_per_second_min': 'float',
            'samples_backup_per_second_max': 'float',
            'samples_backup_per_second_avg': 'float',
            'bytes_read_per_second_min': 'float',
            'bytes_read_per_second_max': 'float',
            'bytes_read_per_second_avg': 'float',
            'bytes_backup_per_second_min': 'float',
            'bytes_backup_per_second_max': 'float',
            'bytes_backup_per_second_avg': 'float'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'media_type': 'mediaType',
            'width': 'width',
            'height': 'height',
            'rate': 'rate',
            'codec': 'codec',
            'samples_read_per_second_min': 'samplesReadPerSecondMin',
            'samples_read_per_second_max': 'samplesReadPerSecondMax',
            'samples_read_per_second_avg': 'samplesReadPerSecondAvg',
            'samples_backup_per_second_min': 'samplesBackupPerSecondMin',
            'samples_backup_per_second_max': 'samplesBackupPerSecondMax',
            'samples_backup_per_second_avg': 'samplesBackupPerSecondAvg',
            'bytes_read_per_second_min': 'bytesReadPerSecondMin',
            'bytes_read_per_second_max': 'bytesReadPerSecondMax',
            'bytes_read_per_second_avg': 'bytesReadPerSecondAvg',
            'bytes_backup_per_second_min': 'bytesBackupPerSecondMin',
            'bytes_backup_per_second_max': 'bytesBackupPerSecondMax',
            'bytes_backup_per_second_avg': 'bytesBackupPerSecondAvg'
        }
        return attributes

    def __init__(self, id=None, media_type=None, width=None, height=None, rate=None, codec=None, samples_read_per_second_min=None, samples_read_per_second_max=None, samples_read_per_second_avg=None, samples_backup_per_second_min=None, samples_backup_per_second_max=None, samples_backup_per_second_avg=None, bytes_read_per_second_min=None, bytes_read_per_second_max=None, bytes_read_per_second_avg=None, bytes_backup_per_second_min=None, bytes_backup_per_second_max=None, bytes_backup_per_second_avg=None, *args, **kwargs):

        self._id = None
        self._media_type = None
        self._width = None
        self._height = None
        self._rate = None
        self._codec = None
        self._samples_read_per_second_min = None
        self._samples_read_per_second_max = None
        self._samples_read_per_second_avg = None
        self._samples_backup_per_second_min = None
        self._samples_backup_per_second_max = None
        self._samples_backup_per_second_avg = None
        self._bytes_read_per_second_min = None
        self._bytes_read_per_second_max = None
        self._bytes_read_per_second_avg = None
        self._bytes_backup_per_second_min = None
        self._bytes_backup_per_second_max = None
        self._bytes_backup_per_second_avg = None
        self.discriminator = None

        self.id = id
        self.media_type = media_type
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        self.rate = rate
        self.codec = codec
        self.samples_read_per_second_min = samples_read_per_second_min
        self.samples_read_per_second_max = samples_read_per_second_max
        self.samples_read_per_second_avg = samples_read_per_second_avg
        self.samples_backup_per_second_min = samples_backup_per_second_min
        self.samples_backup_per_second_max = samples_backup_per_second_max
        self.samples_backup_per_second_avg = samples_backup_per_second_avg
        self.bytes_read_per_second_min = bytes_read_per_second_min
        self.bytes_read_per_second_max = bytes_read_per_second_max
        self.bytes_read_per_second_avg = bytes_read_per_second_avg
        self.bytes_backup_per_second_min = bytes_backup_per_second_min
        self.bytes_backup_per_second_max = bytes_backup_per_second_max
        self.bytes_backup_per_second_avg = bytes_backup_per_second_avg

    @property
    def id(self):
        """Gets the id of this StreamInfosDetails.

        The id of the stream

        :return: The id of this StreamInfosDetails.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StreamInfosDetails.

        The id of the stream

        :param id: The id of this StreamInfosDetails.
        :type: int
        """

        if id is not None:
            if not isinstance(id, int):
                raise TypeError("Invalid type for `id`, type has to be `int`")

            self._id = id


    @property
    def media_type(self):
        """Gets the media_type of this StreamInfosDetails.

        The media type of the stream

        :return: The media_type of this StreamInfosDetails.
        :rtype: MediaType
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this StreamInfosDetails.

        The media type of the stream

        :param media_type: The media_type of this StreamInfosDetails.
        :type: MediaType
        """

        if media_type is not None:
            if not isinstance(media_type, MediaType):
                raise TypeError("Invalid type for `media_type`, type has to be `MediaType`")

            self._media_type = media_type


    @property
    def width(self):
        """Gets the width of this StreamInfosDetails.

        The width of the stream, if it is a video stream

        :return: The width of this StreamInfosDetails.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this StreamInfosDetails.

        The width of the stream, if it is a video stream

        :param width: The width of this StreamInfosDetails.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

            self._width = width


    @property
    def height(self):
        """Gets the height of this StreamInfosDetails.

        The height of the stream, if it is a video stream

        :return: The height of this StreamInfosDetails.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this StreamInfosDetails.

        The height of the stream, if it is a video stream

        :param height: The height of this StreamInfosDetails.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

            self._height = height


    @property
    def rate(self):
        """Gets the rate of this StreamInfosDetails.

        The rate (sample rate / fps) of the stream

        :return: The rate of this StreamInfosDetails.
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this StreamInfosDetails.

        The rate (sample rate / fps) of the stream

        :param rate: The rate of this StreamInfosDetails.
        :type: int
        """

        if rate is not None:
            if not isinstance(rate, int):
                raise TypeError("Invalid type for `rate`, type has to be `int`")

            self._rate = rate


    @property
    def codec(self):
        """Gets the codec of this StreamInfosDetails.

        The codec of the input stream

        :return: The codec of this StreamInfosDetails.
        :rtype: LiveEncodingCodec
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this StreamInfosDetails.

        The codec of the input stream

        :param codec: The codec of this StreamInfosDetails.
        :type: LiveEncodingCodec
        """

        if codec is not None:
            if not isinstance(codec, LiveEncodingCodec):
                raise TypeError("Invalid type for `codec`, type has to be `LiveEncodingCodec`")

            self._codec = codec


    @property
    def samples_read_per_second_min(self):
        """Gets the samples_read_per_second_min of this StreamInfosDetails.

        The minimum samples read per second within the last minute

        :return: The samples_read_per_second_min of this StreamInfosDetails.
        :rtype: float
        """
        return self._samples_read_per_second_min

    @samples_read_per_second_min.setter
    def samples_read_per_second_min(self, samples_read_per_second_min):
        """Sets the samples_read_per_second_min of this StreamInfosDetails.

        The minimum samples read per second within the last minute

        :param samples_read_per_second_min: The samples_read_per_second_min of this StreamInfosDetails.
        :type: float
        """

        if samples_read_per_second_min is not None:
            if not isinstance(samples_read_per_second_min, float):
                raise TypeError("Invalid type for `samples_read_per_second_min`, type has to be `float`")

            self._samples_read_per_second_min = samples_read_per_second_min


    @property
    def samples_read_per_second_max(self):
        """Gets the samples_read_per_second_max of this StreamInfosDetails.

        The maximum samples read per second within the last minute

        :return: The samples_read_per_second_max of this StreamInfosDetails.
        :rtype: float
        """
        return self._samples_read_per_second_max

    @samples_read_per_second_max.setter
    def samples_read_per_second_max(self, samples_read_per_second_max):
        """Sets the samples_read_per_second_max of this StreamInfosDetails.

        The maximum samples read per second within the last minute

        :param samples_read_per_second_max: The samples_read_per_second_max of this StreamInfosDetails.
        :type: float
        """

        if samples_read_per_second_max is not None:
            if not isinstance(samples_read_per_second_max, float):
                raise TypeError("Invalid type for `samples_read_per_second_max`, type has to be `float`")

            self._samples_read_per_second_max = samples_read_per_second_max


    @property
    def samples_read_per_second_avg(self):
        """Gets the samples_read_per_second_avg of this StreamInfosDetails.

        The average samples read per second within the last minute

        :return: The samples_read_per_second_avg of this StreamInfosDetails.
        :rtype: float
        """
        return self._samples_read_per_second_avg

    @samples_read_per_second_avg.setter
    def samples_read_per_second_avg(self, samples_read_per_second_avg):
        """Sets the samples_read_per_second_avg of this StreamInfosDetails.

        The average samples read per second within the last minute

        :param samples_read_per_second_avg: The samples_read_per_second_avg of this StreamInfosDetails.
        :type: float
        """

        if samples_read_per_second_avg is not None:
            if not isinstance(samples_read_per_second_avg, float):
                raise TypeError("Invalid type for `samples_read_per_second_avg`, type has to be `float`")

            self._samples_read_per_second_avg = samples_read_per_second_avg


    @property
    def samples_backup_per_second_min(self):
        """Gets the samples_backup_per_second_min of this StreamInfosDetails.

        The minimum amount of backup samples used per second within the last minute. This will be written when no live stream is ingested. The last picture will be repeated with silent audio.

        :return: The samples_backup_per_second_min of this StreamInfosDetails.
        :rtype: float
        """
        return self._samples_backup_per_second_min

    @samples_backup_per_second_min.setter
    def samples_backup_per_second_min(self, samples_backup_per_second_min):
        """Sets the samples_backup_per_second_min of this StreamInfosDetails.

        The minimum amount of backup samples used per second within the last minute. This will be written when no live stream is ingested. The last picture will be repeated with silent audio.

        :param samples_backup_per_second_min: The samples_backup_per_second_min of this StreamInfosDetails.
        :type: float
        """

        if samples_backup_per_second_min is not None:
            if not isinstance(samples_backup_per_second_min, float):
                raise TypeError("Invalid type for `samples_backup_per_second_min`, type has to be `float`")

            self._samples_backup_per_second_min = samples_backup_per_second_min


    @property
    def samples_backup_per_second_max(self):
        """Gets the samples_backup_per_second_max of this StreamInfosDetails.

        The maximum amount of backup samples used per second within the last minute. This will be written when no live stream is ingested. The last picture will be repeated with silent audio.

        :return: The samples_backup_per_second_max of this StreamInfosDetails.
        :rtype: float
        """
        return self._samples_backup_per_second_max

    @samples_backup_per_second_max.setter
    def samples_backup_per_second_max(self, samples_backup_per_second_max):
        """Sets the samples_backup_per_second_max of this StreamInfosDetails.

        The maximum amount of backup samples used per second within the last minute. This will be written when no live stream is ingested. The last picture will be repeated with silent audio.

        :param samples_backup_per_second_max: The samples_backup_per_second_max of this StreamInfosDetails.
        :type: float
        """

        if samples_backup_per_second_max is not None:
            if not isinstance(samples_backup_per_second_max, float):
                raise TypeError("Invalid type for `samples_backup_per_second_max`, type has to be `float`")

            self._samples_backup_per_second_max = samples_backup_per_second_max


    @property
    def samples_backup_per_second_avg(self):
        """Gets the samples_backup_per_second_avg of this StreamInfosDetails.

        The average amount of backup samples used per second within the last minute. This will be written when no live stream is ingested. The last picture will be repeated with silent audio.

        :return: The samples_backup_per_second_avg of this StreamInfosDetails.
        :rtype: float
        """
        return self._samples_backup_per_second_avg

    @samples_backup_per_second_avg.setter
    def samples_backup_per_second_avg(self, samples_backup_per_second_avg):
        """Sets the samples_backup_per_second_avg of this StreamInfosDetails.

        The average amount of backup samples used per second within the last minute. This will be written when no live stream is ingested. The last picture will be repeated with silent audio.

        :param samples_backup_per_second_avg: The samples_backup_per_second_avg of this StreamInfosDetails.
        :type: float
        """

        if samples_backup_per_second_avg is not None:
            if not isinstance(samples_backup_per_second_avg, float):
                raise TypeError("Invalid type for `samples_backup_per_second_avg`, type has to be `float`")

            self._samples_backup_per_second_avg = samples_backup_per_second_avg


    @property
    def bytes_read_per_second_min(self):
        """Gets the bytes_read_per_second_min of this StreamInfosDetails.

        The minimum bytes read per second within the last minute

        :return: The bytes_read_per_second_min of this StreamInfosDetails.
        :rtype: float
        """
        return self._bytes_read_per_second_min

    @bytes_read_per_second_min.setter
    def bytes_read_per_second_min(self, bytes_read_per_second_min):
        """Sets the bytes_read_per_second_min of this StreamInfosDetails.

        The minimum bytes read per second within the last minute

        :param bytes_read_per_second_min: The bytes_read_per_second_min of this StreamInfosDetails.
        :type: float
        """

        if bytes_read_per_second_min is not None:
            if not isinstance(bytes_read_per_second_min, float):
                raise TypeError("Invalid type for `bytes_read_per_second_min`, type has to be `float`")

            self._bytes_read_per_second_min = bytes_read_per_second_min


    @property
    def bytes_read_per_second_max(self):
        """Gets the bytes_read_per_second_max of this StreamInfosDetails.

        The maximum bytes read per second within the last minute

        :return: The bytes_read_per_second_max of this StreamInfosDetails.
        :rtype: float
        """
        return self._bytes_read_per_second_max

    @bytes_read_per_second_max.setter
    def bytes_read_per_second_max(self, bytes_read_per_second_max):
        """Sets the bytes_read_per_second_max of this StreamInfosDetails.

        The maximum bytes read per second within the last minute

        :param bytes_read_per_second_max: The bytes_read_per_second_max of this StreamInfosDetails.
        :type: float
        """

        if bytes_read_per_second_max is not None:
            if not isinstance(bytes_read_per_second_max, float):
                raise TypeError("Invalid type for `bytes_read_per_second_max`, type has to be `float`")

            self._bytes_read_per_second_max = bytes_read_per_second_max


    @property
    def bytes_read_per_second_avg(self):
        """Gets the bytes_read_per_second_avg of this StreamInfosDetails.

        The average bytes read per second within the last minute

        :return: The bytes_read_per_second_avg of this StreamInfosDetails.
        :rtype: float
        """
        return self._bytes_read_per_second_avg

    @bytes_read_per_second_avg.setter
    def bytes_read_per_second_avg(self, bytes_read_per_second_avg):
        """Sets the bytes_read_per_second_avg of this StreamInfosDetails.

        The average bytes read per second within the last minute

        :param bytes_read_per_second_avg: The bytes_read_per_second_avg of this StreamInfosDetails.
        :type: float
        """

        if bytes_read_per_second_avg is not None:
            if not isinstance(bytes_read_per_second_avg, float):
                raise TypeError("Invalid type for `bytes_read_per_second_avg`, type has to be `float`")

            self._bytes_read_per_second_avg = bytes_read_per_second_avg


    @property
    def bytes_backup_per_second_min(self):
        """Gets the bytes_backup_per_second_min of this StreamInfosDetails.

        The minimum amount of backup bytes used per second within the last minute. This will be written when no live stream is ingested. The last picture will be repeated with silent audio.

        :return: The bytes_backup_per_second_min of this StreamInfosDetails.
        :rtype: float
        """
        return self._bytes_backup_per_second_min

    @bytes_backup_per_second_min.setter
    def bytes_backup_per_second_min(self, bytes_backup_per_second_min):
        """Sets the bytes_backup_per_second_min of this StreamInfosDetails.

        The minimum amount of backup bytes used per second within the last minute. This will be written when no live stream is ingested. The last picture will be repeated with silent audio.

        :param bytes_backup_per_second_min: The bytes_backup_per_second_min of this StreamInfosDetails.
        :type: float
        """

        if bytes_backup_per_second_min is not None:
            if not isinstance(bytes_backup_per_second_min, float):
                raise TypeError("Invalid type for `bytes_backup_per_second_min`, type has to be `float`")

            self._bytes_backup_per_second_min = bytes_backup_per_second_min


    @property
    def bytes_backup_per_second_max(self):
        """Gets the bytes_backup_per_second_max of this StreamInfosDetails.

        The maximum amount of backup bytes used per second within the last minute. This will be written when no live stream is ingested. The last picture will be repeated with silent audio.

        :return: The bytes_backup_per_second_max of this StreamInfosDetails.
        :rtype: float
        """
        return self._bytes_backup_per_second_max

    @bytes_backup_per_second_max.setter
    def bytes_backup_per_second_max(self, bytes_backup_per_second_max):
        """Sets the bytes_backup_per_second_max of this StreamInfosDetails.

        The maximum amount of backup bytes used per second within the last minute. This will be written when no live stream is ingested. The last picture will be repeated with silent audio.

        :param bytes_backup_per_second_max: The bytes_backup_per_second_max of this StreamInfosDetails.
        :type: float
        """

        if bytes_backup_per_second_max is not None:
            if not isinstance(bytes_backup_per_second_max, float):
                raise TypeError("Invalid type for `bytes_backup_per_second_max`, type has to be `float`")

            self._bytes_backup_per_second_max = bytes_backup_per_second_max


    @property
    def bytes_backup_per_second_avg(self):
        """Gets the bytes_backup_per_second_avg of this StreamInfosDetails.

        The average amount of backup bytes used per second within the last minute. This will be written when no live stream is ingested. The last picture will be repeated with silent audio.

        :return: The bytes_backup_per_second_avg of this StreamInfosDetails.
        :rtype: float
        """
        return self._bytes_backup_per_second_avg

    @bytes_backup_per_second_avg.setter
    def bytes_backup_per_second_avg(self, bytes_backup_per_second_avg):
        """Sets the bytes_backup_per_second_avg of this StreamInfosDetails.

        The average amount of backup bytes used per second within the last minute. This will be written when no live stream is ingested. The last picture will be repeated with silent audio.

        :param bytes_backup_per_second_avg: The bytes_backup_per_second_avg of this StreamInfosDetails.
        :type: float
        """

        if bytes_backup_per_second_avg is not None:
            if not isinstance(bytes_backup_per_second_avg, float):
                raise TypeError("Invalid type for `bytes_backup_per_second_avg`, type has to be `float`")

            self._bytes_backup_per_second_avg = bytes_backup_per_second_avg

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
            if issubclass(StreamInfosDetails, dict):
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
        if not isinstance(other, StreamInfosDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
