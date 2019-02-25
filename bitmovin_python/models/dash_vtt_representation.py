# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from enum import Enum


class DashVttRepresentation(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(DashVttRepresentation, self).openapi_types
        types.update({
            'vtt_url': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(DashVttRepresentation, self).attribute_map
        attributes.update({
            'vtt_url': 'vttUrl'
        })
        return attributes

    def __init__(self, vtt_url=None, *args, **kwargs):
        super(DashVttRepresentation, self).__init__(*args, **kwargs)

        self._vtt_url = None
        self.discriminator = None

        self.vtt_url = vtt_url

    @property
    def vtt_url(self):
        """Gets the vtt_url of this DashVttRepresentation.

        URL of the referenced VTT file

        :return: The vtt_url of this DashVttRepresentation.
        :rtype: str
        """
        return self._vtt_url

    @vtt_url.setter
    def vtt_url(self, vtt_url):
        """Sets the vtt_url of this DashVttRepresentation.

        URL of the referenced VTT file

        :param vtt_url: The vtt_url of this DashVttRepresentation.
        :type: str
        """

        if vtt_url is not None:
            if not isinstance(vtt_url, str):
                raise TypeError("Invalid type for `vtt_url`, type has to be `str`")

            self._vtt_url = vtt_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(DashVttRepresentation, self).to_dict()

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
            if issubclass(DashVttRepresentation, dict):
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
        if not isinstance(other, DashVttRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
