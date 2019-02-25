# coding: utf-8

from bitmovin_python.models.filter import Filter
from bitmovin_python.models.filter_type import FilterType
import pprint
import six
from datetime import datetime
from enum import Enum


class UnsharpFilter(Filter):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(UnsharpFilter, self).openapi_types
        types.update({
            'luma_matrix_horizontal_size': 'int',
            'luma_matrix_vertical_size': 'int',
            'luma_effect_strength': 'float',
            'chroma_matrix_horizontal_size': 'int',
            'chroma_matrix_vertical_size': 'int',
            'chroma_effect_strength': 'float'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(UnsharpFilter, self).attribute_map
        attributes.update({
            'luma_matrix_horizontal_size': 'lumaMatrixHorizontalSize',
            'luma_matrix_vertical_size': 'lumaMatrixVerticalSize',
            'luma_effect_strength': 'lumaEffectStrength',
            'chroma_matrix_horizontal_size': 'chromaMatrixHorizontalSize',
            'chroma_matrix_vertical_size': 'chromaMatrixVerticalSize',
            'chroma_effect_strength': 'chromaEffectStrength'
        })
        return attributes

    def __init__(self, luma_matrix_horizontal_size=None, luma_matrix_vertical_size=None, luma_effect_strength=None, chroma_matrix_horizontal_size=None, chroma_matrix_vertical_size=None, chroma_effect_strength=None, *args, **kwargs):
        super(UnsharpFilter, self).__init__(*args, **kwargs)

        self._luma_matrix_horizontal_size = None
        self._luma_matrix_vertical_size = None
        self._luma_effect_strength = None
        self._chroma_matrix_horizontal_size = None
        self._chroma_matrix_vertical_size = None
        self._chroma_effect_strength = None
        self.discriminator = None

        if luma_matrix_horizontal_size is not None:
            self.luma_matrix_horizontal_size = luma_matrix_horizontal_size
        if luma_matrix_vertical_size is not None:
            self.luma_matrix_vertical_size = luma_matrix_vertical_size
        if luma_effect_strength is not None:
            self.luma_effect_strength = luma_effect_strength
        if chroma_matrix_horizontal_size is not None:
            self.chroma_matrix_horizontal_size = chroma_matrix_horizontal_size
        if chroma_matrix_vertical_size is not None:
            self.chroma_matrix_vertical_size = chroma_matrix_vertical_size
        if chroma_effect_strength is not None:
            self.chroma_effect_strength = chroma_effect_strength

    @property
    def luma_matrix_horizontal_size(self):
        """Gets the luma_matrix_horizontal_size of this UnsharpFilter.

        Must be an odd integer between 3 and 23

        :return: The luma_matrix_horizontal_size of this UnsharpFilter.
        :rtype: int
        """
        return self._luma_matrix_horizontal_size

    @luma_matrix_horizontal_size.setter
    def luma_matrix_horizontal_size(self, luma_matrix_horizontal_size):
        """Sets the luma_matrix_horizontal_size of this UnsharpFilter.

        Must be an odd integer between 3 and 23

        :param luma_matrix_horizontal_size: The luma_matrix_horizontal_size of this UnsharpFilter.
        :type: int
        """

        if luma_matrix_horizontal_size is not None:
            if not isinstance(luma_matrix_horizontal_size, int):
                raise TypeError("Invalid type for `luma_matrix_horizontal_size`, type has to be `int`")

            self._luma_matrix_horizontal_size = luma_matrix_horizontal_size


    @property
    def luma_matrix_vertical_size(self):
        """Gets the luma_matrix_vertical_size of this UnsharpFilter.

        Must be an odd integer between 3 and 23

        :return: The luma_matrix_vertical_size of this UnsharpFilter.
        :rtype: int
        """
        return self._luma_matrix_vertical_size

    @luma_matrix_vertical_size.setter
    def luma_matrix_vertical_size(self, luma_matrix_vertical_size):
        """Sets the luma_matrix_vertical_size of this UnsharpFilter.

        Must be an odd integer between 3 and 23

        :param luma_matrix_vertical_size: The luma_matrix_vertical_size of this UnsharpFilter.
        :type: int
        """

        if luma_matrix_vertical_size is not None:
            if not isinstance(luma_matrix_vertical_size, int):
                raise TypeError("Invalid type for `luma_matrix_vertical_size`, type has to be `int`")

            self._luma_matrix_vertical_size = luma_matrix_vertical_size


    @property
    def luma_effect_strength(self):
        """Gets the luma_effect_strength of this UnsharpFilter.

        Negative value: blur, positive value: sharpen, floating point number, valid value range: -1.5 - 1.5

        :return: The luma_effect_strength of this UnsharpFilter.
        :rtype: float
        """
        return self._luma_effect_strength

    @luma_effect_strength.setter
    def luma_effect_strength(self, luma_effect_strength):
        """Sets the luma_effect_strength of this UnsharpFilter.

        Negative value: blur, positive value: sharpen, floating point number, valid value range: -1.5 - 1.5

        :param luma_effect_strength: The luma_effect_strength of this UnsharpFilter.
        :type: float
        """

        if luma_effect_strength is not None:
            if not isinstance(luma_effect_strength, float):
                raise TypeError("Invalid type for `luma_effect_strength`, type has to be `float`")

            self._luma_effect_strength = luma_effect_strength


    @property
    def chroma_matrix_horizontal_size(self):
        """Gets the chroma_matrix_horizontal_size of this UnsharpFilter.

        Must be an odd integer between 3 and 23

        :return: The chroma_matrix_horizontal_size of this UnsharpFilter.
        :rtype: int
        """
        return self._chroma_matrix_horizontal_size

    @chroma_matrix_horizontal_size.setter
    def chroma_matrix_horizontal_size(self, chroma_matrix_horizontal_size):
        """Sets the chroma_matrix_horizontal_size of this UnsharpFilter.

        Must be an odd integer between 3 and 23

        :param chroma_matrix_horizontal_size: The chroma_matrix_horizontal_size of this UnsharpFilter.
        :type: int
        """

        if chroma_matrix_horizontal_size is not None:
            if not isinstance(chroma_matrix_horizontal_size, int):
                raise TypeError("Invalid type for `chroma_matrix_horizontal_size`, type has to be `int`")

            self._chroma_matrix_horizontal_size = chroma_matrix_horizontal_size


    @property
    def chroma_matrix_vertical_size(self):
        """Gets the chroma_matrix_vertical_size of this UnsharpFilter.

        Must be an odd integer between 3 and 23

        :return: The chroma_matrix_vertical_size of this UnsharpFilter.
        :rtype: int
        """
        return self._chroma_matrix_vertical_size

    @chroma_matrix_vertical_size.setter
    def chroma_matrix_vertical_size(self, chroma_matrix_vertical_size):
        """Sets the chroma_matrix_vertical_size of this UnsharpFilter.

        Must be an odd integer between 3 and 23

        :param chroma_matrix_vertical_size: The chroma_matrix_vertical_size of this UnsharpFilter.
        :type: int
        """

        if chroma_matrix_vertical_size is not None:
            if not isinstance(chroma_matrix_vertical_size, int):
                raise TypeError("Invalid type for `chroma_matrix_vertical_size`, type has to be `int`")

            self._chroma_matrix_vertical_size = chroma_matrix_vertical_size


    @property
    def chroma_effect_strength(self):
        """Gets the chroma_effect_strength of this UnsharpFilter.

        Negative value: blur, positive value: sharpen, floating point number, valid value range: -1.5 - 1.5

        :return: The chroma_effect_strength of this UnsharpFilter.
        :rtype: float
        """
        return self._chroma_effect_strength

    @chroma_effect_strength.setter
    def chroma_effect_strength(self, chroma_effect_strength):
        """Sets the chroma_effect_strength of this UnsharpFilter.

        Negative value: blur, positive value: sharpen, floating point number, valid value range: -1.5 - 1.5

        :param chroma_effect_strength: The chroma_effect_strength of this UnsharpFilter.
        :type: float
        """

        if chroma_effect_strength is not None:
            if not isinstance(chroma_effect_strength, float):
                raise TypeError("Invalid type for `chroma_effect_strength`, type has to be `float`")

            self._chroma_effect_strength = chroma_effect_strength

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(UnsharpFilter, self).to_dict()

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
            if issubclass(UnsharpFilter, dict):
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
        if not isinstance(other, UnsharpFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
