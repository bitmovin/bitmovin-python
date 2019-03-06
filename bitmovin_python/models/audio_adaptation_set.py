# coding: utf-8

from bitmovin_python.models.accessibility import Accessibility
from bitmovin_python.models.adaptation_set import AdaptationSet
from bitmovin_python.models.adaptation_set_role import AdaptationSetRole
from bitmovin_python.models.custom_attribute import CustomAttribute
import pprint
import six
from datetime import datetime
from enum import Enum


class AudioAdaptationSet(AdaptationSet):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AudioAdaptationSet, self).openapi_types
        types.update({
            'lang': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AudioAdaptationSet, self).attribute_map
        attributes.update({
            'lang': 'lang'
        })
        return attributes

    def __init__(self, lang=None, *args, **kwargs):
        super(AudioAdaptationSet, self).__init__(*args, **kwargs)

        self._lang = None
        self.discriminator = None

        self.lang = lang

    @property
    def lang(self):
        """Gets the lang of this AudioAdaptationSet.

        ISO 639-1 (Alpha-2) code identifying the language of the audio adaptation set

        :return: The lang of this AudioAdaptationSet.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this AudioAdaptationSet.

        ISO 639-1 (Alpha-2) code identifying the language of the audio adaptation set

        :param lang: The lang of this AudioAdaptationSet.
        :type: str
        """

        if lang is not None:
            if not isinstance(lang, str):
                raise TypeError("Invalid type for `lang`, type has to be `str`")

            self._lang = lang

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AudioAdaptationSet, self).to_dict()

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
            if issubclass(AudioAdaptationSet, dict):
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
        if not isinstance(other, AudioAdaptationSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
