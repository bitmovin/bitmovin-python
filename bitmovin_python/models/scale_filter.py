# coding: utf-8

from bitmovin_python.models.filter import Filter
from bitmovin_python.models.filter_type import FilterType
from bitmovin_python.models.scaling_algorithm import ScalingAlgorithm
import pprint
import six
from datetime import datetime
from enum import Enum


class ScaleFilter(Filter):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(ScaleFilter, self).openapi_types
        types.update({
            'width': 'int',
            'height': 'int',
            'scaling_algorithm': 'ScalingAlgorithm'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(ScaleFilter, self).attribute_map
        attributes.update({
            'width': 'width',
            'height': 'height',
            'scaling_algorithm': 'scalingAlgorithm'
        })
        return attributes

    def __init__(self, width=None, height=None, scaling_algorithm=None, *args, **kwargs):
        super(ScaleFilter, self).__init__(*args, **kwargs)

        self._width = None
        self._height = None
        self._scaling_algorithm = None
        self.discriminator = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if scaling_algorithm is not None:
            self.scaling_algorithm = scaling_algorithm

    @property
    def width(self):
        """Gets the width of this ScaleFilter.

        The width of the output frame in pixel. If not set: codec configuration width will be used.

        :return: The width of this ScaleFilter.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ScaleFilter.

        The width of the output frame in pixel. If not set: codec configuration width will be used.

        :param width: The width of this ScaleFilter.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

            self._width = width


    @property
    def height(self):
        """Gets the height of this ScaleFilter.

        The height of the output frame in pixel. If not set: codec configuration height will be used.

        :return: The height of this ScaleFilter.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ScaleFilter.

        The height of the output frame in pixel. If not set: codec configuration height will be used.

        :param height: The height of this ScaleFilter.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

            self._height = height


    @property
    def scaling_algorithm(self):
        """Gets the scaling_algorithm of this ScaleFilter.


        :return: The scaling_algorithm of this ScaleFilter.
        :rtype: ScalingAlgorithm
        """
        return self._scaling_algorithm

    @scaling_algorithm.setter
    def scaling_algorithm(self, scaling_algorithm):
        """Sets the scaling_algorithm of this ScaleFilter.


        :param scaling_algorithm: The scaling_algorithm of this ScaleFilter.
        :type: ScalingAlgorithm
        """

        if scaling_algorithm is not None:
            if not isinstance(scaling_algorithm, ScalingAlgorithm):
                raise TypeError("Invalid type for `scaling_algorithm`, type has to be `ScalingAlgorithm`")

            self._scaling_algorithm = scaling_algorithm

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(ScaleFilter, self).to_dict()

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
            if issubclass(ScaleFilter, dict):
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
        if not isinstance(other, ScaleFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
