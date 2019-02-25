# coding: utf-8

from bitmovin_python.models.bitmovin_response import BitmovinResponse
import pprint
import six
from datetime import datetime
from enum import Enum


class PlayerVersion(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(PlayerVersion, self).openapi_types
        types.update({
            'version': 'str',
            'cdn_url': 'str',
            'download_url': 'str',
            'created_at': 'datetime'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(PlayerVersion, self).attribute_map
        attributes.update({
            'version': 'version',
            'cdn_url': 'cdnUrl',
            'download_url': 'downloadUrl',
            'created_at': 'createdAt'
        })
        return attributes

    def __init__(self, version=None, cdn_url=None, download_url=None, created_at=None, *args, **kwargs):
        super(PlayerVersion, self).__init__(*args, **kwargs)

        self._version = None
        self._cdn_url = None
        self._download_url = None
        self._created_at = None
        self.discriminator = None

        self.version = version
        self.cdn_url = cdn_url
        self.download_url = download_url
        self.created_at = created_at

    @property
    def version(self):
        """Gets the version of this PlayerVersion.

        Version of the Player

        :return: The version of this PlayerVersion.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PlayerVersion.

        Version of the Player

        :param version: The version of this PlayerVersion.
        :type: str
        """

        if version is not None:
            if not isinstance(version, str):
                raise TypeError("Invalid type for `version`, type has to be `str`")

            self._version = version


    @property
    def cdn_url(self):
        """Gets the cdn_url of this PlayerVersion.

        URL of the specified player

        :return: The cdn_url of this PlayerVersion.
        :rtype: str
        """
        return self._cdn_url

    @cdn_url.setter
    def cdn_url(self, cdn_url):
        """Sets the cdn_url of this PlayerVersion.

        URL of the specified player

        :param cdn_url: The cdn_url of this PlayerVersion.
        :type: str
        """

        if cdn_url is not None:
            if not isinstance(cdn_url, str):
                raise TypeError("Invalid type for `cdn_url`, type has to be `str`")

            self._cdn_url = cdn_url


    @property
    def download_url(self):
        """Gets the download_url of this PlayerVersion.

        Download URL of the specified player package

        :return: The download_url of this PlayerVersion.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this PlayerVersion.

        Download URL of the specified player package

        :param download_url: The download_url of this PlayerVersion.
        :type: str
        """

        if download_url is not None:
            if not isinstance(download_url, str):
                raise TypeError("Invalid type for `download_url`, type has to be `str`")

            self._download_url = download_url


    @property
    def created_at(self):
        """Gets the created_at of this PlayerVersion.

        Creation timestamp expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :return: The created_at of this PlayerVersion.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PlayerVersion.

        Creation timestamp expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :param created_at: The created_at of this PlayerVersion.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

            self._created_at = created_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(PlayerVersion, self).to_dict()

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
            if issubclass(PlayerVersion, dict):
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
        if not isinstance(other, PlayerVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
