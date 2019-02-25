# coding: utf-8

from bitmovin_python.models.ignored_by import IgnoredBy
import pprint
import six
from datetime import datetime
from enum import Enum


class Ignoring(object):
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
            'ignored_by': 'IgnoredBy',
            'ignored_by_description': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'ignored_by': 'ignoredBy',
            'ignored_by_description': 'ignoredByDescription'
        }
        return attributes

    def __init__(self, ignored_by=None, ignored_by_description=None, *args, **kwargs):

        self._ignored_by = None
        self._ignored_by_description = None
        self.discriminator = None

        if ignored_by is not None:
            self.ignored_by = ignored_by
        if ignored_by_description is not None:
            self.ignored_by_description = ignored_by_description

    @property
    def ignored_by(self):
        """Gets the ignored_by of this Ignoring.


        :return: The ignored_by of this Ignoring.
        :rtype: IgnoredBy
        """
        return self._ignored_by

    @ignored_by.setter
    def ignored_by(self, ignored_by):
        """Sets the ignored_by of this Ignoring.


        :param ignored_by: The ignored_by of this Ignoring.
        :type: IgnoredBy
        """

        if ignored_by is not None:
            if not isinstance(ignored_by, IgnoredBy):
                raise TypeError("Invalid type for `ignored_by`, type has to be `IgnoredBy`")

            self._ignored_by = ignored_by


    @property
    def ignored_by_description(self):
        """Gets the ignored_by_description of this Ignoring.

        Describes why ignoredBy has been set to its current value.

        :return: The ignored_by_description of this Ignoring.
        :rtype: str
        """
        return self._ignored_by_description

    @ignored_by_description.setter
    def ignored_by_description(self, ignored_by_description):
        """Sets the ignored_by_description of this Ignoring.

        Describes why ignoredBy has been set to its current value.

        :param ignored_by_description: The ignored_by_description of this Ignoring.
        :type: str
        """

        if ignored_by_description is not None:
            if not isinstance(ignored_by_description, str):
                raise TypeError("Invalid type for `ignored_by_description`, type has to be `str`")

            self._ignored_by_description = ignored_by_description

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
            if issubclass(Ignoring, dict):
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
        if not isinstance(other, Ignoring):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
