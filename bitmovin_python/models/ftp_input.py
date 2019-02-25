# coding: utf-8

from bitmovin_python.models.input import Input
from bitmovin_python.models.input_type import InputType
import pprint
import six
from datetime import datetime
from enum import Enum


class FtpInput(Input):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(FtpInput, self).openapi_types
        types.update({
            'host': 'str',
            'port': 'int',
            'passive': 'bool',
            'username': 'str',
            'password': 'str',
            'remote_verification_enabled': 'bool'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(FtpInput, self).attribute_map
        attributes.update({
            'host': 'host',
            'port': 'port',
            'passive': 'passive',
            'username': 'username',
            'password': 'password',
            'remote_verification_enabled': 'remoteVerificationEnabled'
        })
        return attributes

    def __init__(self, host=None, port=None, passive=None, username=None, password=None, remote_verification_enabled=None, *args, **kwargs):
        super(FtpInput, self).__init__(*args, **kwargs)

        self._host = None
        self._port = None
        self._passive = None
        self._username = None
        self._password = None
        self._remote_verification_enabled = None
        self.discriminator = None

        self.host = host
        if port is not None:
            self.port = port
        if passive is not None:
            self.passive = passive
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if remote_verification_enabled is not None:
            self.remote_verification_enabled = remote_verification_enabled

    @property
    def host(self):
        """Gets the host of this FtpInput.

        Host URL or IP of the FTP server

        :return: The host of this FtpInput.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this FtpInput.

        Host URL or IP of the FTP server

        :param host: The host of this FtpInput.
        :type: str
        """

        if host is not None:
            if not isinstance(host, str):
                raise TypeError("Invalid type for `host`, type has to be `str`")

            self._host = host


    @property
    def port(self):
        """Gets the port of this FtpInput.

        Port to use, standard for FTP: 21

        :return: The port of this FtpInput.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this FtpInput.

        Port to use, standard for FTP: 21

        :param port: The port of this FtpInput.
        :type: int
        """

        if port is not None:
            if not isinstance(port, int):
                raise TypeError("Invalid type for `port`, type has to be `int`")

            self._port = port


    @property
    def passive(self):
        """Gets the passive of this FtpInput.

        Use passive mode. Default is true.

        :return: The passive of this FtpInput.
        :rtype: bool
        """
        return self._passive

    @passive.setter
    def passive(self, passive):
        """Sets the passive of this FtpInput.

        Use passive mode. Default is true.

        :param passive: The passive of this FtpInput.
        :type: bool
        """

        if passive is not None:
            if not isinstance(passive, bool):
                raise TypeError("Invalid type for `passive`, type has to be `bool`")

            self._passive = passive


    @property
    def username(self):
        """Gets the username of this FtpInput.

        Your FTP Username

        :return: The username of this FtpInput.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this FtpInput.

        Your FTP Username

        :param username: The username of this FtpInput.
        :type: str
        """

        if username is not None:
            if not isinstance(username, str):
                raise TypeError("Invalid type for `username`, type has to be `str`")

            self._username = username


    @property
    def password(self):
        """Gets the password of this FtpInput.

        Your FTP password

        :return: The password of this FtpInput.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this FtpInput.

        Your FTP password

        :param password: The password of this FtpInput.
        :type: str
        """

        if password is not None:
            if not isinstance(password, str):
                raise TypeError("Invalid type for `password`, type has to be `str`")

            self._password = password


    @property
    def remote_verification_enabled(self):
        """Gets the remote_verification_enabled of this FtpInput.

        Ensure that connections originate from the declared ftp host. Default is true.

        :return: The remote_verification_enabled of this FtpInput.
        :rtype: bool
        """
        return self._remote_verification_enabled

    @remote_verification_enabled.setter
    def remote_verification_enabled(self, remote_verification_enabled):
        """Sets the remote_verification_enabled of this FtpInput.

        Ensure that connections originate from the declared ftp host. Default is true.

        :param remote_verification_enabled: The remote_verification_enabled of this FtpInput.
        :type: bool
        """

        if remote_verification_enabled is not None:
            if not isinstance(remote_verification_enabled, bool):
                raise TypeError("Invalid type for `remote_verification_enabled`, type has to be `bool`")

            self._remote_verification_enabled = remote_verification_enabled

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(FtpInput, self).to_dict()

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
            if issubclass(FtpInput, dict):
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
        if not isinstance(other, FtpInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
