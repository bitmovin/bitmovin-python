# coding: utf-8

from bitmovin_python.models.dash_representation import DashRepresentation
import pprint
import six
from datetime import datetime
from enum import Enum


class DashSidecarRepresentation(DashRepresentation):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(DashSidecarRepresentation, self).openapi_types
        types.update({
            'sidecar_id': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(DashSidecarRepresentation, self).attribute_map
        attributes.update({
            'sidecar_id': 'sidecarId'
        })
        return attributes

    def __init__(self, sidecar_id=None, *args, **kwargs):
        super(DashSidecarRepresentation, self).__init__(*args, **kwargs)

        self._sidecar_id = None
        self.discriminator = None

        self.sidecar_id = sidecar_id

    @property
    def sidecar_id(self):
        """Gets the sidecar_id of this DashSidecarRepresentation.

        Sidecar Id

        :return: The sidecar_id of this DashSidecarRepresentation.
        :rtype: str
        """
        return self._sidecar_id

    @sidecar_id.setter
    def sidecar_id(self, sidecar_id):
        """Sets the sidecar_id of this DashSidecarRepresentation.

        Sidecar Id

        :param sidecar_id: The sidecar_id of this DashSidecarRepresentation.
        :type: str
        """

        if sidecar_id is not None:
            if not isinstance(sidecar_id, str):
                raise TypeError("Invalid type for `sidecar_id`, type has to be `str`")

            self._sidecar_id = sidecar_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(DashSidecarRepresentation, self).to_dict()

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
            if issubclass(DashSidecarRepresentation, dict):
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
        if not isinstance(other, DashSidecarRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
