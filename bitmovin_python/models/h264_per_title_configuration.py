# coding: utf-8

from bitmovin_python.models.auto_representation import AutoRepresentation
from bitmovin_python.models.per_title_configuration import PerTitleConfiguration
from bitmovin_python.models.per_title_fixed_resolution_and_bitrate_configuration import PerTitleFixedResolutionAndBitrateConfiguration
import pprint
import six
from datetime import datetime
from enum import Enum


class H264PerTitleConfiguration(PerTitleConfiguration):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(H264PerTitleConfiguration, self).openapi_types
        types.update({
            'target_quality_crf': 'float',
            'codec_min_bitrate_factor': 'float',
            'codec_max_bitrate_factor': 'float',
            'codec_bufsize_factor': 'float'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(H264PerTitleConfiguration, self).attribute_map
        attributes.update({
            'target_quality_crf': 'targetQualityCrf',
            'codec_min_bitrate_factor': 'codecMinBitrateFactor',
            'codec_max_bitrate_factor': 'codecMaxBitrateFactor',
            'codec_bufsize_factor': 'codecBufsizeFactor'
        })
        return attributes

    def __init__(self, target_quality_crf=None, codec_min_bitrate_factor=None, codec_max_bitrate_factor=None, codec_bufsize_factor=None, *args, **kwargs):
        super(H264PerTitleConfiguration, self).__init__(*args, **kwargs)

        self._target_quality_crf = None
        self._codec_min_bitrate_factor = None
        self._codec_max_bitrate_factor = None
        self._codec_bufsize_factor = None
        self.discriminator = None

        if target_quality_crf is not None:
            self.target_quality_crf = target_quality_crf
        if codec_min_bitrate_factor is not None:
            self.codec_min_bitrate_factor = codec_min_bitrate_factor
        if codec_max_bitrate_factor is not None:
            self.codec_max_bitrate_factor = codec_max_bitrate_factor
        if codec_bufsize_factor is not None:
            self.codec_bufsize_factor = codec_bufsize_factor

    @property
    def target_quality_crf(self):
        """Gets the target_quality_crf of this H264PerTitleConfiguration.

        Desired target quality of the highest representation expressed as CRF value

        :return: The target_quality_crf of this H264PerTitleConfiguration.
        :rtype: float
        """
        return self._target_quality_crf

    @target_quality_crf.setter
    def target_quality_crf(self, target_quality_crf):
        """Sets the target_quality_crf of this H264PerTitleConfiguration.

        Desired target quality of the highest representation expressed as CRF value

        :param target_quality_crf: The target_quality_crf of this H264PerTitleConfiguration.
        :type: float
        """

        if target_quality_crf is not None:
            if not isinstance(target_quality_crf, float):
                raise TypeError("Invalid type for `target_quality_crf`, type has to be `float`")

            self._target_quality_crf = target_quality_crf


    @property
    def codec_min_bitrate_factor(self):
        """Gets the codec_min_bitrate_factor of this H264PerTitleConfiguration.

        This factor is used to calculate the minBitrate of the codec configuration for the generated representations as a multiple of the targetBitrate

        :return: The codec_min_bitrate_factor of this H264PerTitleConfiguration.
        :rtype: float
        """
        return self._codec_min_bitrate_factor

    @codec_min_bitrate_factor.setter
    def codec_min_bitrate_factor(self, codec_min_bitrate_factor):
        """Sets the codec_min_bitrate_factor of this H264PerTitleConfiguration.

        This factor is used to calculate the minBitrate of the codec configuration for the generated representations as a multiple of the targetBitrate

        :param codec_min_bitrate_factor: The codec_min_bitrate_factor of this H264PerTitleConfiguration.
        :type: float
        """

        if codec_min_bitrate_factor is not None:
            if not isinstance(codec_min_bitrate_factor, float):
                raise TypeError("Invalid type for `codec_min_bitrate_factor`, type has to be `float`")

            self._codec_min_bitrate_factor = codec_min_bitrate_factor


    @property
    def codec_max_bitrate_factor(self):
        """Gets the codec_max_bitrate_factor of this H264PerTitleConfiguration.

        This factor is used to calculate the maxBitrate of the codec configuration for the generated representations as a multiple of the targetBitrate

        :return: The codec_max_bitrate_factor of this H264PerTitleConfiguration.
        :rtype: float
        """
        return self._codec_max_bitrate_factor

    @codec_max_bitrate_factor.setter
    def codec_max_bitrate_factor(self, codec_max_bitrate_factor):
        """Sets the codec_max_bitrate_factor of this H264PerTitleConfiguration.

        This factor is used to calculate the maxBitrate of the codec configuration for the generated representations as a multiple of the targetBitrate

        :param codec_max_bitrate_factor: The codec_max_bitrate_factor of this H264PerTitleConfiguration.
        :type: float
        """

        if codec_max_bitrate_factor is not None:
            if not isinstance(codec_max_bitrate_factor, float):
                raise TypeError("Invalid type for `codec_max_bitrate_factor`, type has to be `float`")

            self._codec_max_bitrate_factor = codec_max_bitrate_factor


    @property
    def codec_bufsize_factor(self):
        """Gets the codec_bufsize_factor of this H264PerTitleConfiguration.

        This factor is used to calculate the bufsize of the codec configuration for the generated representations as a multiple of the targetBitrate

        :return: The codec_bufsize_factor of this H264PerTitleConfiguration.
        :rtype: float
        """
        return self._codec_bufsize_factor

    @codec_bufsize_factor.setter
    def codec_bufsize_factor(self, codec_bufsize_factor):
        """Sets the codec_bufsize_factor of this H264PerTitleConfiguration.

        This factor is used to calculate the bufsize of the codec configuration for the generated representations as a multiple of the targetBitrate

        :param codec_bufsize_factor: The codec_bufsize_factor of this H264PerTitleConfiguration.
        :type: float
        """

        if codec_bufsize_factor is not None:
            if not isinstance(codec_bufsize_factor, float):
                raise TypeError("Invalid type for `codec_bufsize_factor`, type has to be `float`")

            self._codec_bufsize_factor = codec_bufsize_factor

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(H264PerTitleConfiguration, self).to_dict()

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
            if issubclass(H264PerTitleConfiguration, dict):
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
        if not isinstance(other, H264PerTitleConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
