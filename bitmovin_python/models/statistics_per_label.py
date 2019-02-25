# coding: utf-8

from bitmovin_python.models.billable_encoding_feature_minutes import BillableEncodingFeatureMinutes
from bitmovin_python.models.billable_encoding_minutes import BillableEncodingMinutes
from bitmovin_python.models.statistics import Statistics
import pprint
import six
from datetime import datetime
from enum import Enum


class StatisticsPerLabel(Statistics):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(StatisticsPerLabel, self).openapi_types
        types.update({
            'label': 'str',
            'billable_minutes': 'float',
            'billable_encoding_minutes': 'list[BillableEncodingMinutes]',
            'billable_transmuxing_minutes': 'float',
            'billable_feature_minutes': 'list[BillableEncodingFeatureMinutes]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(StatisticsPerLabel, self).attribute_map
        attributes.update({
            'label': 'label',
            'billable_minutes': 'billableMinutes',
            'billable_encoding_minutes': 'billableEncodingMinutes',
            'billable_transmuxing_minutes': 'billableTransmuxingMinutes',
            'billable_feature_minutes': 'billableFeatureMinutes'
        })
        return attributes

    def __init__(self, label=None, billable_minutes=None, billable_encoding_minutes=None, billable_transmuxing_minutes=None, billable_feature_minutes=None, *args, **kwargs):
        super(StatisticsPerLabel, self).__init__(*args, **kwargs)

        self._label = None
        self._billable_minutes = None
        self._billable_encoding_minutes = None
        self._billable_transmuxing_minutes = None
        self._billable_feature_minutes = None
        self.discriminator = None

        self.label = label
        if billable_minutes is not None:
            self.billable_minutes = billable_minutes
        if billable_encoding_minutes is not None:
            self.billable_encoding_minutes = billable_encoding_minutes
        if billable_transmuxing_minutes is not None:
            self.billable_transmuxing_minutes = billable_transmuxing_minutes
        if billable_feature_minutes is not None:
            self.billable_feature_minutes = billable_feature_minutes

    @property
    def label(self):
        """Gets the label of this StatisticsPerLabel.

        An optional error message, when the event is in error state (occurs at event: ERROR)

        :return: The label of this StatisticsPerLabel.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this StatisticsPerLabel.

        An optional error message, when the event is in error state (occurs at event: ERROR)

        :param label: The label of this StatisticsPerLabel.
        :type: str
        """

        if label is not None:
            if not isinstance(label, str):
                raise TypeError("Invalid type for `label`, type has to be `str`")

            self._label = label


    @property
    def billable_minutes(self):
        """Gets the billable_minutes of this StatisticsPerLabel.

        The billable minutes.

        :return: The billable_minutes of this StatisticsPerLabel.
        :rtype: float
        """
        return self._billable_minutes

    @billable_minutes.setter
    def billable_minutes(self, billable_minutes):
        """Sets the billable_minutes of this StatisticsPerLabel.

        The billable minutes.

        :param billable_minutes: The billable_minutes of this StatisticsPerLabel.
        :type: float
        """

        if billable_minutes is not None:
            if not isinstance(billable_minutes, float):
                raise TypeError("Invalid type for `billable_minutes`, type has to be `float`")

            self._billable_minutes = billable_minutes


    @property
    def billable_encoding_minutes(self):
        """Gets the billable_encoding_minutes of this StatisticsPerLabel.

        Billable minutes for each encoding configuration

        :return: The billable_encoding_minutes of this StatisticsPerLabel.
        :rtype: list[BillableEncodingMinutes]
        """
        return self._billable_encoding_minutes

    @billable_encoding_minutes.setter
    def billable_encoding_minutes(self, billable_encoding_minutes):
        """Sets the billable_encoding_minutes of this StatisticsPerLabel.

        Billable minutes for each encoding configuration

        :param billable_encoding_minutes: The billable_encoding_minutes of this StatisticsPerLabel.
        :type: list[BillableEncodingMinutes]
        """

        if billable_encoding_minutes is not None:
            if not isinstance(billable_encoding_minutes, list):
                raise TypeError("Invalid type for `billable_encoding_minutes`, type has to be `list[BillableEncodingMinutes]`")

            self._billable_encoding_minutes = billable_encoding_minutes


    @property
    def billable_transmuxing_minutes(self):
        """Gets the billable_transmuxing_minutes of this StatisticsPerLabel.

        Billable minutes for muxings.

        :return: The billable_transmuxing_minutes of this StatisticsPerLabel.
        :rtype: float
        """
        return self._billable_transmuxing_minutes

    @billable_transmuxing_minutes.setter
    def billable_transmuxing_minutes(self, billable_transmuxing_minutes):
        """Sets the billable_transmuxing_minutes of this StatisticsPerLabel.

        Billable minutes for muxings.

        :param billable_transmuxing_minutes: The billable_transmuxing_minutes of this StatisticsPerLabel.
        :type: float
        """

        if billable_transmuxing_minutes is not None:
            if not isinstance(billable_transmuxing_minutes, float):
                raise TypeError("Invalid type for `billable_transmuxing_minutes`, type has to be `float`")

            self._billable_transmuxing_minutes = billable_transmuxing_minutes


    @property
    def billable_feature_minutes(self):
        """Gets the billable_feature_minutes of this StatisticsPerLabel.

        Billable minutes for features

        :return: The billable_feature_minutes of this StatisticsPerLabel.
        :rtype: list[BillableEncodingFeatureMinutes]
        """
        return self._billable_feature_minutes

    @billable_feature_minutes.setter
    def billable_feature_minutes(self, billable_feature_minutes):
        """Sets the billable_feature_minutes of this StatisticsPerLabel.

        Billable minutes for features

        :param billable_feature_minutes: The billable_feature_minutes of this StatisticsPerLabel.
        :type: list[BillableEncodingFeatureMinutes]
        """

        if billable_feature_minutes is not None:
            if not isinstance(billable_feature_minutes, list):
                raise TypeError("Invalid type for `billable_feature_minutes`, type has to be `list[BillableEncodingFeatureMinutes]`")

            self._billable_feature_minutes = billable_feature_minutes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(StatisticsPerLabel, self).to_dict()

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
            if issubclass(StatisticsPerLabel, dict):
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
        if not isinstance(other, StatisticsPerLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
