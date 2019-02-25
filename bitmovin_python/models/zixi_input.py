# coding: utf-8

from bitmovin_python.models.input import Input
from bitmovin_python.models.input_type import InputType
import pprint
import six
from datetime import datetime
from enum import Enum


class ZixiInput(Input):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(ZixiInput, self).openapi_types
        types.update({
            'host': 'str',
            'port': 'int',
            'stream': 'str',
            'password': 'str',
            'latency': 'int',
            'min_bitrate': 'int',
            'decryption_type': 'str',
            'decryption_key': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(ZixiInput, self).attribute_map
        attributes.update({
            'host': 'host',
            'port': 'port',
            'stream': 'stream',
            'password': 'password',
            'latency': 'latency',
            'min_bitrate': 'minBitrate',
            'decryption_type': 'decryptionType',
            'decryption_key': 'decryptionKey'
        })
        return attributes

    def __init__(self, host=None, port=None, stream=None, password=None, latency=None, min_bitrate=None, decryption_type=None, decryption_key=None, *args, **kwargs):
        super(ZixiInput, self).__init__(*args, **kwargs)

        self._host = None
        self._port = None
        self._stream = None
        self._password = None
        self._latency = None
        self._min_bitrate = None
        self._decryption_type = None
        self._decryption_key = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if stream is not None:
            self.stream = stream
        if password is not None:
            self.password = password
        if latency is not None:
            self.latency = latency
        if min_bitrate is not None:
            self.min_bitrate = min_bitrate
        if decryption_type is not None:
            self.decryption_type = decryption_type
        if decryption_key is not None:
            self.decryption_key = decryption_key

    @property
    def host(self):
        """Gets the host of this ZixiInput.


        :return: The host of this ZixiInput.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ZixiInput.


        :param host: The host of this ZixiInput.
        :type: str
        """

        if host is not None:
            if not isinstance(host, str):
                raise TypeError("Invalid type for `host`, type has to be `str`")

            self._host = host


    @property
    def port(self):
        """Gets the port of this ZixiInput.


        :return: The port of this ZixiInput.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ZixiInput.


        :param port: The port of this ZixiInput.
        :type: int
        """

        if port is not None:
            if not isinstance(port, int):
                raise TypeError("Invalid type for `port`, type has to be `int`")

            self._port = port


    @property
    def stream(self):
        """Gets the stream of this ZixiInput.


        :return: The stream of this ZixiInput.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this ZixiInput.


        :param stream: The stream of this ZixiInput.
        :type: str
        """

        if stream is not None:
            if not isinstance(stream, str):
                raise TypeError("Invalid type for `stream`, type has to be `str`")

            self._stream = stream


    @property
    def password(self):
        """Gets the password of this ZixiInput.


        :return: The password of this ZixiInput.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ZixiInput.


        :param password: The password of this ZixiInput.
        :type: str
        """

        if password is not None:
            if not isinstance(password, str):
                raise TypeError("Invalid type for `password`, type has to be `str`")

            self._password = password


    @property
    def latency(self):
        """Gets the latency of this ZixiInput.


        :return: The latency of this ZixiInput.
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this ZixiInput.


        :param latency: The latency of this ZixiInput.
        :type: int
        """

        if latency is not None:
            if not isinstance(latency, int):
                raise TypeError("Invalid type for `latency`, type has to be `int`")

            self._latency = latency


    @property
    def min_bitrate(self):
        """Gets the min_bitrate of this ZixiInput.


        :return: The min_bitrate of this ZixiInput.
        :rtype: int
        """
        return self._min_bitrate

    @min_bitrate.setter
    def min_bitrate(self, min_bitrate):
        """Sets the min_bitrate of this ZixiInput.


        :param min_bitrate: The min_bitrate of this ZixiInput.
        :type: int
        """

        if min_bitrate is not None:
            if not isinstance(min_bitrate, int):
                raise TypeError("Invalid type for `min_bitrate`, type has to be `int`")

            self._min_bitrate = min_bitrate


    @property
    def decryption_type(self):
        """Gets the decryption_type of this ZixiInput.


        :return: The decryption_type of this ZixiInput.
        :rtype: str
        """
        return self._decryption_type

    @decryption_type.setter
    def decryption_type(self, decryption_type):
        """Sets the decryption_type of this ZixiInput.


        :param decryption_type: The decryption_type of this ZixiInput.
        :type: str
        """

        if decryption_type is not None:
            if not isinstance(decryption_type, str):
                raise TypeError("Invalid type for `decryption_type`, type has to be `str`")

            self._decryption_type = decryption_type


    @property
    def decryption_key(self):
        """Gets the decryption_key of this ZixiInput.


        :return: The decryption_key of this ZixiInput.
        :rtype: str
        """
        return self._decryption_key

    @decryption_key.setter
    def decryption_key(self, decryption_key):
        """Sets the decryption_key of this ZixiInput.


        :param decryption_key: The decryption_key of this ZixiInput.
        :type: str
        """

        if decryption_key is not None:
            if not isinstance(decryption_key, str):
                raise TypeError("Invalid type for `decryption_key`, type has to be `str`")

            self._decryption_key = decryption_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(ZixiInput, self).to_dict()

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
            if issubclass(ZixiInput, dict):
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
        if not isinstance(other, ZixiInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
