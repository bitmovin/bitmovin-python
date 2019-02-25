# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from enum import Enum


class CustomPlayerBuildDetails(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(CustomPlayerBuildDetails, self).openapi_types
        types.update({
            'player_version': 'str',
            'domains': 'list[str]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(CustomPlayerBuildDetails, self).attribute_map
        attributes.update({
            'player_version': 'playerVersion',
            'domains': 'domains'
        })
        return attributes

    def __init__(self, player_version=None, domains=None, *args, **kwargs):
        super(CustomPlayerBuildDetails, self).__init__(*args, **kwargs)

        self._player_version = None
        self._domains = None
        self.discriminator = None

        self.player_version = player_version
        self.domains = domains

    @property
    def player_version(self):
        """Gets the player_version of this CustomPlayerBuildDetails.

        The player version that should be used for the custom player build. If not set the 'latest' version is used. 

        :return: The player_version of this CustomPlayerBuildDetails.
        :rtype: str
        """
        return self._player_version

    @player_version.setter
    def player_version(self, player_version):
        """Sets the player_version of this CustomPlayerBuildDetails.

        The player version that should be used for the custom player build. If not set the 'latest' version is used. 

        :param player_version: The player_version of this CustomPlayerBuildDetails.
        :type: str
        """

        if player_version is not None:
            if not isinstance(player_version, str):
                raise TypeError("Invalid type for `player_version`, type has to be `str`")

            self._player_version = player_version


    @property
    def domains(self):
        """Gets the domains of this CustomPlayerBuildDetails.

        The domains that the player is locked to. If not set the player will only work with 'localhost'. Not more than 49 additional domains can be added. 

        :return: The domains of this CustomPlayerBuildDetails.
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this CustomPlayerBuildDetails.

        The domains that the player is locked to. If not set the player will only work with 'localhost'. Not more than 49 additional domains can be added. 

        :param domains: The domains of this CustomPlayerBuildDetails.
        :type: list[str]
        """

        if domains is not None:
            if not isinstance(domains, list):
                raise TypeError("Invalid type for `domains`, type has to be `list[str]`")

            self._domains = domains

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(CustomPlayerBuildDetails, self).to_dict()

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
            if issubclass(CustomPlayerBuildDetails, dict):
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
        if not isinstance(other, CustomPlayerBuildDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
