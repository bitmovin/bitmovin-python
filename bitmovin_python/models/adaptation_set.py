# coding: utf-8

from bitmovin_python.models.accessibility import Accessibility
from bitmovin_python.models.adaptation_set_role import AdaptationSetRole
from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.custom_attribute import CustomAttribute
import pprint
import six
from datetime import datetime
from enum import Enum


class AdaptationSet(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AdaptationSet, self).openapi_types
        types.update({
            'custom_attributes': 'list[CustomAttribute]',
            'roles': 'list[AdaptationSetRole]',
            'accessibilities': 'list[Accessibility]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AdaptationSet, self).attribute_map
        attributes.update({
            'custom_attributes': 'customAttributes',
            'roles': 'roles',
            'accessibilities': 'accessibilities'
        })
        return attributes

    def __init__(self, custom_attributes=None, roles=None, accessibilities=None, *args, **kwargs):
        super(AdaptationSet, self).__init__(*args, **kwargs)

        self._custom_attributes = None
        self._roles = None
        self._accessibilities = None
        self.discriminator = None

        if custom_attributes is not None:
            self.custom_attributes = custom_attributes
        if roles is not None:
            self.roles = roles
        if accessibilities is not None:
            self.accessibilities = accessibilities

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this AdaptationSet.

        Custom adaptation set attributes

        :return: The custom_attributes of this AdaptationSet.
        :rtype: list[CustomAttribute]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this AdaptationSet.

        Custom adaptation set attributes

        :param custom_attributes: The custom_attributes of this AdaptationSet.
        :type: list[CustomAttribute]
        """

        if custom_attributes is not None:
            if not isinstance(custom_attributes, list):
                raise TypeError("Invalid type for `custom_attributes`, type has to be `list[CustomAttribute]`")

            self._custom_attributes = custom_attributes


    @property
    def roles(self):
        """Gets the roles of this AdaptationSet.

        Roles of the adaptation set

        :return: The roles of this AdaptationSet.
        :rtype: list[AdaptationSetRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this AdaptationSet.

        Roles of the adaptation set

        :param roles: The roles of this AdaptationSet.
        :type: list[AdaptationSetRole]
        """

        if roles is not None:
            if not isinstance(roles, list):
                raise TypeError("Invalid type for `roles`, type has to be `list[AdaptationSetRole]`")

            self._roles = roles


    @property
    def accessibilities(self):
        """Gets the accessibilities of this AdaptationSet.

        Provide signaling of CEA 607 and CEA 708

        :return: The accessibilities of this AdaptationSet.
        :rtype: list[Accessibility]
        """
        return self._accessibilities

    @accessibilities.setter
    def accessibilities(self, accessibilities):
        """Sets the accessibilities of this AdaptationSet.

        Provide signaling of CEA 607 and CEA 708

        :param accessibilities: The accessibilities of this AdaptationSet.
        :type: list[Accessibility]
        """

        if accessibilities is not None:
            if not isinstance(accessibilities, list):
                raise TypeError("Invalid type for `accessibilities`, type has to be `list[Accessibility]`")

            self._accessibilities = accessibilities

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AdaptationSet, self).to_dict()

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
            if issubclass(AdaptationSet, dict):
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
        if not isinstance(other, AdaptationSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
