# coding: utf-8

from bitmovin_python.models.player_third_party_licensing_error_action import PlayerThirdPartyLicensingErrorAction
import pprint
import six
from datetime import datetime
from enum import Enum


class PlayerThirdPartyLicensing(object):
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
            'license_check_server': 'str',
            'license_check_timeout': 'int',
            'error_action': 'PlayerThirdPartyLicensingErrorAction',
            'timeout_action': 'PlayerThirdPartyLicensingErrorAction'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'license_check_server': 'licenseCheckServer',
            'license_check_timeout': 'licenseCheckTimeout',
            'error_action': 'errorAction',
            'timeout_action': 'timeoutAction'
        }
        return attributes

    def __init__(self, license_check_server=None, license_check_timeout=None, error_action=None, timeout_action=None, *args, **kwargs):

        self._license_check_server = None
        self._license_check_timeout = None
        self._error_action = None
        self._timeout_action = None
        self.discriminator = None

        self.license_check_server = license_check_server
        self.license_check_timeout = license_check_timeout
        self.error_action = error_action
        self.timeout_action = timeout_action

    @property
    def license_check_server(self):
        """Gets the license_check_server of this PlayerThirdPartyLicensing.

        URL to your license check server

        :return: The license_check_server of this PlayerThirdPartyLicensing.
        :rtype: str
        """
        return self._license_check_server

    @license_check_server.setter
    def license_check_server(self, license_check_server):
        """Sets the license_check_server of this PlayerThirdPartyLicensing.

        URL to your license check server

        :param license_check_server: The license_check_server of this PlayerThirdPartyLicensing.
        :type: str
        """

        if license_check_server is not None:
            if not isinstance(license_check_server, str):
                raise TypeError("Invalid type for `license_check_server`, type has to be `str`")

            self._license_check_server = license_check_server


    @property
    def license_check_timeout(self):
        """Gets the license_check_timeout of this PlayerThirdPartyLicensing.

        Timeout in ms

        :return: The license_check_timeout of this PlayerThirdPartyLicensing.
        :rtype: int
        """
        return self._license_check_timeout

    @license_check_timeout.setter
    def license_check_timeout(self, license_check_timeout):
        """Sets the license_check_timeout of this PlayerThirdPartyLicensing.

        Timeout in ms

        :param license_check_timeout: The license_check_timeout of this PlayerThirdPartyLicensing.
        :type: int
        """

        if license_check_timeout is not None:
            if license_check_timeout is not None and license_check_timeout > 2000:
                raise ValueError("Invalid value for `license_check_timeout`, must be a value less than or equal to `2000`")
            if license_check_timeout is not None and license_check_timeout < 100:
                raise ValueError("Invalid value for `license_check_timeout`, must be a value greater than or equal to `100`")
            if not isinstance(license_check_timeout, int):
                raise TypeError("Invalid type for `license_check_timeout`, type has to be `int`")

            self._license_check_timeout = license_check_timeout


    @property
    def error_action(self):
        """Gets the error_action of this PlayerThirdPartyLicensing.

        Specify if the Licensing Request should fail or not on Third Party Licensing Error

        :return: The error_action of this PlayerThirdPartyLicensing.
        :rtype: PlayerThirdPartyLicensingErrorAction
        """
        return self._error_action

    @error_action.setter
    def error_action(self, error_action):
        """Sets the error_action of this PlayerThirdPartyLicensing.

        Specify if the Licensing Request should fail or not on Third Party Licensing Error

        :param error_action: The error_action of this PlayerThirdPartyLicensing.
        :type: PlayerThirdPartyLicensingErrorAction
        """

        if error_action is not None:
            if not isinstance(error_action, PlayerThirdPartyLicensingErrorAction):
                raise TypeError("Invalid type for `error_action`, type has to be `PlayerThirdPartyLicensingErrorAction`")

            self._error_action = error_action


    @property
    def timeout_action(self):
        """Gets the timeout_action of this PlayerThirdPartyLicensing.

        Specify if the Licensing Request should fail or not on Third Party Licensing timeout

        :return: The timeout_action of this PlayerThirdPartyLicensing.
        :rtype: PlayerThirdPartyLicensingErrorAction
        """
        return self._timeout_action

    @timeout_action.setter
    def timeout_action(self, timeout_action):
        """Sets the timeout_action of this PlayerThirdPartyLicensing.

        Specify if the Licensing Request should fail or not on Third Party Licensing timeout

        :param timeout_action: The timeout_action of this PlayerThirdPartyLicensing.
        :type: PlayerThirdPartyLicensingErrorAction
        """

        if timeout_action is not None:
            if not isinstance(timeout_action, PlayerThirdPartyLicensingErrorAction):
                raise TypeError("Invalid type for `timeout_action`, type has to be `PlayerThirdPartyLicensingErrorAction`")

            self._timeout_action = timeout_action

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
            if issubclass(PlayerThirdPartyLicensing, dict):
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
        if not isinstance(other, PlayerThirdPartyLicensing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
