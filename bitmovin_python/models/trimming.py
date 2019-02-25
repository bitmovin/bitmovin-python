# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class Trimming(object):
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
            'offset': 'float',
            'duration': 'float',
            'ignore_duration_if_input_too_short': 'bool',
            'start_pic_timing': 'str',
            'end_pic_timing': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'duration': 'duration',
            'ignore_duration_if_input_too_short': 'ignoreDurationIfInputTooShort',
            'start_pic_timing': 'startPicTiming',
            'end_pic_timing': 'endPicTiming'
        }
        return attributes

    def __init__(self, offset=None, duration=None, ignore_duration_if_input_too_short=None, start_pic_timing=None, end_pic_timing=None, *args, **kwargs):

        self._offset = None
        self._duration = None
        self._ignore_duration_if_input_too_short = None
        self._start_pic_timing = None
        self._end_pic_timing = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if duration is not None:
            self.duration = duration
        if ignore_duration_if_input_too_short is not None:
            self.ignore_duration_if_input_too_short = ignore_duration_if_input_too_short
        if start_pic_timing is not None:
            self.start_pic_timing = start_pic_timing
        if end_pic_timing is not None:
            self.end_pic_timing = end_pic_timing

    @property
    def offset(self):
        """Gets the offset of this Trimming.

        Defines the offset in seconds from which the encoding should start, beginning at 0.

        :return: The offset of this Trimming.
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this Trimming.

        Defines the offset in seconds from which the encoding should start, beginning at 0.

        :param offset: The offset of this Trimming.
        :type: float
        """

        if offset is not None:
            if not isinstance(offset, float):
                raise TypeError("Invalid type for `offset`, type has to be `float`")

            self._offset = offset


    @property
    def duration(self):
        """Gets the duration of this Trimming.

        Defines how many seconds from the input will be encoded.

        :return: The duration of this Trimming.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Trimming.

        Defines how many seconds from the input will be encoded.

        :param duration: The duration of this Trimming.
        :type: float
        """

        if duration is not None:
            if not isinstance(duration, float):
                raise TypeError("Invalid type for `duration`, type has to be `float`")

            self._duration = duration


    @property
    def ignore_duration_if_input_too_short(self):
        """Gets the ignore_duration_if_input_too_short of this Trimming.

        If set, \"duration\" will be interpreted as a maximum and not cause an error if the input is too short

        :return: The ignore_duration_if_input_too_short of this Trimming.
        :rtype: bool
        """
        return self._ignore_duration_if_input_too_short

    @ignore_duration_if_input_too_short.setter
    def ignore_duration_if_input_too_short(self, ignore_duration_if_input_too_short):
        """Sets the ignore_duration_if_input_too_short of this Trimming.

        If set, \"duration\" will be interpreted as a maximum and not cause an error if the input is too short

        :param ignore_duration_if_input_too_short: The ignore_duration_if_input_too_short of this Trimming.
        :type: bool
        """

        if ignore_duration_if_input_too_short is not None:
            if not isinstance(ignore_duration_if_input_too_short, bool):
                raise TypeError("Invalid type for `ignore_duration_if_input_too_short`, type has to be `bool`")

            self._ignore_duration_if_input_too_short = ignore_duration_if_input_too_short


    @property
    def start_pic_timing(self):
        """Gets the start_pic_timing of this Trimming.

        Defines the H264 picture timing of the first frame from which the encoding should start. Any defined offset or duration in seconds will be ignored.

        :return: The start_pic_timing of this Trimming.
        :rtype: str
        """
        return self._start_pic_timing

    @start_pic_timing.setter
    def start_pic_timing(self, start_pic_timing):
        """Sets the start_pic_timing of this Trimming.

        Defines the H264 picture timing of the first frame from which the encoding should start. Any defined offset or duration in seconds will be ignored.

        :param start_pic_timing: The start_pic_timing of this Trimming.
        :type: str
        """

        if start_pic_timing is not None:
            if not isinstance(start_pic_timing, str):
                raise TypeError("Invalid type for `start_pic_timing`, type has to be `str`")

            self._start_pic_timing = start_pic_timing


    @property
    def end_pic_timing(self):
        """Gets the end_pic_timing of this Trimming.

        Defines the H264 picture timing of the last frame, that will be included in the encoding. Any defined offset or duration in seconds will be ignored.

        :return: The end_pic_timing of this Trimming.
        :rtype: str
        """
        return self._end_pic_timing

    @end_pic_timing.setter
    def end_pic_timing(self, end_pic_timing):
        """Sets the end_pic_timing of this Trimming.

        Defines the H264 picture timing of the last frame, that will be included in the encoding. Any defined offset or duration in seconds will be ignored.

        :param end_pic_timing: The end_pic_timing of this Trimming.
        :type: str
        """

        if end_pic_timing is not None:
            if not isinstance(end_pic_timing, str):
                raise TypeError("Invalid type for `end_pic_timing`, type has to be `str`")

            self._end_pic_timing = end_pic_timing

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
            if issubclass(Trimming, dict):
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
        if not isinstance(other, Trimming):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
