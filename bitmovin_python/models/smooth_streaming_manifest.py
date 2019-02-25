# coding: utf-8

from bitmovin_python.models.encoding_output import EncodingOutput
from bitmovin_python.models.manifest import Manifest
from bitmovin_python.models.manifest_type import ManifestType
import pprint
import six
from datetime import datetime
from enum import Enum


class SmoothStreamingManifest(Manifest):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(SmoothStreamingManifest, self).openapi_types
        types.update({
            'server_manifest_name': 'str',
            'client_manifest_name': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(SmoothStreamingManifest, self).attribute_map
        attributes.update({
            'server_manifest_name': 'serverManifestName',
            'client_manifest_name': 'clientManifestName'
        })
        return attributes

    def __init__(self, server_manifest_name=None, client_manifest_name=None, *args, **kwargs):
        super(SmoothStreamingManifest, self).__init__(*args, **kwargs)

        self._server_manifest_name = None
        self._client_manifest_name = None
        self.discriminator = None

        if server_manifest_name is not None:
            self.server_manifest_name = server_manifest_name
        if client_manifest_name is not None:
            self.client_manifest_name = client_manifest_name

    @property
    def server_manifest_name(self):
        """Gets the server_manifest_name of this SmoothStreamingManifest.

        Filename of the server manifest

        :return: The server_manifest_name of this SmoothStreamingManifest.
        :rtype: str
        """
        return self._server_manifest_name

    @server_manifest_name.setter
    def server_manifest_name(self, server_manifest_name):
        """Sets the server_manifest_name of this SmoothStreamingManifest.

        Filename of the server manifest

        :param server_manifest_name: The server_manifest_name of this SmoothStreamingManifest.
        :type: str
        """

        if server_manifest_name is not None:
            if not isinstance(server_manifest_name, str):
                raise TypeError("Invalid type for `server_manifest_name`, type has to be `str`")

            self._server_manifest_name = server_manifest_name


    @property
    def client_manifest_name(self):
        """Gets the client_manifest_name of this SmoothStreamingManifest.

        Filename of the client manifest

        :return: The client_manifest_name of this SmoothStreamingManifest.
        :rtype: str
        """
        return self._client_manifest_name

    @client_manifest_name.setter
    def client_manifest_name(self, client_manifest_name):
        """Sets the client_manifest_name of this SmoothStreamingManifest.

        Filename of the client manifest

        :param client_manifest_name: The client_manifest_name of this SmoothStreamingManifest.
        :type: str
        """

        if client_manifest_name is not None:
            if not isinstance(client_manifest_name, str):
                raise TypeError("Invalid type for `client_manifest_name`, type has to be `str`")

            self._client_manifest_name = client_manifest_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(SmoothStreamingManifest, self).to_dict()

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
            if issubclass(SmoothStreamingManifest, dict):
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
        if not isinstance(other, SmoothStreamingManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
