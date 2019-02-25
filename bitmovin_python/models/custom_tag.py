# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.position_mode import PositionMode
import pprint
import six
from datetime import datetime
from enum import Enum


class CustomTag(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(CustomTag, self).openapi_types
        types.update({
            'position_mode': 'PositionMode',
            'keyframe_id': 'str',
            'time': 'float',
            'segment': 'float',
            'data': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(CustomTag, self).attribute_map
        attributes.update({
            'position_mode': 'positionMode',
            'keyframe_id': 'keyframeId',
            'time': 'time',
            'segment': 'segment',
            'data': 'data'
        })
        return attributes

    def __init__(self, position_mode=None, keyframe_id=None, time=None, segment=None, data=None, *args, **kwargs):
        super(CustomTag, self).__init__(*args, **kwargs)

        self._position_mode = None
        self._keyframe_id = None
        self._time = None
        self._segment = None
        self._data = None
        self.discriminator = None

        self.position_mode = position_mode
        if keyframe_id is not None:
            self.keyframe_id = keyframe_id
        if time is not None:
            self.time = time
        if segment is not None:
            self.segment = segment
        self.data = data

    @property
    def position_mode(self):
        """Gets the position_mode of this CustomTag.

        The positioning mode that should be used when inserting the placement opportunity

        :return: The position_mode of this CustomTag.
        :rtype: PositionMode
        """
        return self._position_mode

    @position_mode.setter
    def position_mode(self, position_mode):
        """Sets the position_mode of this CustomTag.

        The positioning mode that should be used when inserting the placement opportunity

        :param position_mode: The position_mode of this CustomTag.
        :type: PositionMode
        """

        if position_mode is not None:
            if not isinstance(position_mode, PositionMode):
                raise TypeError("Invalid type for `position_mode`, type has to be `PositionMode`")

            self._position_mode = position_mode


    @property
    def keyframe_id(self):
        """Gets the keyframe_id of this CustomTag.

        Id of keyframe where the custom tag should be inserted. Required, when KEYFRAME is selected as position mode.

        :return: The keyframe_id of this CustomTag.
        :rtype: str
        """
        return self._keyframe_id

    @keyframe_id.setter
    def keyframe_id(self, keyframe_id):
        """Sets the keyframe_id of this CustomTag.

        Id of keyframe where the custom tag should be inserted. Required, when KEYFRAME is selected as position mode.

        :param keyframe_id: The keyframe_id of this CustomTag.
        :type: str
        """

        if keyframe_id is not None:
            if not isinstance(keyframe_id, str):
                raise TypeError("Invalid type for `keyframe_id`, type has to be `str`")

            self._keyframe_id = keyframe_id


    @property
    def time(self):
        """Gets the time of this CustomTag.

        Time in seconds where the custom tag should be inserted. Required, when TIME is selected as position mode.

        :return: The time of this CustomTag.
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this CustomTag.

        Time in seconds where the custom tag should be inserted. Required, when TIME is selected as position mode.

        :param time: The time of this CustomTag.
        :type: float
        """

        if time is not None:
            if not isinstance(time, float):
                raise TypeError("Invalid type for `time`, type has to be `float`")

            self._time = time


    @property
    def segment(self):
        """Gets the segment of this CustomTag.

        The custom tag will be inserted before the specified segment. Required, when SEGMENT is selected as position mode.

        :return: The segment of this CustomTag.
        :rtype: float
        """
        return self._segment

    @segment.setter
    def segment(self, segment):
        """Sets the segment of this CustomTag.

        The custom tag will be inserted before the specified segment. Required, when SEGMENT is selected as position mode.

        :param segment: The segment of this CustomTag.
        :type: float
        """

        if segment is not None:
            if not isinstance(segment, float):
                raise TypeError("Invalid type for `segment`, type has to be `float`")

            self._segment = segment


    @property
    def data(self):
        """Gets the data of this CustomTag.

        The data to be contained in the custom tag.

        :return: The data of this CustomTag.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CustomTag.

        The data to be contained in the custom tag.

        :param data: The data of this CustomTag.
        :type: str
        """

        if data is not None:
            if not isinstance(data, str):
                raise TypeError("Invalid type for `data`, type has to be `str`")

            self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(CustomTag, self).to_dict()

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
            if issubclass(CustomTag, dict):
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
        if not isinstance(other, CustomTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
