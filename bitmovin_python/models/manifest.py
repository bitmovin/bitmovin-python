# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.encoding_output import EncodingOutput
from bitmovin_python.models.manifest_type import ManifestType
import pprint
import six
from datetime import datetime
from enum import Enum


class Manifest(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Manifest, self).openapi_types
        types.update({
            'type': 'ManifestType',
            'outputs': 'list[EncodingOutput]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Manifest, self).attribute_map
        attributes.update({
            'type': 'type',
            'outputs': 'outputs'
        })
        return attributes

    def __init__(self, type=None, outputs=None, *args, **kwargs):
        super(Manifest, self).__init__(*args, **kwargs)

        self._type = None
        self._outputs = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.outputs = outputs

    @property
    def type(self):
        """Gets the type of this Manifest.


        :return: The type of this Manifest.
        :rtype: ManifestType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Manifest.


        :param type: The type of this Manifest.
        :type: ManifestType
        """

        if type is not None:
            if not isinstance(type, ManifestType):
                raise TypeError("Invalid type for `type`, type has to be `ManifestType`")

            self._type = type


    @property
    def outputs(self):
        """Gets the outputs of this Manifest.

        The outputs to store the manifest

        :return: The outputs of this Manifest.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this Manifest.

        The outputs to store the manifest

        :param outputs: The outputs of this Manifest.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

            self._outputs = outputs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Manifest, self).to_dict()

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
            if issubclass(Manifest, dict):
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
        if not isinstance(other, Manifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
