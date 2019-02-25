# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class PaginationResponse(object):
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
            'total_count': 'int',
            'offset': 'int',
            'limit': 'int',
            'previous': 'str',
            'next': 'str',
            'items': 'list[object]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'total_count': 'totalCount',
            'offset': 'offset',
            'limit': 'limit',
            'previous': 'previous',
            'next': 'next',
            'items': 'items'
        }
        return attributes

    def __init__(self, total_count=None, offset=None, limit=None, previous=None, next=None, items=None, *args, **kwargs):

        self._total_count = None
        self._offset = None
        self._limit = None
        self._previous = None
        self._next = None
        self._items = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if previous is not None:
            self.previous = previous
        if next is not None:
            self.next = next
        if items is not None:
            self.items = items

    @property
    def total_count(self):
        """Gets the total_count of this PaginationResponse.


        :return: The total_count of this PaginationResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this PaginationResponse.


        :param total_count: The total_count of this PaginationResponse.
        :type: int
        """

        if total_count is not None:
            if not isinstance(total_count, int):
                raise TypeError("Invalid type for `total_count`, type has to be `int`")

            self._total_count = total_count


    @property
    def offset(self):
        """Gets the offset of this PaginationResponse.


        :return: The offset of this PaginationResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PaginationResponse.


        :param offset: The offset of this PaginationResponse.
        :type: int
        """

        if offset is not None:
            if not isinstance(offset, int):
                raise TypeError("Invalid type for `offset`, type has to be `int`")

            self._offset = offset


    @property
    def limit(self):
        """Gets the limit of this PaginationResponse.


        :return: The limit of this PaginationResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PaginationResponse.


        :param limit: The limit of this PaginationResponse.
        :type: int
        """

        if limit is not None:
            if not isinstance(limit, int):
                raise TypeError("Invalid type for `limit`, type has to be `int`")

            self._limit = limit


    @property
    def previous(self):
        """Gets the previous of this PaginationResponse.


        :return: The previous of this PaginationResponse.
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this PaginationResponse.


        :param previous: The previous of this PaginationResponse.
        :type: str
        """

        if previous is not None:
            if not isinstance(previous, str):
                raise TypeError("Invalid type for `previous`, type has to be `str`")

            self._previous = previous


    @property
    def next(self):
        """Gets the next of this PaginationResponse.


        :return: The next of this PaginationResponse.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this PaginationResponse.


        :param next: The next of this PaginationResponse.
        :type: str
        """

        if next is not None:
            if not isinstance(next, str):
                raise TypeError("Invalid type for `next`, type has to be `str`")

            self._next = next


    @property
    def items(self):
        """Gets the items of this PaginationResponse.


        :return: The items of this PaginationResponse.
        :rtype: list[object]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PaginationResponse.


        :param items: The items of this PaginationResponse.
        :type: list[object]
        """

        if items is not None:
            if not isinstance(items, list):
                raise TypeError("Invalid type for `items`, type has to be `list[object]`")

            self._items = items

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
            if issubclass(PaginationResponse, dict):
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
        if not isinstance(other, PaginationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
