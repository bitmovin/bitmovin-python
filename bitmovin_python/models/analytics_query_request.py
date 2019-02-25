# coding: utf-8

from bitmovin_python.models.analytics_filter import AnalyticsFilter
from bitmovin_python.models.analytics_interval import AnalyticsInterval
from bitmovin_python.models.analytics_order_by_entry import AnalyticsOrderByEntry
from bitmovin_python.models.analytics_query_timeframe import AnalyticsQueryTimeframe
import pprint
import six
from datetime import datetime
from enum import Enum


class AnalyticsQueryRequest(AnalyticsQueryTimeframe):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AnalyticsQueryRequest, self).openapi_types
        types.update({
            'license_key': 'str',
            'filters': 'list[AnalyticsFilter]',
            'order_by': 'list[AnalyticsOrderByEntry]',
            'dimension': 'str',
            'interval': 'list[AnalyticsInterval]',
            'group_by': 'list[str]',
            'limit': 'int',
            'offset': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AnalyticsQueryRequest, self).attribute_map
        attributes.update({
            'license_key': 'licenseKey',
            'filters': 'filters',
            'order_by': 'orderBy',
            'dimension': 'dimension',
            'interval': 'interval',
            'group_by': 'groupBy',
            'limit': 'limit',
            'offset': 'offset'
        })
        return attributes

    def __init__(self, license_key=None, filters=None, order_by=None, dimension=None, interval=None, group_by=None, limit=None, offset=None, *args, **kwargs):
        super(AnalyticsQueryRequest, self).__init__(*args, **kwargs)

        self._license_key = None
        self._filters = None
        self._order_by = None
        self._dimension = None
        self._interval = None
        self._group_by = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if license_key is not None:
            self.license_key = license_key
        if filters is not None:
            self.filters = filters
        if order_by is not None:
            self.order_by = order_by
        self.dimension = dimension
        if interval is not None:
            self.interval = interval
        if group_by is not None:
            self.group_by = group_by
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def license_key(self):
        """Gets the license_key of this AnalyticsQueryRequest.

        Analytics license key

        :return: The license_key of this AnalyticsQueryRequest.
        :rtype: str
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        """Sets the license_key of this AnalyticsQueryRequest.

        Analytics license key

        :param license_key: The license_key of this AnalyticsQueryRequest.
        :type: str
        """

        if license_key is not None:
            if not isinstance(license_key, str):
                raise TypeError("Invalid type for `license_key`, type has to be `str`")

            self._license_key = license_key


    @property
    def filters(self):
        """Gets the filters of this AnalyticsQueryRequest.


        :return: The filters of this AnalyticsQueryRequest.
        :rtype: list[AnalyticsFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this AnalyticsQueryRequest.


        :param filters: The filters of this AnalyticsQueryRequest.
        :type: list[AnalyticsFilter]
        """

        if filters is not None:
            if not isinstance(filters, list):
                raise TypeError("Invalid type for `filters`, type has to be `list[AnalyticsFilter]`")

            self._filters = filters


    @property
    def order_by(self):
        """Gets the order_by of this AnalyticsQueryRequest.


        :return: The order_by of this AnalyticsQueryRequest.
        :rtype: list[AnalyticsOrderByEntry]
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this AnalyticsQueryRequest.


        :param order_by: The order_by of this AnalyticsQueryRequest.
        :type: list[AnalyticsOrderByEntry]
        """

        if order_by is not None:
            if not isinstance(order_by, list):
                raise TypeError("Invalid type for `order_by`, type has to be `list[AnalyticsOrderByEntry]`")

            self._order_by = order_by


    @property
    def dimension(self):
        """Gets the dimension of this AnalyticsQueryRequest.


        :return: The dimension of this AnalyticsQueryRequest.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this AnalyticsQueryRequest.


        :param dimension: The dimension of this AnalyticsQueryRequest.
        :type: str
        """

        if dimension is not None:
            if not isinstance(dimension, str):
                raise TypeError("Invalid type for `dimension`, type has to be `str`")

            self._dimension = dimension


    @property
    def interval(self):
        """Gets the interval of this AnalyticsQueryRequest.


        :return: The interval of this AnalyticsQueryRequest.
        :rtype: list[AnalyticsInterval]
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this AnalyticsQueryRequest.


        :param interval: The interval of this AnalyticsQueryRequest.
        :type: list[AnalyticsInterval]
        """

        if interval is not None:
            if not isinstance(interval, list):
                raise TypeError("Invalid type for `interval`, type has to be `list[AnalyticsInterval]`")

            self._interval = interval


    @property
    def group_by(self):
        """Gets the group_by of this AnalyticsQueryRequest.


        :return: The group_by of this AnalyticsQueryRequest.
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this AnalyticsQueryRequest.


        :param group_by: The group_by of this AnalyticsQueryRequest.
        :type: list[str]
        """

        if group_by is not None:
            if not isinstance(group_by, list):
                raise TypeError("Invalid type for `group_by`, type has to be `list[str]`")

            self._group_by = group_by


    @property
    def limit(self):
        """Gets the limit of this AnalyticsQueryRequest.

        Maximum number of rows returned (max. 150)

        :return: The limit of this AnalyticsQueryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this AnalyticsQueryRequest.

        Maximum number of rows returned (max. 150)

        :param limit: The limit of this AnalyticsQueryRequest.
        :type: int
        """

        if limit is not None:
            if not isinstance(limit, int):
                raise TypeError("Invalid type for `limit`, type has to be `int`")

            self._limit = limit


    @property
    def offset(self):
        """Gets the offset of this AnalyticsQueryRequest.

        Offset of data

        :return: The offset of this AnalyticsQueryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this AnalyticsQueryRequest.

        Offset of data

        :param offset: The offset of this AnalyticsQueryRequest.
        :type: int
        """

        if offset is not None:
            if not isinstance(offset, int):
                raise TypeError("Invalid type for `offset`, type has to be `int`")

            self._offset = offset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AnalyticsQueryRequest, self).to_dict()

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
            if issubclass(AnalyticsQueryRequest, dict):
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
        if not isinstance(other, AnalyticsQueryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
