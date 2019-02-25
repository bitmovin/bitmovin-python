# coding: utf-8

from bitmovin_python.models.basic_media_info import BasicMediaInfo
import pprint
import six
from datetime import datetime
from enum import Enum


class SegmentsMediaInfo(BasicMediaInfo):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(SegmentsMediaInfo, self).openapi_types
        types.update({
            'segment_path': 'str',
            'encoding_id': 'str',
            'stream_id': 'str',
            'muxing_id': 'str',
            'drm_id': 'str',
            'start_segment_number': 'int',
            'end_segment_number': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(SegmentsMediaInfo, self).attribute_map
        attributes.update({
            'segment_path': 'segmentPath',
            'encoding_id': 'encodingId',
            'stream_id': 'streamId',
            'muxing_id': 'muxingId',
            'drm_id': 'drmId',
            'start_segment_number': 'startSegmentNumber',
            'end_segment_number': 'endSegmentNumber'
        })
        return attributes

    def __init__(self, segment_path=None, encoding_id=None, stream_id=None, muxing_id=None, drm_id=None, start_segment_number=None, end_segment_number=None, *args, **kwargs):
        super(SegmentsMediaInfo, self).__init__(*args, **kwargs)

        self._segment_path = None
        self._encoding_id = None
        self._stream_id = None
        self._muxing_id = None
        self._drm_id = None
        self._start_segment_number = None
        self._end_segment_number = None
        self.discriminator = None

        self.segment_path = segment_path
        self.encoding_id = encoding_id
        self.stream_id = stream_id
        self.muxing_id = muxing_id
        if drm_id is not None:
            self.drm_id = drm_id
        if start_segment_number is not None:
            self.start_segment_number = start_segment_number
        if end_segment_number is not None:
            self.end_segment_number = end_segment_number

    @property
    def segment_path(self):
        """Gets the segment_path of this SegmentsMediaInfo.

        Path to segments.

        :return: The segment_path of this SegmentsMediaInfo.
        :rtype: str
        """
        return self._segment_path

    @segment_path.setter
    def segment_path(self, segment_path):
        """Sets the segment_path of this SegmentsMediaInfo.

        Path to segments.

        :param segment_path: The segment_path of this SegmentsMediaInfo.
        :type: str
        """

        if segment_path is not None:
            if not isinstance(segment_path, str):
                raise TypeError("Invalid type for `segment_path`, type has to be `str`")

            self._segment_path = segment_path


    @property
    def encoding_id(self):
        """Gets the encoding_id of this SegmentsMediaInfo.

        Id of the encoding.

        :return: The encoding_id of this SegmentsMediaInfo.
        :rtype: str
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        """Sets the encoding_id of this SegmentsMediaInfo.

        Id of the encoding.

        :param encoding_id: The encoding_id of this SegmentsMediaInfo.
        :type: str
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, str):
                raise TypeError("Invalid type for `encoding_id`, type has to be `str`")

            self._encoding_id = encoding_id


    @property
    def stream_id(self):
        """Gets the stream_id of this SegmentsMediaInfo.

        Id of the stream.

        :return: The stream_id of this SegmentsMediaInfo.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this SegmentsMediaInfo.

        Id of the stream.

        :param stream_id: The stream_id of this SegmentsMediaInfo.
        :type: str
        """

        if stream_id is not None:
            if not isinstance(stream_id, str):
                raise TypeError("Invalid type for `stream_id`, type has to be `str`")

            self._stream_id = stream_id


    @property
    def muxing_id(self):
        """Gets the muxing_id of this SegmentsMediaInfo.

        Id of the muxing.

        :return: The muxing_id of this SegmentsMediaInfo.
        :rtype: str
        """
        return self._muxing_id

    @muxing_id.setter
    def muxing_id(self, muxing_id):
        """Sets the muxing_id of this SegmentsMediaInfo.

        Id of the muxing.

        :param muxing_id: The muxing_id of this SegmentsMediaInfo.
        :type: str
        """

        if muxing_id is not None:
            if not isinstance(muxing_id, str):
                raise TypeError("Invalid type for `muxing_id`, type has to be `str`")

            self._muxing_id = muxing_id


    @property
    def drm_id(self):
        """Gets the drm_id of this SegmentsMediaInfo.

        Id of the DRM.

        :return: The drm_id of this SegmentsMediaInfo.
        :rtype: str
        """
        return self._drm_id

    @drm_id.setter
    def drm_id(self, drm_id):
        """Sets the drm_id of this SegmentsMediaInfo.

        Id of the DRM.

        :param drm_id: The drm_id of this SegmentsMediaInfo.
        :type: str
        """

        if drm_id is not None:
            if not isinstance(drm_id, str):
                raise TypeError("Invalid type for `drm_id`, type has to be `str`")

            self._drm_id = drm_id


    @property
    def start_segment_number(self):
        """Gets the start_segment_number of this SegmentsMediaInfo.

        Number of the first segment. Default is 0.

        :return: The start_segment_number of this SegmentsMediaInfo.
        :rtype: int
        """
        return self._start_segment_number

    @start_segment_number.setter
    def start_segment_number(self, start_segment_number):
        """Sets the start_segment_number of this SegmentsMediaInfo.

        Number of the first segment. Default is 0.

        :param start_segment_number: The start_segment_number of this SegmentsMediaInfo.
        :type: int
        """

        if start_segment_number is not None:
            if not isinstance(start_segment_number, int):
                raise TypeError("Invalid type for `start_segment_number`, type has to be `int`")

            self._start_segment_number = start_segment_number


    @property
    def end_segment_number(self):
        """Gets the end_segment_number of this SegmentsMediaInfo.

        Number of the last segment. Default is the last one that was encoded.

        :return: The end_segment_number of this SegmentsMediaInfo.
        :rtype: int
        """
        return self._end_segment_number

    @end_segment_number.setter
    def end_segment_number(self, end_segment_number):
        """Sets the end_segment_number of this SegmentsMediaInfo.

        Number of the last segment. Default is the last one that was encoded.

        :param end_segment_number: The end_segment_number of this SegmentsMediaInfo.
        :type: int
        """

        if end_segment_number is not None:
            if not isinstance(end_segment_number, int):
                raise TypeError("Invalid type for `end_segment_number`, type has to be `int`")

            self._end_segment_number = end_segment_number

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(SegmentsMediaInfo, self).to_dict()

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
            if issubclass(SegmentsMediaInfo, dict):
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
        if not isinstance(other, SegmentsMediaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
