# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class AutoRepresentation(object):
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
            'adopt_configuration_threshold': 'float'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'adopt_configuration_threshold': 'adoptConfigurationThreshold'
        }
        return attributes

    def __init__(self, adopt_configuration_threshold=None, *args, **kwargs):

        self._adopt_configuration_threshold = None
        self.discriminator = None

        if adopt_configuration_threshold is not None:
            self.adopt_configuration_threshold = adopt_configuration_threshold

    @property
    def adopt_configuration_threshold(self):
        """Gets the adopt_configuration_threshold of this AutoRepresentation.

        This is the threshold if the settings of the lower or the upper representation (codec configuration) should be used, when representations are added automatically

        :return: The adopt_configuration_threshold of this AutoRepresentation.
        :rtype: float
        """
        return self._adopt_configuration_threshold

    @adopt_configuration_threshold.setter
    def adopt_configuration_threshold(self, adopt_configuration_threshold):
        """Sets the adopt_configuration_threshold of this AutoRepresentation.

        This is the threshold if the settings of the lower or the upper representation (codec configuration) should be used, when representations are added automatically

        :param adopt_configuration_threshold: The adopt_configuration_threshold of this AutoRepresentation.
        :type: float
        """

        if adopt_configuration_threshold is not None:
            if not isinstance(adopt_configuration_threshold, float):
                raise TypeError("Invalid type for `adopt_configuration_threshold`, type has to be `float`")

            self._adopt_configuration_threshold = adopt_configuration_threshold

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
            if issubclass(AutoRepresentation, dict):
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
        if not isinstance(other, AutoRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
