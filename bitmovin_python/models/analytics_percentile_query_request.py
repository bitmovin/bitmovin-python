# coding: utf-8

from bitmovin_python.models.analytics_filter import AnalyticsFilter
from bitmovin_python.models.analytics_interval import AnalyticsInterval
from bitmovin_python.models.analytics_order_by_entry import AnalyticsOrderByEntry
from bitmovin_python.models.analytics_query_request import AnalyticsQueryRequest
import pprint
import six
from datetime import datetime
from enum import Enum


class AnalyticsPercentileQueryRequest(AnalyticsQueryRequest):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AnalyticsPercentileQueryRequest, self).openapi_types
        types.update({
            'percentile': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AnalyticsPercentileQueryRequest, self).attribute_map
        attributes.update({
            'percentile': 'percentile'
        })
        return attributes

    def __init__(self, percentile=None, *args, **kwargs):
        super(AnalyticsPercentileQueryRequest, self).__init__(*args, **kwargs)

        self._percentile = None
        self.discriminator = None

        if percentile is not None:
            self.percentile = percentile

    @property
    def percentile(self):
        """Gets the percentile of this AnalyticsPercentileQueryRequest.

        The percentage (0-99) used for percentile queries.

        :return: The percentile of this AnalyticsPercentileQueryRequest.
        :rtype: int
        """
        return self._percentile

    @percentile.setter
    def percentile(self, percentile):
        """Sets the percentile of this AnalyticsPercentileQueryRequest.

        The percentage (0-99) used for percentile queries.

        :param percentile: The percentile of this AnalyticsPercentileQueryRequest.
        :type: int
        """

        if percentile is not None:
            if not isinstance(percentile, int):
                raise TypeError("Invalid type for `percentile`, type has to be `int`")

            self._percentile = percentile

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AnalyticsPercentileQueryRequest, self).to_dict()

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
            if issubclass(AnalyticsPercentileQueryRequest, dict):
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
        if not isinstance(other, AnalyticsPercentileQueryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
