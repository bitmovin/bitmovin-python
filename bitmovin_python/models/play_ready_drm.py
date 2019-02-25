# coding: utf-8

from bitmovin_python.models.drm import Drm
from bitmovin_python.models.drm_type import DrmType
from bitmovin_python.models.encoding_output import EncodingOutput
from bitmovin_python.models.play_ready_encryption_method import PlayReadyEncryptionMethod
import pprint
import six
from datetime import datetime
from enum import Enum


class PlayReadyDrm(Drm):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(PlayReadyDrm, self).openapi_types
        types.update({
            'key': 'str',
            'key_seed': 'str',
            'la_url': 'str',
            'method': 'PlayReadyEncryptionMethod',
            'kid': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(PlayReadyDrm, self).attribute_map
        attributes.update({
            'key': 'key',
            'key_seed': 'keySeed',
            'la_url': 'laUrl',
            'method': 'method',
            'kid': 'kid'
        })
        return attributes

    def __init__(self, key=None, key_seed=None, la_url=None, method=None, kid=None, *args, **kwargs):
        super(PlayReadyDrm, self).__init__(*args, **kwargs)

        self._key = None
        self._key_seed = None
        self._la_url = None
        self._method = None
        self._kid = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if key_seed is not None:
            self.key_seed = key_seed
        if la_url is not None:
            self.la_url = la_url
        if method is not None:
            self.method = method
        if kid is not None:
            self.kid = kid

    @property
    def key(self):
        """Gets the key of this PlayReadyDrm.

        16 byte encryption key, 32 hexadecimal characters. Either key or keySeed is required.

        :return: The key of this PlayReadyDrm.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PlayReadyDrm.

        16 byte encryption key, 32 hexadecimal characters. Either key or keySeed is required.

        :param key: The key of this PlayReadyDrm.
        :type: str
        """

        if key is not None:
            if not isinstance(key, str):
                raise TypeError("Invalid type for `key`, type has to be `str`")

            self._key = key


    @property
    def key_seed(self):
        """Gets the key_seed of this PlayReadyDrm.

        Key seed to generate key. Either key or keySeed is required.

        :return: The key_seed of this PlayReadyDrm.
        :rtype: str
        """
        return self._key_seed

    @key_seed.setter
    def key_seed(self, key_seed):
        """Sets the key_seed of this PlayReadyDrm.

        Key seed to generate key. Either key or keySeed is required.

        :param key_seed: The key_seed of this PlayReadyDrm.
        :type: str
        """

        if key_seed is not None:
            if not isinstance(key_seed, str):
                raise TypeError("Invalid type for `key_seed`, type has to be `str`")

            self._key_seed = key_seed


    @property
    def la_url(self):
        """Gets the la_url of this PlayReadyDrm.

        URL of the license server

        :return: The la_url of this PlayReadyDrm.
        :rtype: str
        """
        return self._la_url

    @la_url.setter
    def la_url(self, la_url):
        """Sets the la_url of this PlayReadyDrm.

        URL of the license server

        :param la_url: The la_url of this PlayReadyDrm.
        :type: str
        """

        if la_url is not None:
            if not isinstance(la_url, str):
                raise TypeError("Invalid type for `la_url`, type has to be `str`")

            self._la_url = la_url


    @property
    def method(self):
        """Gets the method of this PlayReadyDrm.


        :return: The method of this PlayReadyDrm.
        :rtype: PlayReadyEncryptionMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this PlayReadyDrm.


        :param method: The method of this PlayReadyDrm.
        :type: PlayReadyEncryptionMethod
        """

        if method is not None:
            if not isinstance(method, PlayReadyEncryptionMethod):
                raise TypeError("Invalid type for `method`, type has to be `PlayReadyEncryptionMethod`")

            self._method = method


    @property
    def kid(self):
        """Gets the kid of this PlayReadyDrm.

        Key identifier

        :return: The kid of this PlayReadyDrm.
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """Sets the kid of this PlayReadyDrm.

        Key identifier

        :param kid: The kid of this PlayReadyDrm.
        :type: str
        """

        if kid is not None:
            if not isinstance(kid, str):
                raise TypeError("Invalid type for `kid`, type has to be `str`")

            self._kid = kid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(PlayReadyDrm, self).to_dict()

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
            if issubclass(PlayReadyDrm, dict):
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
        if not isinstance(other, PlayReadyDrm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
