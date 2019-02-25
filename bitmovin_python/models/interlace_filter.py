# coding: utf-8

from bitmovin_python.models.filter import Filter
from bitmovin_python.models.filter_type import FilterType
from bitmovin_python.models.interlace_mode import InterlaceMode
from bitmovin_python.models.vertical_low_pass_filtering_mode import VerticalLowPassFilteringMode
import pprint
import six
from datetime import datetime
from enum import Enum


class InterlaceFilter(Filter):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(InterlaceFilter, self).openapi_types
        types.update({
            'mode': 'InterlaceMode',
            'vertical_low_pass_filtering_mode': 'VerticalLowPassFilteringMode'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(InterlaceFilter, self).attribute_map
        attributes.update({
            'mode': 'mode',
            'vertical_low_pass_filtering_mode': 'verticalLowPassFilteringMode'
        })
        return attributes

    def __init__(self, mode=None, vertical_low_pass_filtering_mode=None, *args, **kwargs):
        super(InterlaceFilter, self).__init__(*args, **kwargs)

        self._mode = None
        self._vertical_low_pass_filtering_mode = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if vertical_low_pass_filtering_mode is not None:
            self.vertical_low_pass_filtering_mode = vertical_low_pass_filtering_mode

    @property
    def mode(self):
        """Gets the mode of this InterlaceFilter.


        :return: The mode of this InterlaceFilter.
        :rtype: InterlaceMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this InterlaceFilter.


        :param mode: The mode of this InterlaceFilter.
        :type: InterlaceMode
        """

        if mode is not None:
            if not isinstance(mode, InterlaceMode):
                raise TypeError("Invalid type for `mode`, type has to be `InterlaceMode`")

            self._mode = mode


    @property
    def vertical_low_pass_filtering_mode(self):
        """Gets the vertical_low_pass_filtering_mode of this InterlaceFilter.


        :return: The vertical_low_pass_filtering_mode of this InterlaceFilter.
        :rtype: VerticalLowPassFilteringMode
        """
        return self._vertical_low_pass_filtering_mode

    @vertical_low_pass_filtering_mode.setter
    def vertical_low_pass_filtering_mode(self, vertical_low_pass_filtering_mode):
        """Sets the vertical_low_pass_filtering_mode of this InterlaceFilter.


        :param vertical_low_pass_filtering_mode: The vertical_low_pass_filtering_mode of this InterlaceFilter.
        :type: VerticalLowPassFilteringMode
        """

        if vertical_low_pass_filtering_mode is not None:
            if not isinstance(vertical_low_pass_filtering_mode, VerticalLowPassFilteringMode):
                raise TypeError("Invalid type for `vertical_low_pass_filtering_mode`, type has to be `VerticalLowPassFilteringMode`")

            self._vertical_low_pass_filtering_mode = vertical_low_pass_filtering_mode

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(InterlaceFilter, self).to_dict()

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
            if issubclass(InterlaceFilter, dict):
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
        if not isinstance(other, InterlaceFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
