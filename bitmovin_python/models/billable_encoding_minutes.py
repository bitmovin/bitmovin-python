# coding: utf-8

from bitmovin_python.models.billable_encoding_minutes_details import BillableEncodingMinutesDetails
from bitmovin_python.models.codec_config_type import CodecConfigType
from bitmovin_python.models.encoding_mode import EncodingMode
from bitmovin_python.models.psnr_per_stream_mode import PsnrPerStreamMode
from bitmovin_python.models.statistics_per_title_stream import StatisticsPerTitleStream
import pprint
import six
from datetime import datetime
from enum import Enum


class BillableEncodingMinutes(object):
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
            'encoding_mode': 'EncodingMode',
            'codec': 'CodecConfigType',
            'per_title_result_stream': 'StatisticsPerTitleStream',
            'psnr_mode': 'PsnrPerStreamMode',
            'billable_minutes_details': 'list[BillableEncodingMinutesDetails]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'encoding_mode': 'encodingMode',
            'codec': 'codec',
            'per_title_result_stream': 'perTitleResultStream',
            'psnr_mode': 'psnrMode',
            'billable_minutes_details': 'billableMinutesDetails'
        }
        return attributes

    def __init__(self, encoding_mode=None, codec=None, per_title_result_stream=None, psnr_mode=None, billable_minutes_details=None, *args, **kwargs):

        self._encoding_mode = None
        self._codec = None
        self._per_title_result_stream = None
        self._psnr_mode = None
        self._billable_minutes_details = None
        self.discriminator = None

        if encoding_mode is not None:
            self.encoding_mode = encoding_mode
        self.codec = codec
        if per_title_result_stream is not None:
            self.per_title_result_stream = per_title_result_stream
        if psnr_mode is not None:
            self.psnr_mode = psnr_mode
        self.billable_minutes_details = billable_minutes_details

    @property
    def encoding_mode(self):
        """Gets the encoding_mode of this BillableEncodingMinutes.


        :return: The encoding_mode of this BillableEncodingMinutes.
        :rtype: EncodingMode
        """
        return self._encoding_mode

    @encoding_mode.setter
    def encoding_mode(self, encoding_mode):
        """Sets the encoding_mode of this BillableEncodingMinutes.


        :param encoding_mode: The encoding_mode of this BillableEncodingMinutes.
        :type: EncodingMode
        """

        if encoding_mode is not None:
            if not isinstance(encoding_mode, EncodingMode):
                raise TypeError("Invalid type for `encoding_mode`, type has to be `EncodingMode`")

            self._encoding_mode = encoding_mode


    @property
    def codec(self):
        """Gets the codec of this BillableEncodingMinutes.


        :return: The codec of this BillableEncodingMinutes.
        :rtype: CodecConfigType
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this BillableEncodingMinutes.


        :param codec: The codec of this BillableEncodingMinutes.
        :type: CodecConfigType
        """

        if codec is not None:
            if not isinstance(codec, CodecConfigType):
                raise TypeError("Invalid type for `codec`, type has to be `CodecConfigType`")

            self._codec = codec


    @property
    def per_title_result_stream(self):
        """Gets the per_title_result_stream of this BillableEncodingMinutes.


        :return: The per_title_result_stream of this BillableEncodingMinutes.
        :rtype: StatisticsPerTitleStream
        """
        return self._per_title_result_stream

    @per_title_result_stream.setter
    def per_title_result_stream(self, per_title_result_stream):
        """Sets the per_title_result_stream of this BillableEncodingMinutes.


        :param per_title_result_stream: The per_title_result_stream of this BillableEncodingMinutes.
        :type: StatisticsPerTitleStream
        """

        if per_title_result_stream is not None:
            if not isinstance(per_title_result_stream, StatisticsPerTitleStream):
                raise TypeError("Invalid type for `per_title_result_stream`, type has to be `StatisticsPerTitleStream`")

            self._per_title_result_stream = per_title_result_stream


    @property
    def psnr_mode(self):
        """Gets the psnr_mode of this BillableEncodingMinutes.


        :return: The psnr_mode of this BillableEncodingMinutes.
        :rtype: PsnrPerStreamMode
        """
        return self._psnr_mode

    @psnr_mode.setter
    def psnr_mode(self, psnr_mode):
        """Sets the psnr_mode of this BillableEncodingMinutes.


        :param psnr_mode: The psnr_mode of this BillableEncodingMinutes.
        :type: PsnrPerStreamMode
        """

        if psnr_mode is not None:
            if not isinstance(psnr_mode, PsnrPerStreamMode):
                raise TypeError("Invalid type for `psnr_mode`, type has to be `PsnrPerStreamMode`")

            self._psnr_mode = psnr_mode


    @property
    def billable_minutes_details(self):
        """Gets the billable_minutes_details of this BillableEncodingMinutes.

        Details about billable minutes for each resolution category

        :return: The billable_minutes_details of this BillableEncodingMinutes.
        :rtype: list[BillableEncodingMinutesDetails]
        """
        return self._billable_minutes_details

    @billable_minutes_details.setter
    def billable_minutes_details(self, billable_minutes_details):
        """Sets the billable_minutes_details of this BillableEncodingMinutes.

        Details about billable minutes for each resolution category

        :param billable_minutes_details: The billable_minutes_details of this BillableEncodingMinutes.
        :type: list[BillableEncodingMinutesDetails]
        """

        if billable_minutes_details is not None:
            if not isinstance(billable_minutes_details, list):
                raise TypeError("Invalid type for `billable_minutes_details`, type has to be `list[BillableEncodingMinutesDetails]`")

            self._billable_minutes_details = billable_minutes_details

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
            if issubclass(BillableEncodingMinutes, dict):
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
        if not isinstance(other, BillableEncodingMinutes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
