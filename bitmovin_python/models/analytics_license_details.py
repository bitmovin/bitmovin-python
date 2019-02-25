# coding: utf-8

from bitmovin_python.models.analytics_license_domain import AnalyticsLicenseDomain
from bitmovin_python.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from enum import Enum


class AnalyticsLicenseDetails(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AnalyticsLicenseDetails, self).openapi_types
        types.update({
            'license_key': 'str',
            'max_datapoints': 'int',
            'datapoints': 'int',
            'domains': 'list[AnalyticsLicenseDomain]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AnalyticsLicenseDetails, self).attribute_map
        attributes.update({
            'license_key': 'licenseKey',
            'max_datapoints': 'maxDatapoints',
            'datapoints': 'datapoints',
            'domains': 'domains'
        })
        return attributes

    def __init__(self, license_key=None, max_datapoints=None, datapoints=None, domains=None, *args, **kwargs):
        super(AnalyticsLicenseDetails, self).__init__(*args, **kwargs)

        self._license_key = None
        self._max_datapoints = None
        self._datapoints = None
        self._domains = None
        self.discriminator = None

        self.license_key = license_key
        self.max_datapoints = max_datapoints
        self.datapoints = datapoints
        self.domains = domains

    @property
    def license_key(self):
        """Gets the license_key of this AnalyticsLicenseDetails.

        License Key

        :return: The license_key of this AnalyticsLicenseDetails.
        :rtype: str
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        """Sets the license_key of this AnalyticsLicenseDetails.

        License Key

        :param license_key: The license_key of this AnalyticsLicenseDetails.
        :type: str
        """

        if license_key is not None:
            if not isinstance(license_key, str):
                raise TypeError("Invalid type for `license_key`, type has to be `str`")

            self._license_key = license_key


    @property
    def max_datapoints(self):
        """Gets the max_datapoints of this AnalyticsLicenseDetails.

        Maximum number of datapoints

        :return: The max_datapoints of this AnalyticsLicenseDetails.
        :rtype: int
        """
        return self._max_datapoints

    @max_datapoints.setter
    def max_datapoints(self, max_datapoints):
        """Sets the max_datapoints of this AnalyticsLicenseDetails.

        Maximum number of datapoints

        :param max_datapoints: The max_datapoints of this AnalyticsLicenseDetails.
        :type: int
        """

        if max_datapoints is not None:
            if not isinstance(max_datapoints, int):
                raise TypeError("Invalid type for `max_datapoints`, type has to be `int`")

            self._max_datapoints = max_datapoints


    @property
    def datapoints(self):
        """Gets the datapoints of this AnalyticsLicenseDetails.

        Number of datapoints recorded

        :return: The datapoints of this AnalyticsLicenseDetails.
        :rtype: int
        """
        return self._datapoints

    @datapoints.setter
    def datapoints(self, datapoints):
        """Sets the datapoints of this AnalyticsLicenseDetails.

        Number of datapoints recorded

        :param datapoints: The datapoints of this AnalyticsLicenseDetails.
        :type: int
        """

        if datapoints is not None:
            if not isinstance(datapoints, int):
                raise TypeError("Invalid type for `datapoints`, type has to be `int`")

            self._datapoints = datapoints


    @property
    def domains(self):
        """Gets the domains of this AnalyticsLicenseDetails.

        Whitelisted domains

        :return: The domains of this AnalyticsLicenseDetails.
        :rtype: list[AnalyticsLicenseDomain]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this AnalyticsLicenseDetails.

        Whitelisted domains

        :param domains: The domains of this AnalyticsLicenseDetails.
        :type: list[AnalyticsLicenseDomain]
        """

        if domains is not None:
            if not isinstance(domains, list):
                raise TypeError("Invalid type for `domains`, type has to be `list[AnalyticsLicenseDomain]`")

            self._domains = domains

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AnalyticsLicenseDetails, self).to_dict()

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
            if issubclass(AnalyticsLicenseDetails, dict):
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
        if not isinstance(other, AnalyticsLicenseDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
