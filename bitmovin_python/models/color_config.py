# coding: utf-8

from bitmovin_python.models.chroma_location import ChromaLocation
from bitmovin_python.models.color_primaries import ColorPrimaries
from bitmovin_python.models.color_range import ColorRange
from bitmovin_python.models.color_space import ColorSpace
from bitmovin_python.models.color_transfer import ColorTransfer
from bitmovin_python.models.input_color_range import InputColorRange
from bitmovin_python.models.input_color_space import InputColorSpace
import pprint
import six
from datetime import datetime
from enum import Enum


class ColorConfig(object):
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
            'copy_chroma_location_flag': 'bool',
            'copy_color_space_flag': 'bool',
            'copy_color_primaries_flag': 'bool',
            'copy_color_range_flag': 'bool',
            'copy_color_transfer_flag': 'bool',
            'chroma_location': 'ChromaLocation',
            'color_space': 'ColorSpace',
            'color_primaries': 'ColorPrimaries',
            'color_range': 'ColorRange',
            'color_transfer': 'ColorTransfer',
            'input_color_space': 'InputColorSpace',
            'input_color_range': 'InputColorRange'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'copy_chroma_location_flag': 'copyChromaLocationFlag',
            'copy_color_space_flag': 'copyColorSpaceFlag',
            'copy_color_primaries_flag': 'copyColorPrimariesFlag',
            'copy_color_range_flag': 'copyColorRangeFlag',
            'copy_color_transfer_flag': 'copyColorTransferFlag',
            'chroma_location': 'chromaLocation',
            'color_space': 'colorSpace',
            'color_primaries': 'colorPrimaries',
            'color_range': 'colorRange',
            'color_transfer': 'colorTransfer',
            'input_color_space': 'inputColorSpace',
            'input_color_range': 'inputColorRange'
        }
        return attributes

    def __init__(self, copy_chroma_location_flag=None, copy_color_space_flag=None, copy_color_primaries_flag=None, copy_color_range_flag=None, copy_color_transfer_flag=None, chroma_location=None, color_space=None, color_primaries=None, color_range=None, color_transfer=None, input_color_space=None, input_color_range=None, *args, **kwargs):

        self._copy_chroma_location_flag = None
        self._copy_color_space_flag = None
        self._copy_color_primaries_flag = None
        self._copy_color_range_flag = None
        self._copy_color_transfer_flag = None
        self._chroma_location = None
        self._color_space = None
        self._color_primaries = None
        self._color_range = None
        self._color_transfer = None
        self._input_color_space = None
        self._input_color_range = None
        self.discriminator = None

        if copy_chroma_location_flag is not None:
            self.copy_chroma_location_flag = copy_chroma_location_flag
        if copy_color_space_flag is not None:
            self.copy_color_space_flag = copy_color_space_flag
        if copy_color_primaries_flag is not None:
            self.copy_color_primaries_flag = copy_color_primaries_flag
        if copy_color_range_flag is not None:
            self.copy_color_range_flag = copy_color_range_flag
        if copy_color_transfer_flag is not None:
            self.copy_color_transfer_flag = copy_color_transfer_flag
        if chroma_location is not None:
            self.chroma_location = chroma_location
        if color_space is not None:
            self.color_space = color_space
        if color_primaries is not None:
            self.color_primaries = color_primaries
        if color_range is not None:
            self.color_range = color_range
        if color_transfer is not None:
            self.color_transfer = color_transfer
        if input_color_space is not None:
            self.input_color_space = input_color_space
        if input_color_range is not None:
            self.input_color_range = input_color_range

    @property
    def copy_chroma_location_flag(self):
        """Gets the copy_chroma_location_flag of this ColorConfig.

        Copy the chroma location setting from the input source

        :return: The copy_chroma_location_flag of this ColorConfig.
        :rtype: bool
        """
        return self._copy_chroma_location_flag

    @copy_chroma_location_flag.setter
    def copy_chroma_location_flag(self, copy_chroma_location_flag):
        """Sets the copy_chroma_location_flag of this ColorConfig.

        Copy the chroma location setting from the input source

        :param copy_chroma_location_flag: The copy_chroma_location_flag of this ColorConfig.
        :type: bool
        """

        if copy_chroma_location_flag is not None:
            if not isinstance(copy_chroma_location_flag, bool):
                raise TypeError("Invalid type for `copy_chroma_location_flag`, type has to be `bool`")

            self._copy_chroma_location_flag = copy_chroma_location_flag


    @property
    def copy_color_space_flag(self):
        """Gets the copy_color_space_flag of this ColorConfig.

        Copy the color space setting from the input source

        :return: The copy_color_space_flag of this ColorConfig.
        :rtype: bool
        """
        return self._copy_color_space_flag

    @copy_color_space_flag.setter
    def copy_color_space_flag(self, copy_color_space_flag):
        """Sets the copy_color_space_flag of this ColorConfig.

        Copy the color space setting from the input source

        :param copy_color_space_flag: The copy_color_space_flag of this ColorConfig.
        :type: bool
        """

        if copy_color_space_flag is not None:
            if not isinstance(copy_color_space_flag, bool):
                raise TypeError("Invalid type for `copy_color_space_flag`, type has to be `bool`")

            self._copy_color_space_flag = copy_color_space_flag


    @property
    def copy_color_primaries_flag(self):
        """Gets the copy_color_primaries_flag of this ColorConfig.

        Copy the color primaries setting from the input source

        :return: The copy_color_primaries_flag of this ColorConfig.
        :rtype: bool
        """
        return self._copy_color_primaries_flag

    @copy_color_primaries_flag.setter
    def copy_color_primaries_flag(self, copy_color_primaries_flag):
        """Sets the copy_color_primaries_flag of this ColorConfig.

        Copy the color primaries setting from the input source

        :param copy_color_primaries_flag: The copy_color_primaries_flag of this ColorConfig.
        :type: bool
        """

        if copy_color_primaries_flag is not None:
            if not isinstance(copy_color_primaries_flag, bool):
                raise TypeError("Invalid type for `copy_color_primaries_flag`, type has to be `bool`")

            self._copy_color_primaries_flag = copy_color_primaries_flag


    @property
    def copy_color_range_flag(self):
        """Gets the copy_color_range_flag of this ColorConfig.

        Copy the color range setting from the input source

        :return: The copy_color_range_flag of this ColorConfig.
        :rtype: bool
        """
        return self._copy_color_range_flag

    @copy_color_range_flag.setter
    def copy_color_range_flag(self, copy_color_range_flag):
        """Sets the copy_color_range_flag of this ColorConfig.

        Copy the color range setting from the input source

        :param copy_color_range_flag: The copy_color_range_flag of this ColorConfig.
        :type: bool
        """

        if copy_color_range_flag is not None:
            if not isinstance(copy_color_range_flag, bool):
                raise TypeError("Invalid type for `copy_color_range_flag`, type has to be `bool`")

            self._copy_color_range_flag = copy_color_range_flag


    @property
    def copy_color_transfer_flag(self):
        """Gets the copy_color_transfer_flag of this ColorConfig.

        Copy the color transfer setting from the input source

        :return: The copy_color_transfer_flag of this ColorConfig.
        :rtype: bool
        """
        return self._copy_color_transfer_flag

    @copy_color_transfer_flag.setter
    def copy_color_transfer_flag(self, copy_color_transfer_flag):
        """Sets the copy_color_transfer_flag of this ColorConfig.

        Copy the color transfer setting from the input source

        :param copy_color_transfer_flag: The copy_color_transfer_flag of this ColorConfig.
        :type: bool
        """

        if copy_color_transfer_flag is not None:
            if not isinstance(copy_color_transfer_flag, bool):
                raise TypeError("Invalid type for `copy_color_transfer_flag`, type has to be `bool`")

            self._copy_color_transfer_flag = copy_color_transfer_flag


    @property
    def chroma_location(self):
        """Gets the chroma_location of this ColorConfig.

        The chroma location to be applied

        :return: The chroma_location of this ColorConfig.
        :rtype: ChromaLocation
        """
        return self._chroma_location

    @chroma_location.setter
    def chroma_location(self, chroma_location):
        """Sets the chroma_location of this ColorConfig.

        The chroma location to be applied

        :param chroma_location: The chroma_location of this ColorConfig.
        :type: ChromaLocation
        """

        if chroma_location is not None:
            if not isinstance(chroma_location, ChromaLocation):
                raise TypeError("Invalid type for `chroma_location`, type has to be `ChromaLocation`")

            self._chroma_location = chroma_location


    @property
    def color_space(self):
        """Gets the color_space of this ColorConfig.

        The color space to be applied

        :return: The color_space of this ColorConfig.
        :rtype: ColorSpace
        """
        return self._color_space

    @color_space.setter
    def color_space(self, color_space):
        """Sets the color_space of this ColorConfig.

        The color space to be applied

        :param color_space: The color_space of this ColorConfig.
        :type: ColorSpace
        """

        if color_space is not None:
            if not isinstance(color_space, ColorSpace):
                raise TypeError("Invalid type for `color_space`, type has to be `ColorSpace`")

            self._color_space = color_space


    @property
    def color_primaries(self):
        """Gets the color_primaries of this ColorConfig.

        The color primaries to be applied

        :return: The color_primaries of this ColorConfig.
        :rtype: ColorPrimaries
        """
        return self._color_primaries

    @color_primaries.setter
    def color_primaries(self, color_primaries):
        """Sets the color_primaries of this ColorConfig.

        The color primaries to be applied

        :param color_primaries: The color_primaries of this ColorConfig.
        :type: ColorPrimaries
        """

        if color_primaries is not None:
            if not isinstance(color_primaries, ColorPrimaries):
                raise TypeError("Invalid type for `color_primaries`, type has to be `ColorPrimaries`")

            self._color_primaries = color_primaries


    @property
    def color_range(self):
        """Gets the color_range of this ColorConfig.

        The color range to be applied

        :return: The color_range of this ColorConfig.
        :rtype: ColorRange
        """
        return self._color_range

    @color_range.setter
    def color_range(self, color_range):
        """Sets the color_range of this ColorConfig.

        The color range to be applied

        :param color_range: The color_range of this ColorConfig.
        :type: ColorRange
        """

        if color_range is not None:
            if not isinstance(color_range, ColorRange):
                raise TypeError("Invalid type for `color_range`, type has to be `ColorRange`")

            self._color_range = color_range


    @property
    def color_transfer(self):
        """Gets the color_transfer of this ColorConfig.

        The color transfer to be applied

        :return: The color_transfer of this ColorConfig.
        :rtype: ColorTransfer
        """
        return self._color_transfer

    @color_transfer.setter
    def color_transfer(self, color_transfer):
        """Sets the color_transfer of this ColorConfig.

        The color transfer to be applied

        :param color_transfer: The color_transfer of this ColorConfig.
        :type: ColorTransfer
        """

        if color_transfer is not None:
            if not isinstance(color_transfer, ColorTransfer):
                raise TypeError("Invalid type for `color_transfer`, type has to be `ColorTransfer`")

            self._color_transfer = color_transfer


    @property
    def input_color_space(self):
        """Gets the input_color_space of this ColorConfig.

        Override the color space detected in the input file. If not set the input color space will be automatically detected if possible.

        :return: The input_color_space of this ColorConfig.
        :rtype: InputColorSpace
        """
        return self._input_color_space

    @input_color_space.setter
    def input_color_space(self, input_color_space):
        """Sets the input_color_space of this ColorConfig.

        Override the color space detected in the input file. If not set the input color space will be automatically detected if possible.

        :param input_color_space: The input_color_space of this ColorConfig.
        :type: InputColorSpace
        """

        if input_color_space is not None:
            if not isinstance(input_color_space, InputColorSpace):
                raise TypeError("Invalid type for `input_color_space`, type has to be `InputColorSpace`")

            self._input_color_space = input_color_space


    @property
    def input_color_range(self):
        """Gets the input_color_range of this ColorConfig.

        Override the color range detected in the input file. If not set the input color range will be automatically detected if possible.

        :return: The input_color_range of this ColorConfig.
        :rtype: InputColorRange
        """
        return self._input_color_range

    @input_color_range.setter
    def input_color_range(self, input_color_range):
        """Sets the input_color_range of this ColorConfig.

        Override the color range detected in the input file. If not set the input color range will be automatically detected if possible.

        :param input_color_range: The input_color_range of this ColorConfig.
        :type: InputColorRange
        """

        if input_color_range is not None:
            if not isinstance(input_color_range, InputColorRange):
                raise TypeError("Invalid type for `input_color_range`, type has to be `InputColorRange`")

            self._input_color_range = input_color_range

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
            if issubclass(ColorConfig, dict):
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
        if not isinstance(other, ColorConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
