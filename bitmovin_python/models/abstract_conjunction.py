# coding: utf-8

from bitmovin_python.models.abstract_condition import AbstractCondition
from bitmovin_python.models.condition_type import ConditionType
import pprint
import six
from datetime import datetime
from enum import Enum


class AbstractConjunction(AbstractCondition):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AbstractConjunction, self).openapi_types
        types.update({
            'conditions': 'list[AbstractCondition]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AbstractConjunction, self).attribute_map
        attributes.update({
            'conditions': 'conditions'
        })
        return attributes

    def __init__(self, conditions=None, *args, **kwargs):
        super(AbstractConjunction, self).__init__(*args, **kwargs)

        self._conditions = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions

    @property
    def conditions(self):
        """Gets the conditions of this AbstractConjunction.

        Array to perform the AND/OR evaluation on

        :return: The conditions of this AbstractConjunction.
        :rtype: list[AbstractCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this AbstractConjunction.

        Array to perform the AND/OR evaluation on

        :param conditions: The conditions of this AbstractConjunction.
        :type: list[AbstractCondition]
        """

        if conditions is not None:
            if not isinstance(conditions, list):
                raise TypeError("Invalid type for `conditions`, type has to be `list[AbstractCondition]`")

            self._conditions = conditions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AbstractConjunction, self).to_dict()

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
            if issubclass(AbstractConjunction, dict):
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
        if not isinstance(other, AbstractConjunction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
