# coding: utf-8

from bitmovin_python.models.account_api_key import AccountApiKey
from bitmovin_python.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from enum import Enum


class AccountInformation(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AccountInformation, self).openapi_types
        types.update({
            'email': 'str',
            'api_keys': 'list[AccountApiKey]',
            'first_name': 'str',
            'last_name': 'str',
            'phone': 'str',
            'company': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AccountInformation, self).attribute_map
        attributes.update({
            'email': 'email',
            'api_keys': 'apiKeys',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'phone': 'phone',
            'company': 'company'
        })
        return attributes

    def __init__(self, email=None, api_keys=None, first_name=None, last_name=None, phone=None, company=None, *args, **kwargs):
        super(AccountInformation, self).__init__(*args, **kwargs)

        self._email = None
        self._api_keys = None
        self._first_name = None
        self._last_name = None
        self._phone = None
        self._company = None
        self.discriminator = None

        self.email = email
        self.api_keys = api_keys
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if phone is not None:
            self.phone = phone
        if company is not None:
            self.company = company

    @property
    def email(self):
        """Gets the email of this AccountInformation.

        Email address of the account.

        :return: The email of this AccountInformation.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AccountInformation.

        Email address of the account.

        :param email: The email of this AccountInformation.
        :type: str
        """

        if email is not None:
            if not isinstance(email, str):
                raise TypeError("Invalid type for `email`, type has to be `str`")

            self._email = email


    @property
    def api_keys(self):
        """Gets the api_keys of this AccountInformation.

        ApiKeys associated with the account

        :return: The api_keys of this AccountInformation.
        :rtype: list[AccountApiKey]
        """
        return self._api_keys

    @api_keys.setter
    def api_keys(self, api_keys):
        """Sets the api_keys of this AccountInformation.

        ApiKeys associated with the account

        :param api_keys: The api_keys of this AccountInformation.
        :type: list[AccountApiKey]
        """

        if api_keys is not None:
            if not isinstance(api_keys, list):
                raise TypeError("Invalid type for `api_keys`, type has to be `list[AccountApiKey]`")

            self._api_keys = api_keys


    @property
    def first_name(self):
        """Gets the first_name of this AccountInformation.

        First name of the tenant.

        :return: The first_name of this AccountInformation.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this AccountInformation.

        First name of the tenant.

        :param first_name: The first_name of this AccountInformation.
        :type: str
        """

        if first_name is not None:
            if not isinstance(first_name, str):
                raise TypeError("Invalid type for `first_name`, type has to be `str`")

            self._first_name = first_name


    @property
    def last_name(self):
        """Gets the last_name of this AccountInformation.

        Last name of the tenant.

        :return: The last_name of this AccountInformation.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this AccountInformation.

        Last name of the tenant.

        :param last_name: The last_name of this AccountInformation.
        :type: str
        """

        if last_name is not None:
            if not isinstance(last_name, str):
                raise TypeError("Invalid type for `last_name`, type has to be `str`")

            self._last_name = last_name


    @property
    def phone(self):
        """Gets the phone of this AccountInformation.

        Phone number of the tenant.

        :return: The phone of this AccountInformation.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this AccountInformation.

        Phone number of the tenant.

        :param phone: The phone of this AccountInformation.
        :type: str
        """

        if phone is not None:
            if not isinstance(phone, str):
                raise TypeError("Invalid type for `phone`, type has to be `str`")

            self._phone = phone


    @property
    def company(self):
        """Gets the company of this AccountInformation.

        Company name of the tenant.

        :return: The company of this AccountInformation.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this AccountInformation.

        Company name of the tenant.

        :param company: The company of this AccountInformation.
        :type: str
        """

        if company is not None:
            if not isinstance(company, str):
                raise TypeError("Invalid type for `company`, type has to be `str`")

            self._company = company

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AccountInformation, self).to_dict()

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
            if issubclass(AccountInformation, dict):
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
        if not isinstance(other, AccountInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
