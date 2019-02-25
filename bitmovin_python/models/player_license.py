# coding: utf-8

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.domain import Domain
import pprint
import six
from datetime import datetime
from enum import Enum


class PlayerLicense(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(PlayerLicense, self).openapi_types
        types.update({
            'name': 'str',
            'created_at': 'datetime',
            'license_key': 'str',
            'impressions': 'int',
            'max_impressions': 'int',
            'third_party_licensing_enabled': 'bool',
            'domains': 'list[Domain]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(PlayerLicense, self).attribute_map
        attributes.update({
            'name': 'name',
            'created_at': 'createdAt',
            'license_key': 'licenseKey',
            'impressions': 'impressions',
            'max_impressions': 'maxImpressions',
            'third_party_licensing_enabled': 'thirdPartyLicensingEnabled',
            'domains': 'domains'
        })
        return attributes

    def __init__(self, name=None, created_at=None, license_key=None, impressions=None, max_impressions=None, third_party_licensing_enabled=None, domains=None, *args, **kwargs):
        super(PlayerLicense, self).__init__(*args, **kwargs)

        self._name = None
        self._created_at = None
        self._license_key = None
        self._impressions = None
        self._max_impressions = None
        self._third_party_licensing_enabled = None
        self._domains = None
        self.discriminator = None

        self.name = name
        self.created_at = created_at
        self.license_key = license_key
        self.impressions = impressions
        self.max_impressions = max_impressions
        self.third_party_licensing_enabled = third_party_licensing_enabled
        self.domains = domains

    @property
    def name(self):
        """Gets the name of this PlayerLicense.

        Name of the resource

        :return: The name of this PlayerLicense.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerLicense.

        Name of the resource

        :param name: The name of this PlayerLicense.
        :type: str
        """

        if name is not None:
            if not isinstance(name, str):
                raise TypeError("Invalid type for `name`, type has to be `str`")

            self._name = name


    @property
    def created_at(self):
        """Gets the created_at of this PlayerLicense.

        Creation timestamp expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :return: The created_at of this PlayerLicense.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PlayerLicense.

        Creation timestamp expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :param created_at: The created_at of this PlayerLicense.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

            self._created_at = created_at


    @property
    def license_key(self):
        """Gets the license_key of this PlayerLicense.

        License Key

        :return: The license_key of this PlayerLicense.
        :rtype: str
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        """Sets the license_key of this PlayerLicense.

        License Key

        :param license_key: The license_key of this PlayerLicense.
        :type: str
        """

        if license_key is not None:
            if not isinstance(license_key, str):
                raise TypeError("Invalid type for `license_key`, type has to be `str`")

            self._license_key = license_key


    @property
    def impressions(self):
        """Gets the impressions of this PlayerLicense.

        Number of impressions recorded

        :return: The impressions of this PlayerLicense.
        :rtype: int
        """
        return self._impressions

    @impressions.setter
    def impressions(self, impressions):
        """Sets the impressions of this PlayerLicense.

        Number of impressions recorded

        :param impressions: The impressions of this PlayerLicense.
        :type: int
        """

        if impressions is not None:
            if not isinstance(impressions, int):
                raise TypeError("Invalid type for `impressions`, type has to be `int`")

            self._impressions = impressions


    @property
    def max_impressions(self):
        """Gets the max_impressions of this PlayerLicense.

        Maximum number of impressions

        :return: The max_impressions of this PlayerLicense.
        :rtype: int
        """
        return self._max_impressions

    @max_impressions.setter
    def max_impressions(self, max_impressions):
        """Sets the max_impressions of this PlayerLicense.

        Maximum number of impressions

        :param max_impressions: The max_impressions of this PlayerLicense.
        :type: int
        """

        if max_impressions is not None:
            if not isinstance(max_impressions, int):
                raise TypeError("Invalid type for `max_impressions`, type has to be `int`")

            self._max_impressions = max_impressions


    @property
    def third_party_licensing_enabled(self):
        """Gets the third_party_licensing_enabled of this PlayerLicense.

        Flag if third party licensing is enabled

        :return: The third_party_licensing_enabled of this PlayerLicense.
        :rtype: bool
        """
        return self._third_party_licensing_enabled

    @third_party_licensing_enabled.setter
    def third_party_licensing_enabled(self, third_party_licensing_enabled):
        """Sets the third_party_licensing_enabled of this PlayerLicense.

        Flag if third party licensing is enabled

        :param third_party_licensing_enabled: The third_party_licensing_enabled of this PlayerLicense.
        :type: bool
        """

        if third_party_licensing_enabled is not None:
            if not isinstance(third_party_licensing_enabled, bool):
                raise TypeError("Invalid type for `third_party_licensing_enabled`, type has to be `bool`")

            self._third_party_licensing_enabled = third_party_licensing_enabled


    @property
    def domains(self):
        """Gets the domains of this PlayerLicense.

        Whitelisted domains

        :return: The domains of this PlayerLicense.
        :rtype: list[Domain]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this PlayerLicense.

        Whitelisted domains

        :param domains: The domains of this PlayerLicense.
        :type: list[Domain]
        """

        if domains is not None:
            if not isinstance(domains, list):
                raise TypeError("Invalid type for `domains`, type has to be `list[Domain]`")

            self._domains = domains

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(PlayerLicense, self).to_dict()

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
            if issubclass(PlayerLicense, dict):
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
        if not isinstance(other, PlayerLicense):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
