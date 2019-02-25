# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class CencPlayReady(object):
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
            'la_url': 'str',
            'pssh': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'la_url': 'laUrl',
            'pssh': 'pssh'
        }
        return attributes

    def __init__(self, la_url=None, pssh=None, *args, **kwargs):

        self._la_url = None
        self._pssh = None
        self.discriminator = None

        if la_url is not None:
            self.la_url = la_url
        if pssh is not None:
            self.pssh = pssh

    @property
    def la_url(self):
        """Gets the la_url of this CencPlayReady.

        Url of the license server. Either the laUrl or the pssh needs to be provided.

        :return: The la_url of this CencPlayReady.
        :rtype: str
        """
        return self._la_url

    @la_url.setter
    def la_url(self, la_url):
        """Sets the la_url of this CencPlayReady.

        Url of the license server. Either the laUrl or the pssh needs to be provided.

        :param la_url: The la_url of this CencPlayReady.
        :type: str
        """

        if la_url is not None:
            if not isinstance(la_url, str):
                raise TypeError("Invalid type for `la_url`, type has to be `str`")

            self._la_url = la_url


    @property
    def pssh(self):
        """Gets the pssh of this CencPlayReady.

        Base64 encoded pssh payload.

        :return: The pssh of this CencPlayReady.
        :rtype: str
        """
        return self._pssh

    @pssh.setter
    def pssh(self, pssh):
        """Sets the pssh of this CencPlayReady.

        Base64 encoded pssh payload.

        :param pssh: The pssh of this CencPlayReady.
        :type: str
        """

        if pssh is not None:
            if not isinstance(pssh, str):
                raise TypeError("Invalid type for `pssh`, type has to be `str`")

            self._pssh = pssh

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
            if issubclass(CencPlayReady, dict):
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
        if not isinstance(other, CencPlayReady):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
