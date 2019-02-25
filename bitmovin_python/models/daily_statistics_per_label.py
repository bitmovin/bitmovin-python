# coding: utf-8

from bitmovin_python.models.daily_statistics import DailyStatistics
import pprint
import six
from datetime import datetime
from enum import Enum


class DailyStatisticsPerLabel(object):
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
            'date': 'datetime',
            'labels': 'list[DailyStatistics]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'date': 'date',
            'labels': 'labels'
        }
        return attributes

    def __init__(self, date=None, labels=None, *args, **kwargs):

        self._date = None
        self._labels = None
        self.discriminator = None

        self.date = date
        self.labels = labels

    @property
    def date(self):
        """Gets the date of this DailyStatisticsPerLabel.

        Date, format. yyyy-MM-dd

        :return: The date of this DailyStatisticsPerLabel.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this DailyStatisticsPerLabel.

        Date, format. yyyy-MM-dd

        :param date: The date of this DailyStatisticsPerLabel.
        :type: datetime
        """

        if date is not None:
            if not isinstance(date, datetime):
                raise TypeError("Invalid type for `date`, type has to be `datetime`")

            self._date = date


    @property
    def labels(self):
        """Gets the labels of this DailyStatisticsPerLabel.

        List of labels and their aggregated statistics

        :return: The labels of this DailyStatisticsPerLabel.
        :rtype: list[DailyStatistics]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this DailyStatisticsPerLabel.

        List of labels and their aggregated statistics

        :param labels: The labels of this DailyStatisticsPerLabel.
        :type: list[DailyStatistics]
        """

        if labels is not None:
            if not isinstance(labels, list):
                raise TypeError("Invalid type for `labels`, type has to be `list[DailyStatistics]`")

            self._labels = labels

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
            if issubclass(DailyStatisticsPerLabel, dict):
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
        if not isinstance(other, DailyStatisticsPerLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
