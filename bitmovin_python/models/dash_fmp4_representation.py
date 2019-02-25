# coding: utf-8

from bitmovin_python.models.dash_muxing_type import DashMuxingType
from bitmovin_python.models.dash_segmented_representation import DashSegmentedRepresentation
import pprint
import six
from datetime import datetime
from enum import Enum


class DashFmp4Representation(DashSegmentedRepresentation):
    def __init__(self, *args, **kwargs):
        super(DashFmp4Representation, self).__init__(*args, **kwargs)
        self.discriminator = None
    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(DashFmp4Representation, self).to_dict()

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
            if issubclass(DashFmp4Representation, dict):
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
        if not isinstance(other, DashFmp4Representation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
