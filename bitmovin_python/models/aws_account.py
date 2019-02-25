# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from enum import Enum


class AwsAccount(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AwsAccount, self).openapi_types
        types.update({
            'access_key': 'str',
            'secret_key': 'str',
            'account_number': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AwsAccount, self).attribute_map
        attributes.update({
            'access_key': 'accessKey',
            'secret_key': 'secretKey',
            'account_number': 'accountNumber'
        })
        return attributes

    def __init__(self, access_key=None, secret_key=None, account_number=None, *args, **kwargs):
        super(AwsAccount, self).__init__(*args, **kwargs)

        self._access_key = None
        self._secret_key = None
        self._account_number = None
        self.discriminator = None

        self.access_key = access_key
        self.secret_key = secret_key
        self.account_number = account_number

    @property
    def access_key(self):
        """Gets the access_key of this AwsAccount.

        Amazon access key

        :return: The access_key of this AwsAccount.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this AwsAccount.

        Amazon access key

        :param access_key: The access_key of this AwsAccount.
        :type: str
        """

        if access_key is not None:
            if not isinstance(access_key, str):
                raise TypeError("Invalid type for `access_key`, type has to be `str`")

            self._access_key = access_key


    @property
    def secret_key(self):
        """Gets the secret_key of this AwsAccount.

        Amazon secret key

        :return: The secret_key of this AwsAccount.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this AwsAccount.

        Amazon secret key

        :param secret_key: The secret_key of this AwsAccount.
        :type: str
        """

        if secret_key is not None:
            if not isinstance(secret_key, str):
                raise TypeError("Invalid type for `secret_key`, type has to be `str`")

            self._secret_key = secret_key


    @property
    def account_number(self):
        """Gets the account_number of this AwsAccount.

        Amazon account number (12 digits as per AWS spec)

        :return: The account_number of this AwsAccount.
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this AwsAccount.

        Amazon account number (12 digits as per AWS spec)

        :param account_number: The account_number of this AwsAccount.
        :type: str
        """

        if account_number is not None:
            if not isinstance(account_number, str):
                raise TypeError("Invalid type for `account_number`, type has to be `str`")

            self._account_number = account_number

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AwsAccount, self).to_dict()

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
            if issubclass(AwsAccount, dict):
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
        if not isinstance(other, AwsAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
