# coding: utf-8

from bitmovin_python.models.muxing_type import MuxingType
import pprint
import six
from datetime import datetime
from enum import Enum


class StatisticsPerMuxing(object):
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
            'stream_id': 'str',
            'muxing_id': 'str',
            'multiplicator': 'float',
            'encoded_bytes': 'int',
            'billable_minutes': 'float',
            'muxing_type': 'MuxingType'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'stream_id': 'streamId',
            'muxing_id': 'muxingId',
            'multiplicator': 'multiplicator',
            'encoded_bytes': 'encodedBytes',
            'billable_minutes': 'billableMinutes',
            'muxing_type': 'muxingType'
        }
        return attributes

    def __init__(self, stream_id=None, muxing_id=None, multiplicator=None, encoded_bytes=None, billable_minutes=None, muxing_type=None, *args, **kwargs):

        self._stream_id = None
        self._muxing_id = None
        self._multiplicator = None
        self._encoded_bytes = None
        self._billable_minutes = None
        self._muxing_type = None
        self.discriminator = None

        self.stream_id = stream_id
        self.muxing_id = muxing_id
        self.multiplicator = multiplicator
        self.encoded_bytes = encoded_bytes
        self.billable_minutes = billable_minutes
        self.muxing_type = muxing_type

    @property
    def stream_id(self):
        """Gets the stream_id of this StatisticsPerMuxing.

        ID of the stream

        :return: The stream_id of this StatisticsPerMuxing.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this StatisticsPerMuxing.

        ID of the stream

        :param stream_id: The stream_id of this StatisticsPerMuxing.
        :type: str
        """

        if stream_id is not None:
            if not isinstance(stream_id, str):
                raise TypeError("Invalid type for `stream_id`, type has to be `str`")

            self._stream_id = stream_id


    @property
    def muxing_id(self):
        """Gets the muxing_id of this StatisticsPerMuxing.

        ID of the muxing

        :return: The muxing_id of this StatisticsPerMuxing.
        :rtype: str
        """
        return self._muxing_id

    @muxing_id.setter
    def muxing_id(self, muxing_id):
        """Sets the muxing_id of this StatisticsPerMuxing.

        ID of the muxing

        :param muxing_id: The muxing_id of this StatisticsPerMuxing.
        :type: str
        """

        if muxing_id is not None:
            if not isinstance(muxing_id, str):
                raise TypeError("Invalid type for `muxing_id`, type has to be `str`")

            self._muxing_id = muxing_id


    @property
    def multiplicator(self):
        """Gets the multiplicator of this StatisticsPerMuxing.

        Multiplier for the encoded minutes. Depends on muxing type.

        :return: The multiplicator of this StatisticsPerMuxing.
        :rtype: float
        """
        return self._multiplicator

    @multiplicator.setter
    def multiplicator(self, multiplicator):
        """Sets the multiplicator of this StatisticsPerMuxing.

        Multiplier for the encoded minutes. Depends on muxing type.

        :param multiplicator: The multiplicator of this StatisticsPerMuxing.
        :type: float
        """

        if multiplicator is not None:
            if not isinstance(multiplicator, float):
                raise TypeError("Invalid type for `multiplicator`, type has to be `float`")

            self._multiplicator = multiplicator


    @property
    def encoded_bytes(self):
        """Gets the encoded_bytes of this StatisticsPerMuxing.

        Encoded bytes.

        :return: The encoded_bytes of this StatisticsPerMuxing.
        :rtype: int
        """
        return self._encoded_bytes

    @encoded_bytes.setter
    def encoded_bytes(self, encoded_bytes):
        """Sets the encoded_bytes of this StatisticsPerMuxing.

        Encoded bytes.

        :param encoded_bytes: The encoded_bytes of this StatisticsPerMuxing.
        :type: int
        """

        if encoded_bytes is not None:
            if not isinstance(encoded_bytes, int):
                raise TypeError("Invalid type for `encoded_bytes`, type has to be `int`")

            self._encoded_bytes = encoded_bytes


    @property
    def billable_minutes(self):
        """Gets the billable_minutes of this StatisticsPerMuxing.

        Resulting minutes you will be charged for.

        :return: The billable_minutes of this StatisticsPerMuxing.
        :rtype: float
        """
        return self._billable_minutes

    @billable_minutes.setter
    def billable_minutes(self, billable_minutes):
        """Sets the billable_minutes of this StatisticsPerMuxing.

        Resulting minutes you will be charged for.

        :param billable_minutes: The billable_minutes of this StatisticsPerMuxing.
        :type: float
        """

        if billable_minutes is not None:
            if not isinstance(billable_minutes, float):
                raise TypeError("Invalid type for `billable_minutes`, type has to be `float`")

            self._billable_minutes = billable_minutes


    @property
    def muxing_type(self):
        """Gets the muxing_type of this StatisticsPerMuxing.


        :return: The muxing_type of this StatisticsPerMuxing.
        :rtype: MuxingType
        """
        return self._muxing_type

    @muxing_type.setter
    def muxing_type(self, muxing_type):
        """Sets the muxing_type of this StatisticsPerMuxing.


        :param muxing_type: The muxing_type of this StatisticsPerMuxing.
        :type: MuxingType
        """

        if muxing_type is not None:
            if not isinstance(muxing_type, MuxingType):
                raise TypeError("Invalid type for `muxing_type`, type has to be `MuxingType`")

            self._muxing_type = muxing_type

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
            if issubclass(StatisticsPerMuxing, dict):
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
        if not isinstance(other, StatisticsPerMuxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
