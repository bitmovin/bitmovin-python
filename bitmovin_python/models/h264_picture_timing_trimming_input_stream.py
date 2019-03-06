# coding: utf-8

from bitmovin_python.models.basic_input_stream import BasicInputStream
from bitmovin_python.models.input_stream_type import InputStreamType
import pprint
import six
from datetime import datetime
from enum import Enum


class H264PictureTimingTrimmingInputStream(BasicInputStream):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(H264PictureTimingTrimmingInputStream, self).openapi_types
        types.update({
            'input_stream_id': 'str',
            'start_pic_timing': 'str',
            'end_pic_timing': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(H264PictureTimingTrimmingInputStream, self).attribute_map
        attributes.update({
            'input_stream_id': 'inputStreamId',
            'start_pic_timing': 'startPicTiming',
            'end_pic_timing': 'endPicTiming'
        })
        return attributes

    def __init__(self, input_stream_id=None, start_pic_timing=None, end_pic_timing=None, *args, **kwargs):
        super(H264PictureTimingTrimmingInputStream, self).__init__(*args, **kwargs)

        self._input_stream_id = None
        self._start_pic_timing = None
        self._end_pic_timing = None
        self.discriminator = None

        if input_stream_id is not None:
            self.input_stream_id = input_stream_id
        if start_pic_timing is not None:
            self.start_pic_timing = start_pic_timing
        if end_pic_timing is not None:
            self.end_pic_timing = end_pic_timing

    @property
    def input_stream_id(self):
        """Gets the input_stream_id of this H264PictureTimingTrimmingInputStream.

        The id of the ingest input stream that should be trimmed

        :return: The input_stream_id of this H264PictureTimingTrimmingInputStream.
        :rtype: str
        """
        return self._input_stream_id

    @input_stream_id.setter
    def input_stream_id(self, input_stream_id):
        """Sets the input_stream_id of this H264PictureTimingTrimmingInputStream.

        The id of the ingest input stream that should be trimmed

        :param input_stream_id: The input_stream_id of this H264PictureTimingTrimmingInputStream.
        :type: str
        """

        if input_stream_id is not None:
            if not isinstance(input_stream_id, str):
                raise TypeError("Invalid type for `input_stream_id`, type has to be `str`")

            self._input_stream_id = input_stream_id


    @property
    def start_pic_timing(self):
        """Gets the start_pic_timing of this H264PictureTimingTrimmingInputStream.

        Defines the H264 SEI picture timing, as specified in ISO/IEC 14496-10:2008, of the frame from which the encoding should start. The frame indicated by this value will be included in the encoding

        :return: The start_pic_timing of this H264PictureTimingTrimmingInputStream.
        :rtype: str
        """
        return self._start_pic_timing

    @start_pic_timing.setter
    def start_pic_timing(self, start_pic_timing):
        """Sets the start_pic_timing of this H264PictureTimingTrimmingInputStream.

        Defines the H264 SEI picture timing, as specified in ISO/IEC 14496-10:2008, of the frame from which the encoding should start. The frame indicated by this value will be included in the encoding

        :param start_pic_timing: The start_pic_timing of this H264PictureTimingTrimmingInputStream.
        :type: str
        """

        if start_pic_timing is not None:
            if not isinstance(start_pic_timing, str):
                raise TypeError("Invalid type for `start_pic_timing`, type has to be `str`")

            self._start_pic_timing = start_pic_timing


    @property
    def end_pic_timing(self):
        """Gets the end_pic_timing of this H264PictureTimingTrimmingInputStream.

        Defines the H264 SEI picture timing, as specified in ISO/IEC 14496-10:2008, of the frame at which the encoding should stop. The frame indicated by this value will be included in the encoding

        :return: The end_pic_timing of this H264PictureTimingTrimmingInputStream.
        :rtype: str
        """
        return self._end_pic_timing

    @end_pic_timing.setter
    def end_pic_timing(self, end_pic_timing):
        """Sets the end_pic_timing of this H264PictureTimingTrimmingInputStream.

        Defines the H264 SEI picture timing, as specified in ISO/IEC 14496-10:2008, of the frame at which the encoding should stop. The frame indicated by this value will be included in the encoding

        :param end_pic_timing: The end_pic_timing of this H264PictureTimingTrimmingInputStream.
        :type: str
        """

        if end_pic_timing is not None:
            if not isinstance(end_pic_timing, str):
                raise TypeError("Invalid type for `end_pic_timing`, type has to be `str`")

            self._end_pic_timing = end_pic_timing

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(H264PictureTimingTrimmingInputStream, self).to_dict()

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
            if issubclass(H264PictureTimingTrimmingInputStream, dict):
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
        if not isinstance(other, H264PictureTimingTrimmingInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
