# coding: utf-8

from bitmovin_python.models.stream_infos_details import StreamInfosDetails
import pprint
import six
from datetime import datetime
from enum import Enum


class StreamInfos(object):
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
            'time': 'datetime',
            'stream_infos': 'list[StreamInfosDetails]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'time': 'time',
            'stream_infos': 'streamInfos'
        }
        return attributes

    def __init__(self, time=None, stream_infos=None, *args, **kwargs):

        self._time = None
        self._stream_infos = None
        self.discriminator = None

        self.time = time
        if stream_infos is not None:
            self.stream_infos = stream_infos

    @property
    def time(self):
        """Gets the time of this StreamInfos.

        Timestamp of the event expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :return: The time of this StreamInfos.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this StreamInfos.

        Timestamp of the event expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :param time: The time of this StreamInfos.
        :type: datetime
        """

        if time is not None:
            if not isinstance(time, datetime):
                raise TypeError("Invalid type for `time`, type has to be `datetime`")

            self._time = time


    @property
    def stream_infos(self):
        """Gets the stream_infos of this StreamInfos.

        Details about billable minutes for each resolution category

        :return: The stream_infos of this StreamInfos.
        :rtype: list[StreamInfosDetails]
        """
        return self._stream_infos

    @stream_infos.setter
    def stream_infos(self, stream_infos):
        """Sets the stream_infos of this StreamInfos.

        Details about billable minutes for each resolution category

        :param stream_infos: The stream_infos of this StreamInfos.
        :type: list[StreamInfosDetails]
        """

        if stream_infos is not None:
            if not isinstance(stream_infos, list):
                raise TypeError("Invalid type for `stream_infos`, type has to be `list[StreamInfosDetails]`")

            self._stream_infos = stream_infos

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
            if issubclass(StreamInfos, dict):
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
        if not isinstance(other, StreamInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
