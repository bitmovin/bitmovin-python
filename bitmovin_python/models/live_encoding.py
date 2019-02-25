# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class LiveEncoding(object):
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
            'stream_key': 'str',
            'encoder_ip': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'stream_key': 'streamKey',
            'encoder_ip': 'encoderIp'
        }
        return attributes

    def __init__(self, stream_key=None, encoder_ip=None, *args, **kwargs):

        self._stream_key = None
        self._encoder_ip = None
        self.discriminator = None

        self.stream_key = stream_key
        self.encoder_ip = encoder_ip

    @property
    def stream_key(self):
        """Gets the stream_key of this LiveEncoding.

        Stream key of the live encoder

        :return: The stream_key of this LiveEncoding.
        :rtype: str
        """
        return self._stream_key

    @stream_key.setter
    def stream_key(self, stream_key):
        """Sets the stream_key of this LiveEncoding.

        Stream key of the live encoder

        :param stream_key: The stream_key of this LiveEncoding.
        :type: str
        """

        if stream_key is not None:
            if not isinstance(stream_key, str):
                raise TypeError("Invalid type for `stream_key`, type has to be `str`")

            self._stream_key = stream_key


    @property
    def encoder_ip(self):
        """Gets the encoder_ip of this LiveEncoding.

        IP address of the live encoder

        :return: The encoder_ip of this LiveEncoding.
        :rtype: str
        """
        return self._encoder_ip

    @encoder_ip.setter
    def encoder_ip(self, encoder_ip):
        """Sets the encoder_ip of this LiveEncoding.

        IP address of the live encoder

        :param encoder_ip: The encoder_ip of this LiveEncoding.
        :type: str
        """

        if encoder_ip is not None:
            if not isinstance(encoder_ip, str):
                raise TypeError("Invalid type for `encoder_ip`, type has to be `str`")

            self._encoder_ip = encoder_ip

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
            if issubclass(LiveEncoding, dict):
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
        if not isinstance(other, LiveEncoding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
