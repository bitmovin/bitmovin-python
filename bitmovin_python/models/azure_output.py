# coding: utf-8

from bitmovin_python.models.acl_entry import AclEntry
from bitmovin_python.models.output import Output
from bitmovin_python.models.output_type import OutputType
import pprint
import six
from datetime import datetime
from enum import Enum


class AzureOutput(Output):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AzureOutput, self).openapi_types
        types.update({
            'account_name': 'str',
            'account_key': 'str',
            'container': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AzureOutput, self).attribute_map
        attributes.update({
            'account_name': 'accountName',
            'account_key': 'accountKey',
            'container': 'container'
        })
        return attributes

    def __init__(self, account_name=None, account_key=None, container=None, *args, **kwargs):
        super(AzureOutput, self).__init__(*args, **kwargs)

        self._account_name = None
        self._account_key = None
        self._container = None
        self.discriminator = None

        self.account_name = account_name
        self.account_key = account_key
        self.container = container

    @property
    def account_name(self):
        """Gets the account_name of this AzureOutput.

        Azure Account Name

        :return: The account_name of this AzureOutput.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this AzureOutput.

        Azure Account Name

        :param account_name: The account_name of this AzureOutput.
        :type: str
        """

        if account_name is not None:
            if not isinstance(account_name, str):
                raise TypeError("Invalid type for `account_name`, type has to be `str`")

            self._account_name = account_name


    @property
    def account_key(self):
        """Gets the account_key of this AzureOutput.

        Azure Account Key

        :return: The account_key of this AzureOutput.
        :rtype: str
        """
        return self._account_key

    @account_key.setter
    def account_key(self, account_key):
        """Sets the account_key of this AzureOutput.

        Azure Account Key

        :param account_key: The account_key of this AzureOutput.
        :type: str
        """

        if account_key is not None:
            if not isinstance(account_key, str):
                raise TypeError("Invalid type for `account_key`, type has to be `str`")

            self._account_key = account_key


    @property
    def container(self):
        """Gets the container of this AzureOutput.

        Name of the bucket

        :return: The container of this AzureOutput.
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this AzureOutput.

        Name of the bucket

        :param container: The container of this AzureOutput.
        :type: str
        """

        if container is not None:
            if not isinstance(container, str):
                raise TypeError("Invalid type for `container`, type has to be `str`")

            self._container = container

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AzureOutput, self).to_dict()

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
            if issubclass(AzureOutput, dict):
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
        if not isinstance(other, AzureOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
