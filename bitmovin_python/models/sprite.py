# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.encoding_output import EncodingOutput
from bitmovin_python.models.sprite_unit import SpriteUnit
import pprint
import six
from datetime import datetime
from enum import Enum


class Sprite(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Sprite, self).openapi_types
        types.update({
            'height': 'int',
            'width': 'int',
            'unit': 'SpriteUnit',
            'distance': 'float',
            'sprite_name': 'str',
            'file_name': 'str',
            'vtt_name': 'str',
            'outputs': 'list[EncodingOutput]',
            'images_per_file': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Sprite, self).attribute_map
        attributes.update({
            'height': 'height',
            'width': 'width',
            'unit': 'unit',
            'distance': 'distance',
            'sprite_name': 'spriteName',
            'file_name': 'fileName',
            'vtt_name': 'vttName',
            'outputs': 'outputs',
            'images_per_file': 'imagesPerFile'
        })
        return attributes

    def __init__(self, height=None, width=None, unit=None, distance=None, sprite_name=None, file_name=None, vtt_name=None, outputs=None, images_per_file=None, *args, **kwargs):
        super(Sprite, self).__init__(*args, **kwargs)

        self._height = None
        self._width = None
        self._unit = None
        self._distance = None
        self._sprite_name = None
        self._file_name = None
        self._vtt_name = None
        self._outputs = None
        self._images_per_file = None
        self.discriminator = None

        self.height = height
        self.width = width
        if unit is not None:
            self.unit = unit
        if distance is not None:
            self.distance = distance
        self.sprite_name = sprite_name
        if file_name is not None:
            self.file_name = file_name
        self.vtt_name = vtt_name
        if outputs is not None:
            self.outputs = outputs
        if images_per_file is not None:
            self.images_per_file = images_per_file

    @property
    def height(self):
        """Gets the height of this Sprite.

        Height of one thumbnail

        :return: The height of this Sprite.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Sprite.

        Height of one thumbnail

        :param height: The height of this Sprite.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

            self._height = height


    @property
    def width(self):
        """Gets the width of this Sprite.

        Width of one thumbnail

        :return: The width of this Sprite.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Sprite.

        Width of one thumbnail

        :param width: The width of this Sprite.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

            self._width = width


    @property
    def unit(self):
        """Gets the unit of this Sprite.


        :return: The unit of this Sprite.
        :rtype: SpriteUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Sprite.


        :param unit: The unit of this Sprite.
        :type: SpriteUnit
        """

        if unit is not None:
            if not isinstance(unit, SpriteUnit):
                raise TypeError("Invalid type for `unit`, type has to be `SpriteUnit`")

            self._unit = unit


    @property
    def distance(self):
        """Gets the distance of this Sprite.

        Distance in the given unit between a screenshot

        :return: The distance of this Sprite.
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this Sprite.

        Distance in the given unit between a screenshot

        :param distance: The distance of this Sprite.
        :type: float
        """

        if distance is not None:
            if not isinstance(distance, float):
                raise TypeError("Invalid type for `distance`, type has to be `float`")

            self._distance = distance


    @property
    def sprite_name(self):
        """Gets the sprite_name of this Sprite.

        Name of the sprite image. File extension \".jpg\" or \".png\" is required.

        :return: The sprite_name of this Sprite.
        :rtype: str
        """
        return self._sprite_name

    @sprite_name.setter
    def sprite_name(self, sprite_name):
        """Sets the sprite_name of this Sprite.

        Name of the sprite image. File extension \".jpg\" or \".png\" is required.

        :param sprite_name: The sprite_name of this Sprite.
        :type: str
        """

        if sprite_name is not None:
            if not isinstance(sprite_name, str):
                raise TypeError("Invalid type for `sprite_name`, type has to be `str`")

            self._sprite_name = sprite_name


    @property
    def file_name(self):
        """Gets the file_name of this Sprite.

        Filename of the sprite image. If not set, spriteName will be used, but without an extension.

        :return: The file_name of this Sprite.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this Sprite.

        Filename of the sprite image. If not set, spriteName will be used, but without an extension.

        :param file_name: The file_name of this Sprite.
        :type: str
        """

        if file_name is not None:
            if not isinstance(file_name, str):
                raise TypeError("Invalid type for `file_name`, type has to be `str`")

            self._file_name = file_name


    @property
    def vtt_name(self):
        """Gets the vtt_name of this Sprite.

        Filename of the vtt-file. The file-extension \".vtt\" is required.

        :return: The vtt_name of this Sprite.
        :rtype: str
        """
        return self._vtt_name

    @vtt_name.setter
    def vtt_name(self, vtt_name):
        """Sets the vtt_name of this Sprite.

        Filename of the vtt-file. The file-extension \".vtt\" is required.

        :param vtt_name: The vtt_name of this Sprite.
        :type: str
        """

        if vtt_name is not None:
            if not isinstance(vtt_name, str):
                raise TypeError("Invalid type for `vtt_name`, type has to be `str`")

            self._vtt_name = vtt_name


    @property
    def outputs(self):
        """Gets the outputs of this Sprite.


        :return: The outputs of this Sprite.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this Sprite.


        :param outputs: The outputs of this Sprite.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

            self._outputs = outputs


    @property
    def images_per_file(self):
        """Gets the images_per_file of this Sprite.

        Number of images per file. If more images are generated than specified in this value, multiple sprites will be created. You can use the placeholder '%number%' in the spriteName to specify the naming policy.

        :return: The images_per_file of this Sprite.
        :rtype: int
        """
        return self._images_per_file

    @images_per_file.setter
    def images_per_file(self, images_per_file):
        """Sets the images_per_file of this Sprite.

        Number of images per file. If more images are generated than specified in this value, multiple sprites will be created. You can use the placeholder '%number%' in the spriteName to specify the naming policy.

        :param images_per_file: The images_per_file of this Sprite.
        :type: int
        """

        if images_per_file is not None:
            if not isinstance(images_per_file, int):
                raise TypeError("Invalid type for `images_per_file`, type has to be `int`")

            self._images_per_file = images_per_file

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Sprite, self).to_dict()

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
            if issubclass(Sprite, dict):
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
        if not isinstance(other, Sprite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
