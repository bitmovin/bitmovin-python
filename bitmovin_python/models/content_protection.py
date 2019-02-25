# coding: utf-8

from bitmovin_python.models.dash_representation import DashRepresentation
import pprint
import six
from datetime import datetime
from enum import Enum


class ContentProtection(DashRepresentation):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(ContentProtection, self).openapi_types
        types.update({
            'drm_id': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(ContentProtection, self).attribute_map
        attributes.update({
            'drm_id': 'drmId'
        })
        return attributes

    def __init__(self, drm_id=None, *args, **kwargs):
        super(ContentProtection, self).__init__(*args, **kwargs)

        self._drm_id = None
        self.discriminator = None

        self.drm_id = drm_id

    @property
    def drm_id(self):
        """Gets the drm_id of this ContentProtection.

        DRM Id

        :return: The drm_id of this ContentProtection.
        :rtype: str
        """
        return self._drm_id

    @drm_id.setter
    def drm_id(self, drm_id):
        """Sets the drm_id of this ContentProtection.

        DRM Id

        :param drm_id: The drm_id of this ContentProtection.
        :type: str
        """

        if drm_id is not None:
            if not isinstance(drm_id, str):
                raise TypeError("Invalid type for `drm_id`, type has to be `str`")

            self._drm_id = drm_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(ContentProtection, self).to_dict()

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
            if issubclass(ContentProtection, dict):
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
        if not isinstance(other, ContentProtection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
