# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from enum import Enum


class Keyframe(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Keyframe, self).openapi_types
        types.update({
            'time': 'float',
            'segment_cut': 'bool'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Keyframe, self).attribute_map
        attributes.update({
            'time': 'time',
            'segment_cut': 'segmentCut'
        })
        return attributes

    def __init__(self, time=None, segment_cut=True, *args, **kwargs):
        super(Keyframe, self).__init__(*args, **kwargs)

        self._time = None
        self._segment_cut = None
        self.discriminator = None

        self.time = time
        if segment_cut is not None:
            self.segment_cut = segment_cut

    @property
    def time(self):
        """Gets the time of this Keyframe.

        Time in seconds where the keyframe should be inserted

        :return: The time of this Keyframe.
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Keyframe.

        Time in seconds where the keyframe should be inserted

        :param time: The time of this Keyframe.
        :type: float
        """

        if time is not None:
            if not isinstance(time, float):
                raise TypeError("Invalid type for `time`, type has to be `float`")

            self._time = time


    @property
    def segment_cut(self):
        """Gets the segment_cut of this Keyframe.

        Instructs the encoder to cut the segment at this position

        :return: The segment_cut of this Keyframe.
        :rtype: bool
        """
        return self._segment_cut

    @segment_cut.setter
    def segment_cut(self, segment_cut):
        """Sets the segment_cut of this Keyframe.

        Instructs the encoder to cut the segment at this position

        :param segment_cut: The segment_cut of this Keyframe.
        :type: bool
        """

        if segment_cut is not None:
            if not isinstance(segment_cut, bool):
                raise TypeError("Invalid type for `segment_cut`, type has to be `bool`")

            self._segment_cut = segment_cut

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Keyframe, self).to_dict()

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
            if issubclass(Keyframe, dict):
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
        if not isinstance(other, Keyframe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
