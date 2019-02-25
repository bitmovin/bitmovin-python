# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class StorageStatistics(object):
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
            'bytes_stored': 'int',
            'bytes_transferred': 'int',
            'storage': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'bytes_stored': 'bytesStored',
            'bytes_transferred': 'bytesTransferred',
            'storage': 'storage'
        }
        return attributes

    def __init__(self, bytes_stored=None, bytes_transferred=None, storage=None, *args, **kwargs):

        self._bytes_stored = None
        self._bytes_transferred = None
        self._storage = None
        self.discriminator = None

        if bytes_stored is not None:
            self.bytes_stored = bytes_stored
        if bytes_transferred is not None:
            self.bytes_transferred = bytes_transferred
        if storage is not None:
            self.storage = storage

    @property
    def bytes_stored(self):
        """Gets the bytes_stored of this StorageStatistics.


        :return: The bytes_stored of this StorageStatistics.
        :rtype: int
        """
        return self._bytes_stored

    @bytes_stored.setter
    def bytes_stored(self, bytes_stored):
        """Sets the bytes_stored of this StorageStatistics.


        :param bytes_stored: The bytes_stored of this StorageStatistics.
        :type: int
        """

        if bytes_stored is not None:
            if not isinstance(bytes_stored, int):
                raise TypeError("Invalid type for `bytes_stored`, type has to be `int`")

            self._bytes_stored = bytes_stored


    @property
    def bytes_transferred(self):
        """Gets the bytes_transferred of this StorageStatistics.


        :return: The bytes_transferred of this StorageStatistics.
        :rtype: int
        """
        return self._bytes_transferred

    @bytes_transferred.setter
    def bytes_transferred(self, bytes_transferred):
        """Sets the bytes_transferred of this StorageStatistics.


        :param bytes_transferred: The bytes_transferred of this StorageStatistics.
        :type: int
        """

        if bytes_transferred is not None:
            if not isinstance(bytes_transferred, int):
                raise TypeError("Invalid type for `bytes_transferred`, type has to be `int`")

            self._bytes_transferred = bytes_transferred


    @property
    def storage(self):
        """Gets the storage of this StorageStatistics.


        :return: The storage of this StorageStatistics.
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this StorageStatistics.


        :param storage: The storage of this StorageStatistics.
        :type: str
        """

        if storage is not None:
            if not isinstance(storage, str):
                raise TypeError("Invalid type for `storage`, type has to be `str`")

            self._storage = storage

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
            if issubclass(StorageStatistics, dict):
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
        if not isinstance(other, StorageStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
