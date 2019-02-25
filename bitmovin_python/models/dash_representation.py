# coding: utf-8

from bitmovin_python.models.bitmovin_response import BitmovinResponse
import pprint
import six
from datetime import datetime
from enum import Enum


class DashRepresentation(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(DashRepresentation, self).openapi_types
        types.update({
            'encoding_id': 'str',
            'muxing_id': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(DashRepresentation, self).attribute_map
        attributes.update({
            'encoding_id': 'encodingId',
            'muxing_id': 'muxingId'
        })
        return attributes

    def __init__(self, encoding_id=None, muxing_id=None, *args, **kwargs):
        super(DashRepresentation, self).__init__(*args, **kwargs)

        self._encoding_id = None
        self._muxing_id = None
        self.discriminator = None

        self.encoding_id = encoding_id
        self.muxing_id = muxing_id

    @property
    def encoding_id(self):
        """Gets the encoding_id of this DashRepresentation.

        UUID of an encoding

        :return: The encoding_id of this DashRepresentation.
        :rtype: str
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        """Sets the encoding_id of this DashRepresentation.

        UUID of an encoding

        :param encoding_id: The encoding_id of this DashRepresentation.
        :type: str
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, str):
                raise TypeError("Invalid type for `encoding_id`, type has to be `str`")

            self._encoding_id = encoding_id


    @property
    def muxing_id(self):
        """Gets the muxing_id of this DashRepresentation.

        UUID of a muxing

        :return: The muxing_id of this DashRepresentation.
        :rtype: str
        """
        return self._muxing_id

    @muxing_id.setter
    def muxing_id(self, muxing_id):
        """Sets the muxing_id of this DashRepresentation.

        UUID of a muxing

        :param muxing_id: The muxing_id of this DashRepresentation.
        :type: str
        """

        if muxing_id is not None:
            if not isinstance(muxing_id, str):
                raise TypeError("Invalid type for `muxing_id`, type has to be `str`")

            self._muxing_id = muxing_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(DashRepresentation, self).to_dict()

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
            if issubclass(DashRepresentation, dict):
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
        if not isinstance(other, DashRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
