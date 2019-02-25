# coding: utf-8

from bitmovin_python.models.adaptation_set import AdaptationSet
from bitmovin_python.models.adaptation_set_role import AdaptationSetRole
from bitmovin_python.models.custom_attribute import CustomAttribute
import pprint
import six
from datetime import datetime
from enum import Enum


class VideoAdaptationSet(AdaptationSet):
    def __init__(self, *args, **kwargs):
        super(VideoAdaptationSet, self).__init__(*args, **kwargs)
        self.discriminator = None
    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(VideoAdaptationSet, self).to_dict()

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
            if issubclass(VideoAdaptationSet, dict):
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
        if not isinstance(other, VideoAdaptationSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
