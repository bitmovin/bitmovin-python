# coding: utf-8

from bitmovin_python.models.acl_entry import AclEntry
from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.output_type import OutputType
import pprint
import six
from datetime import datetime
from enum import Enum


class Output(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Output, self).openapi_types
        types.update({
            'acl': 'list[AclEntry]',
            'type': 'OutputType'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Output, self).attribute_map
        attributes.update({
            'acl': 'acl',
            'type': 'type'
        })
        return attributes

    discriminator_value_class_map = {
        'AKAMAI_NETSTORAGE': 'AkamaiNetStorageOutput',
        'AZURE': 'AzureOutput',
        'GENERIC_S3': 'GenericS3Output',
        'GCS': 'GcsOutput',
        'FTP': 'FtpOutput',
        'LOCAL': 'LocalOutput',
        'S3': 'S3Output',
        'S3_ROLE_BASED': 'S3RoleBasedOutput',
        'SFTP': 'SftpOutput'
    }

    def __init__(self, acl=None, type=None, *args, **kwargs):
        super(Output, self).__init__(*args, **kwargs)

        self._acl = None
        self._type = None
        self.discriminator = 'type'

        if acl is not None:
            self.acl = acl
        if type is not None:
            self.type = type

    @property
    def acl(self):
        """Gets the acl of this Output.


        :return: The acl of this Output.
        :rtype: list[AclEntry]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this Output.


        :param acl: The acl of this Output.
        :type: list[AclEntry]
        """

        if acl is not None:
            if not isinstance(acl, list):
                raise TypeError("Invalid type for `acl`, type has to be `list[AclEntry]`")

            self._acl = acl


    @property
    def type(self):
        """Gets the type of this Output.

        The type of the output

        :return: The type of this Output.
        :rtype: OutputType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Output.

        The type of the output

        :param type: The type of this Output.
        :type: OutputType
        """

        if type is not None:
            if not isinstance(type, OutputType):
                raise TypeError("Invalid type for `type`, type has to be `OutputType`")

            self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator]
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Output, self).to_dict()

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
            if issubclass(Output, dict):
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
        if not isinstance(other, Output):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
