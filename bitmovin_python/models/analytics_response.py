# coding: utf-8

from bitmovin_python.models.analytics_column_label import AnalyticsColumnLabel
import pprint
import six
from datetime import datetime
from enum import Enum


class AnalyticsResponse(object):
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
            'rows': 'list[object]',
            'row_count': 'int',
            'column_labels': 'list[AnalyticsColumnLabel]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'rows': 'rows',
            'row_count': 'rowCount',
            'column_labels': 'columnLabels'
        }
        return attributes

    def __init__(self, rows=None, row_count=None, column_labels=None, *args, **kwargs):

        self._rows = None
        self._row_count = None
        self._column_labels = None
        self.discriminator = None

        if rows is not None:
            self.rows = rows
        if row_count is not None:
            self.row_count = row_count
        if column_labels is not None:
            self.column_labels = column_labels

    @property
    def rows(self):
        """Gets the rows of this AnalyticsResponse.


        :return: The rows of this AnalyticsResponse.
        :rtype: list[object]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this AnalyticsResponse.


        :param rows: The rows of this AnalyticsResponse.
        :type: list[object]
        """

        if rows is not None:
            if not isinstance(rows, list):
                raise TypeError("Invalid type for `rows`, type has to be `list[object]`")

            self._rows = rows


    @property
    def row_count(self):
        """Gets the row_count of this AnalyticsResponse.

        Number of rows returned

        :return: The row_count of this AnalyticsResponse.
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """Sets the row_count of this AnalyticsResponse.

        Number of rows returned

        :param row_count: The row_count of this AnalyticsResponse.
        :type: int
        """

        if row_count is not None:
            if not isinstance(row_count, int):
                raise TypeError("Invalid type for `row_count`, type has to be `int`")

            self._row_count = row_count


    @property
    def column_labels(self):
        """Gets the column_labels of this AnalyticsResponse.


        :return: The column_labels of this AnalyticsResponse.
        :rtype: list[AnalyticsColumnLabel]
        """
        return self._column_labels

    @column_labels.setter
    def column_labels(self, column_labels):
        """Sets the column_labels of this AnalyticsResponse.


        :param column_labels: The column_labels of this AnalyticsResponse.
        :type: list[AnalyticsColumnLabel]
        """

        if column_labels is not None:
            if not isinstance(column_labels, list):
                raise TypeError("Invalid type for `column_labels`, type has to be `list[AnalyticsColumnLabel]`")

            self._column_labels = column_labels

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
            if issubclass(AnalyticsResponse, dict):
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
        if not isinstance(other, AnalyticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
