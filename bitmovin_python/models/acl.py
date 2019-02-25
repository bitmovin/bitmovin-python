# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.permission import Permission
from bitmovin_python.models.policy import Policy
import pprint
import six
from datetime import datetime
from enum import Enum


class Acl(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Acl, self).openapi_types
        types.update({
            'resource': 'str',
            'policy': 'Policy',
            'permissions': 'list[Permission]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Acl, self).attribute_map
        attributes.update({
            'resource': 'resource',
            'policy': 'policy',
            'permissions': 'permissions'
        })
        return attributes

    def __init__(self, resource=None, policy=None, permissions=None, *args, **kwargs):
        super(Acl, self).__init__(*args, **kwargs)

        self._resource = None
        self._policy = None
        self._permissions = None
        self.discriminator = None

        self.resource = resource
        self.policy = policy
        self.permissions = permissions

    @property
    def resource(self):
        """Gets the resource of this Acl.

        Resource to define the permission for.

        :return: The resource of this Acl.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Acl.

        Resource to define the permission for.

        :param resource: The resource of this Acl.
        :type: str
        """

        if resource is not None:
            if not isinstance(resource, str):
                raise TypeError("Invalid type for `resource`, type has to be `str`")

            self._resource = resource


    @property
    def policy(self):
        """Gets the policy of this Acl.


        :return: The policy of this Acl.
        :rtype: Policy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this Acl.


        :param policy: The policy of this Acl.
        :type: Policy
        """

        if policy is not None:
            if not isinstance(policy, Policy):
                raise TypeError("Invalid type for `policy`, type has to be `Policy`")

            self._policy = policy


    @property
    def permissions(self):
        """Gets the permissions of this Acl.

        Permissions to assign.

        :return: The permissions of this Acl.
        :rtype: list[Permission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Acl.

        Permissions to assign.

        :param permissions: The permissions of this Acl.
        :type: list[Permission]
        """

        if permissions is not None:
            if not isinstance(permissions, list):
                raise TypeError("Invalid type for `permissions`, type has to be `list[Permission]`")

            self._permissions = permissions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Acl, self).to_dict()

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
            if issubclass(Acl, dict):
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
        if not isinstance(other, Acl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
