# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class Login(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = {
            'e_mail': 'str',
            'password': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'e_mail': 'eMail',
            'password': 'password'
        }
        return attributes

    def __init__(self, e_mail=None, password=None, *args, **kwargs):

        self._e_mail = None
        self._password = None
        self.discriminator = None

        self.e_mail = e_mail
        self.password = password

    @property
    def e_mail(self):
        """Gets the e_mail of this Login.

        Email address of the account.

        :return: The e_mail of this Login.
        :rtype: str
        """
        return self._e_mail

    @e_mail.setter
    def e_mail(self, e_mail):
        """Sets the e_mail of this Login.

        Email address of the account.

        :param e_mail: The e_mail of this Login.
        :type: str
        """

        if e_mail is not None:
            if not isinstance(e_mail, str):
                raise TypeError("Invalid type for `e_mail`, type has to be `str`")

            self._e_mail = e_mail


    @property
    def password(self):
        """Gets the password of this Login.

        Password of the account.

        :return: The password of this Login.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Login.

        Password of the account.

        :param password: The password of this Login.
        :type: str
        """

        if password is not None:
            if not isinstance(password, str):
                raise TypeError("Invalid type for `password`, type has to be `str`")

            self._password = password

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

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
            if issubclass(Login, dict):
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
        if not isinstance(other, Login):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
