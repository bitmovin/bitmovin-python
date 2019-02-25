# coding: utf-8

from bitmovin_python.models.bitmovin_response import BitmovinResponse
import pprint
import six
from datetime import datetime
from enum import Enum


class BitmovinResource(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(BitmovinResource, self).openapi_types
        types.update({
            'name': 'str',
            'description': 'str',
            'created_at': 'datetime',
            'modified_at': 'datetime',
            'custom_data': 'dict(str, object)'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(BitmovinResource, self).attribute_map
        attributes.update({
            'name': 'name',
            'description': 'description',
            'created_at': 'createdAt',
            'modified_at': 'modifiedAt',
            'custom_data': 'customData'
        })
        return attributes

    def __init__(self, name=None, description=None, created_at=None, modified_at=None, custom_data=None, *args, **kwargs):
        super(BitmovinResource, self).__init__(*args, **kwargs)

        self._name = None
        self._description = None
        self._created_at = None
        self._modified_at = None
        self._custom_data = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if custom_data is not None:
            self.custom_data = custom_data

    @property
    def name(self):
        """Gets the name of this BitmovinResource.

        Name of the resource. Can be freely chosen by the user.

        :return: The name of this BitmovinResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BitmovinResource.

        Name of the resource. Can be freely chosen by the user.

        :param name: The name of this BitmovinResource.
        :type: str
        """

        if name is not None:
            if not isinstance(name, str):
                raise TypeError("Invalid type for `name`, type has to be `str`")

            self._name = name


    @property
    def description(self):
        """Gets the description of this BitmovinResource.

        Description of the resource. Can be freely chosen by the user.

        :return: The description of this BitmovinResource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BitmovinResource.

        Description of the resource. Can be freely chosen by the user.

        :param description: The description of this BitmovinResource.
        :type: str
        """

        if description is not None:
            if not isinstance(description, str):
                raise TypeError("Invalid type for `description`, type has to be `str`")

            self._description = description


    @property
    def created_at(self):
        """Gets the created_at of this BitmovinResource.

        Creation timestamp expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :return: The created_at of this BitmovinResource.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BitmovinResource.

        Creation timestamp expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :param created_at: The created_at of this BitmovinResource.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

            self._created_at = created_at


    @property
    def modified_at(self):
        """Gets the modified_at of this BitmovinResource.

        Modified timestamp expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :return: The modified_at of this BitmovinResource.
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this BitmovinResource.

        Modified timestamp expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :param modified_at: The modified_at of this BitmovinResource.
        :type: datetime
        """

        if modified_at is not None:
            if not isinstance(modified_at, datetime):
                raise TypeError("Invalid type for `modified_at`, type has to be `datetime`")

            self._modified_at = modified_at


    @property
    def custom_data(self):
        """Gets the custom_data of this BitmovinResource.

        User-specific meta data. This can hold anything.

        :return: The custom_data of this BitmovinResource.
        :rtype: dict(str, object)
        """
        return self._custom_data

    @custom_data.setter
    def custom_data(self, custom_data):
        """Sets the custom_data of this BitmovinResource.

        User-specific meta data. This can hold anything.

        :param custom_data: The custom_data of this BitmovinResource.
        :type: dict(str, object)
        """

        if custom_data is not None:
            if not isinstance(custom_data, dict):
                raise TypeError("Invalid type for `custom_data`, type has to be `dict(str, object)`")

            self._custom_data = custom_data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(BitmovinResource, self).to_dict()

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
            if issubclass(BitmovinResource, dict):
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
        if not isinstance(other, BitmovinResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
