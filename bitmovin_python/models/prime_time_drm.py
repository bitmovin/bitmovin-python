# coding: utf-8

from bitmovin_python.models.drm import Drm
from bitmovin_python.models.drm_type import DrmType
from bitmovin_python.models.encoding_output import EncodingOutput
import pprint
import six
from datetime import datetime
from enum import Enum


class PrimeTimeDrm(Drm):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(PrimeTimeDrm, self).openapi_types
        types.update({
            'key': 'str',
            'kid': 'str',
            'pssh': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(PrimeTimeDrm, self).attribute_map
        attributes.update({
            'key': 'key',
            'kid': 'kid',
            'pssh': 'pssh'
        })
        return attributes

    def __init__(self, key=None, kid=None, pssh=None, *args, **kwargs):
        super(PrimeTimeDrm, self).__init__(*args, **kwargs)

        self._key = None
        self._kid = None
        self._pssh = None
        self.discriminator = None

        self.key = key
        self.kid = kid
        self.pssh = pssh

    @property
    def key(self):
        """Gets the key of this PrimeTimeDrm.

        16 byte Encryption key, 32 hexadecimal characters

        :return: The key of this PrimeTimeDrm.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PrimeTimeDrm.

        16 byte Encryption key, 32 hexadecimal characters

        :param key: The key of this PrimeTimeDrm.
        :type: str
        """

        if key is not None:
            if not isinstance(key, str):
                raise TypeError("Invalid type for `key`, type has to be `str`")

            self._key = key


    @property
    def kid(self):
        """Gets the kid of this PrimeTimeDrm.

        16 byte Key id, 32 hexadecimal characters

        :return: The kid of this PrimeTimeDrm.
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """Sets the kid of this PrimeTimeDrm.

        16 byte Key id, 32 hexadecimal characters

        :param kid: The kid of this PrimeTimeDrm.
        :type: str
        """

        if kid is not None:
            if not isinstance(kid, str):
                raise TypeError("Invalid type for `kid`, type has to be `str`")

            self._kid = kid


    @property
    def pssh(self):
        """Gets the pssh of this PrimeTimeDrm.

        Base 64 Encoded

        :return: The pssh of this PrimeTimeDrm.
        :rtype: str
        """
        return self._pssh

    @pssh.setter
    def pssh(self, pssh):
        """Sets the pssh of this PrimeTimeDrm.

        Base 64 Encoded

        :param pssh: The pssh of this PrimeTimeDrm.
        :type: str
        """

        if pssh is not None:
            if not isinstance(pssh, str):
                raise TypeError("Invalid type for `pssh`, type has to be `str`")

            self._pssh = pssh

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(PrimeTimeDrm, self).to_dict()

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
            if issubclass(PrimeTimeDrm, dict):
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
        if not isinstance(other, PrimeTimeDrm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
