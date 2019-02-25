# coding: utf-8

from bitmovin_python.models.filter import Filter
from bitmovin_python.models.filter_type import FilterType
import pprint
import six
from datetime import datetime
from enum import Enum


class RotateFilter(Filter):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(RotateFilter, self).openapi_types
        types.update({
            'rotation': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(RotateFilter, self).attribute_map
        attributes.update({
            'rotation': 'rotation'
        })
        return attributes

    def __init__(self, rotation=None, *args, **kwargs):
        super(RotateFilter, self).__init__(*args, **kwargs)

        self._rotation = None
        self.discriminator = None

        self.rotation = rotation

    @property
    def rotation(self):
        """Gets the rotation of this RotateFilter.

        Rotation of the video in degrees. A positive value will rotate the video clockwise and a negative one counter clockwise.

        :return: The rotation of this RotateFilter.
        :rtype: int
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this RotateFilter.

        Rotation of the video in degrees. A positive value will rotate the video clockwise and a negative one counter clockwise.

        :param rotation: The rotation of this RotateFilter.
        :type: int
        """

        if rotation is not None:
            if not isinstance(rotation, int):
                raise TypeError("Invalid type for `rotation`, type has to be `int`")

            self._rotation = rotation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(RotateFilter, self).to_dict()

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
            if issubclass(RotateFilter, dict):
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
        if not isinstance(other, RotateFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
