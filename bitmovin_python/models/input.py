# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.input_type import InputType
import pprint
import six
from datetime import datetime
from enum import Enum


class Input(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Input, self).openapi_types
        types.update({
            'type': 'InputType'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Input, self).attribute_map
        attributes.update({
            'type': 'type'
        })
        return attributes

    discriminator_value_class_map = {
        'AKAMAI_NETSTORAGE': 'AkamaiNetStorageInput',
        'ASPERA': 'AsperaInput',
        'AZURE': 'AzureInput',
        'REDUNDANT_RTMP': 'RedundantRtmpInput',
        'FTP': 'FtpInput',
        'GENERIC_S3': 'GenericS3Input',
        'GCS': 'GcsInput',
        'HTTP': 'HttpInput',
        'HTTPS': 'HttpsInput',
        'LOCAL': 'LocalInput',
        'RTMP': 'RtmpInput',
        'S3': 'S3Input',
        'S3_ROLE_BASED': 'S3RoleBasedInput',
        'SFTP': 'SftpInput',
        'TCP': 'TcpInput',
        'UDP': 'UdpInput',
        'UDP_MULTICAST': 'UdpMulticastInput',
        'ZIXI': 'ZixiInput'
    }

    def __init__(self, type=None, *args, **kwargs):
        super(Input, self).__init__(*args, **kwargs)

        self._type = None
        self.discriminator = 'type'

        if type is not None:
            self.type = type

    @property
    def type(self):
        """Gets the type of this Input.

        The type of the input

        :return: The type of this Input.
        :rtype: InputType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Input.

        The type of the input

        :param type: The type of this Input.
        :type: InputType
        """

        if type is not None:
            if not isinstance(type, InputType):
                raise TypeError("Invalid type for `type`, type has to be `InputType`")

            self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator]
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Input, self).to_dict()

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
            if issubclass(Input, dict):
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
        if not isinstance(other, Input):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
