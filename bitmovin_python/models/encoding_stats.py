# coding: utf-8

from bitmovin_python.models.billable_encoding_feature_minutes import BillableEncodingFeatureMinutes
from bitmovin_python.models.billable_encoding_minutes import BillableEncodingMinutes
from bitmovin_python.models.statistics_per_muxing import StatisticsPerMuxing
from bitmovin_python.models.statistics_per_stream import StatisticsPerStream
import pprint
import six
from datetime import datetime
from enum import Enum


class EncodingStats(object):
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
            'encoding_id': 'str',
            'bytes_encoded': 'int',
            'time_encoded': 'int',
            'downloaded_size': 'int',
            'billable_minutes': 'float',
            'billable_encoding_minutes': 'list[BillableEncodingMinutes]',
            'billable_transmuxing_minutes': 'float',
            'billable_feature_minutes': 'float',
            'streams': 'list[StatisticsPerStream]',
            'muxings': 'list[StatisticsPerMuxing]',
            'features': 'list[BillableEncodingFeatureMinutes]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'date': 'date',
            'encoding_id': 'encodingId',
            'bytes_encoded': 'bytesEncoded',
            'time_encoded': 'timeEncoded',
            'downloaded_size': 'downloadedSize',
            'billable_minutes': 'billableMinutes',
            'billable_encoding_minutes': 'billableEncodingMinutes',
            'billable_transmuxing_minutes': 'billableTransmuxingMinutes',
            'billable_feature_minutes': 'billableFeatureMinutes',
            'streams': 'streams',
            'muxings': 'muxings',
            'features': 'features'
        }
        return attributes

    def __init__(self, date=None, encoding_id=None, bytes_encoded=None, time_encoded=None, downloaded_size=None, billable_minutes=None, billable_encoding_minutes=None, billable_transmuxing_minutes=None, billable_feature_minutes=None, streams=None, muxings=None, features=None, *args, **kwargs):

        self._date = None
        self._encoding_id = None
        self._bytes_encoded = None
        self._time_encoded = None
        self._downloaded_size = None
        self._billable_minutes = None
        self._billable_encoding_minutes = None
        self._billable_transmuxing_minutes = None
        self._billable_feature_minutes = None
        self._streams = None
        self._muxings = None
        self._features = None
        self.discriminator = None

        if date is not None:
            self.date = date
        self.encoding_id = encoding_id
        if bytes_encoded is not None:
            self.bytes_encoded = bytes_encoded
        if time_encoded is not None:
            self.time_encoded = time_encoded
        if downloaded_size is not None:
            self.downloaded_size = downloaded_size
        if billable_minutes is not None:
            self.billable_minutes = billable_minutes
        if billable_encoding_minutes is not None:
            self.billable_encoding_minutes = billable_encoding_minutes
        self.billable_transmuxing_minutes = billable_transmuxing_minutes
        if billable_feature_minutes is not None:
            self.billable_feature_minutes = billable_feature_minutes
        self.streams = streams
        self.muxings = muxings
        if features is not None:
            self.features = features

    @property
    def date(self):
        """Gets the date of this EncodingStats.

        Date, format. yyyy-MM-dd

        :return: The date of this EncodingStats.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this EncodingStats.

        Date, format. yyyy-MM-dd

        :param date: The date of this EncodingStats.
        :type: datetime
        """

        if date is not None:
            if not isinstance(date, datetime):
                raise TypeError("Invalid type for `date`, type has to be `datetime`")

            self._date = date


    @property
    def encoding_id(self):
        """Gets the encoding_id of this EncodingStats.

        The id of the encoding

        :return: The encoding_id of this EncodingStats.
        :rtype: str
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        """Sets the encoding_id of this EncodingStats.

        The id of the encoding

        :param encoding_id: The encoding_id of this EncodingStats.
        :type: str
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, str):
                raise TypeError("Invalid type for `encoding_id`, type has to be `str`")

            self._encoding_id = encoding_id


    @property
    def bytes_encoded(self):
        """Gets the bytes_encoded of this EncodingStats.

        Total bytes encoded

        :return: The bytes_encoded of this EncodingStats.
        :rtype: int
        """
        return self._bytes_encoded

    @bytes_encoded.setter
    def bytes_encoded(self, bytes_encoded):
        """Sets the bytes_encoded of this EncodingStats.

        Total bytes encoded

        :param bytes_encoded: The bytes_encoded of this EncodingStats.
        :type: int
        """

        if bytes_encoded is not None:
            if not isinstance(bytes_encoded, int):
                raise TypeError("Invalid type for `bytes_encoded`, type has to be `int`")

            self._bytes_encoded = bytes_encoded


    @property
    def time_encoded(self):
        """Gets the time_encoded of this EncodingStats.

        Total time encoded

        :return: The time_encoded of this EncodingStats.
        :rtype: int
        """
        return self._time_encoded

    @time_encoded.setter
    def time_encoded(self, time_encoded):
        """Sets the time_encoded of this EncodingStats.

        Total time encoded

        :param time_encoded: The time_encoded of this EncodingStats.
        :type: int
        """

        if time_encoded is not None:
            if not isinstance(time_encoded, int):
                raise TypeError("Invalid type for `time_encoded`, type has to be `int`")

            self._time_encoded = time_encoded


    @property
    def downloaded_size(self):
        """Gets the downloaded_size of this EncodingStats.

        Downloaded size of the input file

        :return: The downloaded_size of this EncodingStats.
        :rtype: int
        """
        return self._downloaded_size

    @downloaded_size.setter
    def downloaded_size(self, downloaded_size):
        """Sets the downloaded_size of this EncodingStats.

        Downloaded size of the input file

        :param downloaded_size: The downloaded_size of this EncodingStats.
        :type: int
        """

        if downloaded_size is not None:
            if not isinstance(downloaded_size, int):
                raise TypeError("Invalid type for `downloaded_size`, type has to be `int`")

            self._downloaded_size = downloaded_size


    @property
    def billable_minutes(self):
        """Gets the billable_minutes of this EncodingStats.

        Billable minutes

        :return: The billable_minutes of this EncodingStats.
        :rtype: float
        """
        return self._billable_minutes

    @billable_minutes.setter
    def billable_minutes(self, billable_minutes):
        """Sets the billable_minutes of this EncodingStats.

        Billable minutes

        :param billable_minutes: The billable_minutes of this EncodingStats.
        :type: float
        """

        if billable_minutes is not None:
            if not isinstance(billable_minutes, float):
                raise TypeError("Invalid type for `billable_minutes`, type has to be `float`")

            self._billable_minutes = billable_minutes


    @property
    def billable_encoding_minutes(self):
        """Gets the billable_encoding_minutes of this EncodingStats.

        Detailed statistics per stream

        :return: The billable_encoding_minutes of this EncodingStats.
        :rtype: list[BillableEncodingMinutes]
        """
        return self._billable_encoding_minutes

    @billable_encoding_minutes.setter
    def billable_encoding_minutes(self, billable_encoding_minutes):
        """Sets the billable_encoding_minutes of this EncodingStats.

        Detailed statistics per stream

        :param billable_encoding_minutes: The billable_encoding_minutes of this EncodingStats.
        :type: list[BillableEncodingMinutes]
        """

        if billable_encoding_minutes is not None:
            if not isinstance(billable_encoding_minutes, list):
                raise TypeError("Invalid type for `billable_encoding_minutes`, type has to be `list[BillableEncodingMinutes]`")

            self._billable_encoding_minutes = billable_encoding_minutes


    @property
    def billable_transmuxing_minutes(self):
        """Gets the billable_transmuxing_minutes of this EncodingStats.

        Billable transmuxing minutes

        :return: The billable_transmuxing_minutes of this EncodingStats.
        :rtype: float
        """
        return self._billable_transmuxing_minutes

    @billable_transmuxing_minutes.setter
    def billable_transmuxing_minutes(self, billable_transmuxing_minutes):
        """Sets the billable_transmuxing_minutes of this EncodingStats.

        Billable transmuxing minutes

        :param billable_transmuxing_minutes: The billable_transmuxing_minutes of this EncodingStats.
        :type: float
        """

        if billable_transmuxing_minutes is not None:
            if not isinstance(billable_transmuxing_minutes, float):
                raise TypeError("Invalid type for `billable_transmuxing_minutes`, type has to be `float`")

            self._billable_transmuxing_minutes = billable_transmuxing_minutes


    @property
    def billable_feature_minutes(self):
        """Gets the billable_feature_minutes of this EncodingStats.

        Billable feature minutes

        :return: The billable_feature_minutes of this EncodingStats.
        :rtype: float
        """
        return self._billable_feature_minutes

    @billable_feature_minutes.setter
    def billable_feature_minutes(self, billable_feature_minutes):
        """Sets the billable_feature_minutes of this EncodingStats.

        Billable feature minutes

        :param billable_feature_minutes: The billable_feature_minutes of this EncodingStats.
        :type: float
        """

        if billable_feature_minutes is not None:
            if not isinstance(billable_feature_minutes, float):
                raise TypeError("Invalid type for `billable_feature_minutes`, type has to be `float`")

            self._billable_feature_minutes = billable_feature_minutes


    @property
    def streams(self):
        """Gets the streams of this EncodingStats.

        Detailed statistics per stream

        :return: The streams of this EncodingStats.
        :rtype: list[StatisticsPerStream]
        """
        return self._streams

    @streams.setter
    def streams(self, streams):
        """Sets the streams of this EncodingStats.

        Detailed statistics per stream

        :param streams: The streams of this EncodingStats.
        :type: list[StatisticsPerStream]
        """

        if streams is not None:
            if not isinstance(streams, list):
                raise TypeError("Invalid type for `streams`, type has to be `list[StatisticsPerStream]`")

            self._streams = streams


    @property
    def muxings(self):
        """Gets the muxings of this EncodingStats.

        Detailed statistics per muxing

        :return: The muxings of this EncodingStats.
        :rtype: list[StatisticsPerMuxing]
        """
        return self._muxings

    @muxings.setter
    def muxings(self, muxings):
        """Sets the muxings of this EncodingStats.

        Detailed statistics per muxing

        :param muxings: The muxings of this EncodingStats.
        :type: list[StatisticsPerMuxing]
        """

        if muxings is not None:
            if not isinstance(muxings, list):
                raise TypeError("Invalid type for `muxings`, type has to be `list[StatisticsPerMuxing]`")

            self._muxings = muxings


    @property
    def features(self):
        """Gets the features of this EncodingStats.

        Detailed statistics per feature

        :return: The features of this EncodingStats.
        :rtype: list[BillableEncodingFeatureMinutes]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this EncodingStats.

        Detailed statistics per feature

        :param features: The features of this EncodingStats.
        :type: list[BillableEncodingFeatureMinutes]
        """

        if features is not None:
            if not isinstance(features, list):
                raise TypeError("Invalid type for `features`, type has to be `list[BillableEncodingFeatureMinutes]`")

            self._features = features

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
            if issubclass(EncodingStats, dict):
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
        if not isinstance(other, EncodingStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
