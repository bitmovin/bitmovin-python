# coding: utf-8

from bitmovin_python.models.dash_representation import DashRepresentation
import pprint
import six
from datetime import datetime
from enum import Enum


class DashMp4Representation(DashRepresentation):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(DashMp4Representation, self).openapi_types
        types.update({
            'file_path': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(DashMp4Representation, self).attribute_map
        attributes.update({
            'file_path': 'filePath'
        })
        return attributes

    def __init__(self, file_path=None, *args, **kwargs):
        super(DashMp4Representation, self).__init__(*args, **kwargs)

        self._file_path = None
        self.discriminator = None

        self.file_path = file_path

    @property
    def file_path(self):
        """Gets the file_path of this DashMp4Representation.

        Path to the MP4 file

        :return: The file_path of this DashMp4Representation.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this DashMp4Representation.

        Path to the MP4 file

        :param file_path: The file_path of this DashMp4Representation.
        :type: str
        """

        if file_path is not None:
            if not isinstance(file_path, str):
                raise TypeError("Invalid type for `file_path`, type has to be `str`")

            self._file_path = file_path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(DashMp4Representation, self).to_dict()

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
            if issubclass(DashMp4Representation, dict):
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
        if not isinstance(other, DashMp4Representation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
