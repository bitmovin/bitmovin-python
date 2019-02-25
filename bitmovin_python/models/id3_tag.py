# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.id3_tag_position_mode import Id3TagPositionMode
from bitmovin_python.models.id3_tag_type import Id3TagType
import pprint
import six
from datetime import datetime
from enum import Enum


class Id3Tag(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Id3Tag, self).openapi_types
        types.update({
            'type': 'Id3TagType',
            'position_mode': 'Id3TagPositionMode',
            'frame': 'float',
            'time': 'float'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Id3Tag, self).attribute_map
        attributes.update({
            'type': 'type',
            'position_mode': 'positionMode',
            'frame': 'frame',
            'time': 'time'
        })
        return attributes

    discriminator_value_class_map = {
        'RAW': 'RawId3Tag',
        'FRAME_ID': 'FrameIdId3Tag',
        'PLAIN_TEXT': 'PlaintextId3Tag'
    }

    def __init__(self, type=None, position_mode=None, frame=None, time=None, *args, **kwargs):
        super(Id3Tag, self).__init__(*args, **kwargs)

        self._type = None
        self._position_mode = None
        self._frame = None
        self._time = None
        self.discriminator = 'type'

        self.type = type
        if position_mode is not None:
            self.position_mode = position_mode
        if frame is not None:
            self.frame = frame
        if time is not None:
            self.time = time

    @property
    def type(self):
        """Gets the type of this Id3Tag.

        Type of the tag

        :return: The type of this Id3Tag.
        :rtype: Id3TagType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Id3Tag.

        Type of the tag

        :param type: The type of this Id3Tag.
        :type: Id3TagType
        """

        if type is not None:
            if not isinstance(type, Id3TagType):
                raise TypeError("Invalid type for `type`, type has to be `Id3TagType`")

            self._type = type


    @property
    def position_mode(self):
        """Gets the position_mode of this Id3Tag.


        :return: The position_mode of this Id3Tag.
        :rtype: Id3TagPositionMode
        """
        return self._position_mode

    @position_mode.setter
    def position_mode(self, position_mode):
        """Sets the position_mode of this Id3Tag.


        :param position_mode: The position_mode of this Id3Tag.
        :type: Id3TagPositionMode
        """

        if position_mode is not None:
            if not isinstance(position_mode, Id3TagPositionMode):
                raise TypeError("Invalid type for `position_mode`, type has to be `Id3TagPositionMode`")

            self._position_mode = position_mode


    @property
    def frame(self):
        """Gets the frame of this Id3Tag.

        Number of frame where the Tag should be inserted

        :return: The frame of this Id3Tag.
        :rtype: float
        """
        return self._frame

    @frame.setter
    def frame(self, frame):
        """Sets the frame of this Id3Tag.

        Number of frame where the Tag should be inserted

        :param frame: The frame of this Id3Tag.
        :type: float
        """

        if frame is not None:
            if not isinstance(frame, float):
                raise TypeError("Invalid type for `frame`, type has to be `float`")

            self._frame = frame


    @property
    def time(self):
        """Gets the time of this Id3Tag.

        Time in seconds where the frame should be inserted

        :return: The time of this Id3Tag.
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Id3Tag.

        Time in seconds where the frame should be inserted

        :param time: The time of this Id3Tag.
        :type: float
        """

        if time is not None:
            if not isinstance(time, float):
                raise TypeError("Invalid type for `time`, type has to be `float`")

            self._time = time

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator]
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Id3Tag, self).to_dict()

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
            if issubclass(Id3Tag, dict):
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
        if not isinstance(other, Id3Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
