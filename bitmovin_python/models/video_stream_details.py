# coding: utf-8

from bitmovin_python.models.stream_details import StreamDetails
import pprint
import six
from datetime import datetime
from enum import Enum


class VideoStreamDetails(StreamDetails):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(VideoStreamDetails, self).openapi_types
        types.update({
            'fps': 'str',
            'width': 'int',
            'height': 'int',
            'bitrate': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(VideoStreamDetails, self).attribute_map
        attributes.update({
            'fps': 'fps',
            'width': 'width',
            'height': 'height',
            'bitrate': 'bitrate'
        })
        return attributes

    def __init__(self, fps=None, width=None, height=None, bitrate=None, *args, **kwargs):
        super(VideoStreamDetails, self).__init__(*args, **kwargs)

        self._fps = None
        self._width = None
        self._height = None
        self._bitrate = None
        self.discriminator = None

        if fps is not None:
            self.fps = fps
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if bitrate is not None:
            self.bitrate = bitrate

    @property
    def fps(self):
        """Gets the fps of this VideoStreamDetails.


        :return: The fps of this VideoStreamDetails.
        :rtype: str
        """
        return self._fps

    @fps.setter
    def fps(self, fps):
        """Sets the fps of this VideoStreamDetails.


        :param fps: The fps of this VideoStreamDetails.
        :type: str
        """

        if fps is not None:
            if not isinstance(fps, str):
                raise TypeError("Invalid type for `fps`, type has to be `str`")

            self._fps = fps


    @property
    def width(self):
        """Gets the width of this VideoStreamDetails.


        :return: The width of this VideoStreamDetails.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this VideoStreamDetails.


        :param width: The width of this VideoStreamDetails.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

            self._width = width


    @property
    def height(self):
        """Gets the height of this VideoStreamDetails.


        :return: The height of this VideoStreamDetails.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this VideoStreamDetails.


        :param height: The height of this VideoStreamDetails.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

            self._height = height


    @property
    def bitrate(self):
        """Gets the bitrate of this VideoStreamDetails.


        :return: The bitrate of this VideoStreamDetails.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this VideoStreamDetails.


        :param bitrate: The bitrate of this VideoStreamDetails.
        :type: int
        """

        if bitrate is not None:
            if not isinstance(bitrate, int):
                raise TypeError("Invalid type for `bitrate`, type has to be `int`")

            self._bitrate = bitrate

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(VideoStreamDetails, self).to_dict()

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
            if issubclass(VideoStreamDetails, dict):
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
        if not isinstance(other, VideoStreamDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
