# coding: utf-8

from bitmovin_python.models.folder_entry_type import FolderEntryType
import pprint
import six
from datetime import datetime
from enum import Enum


class FolderEntry(object):
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
            'type': 'FolderEntryType',
            'path': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'type': 'type',
            'path': 'path'
        }
        return attributes

    def __init__(self, type=None, path=None, *args, **kwargs):

        self._type = None
        self._path = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if path is not None:
            self.path = path

    @property
    def type(self):
        """Gets the type of this FolderEntry.


        :return: The type of this FolderEntry.
        :rtype: FolderEntryType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FolderEntry.


        :param type: The type of this FolderEntry.
        :type: FolderEntryType
        """

        if type is not None:
            if not isinstance(type, FolderEntryType):
                raise TypeError("Invalid type for `type`, type has to be `FolderEntryType`")

            self._type = type


    @property
    def path(self):
        """Gets the path of this FolderEntry.


        :return: The path of this FolderEntry.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FolderEntry.


        :param path: The path of this FolderEntry.
        :type: str
        """

        if path is not None:
            if not isinstance(path, str):
                raise TypeError("Invalid type for `path`, type has to be `str`")

            self._path = path

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
            if issubclass(FolderEntry, dict):
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
        if not isinstance(other, FolderEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
