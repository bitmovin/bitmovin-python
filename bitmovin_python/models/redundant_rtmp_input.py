# coding: utf-8

from bitmovin_python.models.input import Input
from bitmovin_python.models.input_type import InputType
from bitmovin_python.models.rtmp_ingest_point import RtmpIngestPoint
import pprint
import six
from datetime import datetime
from enum import Enum


class RedundantRtmpInput(Input):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(RedundantRtmpInput, self).openapi_types
        types.update({
            'delay_threshold': 'float',
            'ingest_points': 'list[RtmpIngestPoint]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(RedundantRtmpInput, self).attribute_map
        attributes.update({
            'delay_threshold': 'delayThreshold',
            'ingest_points': 'ingestPoints'
        })
        return attributes

    def __init__(self, delay_threshold=30, ingest_points=None, *args, **kwargs):
        super(RedundantRtmpInput, self).__init__(*args, **kwargs)

        self._delay_threshold = None
        self._ingest_points = None
        self.discriminator = None

        if delay_threshold is not None:
            self.delay_threshold = delay_threshold
        self.ingest_points = ingest_points

    @property
    def delay_threshold(self):
        """Gets the delay_threshold of this RedundantRtmpInput.

        When there is no input signal present and this threshold in seconds is reached it will switch to another ingest point

        :return: The delay_threshold of this RedundantRtmpInput.
        :rtype: float
        """
        return self._delay_threshold

    @delay_threshold.setter
    def delay_threshold(self, delay_threshold):
        """Sets the delay_threshold of this RedundantRtmpInput.

        When there is no input signal present and this threshold in seconds is reached it will switch to another ingest point

        :param delay_threshold: The delay_threshold of this RedundantRtmpInput.
        :type: float
        """

        if delay_threshold is not None:
            if not isinstance(delay_threshold, float):
                raise TypeError("Invalid type for `delay_threshold`, type has to be `float`")

            self._delay_threshold = delay_threshold


    @property
    def ingest_points(self):
        """Gets the ingest_points of this RedundantRtmpInput.


        :return: The ingest_points of this RedundantRtmpInput.
        :rtype: list[RtmpIngestPoint]
        """
        return self._ingest_points

    @ingest_points.setter
    def ingest_points(self, ingest_points):
        """Sets the ingest_points of this RedundantRtmpInput.


        :param ingest_points: The ingest_points of this RedundantRtmpInput.
        :type: list[RtmpIngestPoint]
        """

        if ingest_points is not None:
            if not isinstance(ingest_points, list):
                raise TypeError("Invalid type for `ingest_points`, type has to be `list[RtmpIngestPoint]`")

            self._ingest_points = ingest_points

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(RedundantRtmpInput, self).to_dict()

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
            if issubclass(RedundantRtmpInput, dict):
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
        if not isinstance(other, RedundantRtmpInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
