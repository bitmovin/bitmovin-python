# coding: utf-8

from bitmovin_python.models.billable_encoding_feature_minutes import BillableEncodingFeatureMinutes
from bitmovin_python.models.billable_encoding_minutes import BillableEncodingMinutes
import pprint
import six
from datetime import datetime
from enum import Enum


class DailyStatistics(object):
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
            'bytes_encoded': 'int',
            'time_encoded': 'int',
            'billable_minutes': 'float',
            'label': 'datetime',
            'billable_encoding_minutes': 'list[BillableEncodingMinutes]',
            'billable_transmuxing_minutes': 'float',
            'billable_feature_minutes': 'list[BillableEncodingFeatureMinutes]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'date': 'date',
            'bytes_encoded': 'bytesEncoded',
            'time_encoded': 'timeEncoded',
            'billable_minutes': 'billableMinutes',
            'label': 'label',
            'billable_encoding_minutes': 'billableEncodingMinutes',
            'billable_transmuxing_minutes': 'billableTransmuxingMinutes',
            'billable_feature_minutes': 'billableFeatureMinutes'
        }
        return attributes

    def __init__(self, date=None, bytes_encoded=None, time_encoded=None, billable_minutes=None, label=None, billable_encoding_minutes=None, billable_transmuxing_minutes=None, billable_feature_minutes=None, *args, **kwargs):

        self._date = None
        self._bytes_encoded = None
        self._time_encoded = None
        self._billable_minutes = None
        self._label = None
        self._billable_encoding_minutes = None
        self._billable_transmuxing_minutes = None
        self._billable_feature_minutes = None
        self.discriminator = None

        self.date = date
        self.bytes_encoded = bytes_encoded
        self.time_encoded = time_encoded
        if billable_minutes is not None:
            self.billable_minutes = billable_minutes
        if label is not None:
            self.label = label
        if billable_encoding_minutes is not None:
            self.billable_encoding_minutes = billable_encoding_minutes
        if billable_transmuxing_minutes is not None:
            self.billable_transmuxing_minutes = billable_transmuxing_minutes
        if billable_feature_minutes is not None:
            self.billable_feature_minutes = billable_feature_minutes

    @property
    def date(self):
        """Gets the date of this DailyStatistics.

        Date for the shown data. Format: yyyy-MM-dd

        :return: The date of this DailyStatistics.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this DailyStatistics.

        Date for the shown data. Format: yyyy-MM-dd

        :param date: The date of this DailyStatistics.
        :type: datetime
        """

        if date is not None:
            if not isinstance(date, datetime):
                raise TypeError("Invalid type for `date`, type has to be `datetime`")

            self._date = date


    @property
    def bytes_encoded(self):
        """Gets the bytes_encoded of this DailyStatistics.

        Bytes encoded.

        :return: The bytes_encoded of this DailyStatistics.
        :rtype: int
        """
        return self._bytes_encoded

    @bytes_encoded.setter
    def bytes_encoded(self, bytes_encoded):
        """Sets the bytes_encoded of this DailyStatistics.

        Bytes encoded.

        :param bytes_encoded: The bytes_encoded of this DailyStatistics.
        :type: int
        """

        if bytes_encoded is not None:
            if not isinstance(bytes_encoded, int):
                raise TypeError("Invalid type for `bytes_encoded`, type has to be `int`")

            self._bytes_encoded = bytes_encoded


    @property
    def time_encoded(self):
        """Gets the time_encoded of this DailyStatistics.

        Time in seconds encoded for this day.

        :return: The time_encoded of this DailyStatistics.
        :rtype: int
        """
        return self._time_encoded

    @time_encoded.setter
    def time_encoded(self, time_encoded):
        """Sets the time_encoded of this DailyStatistics.

        Time in seconds encoded for this day.

        :param time_encoded: The time_encoded of this DailyStatistics.
        :type: int
        """

        if time_encoded is not None:
            if not isinstance(time_encoded, int):
                raise TypeError("Invalid type for `time_encoded`, type has to be `int`")

            self._time_encoded = time_encoded


    @property
    def billable_minutes(self):
        """Gets the billable_minutes of this DailyStatistics.

        The billable minutes.

        :return: The billable_minutes of this DailyStatistics.
        :rtype: float
        """
        return self._billable_minutes

    @billable_minutes.setter
    def billable_minutes(self, billable_minutes):
        """Sets the billable_minutes of this DailyStatistics.

        The billable minutes.

        :param billable_minutes: The billable_minutes of this DailyStatistics.
        :type: float
        """

        if billable_minutes is not None:
            if not isinstance(billable_minutes, float):
                raise TypeError("Invalid type for `billable_minutes`, type has to be `float`")

            self._billable_minutes = billable_minutes


    @property
    def label(self):
        """Gets the label of this DailyStatistics.

        Label identifier.

        :return: The label of this DailyStatistics.
        :rtype: datetime
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DailyStatistics.

        Label identifier.

        :param label: The label of this DailyStatistics.
        :type: datetime
        """

        if label is not None:
            if not isinstance(label, datetime):
                raise TypeError("Invalid type for `label`, type has to be `datetime`")

            self._label = label


    @property
    def billable_encoding_minutes(self):
        """Gets the billable_encoding_minutes of this DailyStatistics.

        Billable minutes for each encoding configuration.

        :return: The billable_encoding_minutes of this DailyStatistics.
        :rtype: list[BillableEncodingMinutes]
        """
        return self._billable_encoding_minutes

    @billable_encoding_minutes.setter
    def billable_encoding_minutes(self, billable_encoding_minutes):
        """Sets the billable_encoding_minutes of this DailyStatistics.

        Billable minutes for each encoding configuration.

        :param billable_encoding_minutes: The billable_encoding_minutes of this DailyStatistics.
        :type: list[BillableEncodingMinutes]
        """

        if billable_encoding_minutes is not None:
            if not isinstance(billable_encoding_minutes, list):
                raise TypeError("Invalid type for `billable_encoding_minutes`, type has to be `list[BillableEncodingMinutes]`")

            self._billable_encoding_minutes = billable_encoding_minutes


    @property
    def billable_transmuxing_minutes(self):
        """Gets the billable_transmuxing_minutes of this DailyStatistics.

        Billable minutes for muxings.

        :return: The billable_transmuxing_minutes of this DailyStatistics.
        :rtype: float
        """
        return self._billable_transmuxing_minutes

    @billable_transmuxing_minutes.setter
    def billable_transmuxing_minutes(self, billable_transmuxing_minutes):
        """Sets the billable_transmuxing_minutes of this DailyStatistics.

        Billable minutes for muxings.

        :param billable_transmuxing_minutes: The billable_transmuxing_minutes of this DailyStatistics.
        :type: float
        """

        if billable_transmuxing_minutes is not None:
            if not isinstance(billable_transmuxing_minutes, float):
                raise TypeError("Invalid type for `billable_transmuxing_minutes`, type has to be `float`")

            self._billable_transmuxing_minutes = billable_transmuxing_minutes


    @property
    def billable_feature_minutes(self):
        """Gets the billable_feature_minutes of this DailyStatistics.

        Billable minutes for features

        :return: The billable_feature_minutes of this DailyStatistics.
        :rtype: list[BillableEncodingFeatureMinutes]
        """
        return self._billable_feature_minutes

    @billable_feature_minutes.setter
    def billable_feature_minutes(self, billable_feature_minutes):
        """Sets the billable_feature_minutes of this DailyStatistics.

        Billable minutes for features

        :param billable_feature_minutes: The billable_feature_minutes of this DailyStatistics.
        :type: list[BillableEncodingFeatureMinutes]
        """

        if billable_feature_minutes is not None:
            if not isinstance(billable_feature_minutes, list):
                raise TypeError("Invalid type for `billable_feature_minutes`, type has to be `list[BillableEncodingFeatureMinutes]`")

            self._billable_feature_minutes = billable_feature_minutes

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
            if issubclass(DailyStatistics, dict):
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
        if not isinstance(other, DailyStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
