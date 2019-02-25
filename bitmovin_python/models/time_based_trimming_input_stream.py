# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from enum import Enum


class TimeBasedTrimmingInputStream(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(TimeBasedTrimmingInputStream, self).openapi_types
        types.update({
            'input_stream_id': 'str',
            'offset': 'float',
            'duration': 'float'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(TimeBasedTrimmingInputStream, self).attribute_map
        attributes.update({
            'input_stream_id': 'inputStreamId',
            'offset': 'offset',
            'duration': 'duration'
        })
        return attributes

    def __init__(self, input_stream_id=None, offset=None, duration=None, *args, **kwargs):
        super(TimeBasedTrimmingInputStream, self).__init__(*args, **kwargs)

        self._input_stream_id = None
        self._offset = None
        self._duration = None
        self.discriminator = None

        if input_stream_id is not None:
            self.input_stream_id = input_stream_id
        if offset is not None:
            self.offset = offset
        if duration is not None:
            self.duration = duration

    @property
    def input_stream_id(self):
        """Gets the input_stream_id of this TimeBasedTrimmingInputStream.

        The id of the ingest input stream that should be trimmed

        :return: The input_stream_id of this TimeBasedTrimmingInputStream.
        :rtype: str
        """
        return self._input_stream_id

    @input_stream_id.setter
    def input_stream_id(self, input_stream_id):
        """Sets the input_stream_id of this TimeBasedTrimmingInputStream.

        The id of the ingest input stream that should be trimmed

        :param input_stream_id: The input_stream_id of this TimeBasedTrimmingInputStream.
        :type: str
        """

        if input_stream_id is not None:
            if not isinstance(input_stream_id, str):
                raise TypeError("Invalid type for `input_stream_id`, type has to be `str`")

            self._input_stream_id = input_stream_id


    @property
    def offset(self):
        """Gets the offset of this TimeBasedTrimmingInputStream.

        Defines the offset in seconds at which the encoding should start, beginning at 0. The frame indicated by this value will be included in the encoding

        :return: The offset of this TimeBasedTrimmingInputStream.
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TimeBasedTrimmingInputStream.

        Defines the offset in seconds at which the encoding should start, beginning at 0. The frame indicated by this value will be included in the encoding

        :param offset: The offset of this TimeBasedTrimmingInputStream.
        :type: float
        """

        if offset is not None:
            if offset is not None and offset < 0:
                raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")
            if not isinstance(offset, float):
                raise TypeError("Invalid type for `offset`, type has to be `float`")

            self._offset = offset


    @property
    def duration(self):
        """Gets the duration of this TimeBasedTrimmingInputStream.

        Defines how many seconds of the input will be encoded

        :return: The duration of this TimeBasedTrimmingInputStream.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TimeBasedTrimmingInputStream.

        Defines how many seconds of the input will be encoded

        :param duration: The duration of this TimeBasedTrimmingInputStream.
        :type: float
        """

        if duration is not None:
            if duration is not None and duration < 0:
                raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `0`")
            if not isinstance(duration, float):
                raise TypeError("Invalid type for `duration`, type has to be `float`")

            self._duration = duration

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(TimeBasedTrimmingInputStream, self).to_dict()

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
            if issubclass(TimeBasedTrimmingInputStream, dict):
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
        if not isinstance(other, TimeBasedTrimmingInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
