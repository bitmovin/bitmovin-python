# coding: utf-8

from bitmovin_python.models.input import Input
from bitmovin_python.models.input_type import InputType
import pprint
import six
from datetime import datetime
from enum import Enum


class AsperaInput(Input):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AsperaInput, self).openapi_types
        types.update({
            'min_bandwidth': 'str',
            'max_bandwidth': 'str',
            'host': 'str',
            'username': 'str',
            'password': 'str',
            'token': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AsperaInput, self).attribute_map
        attributes.update({
            'min_bandwidth': 'minBandwidth',
            'max_bandwidth': 'maxBandwidth',
            'host': 'host',
            'username': 'username',
            'password': 'password',
            'token': 'token'
        })
        return attributes

    def __init__(self, min_bandwidth=None, max_bandwidth=None, host=None, username=None, password=None, token=None, *args, **kwargs):
        super(AsperaInput, self).__init__(*args, **kwargs)

        self._min_bandwidth = None
        self._max_bandwidth = None
        self._host = None
        self._username = None
        self._password = None
        self._token = None
        self.discriminator = None

        if min_bandwidth is not None:
            self.min_bandwidth = min_bandwidth
        if max_bandwidth is not None:
            self.max_bandwidth = max_bandwidth
        self.host = host
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if token is not None:
            self.token = token

    @property
    def min_bandwidth(self):
        """Gets the min_bandwidth of this AsperaInput.

        Minimal download bandwidth. Examples: 100k, 100m, 100g

        :return: The min_bandwidth of this AsperaInput.
        :rtype: str
        """
        return self._min_bandwidth

    @min_bandwidth.setter
    def min_bandwidth(self, min_bandwidth):
        """Sets the min_bandwidth of this AsperaInput.

        Minimal download bandwidth. Examples: 100k, 100m, 100g

        :param min_bandwidth: The min_bandwidth of this AsperaInput.
        :type: str
        """

        if min_bandwidth is not None:
            if not isinstance(min_bandwidth, str):
                raise TypeError("Invalid type for `min_bandwidth`, type has to be `str`")

            self._min_bandwidth = min_bandwidth


    @property
    def max_bandwidth(self):
        """Gets the max_bandwidth of this AsperaInput.

        Maximal download bandwidth. Examples: 100k, 100m, 100g

        :return: The max_bandwidth of this AsperaInput.
        :rtype: str
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        """Sets the max_bandwidth of this AsperaInput.

        Maximal download bandwidth. Examples: 100k, 100m, 100g

        :param max_bandwidth: The max_bandwidth of this AsperaInput.
        :type: str
        """

        if max_bandwidth is not None:
            if not isinstance(max_bandwidth, str):
                raise TypeError("Invalid type for `max_bandwidth`, type has to be `str`")

            self._max_bandwidth = max_bandwidth


    @property
    def host(self):
        """Gets the host of this AsperaInput.

        Host to use for Aspera transfers

        :return: The host of this AsperaInput.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this AsperaInput.

        Host to use for Aspera transfers

        :param host: The host of this AsperaInput.
        :type: str
        """

        if host is not None:
            if not isinstance(host, str):
                raise TypeError("Invalid type for `host`, type has to be `str`")

            self._host = host


    @property
    def username(self):
        """Gets the username of this AsperaInput.

        Username to log into Aspera host (either password and user must be set or token)

        :return: The username of this AsperaInput.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AsperaInput.

        Username to log into Aspera host (either password and user must be set or token)

        :param username: The username of this AsperaInput.
        :type: str
        """

        if username is not None:
            if not isinstance(username, str):
                raise TypeError("Invalid type for `username`, type has to be `str`")

            self._username = username


    @property
    def password(self):
        """Gets the password of this AsperaInput.

        corresponding password (either password and user must be set or token)

        :return: The password of this AsperaInput.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AsperaInput.

        corresponding password (either password and user must be set or token)

        :param password: The password of this AsperaInput.
        :type: str
        """

        if password is not None:
            if not isinstance(password, str):
                raise TypeError("Invalid type for `password`, type has to be `str`")

            self._password = password


    @property
    def token(self):
        """Gets the token of this AsperaInput.

        Token used for authentication (either password and user must be set or token)

        :return: The token of this AsperaInput.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AsperaInput.

        Token used for authentication (either password and user must be set or token)

        :param token: The token of this AsperaInput.
        :type: str
        """

        if token is not None:
            if not isinstance(token, str):
                raise TypeError("Invalid type for `token`, type has to be `str`")

            self._token = token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AsperaInput, self).to_dict()

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
            if issubclass(AsperaInput, dict):
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
        if not isinstance(other, AsperaInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
