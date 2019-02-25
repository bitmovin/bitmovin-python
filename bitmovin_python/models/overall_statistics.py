# coding: utf-8

from bitmovin_python.models.storage_statistics import StorageStatistics
import pprint
import six
from datetime import datetime
from enum import Enum


class OverallStatistics(object):
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
            'bytes_stored_total': 'int',
            'bytes_transferred_total': 'int',
            'storages': 'list[StorageStatistics]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'bytes_stored_total': 'bytesStoredTotal',
            'bytes_transferred_total': 'bytesTransferredTotal',
            'storages': 'storages'
        }
        return attributes

    def __init__(self, bytes_stored_total=None, bytes_transferred_total=None, storages=None, *args, **kwargs):

        self._bytes_stored_total = None
        self._bytes_transferred_total = None
        self._storages = None
        self.discriminator = None

        if bytes_stored_total is not None:
            self.bytes_stored_total = bytes_stored_total
        if bytes_transferred_total is not None:
            self.bytes_transferred_total = bytes_transferred_total
        if storages is not None:
            self.storages = storages

    @property
    def bytes_stored_total(self):
        """Gets the bytes_stored_total of this OverallStatistics.


        :return: The bytes_stored_total of this OverallStatistics.
        :rtype: int
        """
        return self._bytes_stored_total

    @bytes_stored_total.setter
    def bytes_stored_total(self, bytes_stored_total):
        """Sets the bytes_stored_total of this OverallStatistics.


        :param bytes_stored_total: The bytes_stored_total of this OverallStatistics.
        :type: int
        """

        if bytes_stored_total is not None:
            if not isinstance(bytes_stored_total, int):
                raise TypeError("Invalid type for `bytes_stored_total`, type has to be `int`")

            self._bytes_stored_total = bytes_stored_total


    @property
    def bytes_transferred_total(self):
        """Gets the bytes_transferred_total of this OverallStatistics.


        :return: The bytes_transferred_total of this OverallStatistics.
        :rtype: int
        """
        return self._bytes_transferred_total

    @bytes_transferred_total.setter
    def bytes_transferred_total(self, bytes_transferred_total):
        """Sets the bytes_transferred_total of this OverallStatistics.


        :param bytes_transferred_total: The bytes_transferred_total of this OverallStatistics.
        :type: int
        """

        if bytes_transferred_total is not None:
            if not isinstance(bytes_transferred_total, int):
                raise TypeError("Invalid type for `bytes_transferred_total`, type has to be `int`")

            self._bytes_transferred_total = bytes_transferred_total


    @property
    def storages(self):
        """Gets the storages of this OverallStatistics.


        :return: The storages of this OverallStatistics.
        :rtype: list[StorageStatistics]
        """
        return self._storages

    @storages.setter
    def storages(self, storages):
        """Sets the storages of this OverallStatistics.


        :param storages: The storages of this OverallStatistics.
        :type: list[StorageStatistics]
        """

        if storages is not None:
            if not isinstance(storages, list):
                raise TypeError("Invalid type for `storages`, type has to be `list[StorageStatistics]`")

            self._storages = storages

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
            if issubclass(OverallStatistics, dict):
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
        if not isinstance(other, OverallStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
