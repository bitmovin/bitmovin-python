# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.encoding_output import EncodingOutput
from bitmovin_python.models.thumbnail_unit import ThumbnailUnit
import pprint
import six
from datetime import datetime
from enum import Enum


class Thumbnail(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Thumbnail, self).openapi_types
        types.update({
            'height': 'int',
            'pattern': 'str',
            'positions': 'list[float]',
            'outputs': 'list[EncodingOutput]',
            'unit': 'ThumbnailUnit'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Thumbnail, self).attribute_map
        attributes.update({
            'height': 'height',
            'pattern': 'pattern',
            'positions': 'positions',
            'outputs': 'outputs',
            'unit': 'unit'
        })
        return attributes

    def __init__(self, height=None, pattern=None, positions=None, outputs=None, unit=None, *args, **kwargs):
        super(Thumbnail, self).__init__(*args, **kwargs)

        self._height = None
        self._pattern = None
        self._positions = None
        self._outputs = None
        self._unit = None
        self.discriminator = None

        self.height = height
        if pattern is not None:
            self.pattern = pattern
        self.positions = positions
        if outputs is not None:
            self.outputs = outputs
        if unit is not None:
            self.unit = unit

    @property
    def height(self):
        """Gets the height of this Thumbnail.

        Height of the thumbnail

        :return: The height of this Thumbnail.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Thumbnail.

        Height of the thumbnail

        :param height: The height of this Thumbnail.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

            self._height = height


    @property
    def pattern(self):
        """Gets the pattern of this Thumbnail.

         Pattern which describes the thumbnail filenames. For example with thumbnail-%number%.png as pattern and 3 positions: thumbnail-3.png, thumbnail-5.png and thumbnail-25_5.png. (The number represents the position in the source video in seconds, in the previous example the first filename represents the thumbnail at 3s, the second one at 5s and the third one at 25.5s)

        :return: The pattern of this Thumbnail.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this Thumbnail.

         Pattern which describes the thumbnail filenames. For example with thumbnail-%number%.png as pattern and 3 positions: thumbnail-3.png, thumbnail-5.png and thumbnail-25_5.png. (The number represents the position in the source video in seconds, in the previous example the first filename represents the thumbnail at 3s, the second one at 5s and the third one at 25.5s)

        :param pattern: The pattern of this Thumbnail.
        :type: str
        """

        if pattern is not None:
            if not isinstance(pattern, str):
                raise TypeError("Invalid type for `pattern`, type has to be `str`")

            self._pattern = pattern


    @property
    def positions(self):
        """Gets the positions of this Thumbnail.

        Position in the unit where the thumbnail should be created from.

        :return: The positions of this Thumbnail.
        :rtype: list[float]
        """
        return self._positions

    @positions.setter
    def positions(self, positions):
        """Sets the positions of this Thumbnail.

        Position in the unit where the thumbnail should be created from.

        :param positions: The positions of this Thumbnail.
        :type: list[float]
        """

        if positions is not None:
            if not isinstance(positions, list):
                raise TypeError("Invalid type for `positions`, type has to be `list[float]`")

            self._positions = positions


    @property
    def outputs(self):
        """Gets the outputs of this Thumbnail.


        :return: The outputs of this Thumbnail.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this Thumbnail.


        :param outputs: The outputs of this Thumbnail.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

            self._outputs = outputs


    @property
    def unit(self):
        """Gets the unit of this Thumbnail.


        :return: The unit of this Thumbnail.
        :rtype: ThumbnailUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Thumbnail.


        :param unit: The unit of this Thumbnail.
        :type: ThumbnailUnit
        """

        if unit is not None:
            if not isinstance(unit, ThumbnailUnit):
                raise TypeError("Invalid type for `unit`, type has to be `ThumbnailUnit`")

            self._unit = unit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Thumbnail, self).to_dict()

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
            if issubclass(Thumbnail, dict):
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
        if not isinstance(other, Thumbnail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
