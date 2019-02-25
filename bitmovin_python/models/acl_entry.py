# coding: utf-8

from bitmovin_python.models.acl_permission import AclPermission
import pprint
import six
from datetime import datetime
from enum import Enum


class AclEntry(object):
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
            'scope': 'str',
            'permission': 'AclPermission'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'scope': 'scope',
            'permission': 'permission'
        }
        return attributes

    def __init__(self, scope=None, permission=None, *args, **kwargs):

        self._scope = None
        self._permission = None
        self.discriminator = None

        if scope is not None:
            self.scope = scope
        self.permission = permission

    @property
    def scope(self):
        """Gets the scope of this AclEntry.


        :return: The scope of this AclEntry.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this AclEntry.


        :param scope: The scope of this AclEntry.
        :type: str
        """

        if scope is not None:
            if not isinstance(scope, str):
                raise TypeError("Invalid type for `scope`, type has to be `str`")

            self._scope = scope


    @property
    def permission(self):
        """Gets the permission of this AclEntry.


        :return: The permission of this AclEntry.
        :rtype: AclPermission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this AclEntry.


        :param permission: The permission of this AclEntry.
        :type: AclPermission
        """

        if permission is not None:
            if not isinstance(permission, AclPermission):
                raise TypeError("Invalid type for `permission`, type has to be `AclPermission`")

            self._permission = permission

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
            if issubclass(AclEntry, dict):
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
        if not isinstance(other, AclEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
