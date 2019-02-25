# coding: utf-8

from bitmovin_python.models.audio_volume_unit import AudioVolumeUnit
from bitmovin_python.models.filter import Filter
from bitmovin_python.models.filter_type import FilterType
import pprint
import six
from datetime import datetime
from enum import Enum


class AudioVolumeFilter(Filter):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AudioVolumeFilter, self).openapi_types
        types.update({
            'volume': 'float',
            'unit': 'AudioVolumeUnit'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AudioVolumeFilter, self).attribute_map
        attributes.update({
            'volume': 'volume',
            'unit': 'unit'
        })
        return attributes

    def __init__(self, volume=None, unit=None, *args, **kwargs):
        super(AudioVolumeFilter, self).__init__(*args, **kwargs)

        self._volume = None
        self._unit = None
        self.discriminator = None

        self.volume = volume
        self.unit = unit

    @property
    def volume(self):
        """Gets the volume of this AudioVolumeFilter.

        Audio volume value

        :return: The volume of this AudioVolumeFilter.
        :rtype: float
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this AudioVolumeFilter.

        Audio volume value

        :param volume: The volume of this AudioVolumeFilter.
        :type: float
        """

        if volume is not None:
            if not isinstance(volume, float):
                raise TypeError("Invalid type for `volume`, type has to be `float`")

            self._volume = volume


    @property
    def unit(self):
        """Gets the unit of this AudioVolumeFilter.


        :return: The unit of this AudioVolumeFilter.
        :rtype: AudioVolumeUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this AudioVolumeFilter.


        :param unit: The unit of this AudioVolumeFilter.
        :type: AudioVolumeUnit
        """

        if unit is not None:
            if not isinstance(unit, AudioVolumeUnit):
                raise TypeError("Invalid type for `unit`, type has to be `AudioVolumeUnit`")

            self._unit = unit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AudioVolumeFilter, self).to_dict()

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
            if issubclass(AudioVolumeFilter, dict):
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
        if not isinstance(other, AudioVolumeFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
