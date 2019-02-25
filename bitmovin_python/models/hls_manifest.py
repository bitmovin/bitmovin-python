# coding: utf-8

from bitmovin_python.models.encoding_output import EncodingOutput
from bitmovin_python.models.hls_version import HlsVersion
from bitmovin_python.models.manifest import Manifest
from bitmovin_python.models.manifest_type import ManifestType
import pprint
import six
from datetime import datetime
from enum import Enum


class HlsManifest(Manifest):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(HlsManifest, self).openapi_types
        types.update({
            'manifest_name': 'str',
            'hls_media_playlist_version': 'HlsVersion',
            'hls_master_playlist_version': 'HlsVersion'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(HlsManifest, self).attribute_map
        attributes.update({
            'manifest_name': 'manifestName',
            'hls_media_playlist_version': 'hlsMediaPlaylistVersion',
            'hls_master_playlist_version': 'hlsMasterPlaylistVersion'
        })
        return attributes

    def __init__(self, manifest_name=None, hls_media_playlist_version=None, hls_master_playlist_version=None, *args, **kwargs):
        super(HlsManifest, self).__init__(*args, **kwargs)

        self._manifest_name = None
        self._hls_media_playlist_version = None
        self._hls_master_playlist_version = None
        self.discriminator = None

        self.manifest_name = manifest_name
        if hls_media_playlist_version is not None:
            self.hls_media_playlist_version = hls_media_playlist_version
        if hls_master_playlist_version is not None:
            self.hls_master_playlist_version = hls_master_playlist_version

    @property
    def manifest_name(self):
        """Gets the manifest_name of this HlsManifest.

        The filename of your manifest

        :return: The manifest_name of this HlsManifest.
        :rtype: str
        """
        return self._manifest_name

    @manifest_name.setter
    def manifest_name(self, manifest_name):
        """Sets the manifest_name of this HlsManifest.

        The filename of your manifest

        :param manifest_name: The manifest_name of this HlsManifest.
        :type: str
        """

        if manifest_name is not None:
            if not isinstance(manifest_name, str):
                raise TypeError("Invalid type for `manifest_name`, type has to be `str`")

            self._manifest_name = manifest_name


    @property
    def hls_media_playlist_version(self):
        """Gets the hls_media_playlist_version of this HlsManifest.

        If this is set, the EXT-X-VERSION tags of the Media Playlists are set to the provided version

        :return: The hls_media_playlist_version of this HlsManifest.
        :rtype: HlsVersion
        """
        return self._hls_media_playlist_version

    @hls_media_playlist_version.setter
    def hls_media_playlist_version(self, hls_media_playlist_version):
        """Sets the hls_media_playlist_version of this HlsManifest.

        If this is set, the EXT-X-VERSION tags of the Media Playlists are set to the provided version

        :param hls_media_playlist_version: The hls_media_playlist_version of this HlsManifest.
        :type: HlsVersion
        """

        if hls_media_playlist_version is not None:
            if not isinstance(hls_media_playlist_version, HlsVersion):
                raise TypeError("Invalid type for `hls_media_playlist_version`, type has to be `HlsVersion`")

            self._hls_media_playlist_version = hls_media_playlist_version


    @property
    def hls_master_playlist_version(self):
        """Gets the hls_master_playlist_version of this HlsManifest.

        If this is set, the EXT-X-VERSION tag of the Master Playlist is set to the provided version

        :return: The hls_master_playlist_version of this HlsManifest.
        :rtype: HlsVersion
        """
        return self._hls_master_playlist_version

    @hls_master_playlist_version.setter
    def hls_master_playlist_version(self, hls_master_playlist_version):
        """Sets the hls_master_playlist_version of this HlsManifest.

        If this is set, the EXT-X-VERSION tag of the Master Playlist is set to the provided version

        :param hls_master_playlist_version: The hls_master_playlist_version of this HlsManifest.
        :type: HlsVersion
        """

        if hls_master_playlist_version is not None:
            if not isinstance(hls_master_playlist_version, HlsVersion):
                raise TypeError("Invalid type for `hls_master_playlist_version`, type has to be `HlsVersion`")

            self._hls_master_playlist_version = hls_master_playlist_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(HlsManifest, self).to_dict()

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
            if issubclass(HlsManifest, dict):
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
        if not isinstance(other, HlsManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
