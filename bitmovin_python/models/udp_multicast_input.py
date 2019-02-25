# coding: utf-8

from bitmovin_python.models.input import Input
from bitmovin_python.models.input_type import InputType
import pprint
import six
from datetime import datetime
from enum import Enum


class UdpMulticastInput(Input):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(UdpMulticastInput, self).openapi_types
        types.update({
            'host': 'str',
            'port': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(UdpMulticastInput, self).attribute_map
        attributes.update({
            'host': 'host',
            'port': 'port'
        })
        return attributes

    def __init__(self, host=None, port=None, *args, **kwargs):
        super(UdpMulticastInput, self).__init__(*args, **kwargs)

        self._host = None
        self._port = None
        self.discriminator = None

        self.host = host
        self.port = port

    @property
    def host(self):
        """Gets the host of this UdpMulticastInput.

        Host name or IP address to use

        :return: The host of this UdpMulticastInput.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this UdpMulticastInput.

        Host name or IP address to use

        :param host: The host of this UdpMulticastInput.
        :type: str
        """

        if host is not None:
            if not isinstance(host, str):
                raise TypeError("Invalid type for `host`, type has to be `str`")

            self._host = host


    @property
    def port(self):
        """Gets the port of this UdpMulticastInput.

        Port to use

        :return: The port of this UdpMulticastInput.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this UdpMulticastInput.

        Port to use

        :param port: The port of this UdpMulticastInput.
        :type: int
        """

        if port is not None:
            if not isinstance(port, int):
                raise TypeError("Invalid type for `port`, type has to be `int`")

            self._port = port

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(UdpMulticastInput, self).to_dict()

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
            if issubclass(UdpMulticastInput, dict):
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
        if not isinstance(other, UdpMulticastInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
