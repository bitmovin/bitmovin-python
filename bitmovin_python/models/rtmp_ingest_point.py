# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class RtmpIngestPoint(object):
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
            'application_name': 'str',
            'stream_key': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'application_name': 'applicationName',
            'stream_key': 'streamKey'
        }
        return attributes

    def __init__(self, application_name=None, stream_key=None, *args, **kwargs):

        self._application_name = None
        self._stream_key = None
        self.discriminator = None

        self.application_name = application_name
        self.stream_key = stream_key

    @property
    def application_name(self):
        """Gets the application_name of this RtmpIngestPoint.

        The name of the application where the ingest is streamed to. This has to be unique for each ingest point

        :return: The application_name of this RtmpIngestPoint.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this RtmpIngestPoint.

        The name of the application where the ingest is streamed to. This has to be unique for each ingest point

        :param application_name: The application_name of this RtmpIngestPoint.
        :type: str
        """

        if application_name is not None:
            if not isinstance(application_name, str):
                raise TypeError("Invalid type for `application_name`, type has to be `str`")

            self._application_name = application_name


    @property
    def stream_key(self):
        """Gets the stream_key of this RtmpIngestPoint.

        The stream key for the backup input

        :return: The stream_key of this RtmpIngestPoint.
        :rtype: str
        """
        return self._stream_key

    @stream_key.setter
    def stream_key(self, stream_key):
        """Sets the stream_key of this RtmpIngestPoint.

        The stream key for the backup input

        :param stream_key: The stream_key of this RtmpIngestPoint.
        :type: str
        """

        if stream_key is not None:
            if not isinstance(stream_key, str):
                raise TypeError("Invalid type for `stream_key`, type has to be `str`")

            self._stream_key = stream_key

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
            if issubclass(RtmpIngestPoint, dict):
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
        if not isinstance(other, RtmpIngestPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
