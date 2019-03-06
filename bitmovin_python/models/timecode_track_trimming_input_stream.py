# coding: utf-8

from bitmovin_python.models.basic_input_stream import BasicInputStream
from bitmovin_python.models.input_stream_type import InputStreamType
import pprint
import six
from datetime import datetime
from enum import Enum


class TimecodeTrackTrimmingInputStream(BasicInputStream):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(TimecodeTrackTrimmingInputStream, self).openapi_types
        types.update({
            'input_stream_id': 'str',
            'start_time_code': 'str',
            'end_time_code': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(TimecodeTrackTrimmingInputStream, self).attribute_map
        attributes.update({
            'input_stream_id': 'inputStreamId',
            'start_time_code': 'startTimeCode',
            'end_time_code': 'endTimeCode'
        })
        return attributes

    def __init__(self, input_stream_id=None, start_time_code=None, end_time_code=None, *args, **kwargs):
        super(TimecodeTrackTrimmingInputStream, self).__init__(*args, **kwargs)

        self._input_stream_id = None
        self._start_time_code = None
        self._end_time_code = None
        self.discriminator = None

        if input_stream_id is not None:
            self.input_stream_id = input_stream_id
        if start_time_code is not None:
            self.start_time_code = start_time_code
        if end_time_code is not None:
            self.end_time_code = end_time_code

    @property
    def input_stream_id(self):
        """Gets the input_stream_id of this TimecodeTrackTrimmingInputStream.

        The id of the ingest input stream that should be trimmed

        :return: The input_stream_id of this TimecodeTrackTrimmingInputStream.
        :rtype: str
        """
        return self._input_stream_id

    @input_stream_id.setter
    def input_stream_id(self, input_stream_id):
        """Sets the input_stream_id of this TimecodeTrackTrimmingInputStream.

        The id of the ingest input stream that should be trimmed

        :param input_stream_id: The input_stream_id of this TimecodeTrackTrimmingInputStream.
        :type: str
        """

        if input_stream_id is not None:
            if not isinstance(input_stream_id, str):
                raise TypeError("Invalid type for `input_stream_id`, type has to be `str`")

            self._input_stream_id = input_stream_id


    @property
    def start_time_code(self):
        """Gets the start_time_code of this TimecodeTrackTrimmingInputStream.

        Defines the timecode, in SMPTE-12M format, of the frame from which the encoding should start. The frame indicated by this value will be included in the encoding

        :return: The start_time_code of this TimecodeTrackTrimmingInputStream.
        :rtype: str
        """
        return self._start_time_code

    @start_time_code.setter
    def start_time_code(self, start_time_code):
        """Sets the start_time_code of this TimecodeTrackTrimmingInputStream.

        Defines the timecode, in SMPTE-12M format, of the frame from which the encoding should start. The frame indicated by this value will be included in the encoding

        :param start_time_code: The start_time_code of this TimecodeTrackTrimmingInputStream.
        :type: str
        """

        if start_time_code is not None:
            if not isinstance(start_time_code, str):
                raise TypeError("Invalid type for `start_time_code`, type has to be `str`")

            self._start_time_code = start_time_code


    @property
    def end_time_code(self):
        """Gets the end_time_code of this TimecodeTrackTrimmingInputStream.

        Defines the timecode, in SMPTE-12M format, of the frame at which the encoding should stop. The frame indicated by this value will be included in the encoding

        :return: The end_time_code of this TimecodeTrackTrimmingInputStream.
        :rtype: str
        """
        return self._end_time_code

    @end_time_code.setter
    def end_time_code(self, end_time_code):
        """Sets the end_time_code of this TimecodeTrackTrimmingInputStream.

        Defines the timecode, in SMPTE-12M format, of the frame at which the encoding should stop. The frame indicated by this value will be included in the encoding

        :param end_time_code: The end_time_code of this TimecodeTrackTrimmingInputStream.
        :type: str
        """

        if end_time_code is not None:
            if not isinstance(end_time_code, str):
                raise TypeError("Invalid type for `end_time_code`, type has to be `str`")

            self._end_time_code = end_time_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(TimecodeTrackTrimmingInputStream, self).to_dict()

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
            if issubclass(TimecodeTrackTrimmingInputStream, dict):
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
        if not isinstance(other, TimecodeTrackTrimmingInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
