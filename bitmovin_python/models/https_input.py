# coding: utf-8

from bitmovin_python.models.input import Input
from bitmovin_python.models.input_type import InputType
import pprint
import six
from datetime import datetime
from enum import Enum


class HttpsInput(Input):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(HttpsInput, self).openapi_types
        types.update({
            'host': 'str',
            'username': 'str',
            'password': 'str',
            'port': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(HttpsInput, self).attribute_map
        attributes.update({
            'host': 'host',
            'username': 'username',
            'password': 'password',
            'port': 'port'
        })
        return attributes

    def __init__(self, host=None, username=None, password=None, port=None, *args, **kwargs):
        super(HttpsInput, self).__init__(*args, **kwargs)

        self._host = None
        self._username = None
        self._password = None
        self._port = None
        self.discriminator = None

        self.host = host
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if port is not None:
            self.port = port

    @property
    def host(self):
        """Gets the host of this HttpsInput.

        Host Url or IP of the HTTP server

        :return: The host of this HttpsInput.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this HttpsInput.

        Host Url or IP of the HTTP server

        :param host: The host of this HttpsInput.
        :type: str
        """

        if host is not None:
            if not isinstance(host, str):
                raise TypeError("Invalid type for `host`, type has to be `str`")

            self._host = host


    @property
    def username(self):
        """Gets the username of this HttpsInput.

        Basic Auth Username, if required

        :return: The username of this HttpsInput.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this HttpsInput.

        Basic Auth Username, if required

        :param username: The username of this HttpsInput.
        :type: str
        """

        if username is not None:
            if not isinstance(username, str):
                raise TypeError("Invalid type for `username`, type has to be `str`")

            self._username = username


    @property
    def password(self):
        """Gets the password of this HttpsInput.

        Basic Auth Password, if required

        :return: The password of this HttpsInput.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this HttpsInput.

        Basic Auth Password, if required

        :param password: The password of this HttpsInput.
        :type: str
        """

        if password is not None:
            if not isinstance(password, str):
                raise TypeError("Invalid type for `password`, type has to be `str`")

            self._password = password


    @property
    def port(self):
        """Gets the port of this HttpsInput.

        Custom Port

        :return: The port of this HttpsInput.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this HttpsInput.

        Custom Port

        :param port: The port of this HttpsInput.
        :type: int
        """

        if port is not None:
            if not isinstance(port, int):
                raise TypeError("Invalid type for `port`, type has to be `int`")

            self._port = port

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(HttpsInput, self).to_dict()

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
            if issubclass(HttpsInput, dict):
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
        if not isinstance(other, HttpsInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
