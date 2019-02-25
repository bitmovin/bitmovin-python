# coding: utf-8

from bitmovin_python.models.stream_per_title_fixed_resolution_and_bitrate_settings import StreamPerTitleFixedResolutionAndBitrateSettings
import pprint
import six
from datetime import datetime
from enum import Enum


class StreamPerTitleSettings(object):
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
            'fixed_resolution_and_bitrate_settings': 'StreamPerTitleFixedResolutionAndBitrateSettings'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'fixed_resolution_and_bitrate_settings': 'fixedResolutionAndBitrateSettings'
        }
        return attributes

    def __init__(self, fixed_resolution_and_bitrate_settings=None, *args, **kwargs):

        self._fixed_resolution_and_bitrate_settings = None
        self.discriminator = None

        if fixed_resolution_and_bitrate_settings is not None:
            self.fixed_resolution_and_bitrate_settings = fixed_resolution_and_bitrate_settings

    @property
    def fixed_resolution_and_bitrate_settings(self):
        """Gets the fixed_resolution_and_bitrate_settings of this StreamPerTitleSettings.

        Settings for PER_TITLE_TEMPLATE_FIXED_RESOLUTION_AND_BITRATE mode

        :return: The fixed_resolution_and_bitrate_settings of this StreamPerTitleSettings.
        :rtype: StreamPerTitleFixedResolutionAndBitrateSettings
        """
        return self._fixed_resolution_and_bitrate_settings

    @fixed_resolution_and_bitrate_settings.setter
    def fixed_resolution_and_bitrate_settings(self, fixed_resolution_and_bitrate_settings):
        """Sets the fixed_resolution_and_bitrate_settings of this StreamPerTitleSettings.

        Settings for PER_TITLE_TEMPLATE_FIXED_RESOLUTION_AND_BITRATE mode

        :param fixed_resolution_and_bitrate_settings: The fixed_resolution_and_bitrate_settings of this StreamPerTitleSettings.
        :type: StreamPerTitleFixedResolutionAndBitrateSettings
        """

        if fixed_resolution_and_bitrate_settings is not None:
            if not isinstance(fixed_resolution_and_bitrate_settings, StreamPerTitleFixedResolutionAndBitrateSettings):
                raise TypeError("Invalid type for `fixed_resolution_and_bitrate_settings`, type has to be `StreamPerTitleFixedResolutionAndBitrateSettings`")

            self._fixed_resolution_and_bitrate_settings = fixed_resolution_and_bitrate_settings

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
            if issubclass(StreamPerTitleSettings, dict):
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
        if not isinstance(other, StreamPerTitleSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
