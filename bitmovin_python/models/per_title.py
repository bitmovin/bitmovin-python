# coding: utf-8

from bitmovin_python.models.h264_per_title_configuration import H264PerTitleConfiguration
from bitmovin_python.models.h265_per_title_configuration import H265PerTitleConfiguration
from bitmovin_python.models.vp9_per_title_configuration import Vp9PerTitleConfiguration
import pprint
import six
from datetime import datetime
from enum import Enum


class PerTitle(object):
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
            'h264_configuration': 'H264PerTitleConfiguration',
            'h265_configuration': 'H265PerTitleConfiguration',
            'vp9_configuration': 'Vp9PerTitleConfiguration'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'h264_configuration': 'h264Configuration',
            'h265_configuration': 'h265Configuration',
            'vp9_configuration': 'vp9Configuration'
        }
        return attributes

    def __init__(self, h264_configuration=None, h265_configuration=None, vp9_configuration=None, *args, **kwargs):

        self._h264_configuration = None
        self._h265_configuration = None
        self._vp9_configuration = None
        self.discriminator = None

        if h264_configuration is not None:
            self.h264_configuration = h264_configuration
        if h265_configuration is not None:
            self.h265_configuration = h265_configuration
        if vp9_configuration is not None:
            self.vp9_configuration = vp9_configuration

    @property
    def h264_configuration(self):
        """Gets the h264_configuration of this PerTitle.

        Per-Title configuration for H264

        :return: The h264_configuration of this PerTitle.
        :rtype: H264PerTitleConfiguration
        """
        return self._h264_configuration

    @h264_configuration.setter
    def h264_configuration(self, h264_configuration):
        """Sets the h264_configuration of this PerTitle.

        Per-Title configuration for H264

        :param h264_configuration: The h264_configuration of this PerTitle.
        :type: H264PerTitleConfiguration
        """

        if h264_configuration is not None:
            if not isinstance(h264_configuration, H264PerTitleConfiguration):
                raise TypeError("Invalid type for `h264_configuration`, type has to be `H264PerTitleConfiguration`")

            self._h264_configuration = h264_configuration


    @property
    def h265_configuration(self):
        """Gets the h265_configuration of this PerTitle.

        Per-Title configuration for H265

        :return: The h265_configuration of this PerTitle.
        :rtype: H265PerTitleConfiguration
        """
        return self._h265_configuration

    @h265_configuration.setter
    def h265_configuration(self, h265_configuration):
        """Sets the h265_configuration of this PerTitle.

        Per-Title configuration for H265

        :param h265_configuration: The h265_configuration of this PerTitle.
        :type: H265PerTitleConfiguration
        """

        if h265_configuration is not None:
            if not isinstance(h265_configuration, H265PerTitleConfiguration):
                raise TypeError("Invalid type for `h265_configuration`, type has to be `H265PerTitleConfiguration`")

            self._h265_configuration = h265_configuration


    @property
    def vp9_configuration(self):
        """Gets the vp9_configuration of this PerTitle.

        Per-Title configuration for VP9

        :return: The vp9_configuration of this PerTitle.
        :rtype: Vp9PerTitleConfiguration
        """
        return self._vp9_configuration

    @vp9_configuration.setter
    def vp9_configuration(self, vp9_configuration):
        """Sets the vp9_configuration of this PerTitle.

        Per-Title configuration for VP9

        :param vp9_configuration: The vp9_configuration of this PerTitle.
        :type: Vp9PerTitleConfiguration
        """

        if vp9_configuration is not None:
            if not isinstance(vp9_configuration, Vp9PerTitleConfiguration):
                raise TypeError("Invalid type for `vp9_configuration`, type has to be `Vp9PerTitleConfiguration`")

            self._vp9_configuration = vp9_configuration

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
            if issubclass(PerTitle, dict):
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
        if not isinstance(other, PerTitle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
