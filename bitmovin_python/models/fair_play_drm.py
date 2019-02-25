# coding: utf-8

from bitmovin_python.models.drm import Drm
from bitmovin_python.models.drm_type import DrmType
from bitmovin_python.models.encoding_output import EncodingOutput
import pprint
import six
from datetime import datetime
from enum import Enum


class FairPlayDrm(Drm):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(FairPlayDrm, self).openapi_types
        types.update({
            'key': 'str',
            'iv': 'str',
            'uri': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(FairPlayDrm, self).attribute_map
        attributes.update({
            'key': 'key',
            'iv': 'iv',
            'uri': 'uri'
        })
        return attributes

    def __init__(self, key=None, iv=None, uri=None, *args, **kwargs):
        super(FairPlayDrm, self).__init__(*args, **kwargs)

        self._key = None
        self._iv = None
        self._uri = None
        self.discriminator = None

        self.key = key
        self.iv = iv
        if uri is not None:
            self.uri = uri

    @property
    def key(self):
        """Gets the key of this FairPlayDrm.

        16 byte Encryption key, 32 hexadecimal characters

        :return: The key of this FairPlayDrm.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FairPlayDrm.

        16 byte Encryption key, 32 hexadecimal characters

        :param key: The key of this FairPlayDrm.
        :type: str
        """

        if key is not None:
            if not isinstance(key, str):
                raise TypeError("Invalid type for `key`, type has to be `str`")

            self._key = key


    @property
    def iv(self):
        """Gets the iv of this FairPlayDrm.

        16 byte initialization vector

        :return: The iv of this FairPlayDrm.
        :rtype: str
        """
        return self._iv

    @iv.setter
    def iv(self, iv):
        """Sets the iv of this FairPlayDrm.

        16 byte initialization vector

        :param iv: The iv of this FairPlayDrm.
        :type: str
        """

        if iv is not None:
            if not isinstance(iv, str):
                raise TypeError("Invalid type for `iv`, type has to be `str`")

            self._iv = iv


    @property
    def uri(self):
        """Gets the uri of this FairPlayDrm.

        Url of the licensing server

        :return: The uri of this FairPlayDrm.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this FairPlayDrm.

        Url of the licensing server

        :param uri: The uri of this FairPlayDrm.
        :type: str
        """

        if uri is not None:
            if not isinstance(uri, str):
                raise TypeError("Invalid type for `uri`, type has to be `str`")

            self._uri = uri

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(FairPlayDrm, self).to_dict()

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
            if issubclass(FairPlayDrm, dict):
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
        if not isinstance(other, FairPlayDrm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
