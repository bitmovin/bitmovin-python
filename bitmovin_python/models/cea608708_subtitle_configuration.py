# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class Cea608708SubtitleConfiguration(object):
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
            'passthrough_activated': 'bool'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'passthrough_activated': 'passthroughActivated'
        }
        return attributes

    def __init__(self, passthrough_activated=None, *args, **kwargs):

        self._passthrough_activated = None
        self.discriminator = None

        if passthrough_activated is not None:
            self.passthrough_activated = passthrough_activated

    @property
    def passthrough_activated(self):
        """Gets the passthrough_activated of this Cea608708SubtitleConfiguration.

        If enabled, CEA 608 an CEA 708 subtitles will be copied from the input video stream to the output video stream. Note: This does not work, if the output framerate is different than the input framerate (except doubling the framerate with deinterlacing per field)

        :return: The passthrough_activated of this Cea608708SubtitleConfiguration.
        :rtype: bool
        """
        return self._passthrough_activated

    @passthrough_activated.setter
    def passthrough_activated(self, passthrough_activated):
        """Sets the passthrough_activated of this Cea608708SubtitleConfiguration.

        If enabled, CEA 608 an CEA 708 subtitles will be copied from the input video stream to the output video stream. Note: This does not work, if the output framerate is different than the input framerate (except doubling the framerate with deinterlacing per field)

        :param passthrough_activated: The passthrough_activated of this Cea608708SubtitleConfiguration.
        :type: bool
        """

        if passthrough_activated is not None:
            if not isinstance(passthrough_activated, bool):
                raise TypeError("Invalid type for `passthrough_activated`, type has to be `bool`")

            self._passthrough_activated = passthrough_activated

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
            if issubclass(Cea608708SubtitleConfiguration, dict):
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
        if not isinstance(other, Cea608708SubtitleConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
