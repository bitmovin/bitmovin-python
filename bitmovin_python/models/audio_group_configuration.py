# coding: utf-8

from bitmovin_python.models.audio_group import AudioGroup
from bitmovin_python.models.variant_stream_dropping_mode import VariantStreamDroppingMode
import pprint
import six
from datetime import datetime
from enum import Enum


class AudioGroupConfiguration(object):
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
            'dropping_mode': 'VariantStreamDroppingMode',
            'groups': 'list[AudioGroup]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'dropping_mode': 'droppingMode',
            'groups': 'groups'
        }
        return attributes

    def __init__(self, dropping_mode=None, groups=None, *args, **kwargs):

        self._dropping_mode = None
        self._groups = None
        self.discriminator = None

        self.dropping_mode = dropping_mode
        self.groups = groups

    @property
    def dropping_mode(self):
        """Gets the dropping_mode of this AudioGroupConfiguration.

        Dropping mode

        :return: The dropping_mode of this AudioGroupConfiguration.
        :rtype: VariantStreamDroppingMode
        """
        return self._dropping_mode

    @dropping_mode.setter
    def dropping_mode(self, dropping_mode):
        """Sets the dropping_mode of this AudioGroupConfiguration.

        Dropping mode

        :param dropping_mode: The dropping_mode of this AudioGroupConfiguration.
        :type: VariantStreamDroppingMode
        """

        if dropping_mode is not None:
            if not isinstance(dropping_mode, VariantStreamDroppingMode):
                raise TypeError("Invalid type for `dropping_mode`, type has to be `VariantStreamDroppingMode`")

            self._dropping_mode = dropping_mode


    @property
    def groups(self):
        """Gets the groups of this AudioGroupConfiguration.

        Audio groups

        :return: The groups of this AudioGroupConfiguration.
        :rtype: list[AudioGroup]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this AudioGroupConfiguration.

        Audio groups

        :param groups: The groups of this AudioGroupConfiguration.
        :type: list[AudioGroup]
        """

        if groups is not None:
            if not isinstance(groups, list):
                raise TypeError("Invalid type for `groups`, type has to be `list[AudioGroup]`")

            self._groups = groups

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
            if issubclass(AudioGroupConfiguration, dict):
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
        if not isinstance(other, AudioGroupConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
