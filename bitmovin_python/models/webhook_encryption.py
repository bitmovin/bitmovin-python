# coding: utf-8

from bitmovin_python.models.encryption_type import EncryptionType
import pprint
import six
from datetime import datetime
from enum import Enum


class WebhookEncryption(object):
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
            'type': 'EncryptionType',
            'key': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'type': 'type',
            'key': 'key'
        }
        return attributes

    def __init__(self, type=None, key=None, *args, **kwargs):

        self._type = None
        self._key = None
        self.discriminator = None

        self.type = type
        self.key = key

    @property
    def type(self):
        """Gets the type of this WebhookEncryption.

        The encryption algorithm used for the webhook

        :return: The type of this WebhookEncryption.
        :rtype: EncryptionType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebhookEncryption.

        The encryption algorithm used for the webhook

        :param type: The type of this WebhookEncryption.
        :type: EncryptionType
        """

        if type is not None:
            if not isinstance(type, EncryptionType):
                raise TypeError("Invalid type for `type`, type has to be `EncryptionType`")

            self._type = type


    @property
    def key(self):
        """Gets the key of this WebhookEncryption.

        The key of the encryption

        :return: The key of this WebhookEncryption.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this WebhookEncryption.

        The key of the encryption

        :param key: The key of this WebhookEncryption.
        :type: str
        """

        if key is not None:
            if not isinstance(key, str):
                raise TypeError("Invalid type for `key`, type has to be `str`")

            self._key = key

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
            if issubclass(WebhookEncryption, dict):
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
        if not isinstance(other, WebhookEncryption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
