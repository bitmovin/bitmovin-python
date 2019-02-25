# coding: utf-8

from bitmovin_python.models.drm import Drm
from bitmovin_python.models.drm_type import DrmType
from bitmovin_python.models.encoding_output import EncodingOutput
import pprint
import six
from datetime import datetime
from enum import Enum


class ClearKeyDrm(Drm):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(ClearKeyDrm, self).openapi_types
        types.update({
            'key': 'str',
            'kid': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(ClearKeyDrm, self).attribute_map
        attributes.update({
            'key': 'key',
            'kid': 'kid'
        })
        return attributes

    def __init__(self, key=None, kid=None, *args, **kwargs):
        super(ClearKeyDrm, self).__init__(*args, **kwargs)

        self._key = None
        self._kid = None
        self.discriminator = None

        self.key = key
        self.kid = kid

    @property
    def key(self):
        """Gets the key of this ClearKeyDrm.

        16 byte encryption key, 32 hexadecimal characters

        :return: The key of this ClearKeyDrm.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ClearKeyDrm.

        16 byte encryption key, 32 hexadecimal characters

        :param key: The key of this ClearKeyDrm.
        :type: str
        """

        if key is not None:
            if not isinstance(key, str):
                raise TypeError("Invalid type for `key`, type has to be `str`")

            self._key = key


    @property
    def kid(self):
        """Gets the kid of this ClearKeyDrm.

        16 byte key id

        :return: The kid of this ClearKeyDrm.
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """Sets the kid of this ClearKeyDrm.

        16 byte key id

        :param kid: The kid of this ClearKeyDrm.
        :type: str
        """

        if kid is not None:
            if not isinstance(kid, str):
                raise TypeError("Invalid type for `kid`, type has to be `str`")

            self._kid = kid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(ClearKeyDrm, self).to_dict()

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
            if issubclass(ClearKeyDrm, dict):
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
        if not isinstance(other, ClearKeyDrm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
