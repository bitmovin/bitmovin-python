# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class Scheduling(object):
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
            'priority': 'int',
            'prewarmed_instance_pool_ids': 'list[str]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'priority': 'priority',
            'prewarmed_instance_pool_ids': 'prewarmedInstancePoolIds'
        }
        return attributes

    def __init__(self, priority=None, prewarmed_instance_pool_ids=None, *args, **kwargs):

        self._priority = None
        self._prewarmed_instance_pool_ids = None
        self.discriminator = None

        if priority is not None:
            self.priority = priority
        if prewarmed_instance_pool_ids is not None:
            self.prewarmed_instance_pool_ids = prewarmed_instance_pool_ids

    @property
    def priority(self):
        """Gets the priority of this Scheduling.

        Specify the priority of this encoding (0 - 100). Higher numbers mean higher priority. Default is 50.

        :return: The priority of this Scheduling.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Scheduling.

        Specify the priority of this encoding (0 - 100). Higher numbers mean higher priority. Default is 50.

        :param priority: The priority of this Scheduling.
        :type: int
        """

        if priority is not None:
            if priority is not None and priority > 100:
                raise ValueError("Invalid value for `priority`, must be a value less than or equal to `100`")
            if priority is not None and priority < 0:
                raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `0`")
            if not isinstance(priority, int):
                raise TypeError("Invalid type for `priority`, type has to be `int`")

            self._priority = priority


    @property
    def prewarmed_instance_pool_ids(self):
        """Gets the prewarmed_instance_pool_ids of this Scheduling.

        List of prewarmed Instance pools. If set, prewarmed instances from pools with these IDs will be used for the Encoding if available. The pool IDs will be tried in the order in which they are passed.

        :return: The prewarmed_instance_pool_ids of this Scheduling.
        :rtype: list[str]
        """
        return self._prewarmed_instance_pool_ids

    @prewarmed_instance_pool_ids.setter
    def prewarmed_instance_pool_ids(self, prewarmed_instance_pool_ids):
        """Sets the prewarmed_instance_pool_ids of this Scheduling.

        List of prewarmed Instance pools. If set, prewarmed instances from pools with these IDs will be used for the Encoding if available. The pool IDs will be tried in the order in which they are passed.

        :param prewarmed_instance_pool_ids: The prewarmed_instance_pool_ids of this Scheduling.
        :type: list[str]
        """

        if prewarmed_instance_pool_ids is not None:
            if not isinstance(prewarmed_instance_pool_ids, list):
                raise TypeError("Invalid type for `prewarmed_instance_pool_ids`, type has to be `list[str]`")

            self._prewarmed_instance_pool_ids = prewarmed_instance_pool_ids

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
            if issubclass(Scheduling, dict):
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
        if not isinstance(other, Scheduling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
