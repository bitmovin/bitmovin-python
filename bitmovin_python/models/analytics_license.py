# coding: utf-8

from bitmovin_python.models.bitmovin_response import BitmovinResponse
import pprint
import six
from datetime import datetime
from enum import Enum


class AnalyticsLicense(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AnalyticsLicense, self).openapi_types
        types.update({
            'name': 'str',
            'license_key': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AnalyticsLicense, self).attribute_map
        attributes.update({
            'name': 'name',
            'license_key': 'licenseKey'
        })
        return attributes

    def __init__(self, name=None, license_key=None, *args, **kwargs):
        super(AnalyticsLicense, self).__init__(*args, **kwargs)

        self._name = None
        self._license_key = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.license_key = license_key

    @property
    def name(self):
        """Gets the name of this AnalyticsLicense.

        Name of the Analytics License

        :return: The name of this AnalyticsLicense.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnalyticsLicense.

        Name of the Analytics License

        :param name: The name of this AnalyticsLicense.
        :type: str
        """

        if name is not None:
            if not isinstance(name, str):
                raise TypeError("Invalid type for `name`, type has to be `str`")

            self._name = name


    @property
    def license_key(self):
        """Gets the license_key of this AnalyticsLicense.

        License Key

        :return: The license_key of this AnalyticsLicense.
        :rtype: str
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        """Sets the license_key of this AnalyticsLicense.

        License Key

        :param license_key: The license_key of this AnalyticsLicense.
        :type: str
        """

        if license_key is not None:
            if not isinstance(license_key, str):
                raise TypeError("Invalid type for `license_key`, type has to be `str`")

            self._license_key = license_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AnalyticsLicense, self).to_dict()

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
            if issubclass(AnalyticsLicense, dict):
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
        if not isinstance(other, AnalyticsLicense):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
