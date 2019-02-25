# coding: utf-8

from bitmovin_python.models.media_stream import MediaStream
import pprint
import six
from datetime import datetime
from enum import Enum


class VideoStream(MediaStream):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(VideoStream, self).openapi_types
        types.update({
            'fps': 'str',
            'bitrate': 'str',
            'rate': 'int',
            'width': 'int',
            'height': 'int',
            'par': 'float',
            'rotation': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(VideoStream, self).attribute_map
        attributes.update({
            'fps': 'fps',
            'bitrate': 'bitrate',
            'rate': 'rate',
            'width': 'width',
            'height': 'height',
            'par': 'par',
            'rotation': 'rotation'
        })
        return attributes

    def __init__(self, fps=None, bitrate=None, rate=None, width=None, height=None, par=None, rotation=None, *args, **kwargs):
        super(VideoStream, self).__init__(*args, **kwargs)

        self._fps = None
        self._bitrate = None
        self._rate = None
        self._width = None
        self._height = None
        self._par = None
        self._rotation = None
        self.discriminator = None

        if fps is not None:
            self.fps = fps
        if bitrate is not None:
            self.bitrate = bitrate
        if rate is not None:
            self.rate = rate
        self.width = width
        self.height = height
        if par is not None:
            self.par = par
        if rotation is not None:
            self.rotation = rotation

    @property
    def fps(self):
        """Gets the fps of this VideoStream.

        Frame rate of the video

        :return: The fps of this VideoStream.
        :rtype: str
        """
        return self._fps

    @fps.setter
    def fps(self, fps):
        """Sets the fps of this VideoStream.

        Frame rate of the video

        :param fps: The fps of this VideoStream.
        :type: str
        """

        if fps is not None:
            if not isinstance(fps, str):
                raise TypeError("Invalid type for `fps`, type has to be `str`")

            self._fps = fps


    @property
    def bitrate(self):
        """Gets the bitrate of this VideoStream.

        Bitrate in bps

        :return: The bitrate of this VideoStream.
        :rtype: str
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this VideoStream.

        Bitrate in bps

        :param bitrate: The bitrate of this VideoStream.
        :type: str
        """

        if bitrate is not None:
            if not isinstance(bitrate, str):
                raise TypeError("Invalid type for `bitrate`, type has to be `str`")

            self._bitrate = bitrate


    @property
    def rate(self):
        """Gets the rate of this VideoStream.

        Bitrate in bps

        :return: The rate of this VideoStream.
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this VideoStream.

        Bitrate in bps

        :param rate: The rate of this VideoStream.
        :type: int
        """

        if rate is not None:
            if not isinstance(rate, int):
                raise TypeError("Invalid type for `rate`, type has to be `int`")

            self._rate = rate


    @property
    def width(self):
        """Gets the width of this VideoStream.

        Width of the video

        :return: The width of this VideoStream.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this VideoStream.

        Width of the video

        :param width: The width of this VideoStream.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

            self._width = width


    @property
    def height(self):
        """Gets the height of this VideoStream.

        Height of the video

        :return: The height of this VideoStream.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this VideoStream.

        Height of the video

        :param height: The height of this VideoStream.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

            self._height = height


    @property
    def par(self):
        """Gets the par of this VideoStream.

        Pixel aspect ratio of the video. Default is 1.0

        :return: The par of this VideoStream.
        :rtype: float
        """
        return self._par

    @par.setter
    def par(self, par):
        """Sets the par of this VideoStream.

        Pixel aspect ratio of the video. Default is 1.0

        :param par: The par of this VideoStream.
        :type: float
        """

        if par is not None:
            if not isinstance(par, float):
                raise TypeError("Invalid type for `par`, type has to be `float`")

            self._par = par


    @property
    def rotation(self):
        """Gets the rotation of this VideoStream.

        Rotation of the video for mobile devices. Default is 0.

        :return: The rotation of this VideoStream.
        :rtype: int
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this VideoStream.

        Rotation of the video for mobile devices. Default is 0.

        :param rotation: The rotation of this VideoStream.
        :type: int
        """

        if rotation is not None:
            if not isinstance(rotation, int):
                raise TypeError("Invalid type for `rotation`, type has to be `int`")

            self._rotation = rotation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(VideoStream, self).to_dict()

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
            if issubclass(VideoStream, dict):
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
        if not isinstance(other, VideoStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
