# coding: utf-8

from bitmovin_python.models.input import Input
from bitmovin_python.models.input_type import InputType
import pprint
import six
from datetime import datetime
from enum import Enum


class AkamaiNetStorageInput(Input):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AkamaiNetStorageInput, self).openapi_types
        types.update({
            'host': 'str',
            'username': 'str',
            'password': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AkamaiNetStorageInput, self).attribute_map
        attributes.update({
            'host': 'host',
            'username': 'username',
            'password': 'password'
        })
        return attributes

    def __init__(self, host=None, username=None, password=None, *args, **kwargs):
        super(AkamaiNetStorageInput, self).__init__(*args, **kwargs)

        self._host = None
        self._username = None
        self._password = None
        self.discriminator = None

        self.host = host
        self.username = username
        self.password = password

    @property
    def host(self):
        """Gets the host of this AkamaiNetStorageInput.

        Host to use for Akamai NetStorage transfers

        :return: The host of this AkamaiNetStorageInput.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this AkamaiNetStorageInput.

        Host to use for Akamai NetStorage transfers

        :param host: The host of this AkamaiNetStorageInput.
        :type: str
        """

        if host is not None:
            if not isinstance(host, str):
                raise TypeError("Invalid type for `host`, type has to be `str`")

            self._host = host


    @property
    def username(self):
        """Gets the username of this AkamaiNetStorageInput.

        Your Akamai NetStorage Username

        :return: The username of this AkamaiNetStorageInput.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AkamaiNetStorageInput.

        Your Akamai NetStorage Username

        :param username: The username of this AkamaiNetStorageInput.
        :type: str
        """

        if username is not None:
            if not isinstance(username, str):
                raise TypeError("Invalid type for `username`, type has to be `str`")

            self._username = username


    @property
    def password(self):
        """Gets the password of this AkamaiNetStorageInput.

        Your Akamai NetStorage password

        :return: The password of this AkamaiNetStorageInput.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AkamaiNetStorageInput.

        Your Akamai NetStorage password

        :param password: The password of this AkamaiNetStorageInput.
        :type: str
        """

        if password is not None:
            if not isinstance(password, str):
                raise TypeError("Invalid type for `password`, type has to be `str`")

            self._password = password

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AkamaiNetStorageInput, self).to_dict()

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
            if issubclass(AkamaiNetStorageInput, dict):
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
        if not isinstance(other, AkamaiNetStorageInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
