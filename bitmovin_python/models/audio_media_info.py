# coding: utf-8

from bitmovin_python.models.standard_media_info import StandardMediaInfo
import pprint
import six
from datetime import datetime
from enum import Enum


class AudioMediaInfo(StandardMediaInfo):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AudioMediaInfo, self).openapi_types
        types.update({
            'forced': 'bool'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AudioMediaInfo, self).attribute_map
        attributes.update({
            'forced': 'forced'
        })
        return attributes

    def __init__(self, forced=None, *args, **kwargs):
        super(AudioMediaInfo, self).__init__(*args, **kwargs)

        self._forced = None
        self.discriminator = None

        if forced is not None:
            self.forced = forced

    @property
    def forced(self):
        """Gets the forced of this AudioMediaInfo.

        A value of true indicates that the Rendition contains content which is considered essential to play.

        :return: The forced of this AudioMediaInfo.
        :rtype: bool
        """
        return self._forced

    @forced.setter
    def forced(self, forced):
        """Sets the forced of this AudioMediaInfo.

        A value of true indicates that the Rendition contains content which is considered essential to play.

        :param forced: The forced of this AudioMediaInfo.
        :type: bool
        """

        if forced is not None:
            if not isinstance(forced, bool):
                raise TypeError("Invalid type for `forced`, type has to be `bool`")

            self._forced = forced

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AudioMediaInfo, self).to_dict()

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
            if issubclass(AudioMediaInfo, dict):
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
        if not isinstance(other, AudioMediaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
