# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class CustomPlayerBuildDownload(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = {
            'download_link': 'str',
            'expires_at': 'datetime'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'download_link': 'downloadLink',
            'expires_at': 'expiresAt'
        }
        return attributes

    def __init__(self, download_link=None, expires_at=None, *args, **kwargs):

        self._download_link = None
        self._expires_at = None
        self.discriminator = None

        self.download_link = download_link
        self.expires_at = expires_at

    @property
    def download_link(self):
        """Gets the download_link of this CustomPlayerBuildDownload.

        The link to download the custom built player

        :return: The download_link of this CustomPlayerBuildDownload.
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        """Sets the download_link of this CustomPlayerBuildDownload.

        The link to download the custom built player

        :param download_link: The download_link of this CustomPlayerBuildDownload.
        :type: str
        """

        if download_link is not None:
            if not isinstance(download_link, str):
                raise TypeError("Invalid type for `download_link`, type has to be `str`")

            self._download_link = download_link


    @property
    def expires_at(self):
        """Gets the expires_at of this CustomPlayerBuildDownload.

        Until this date the download link is valid and can be downloaded.

        :return: The expires_at of this CustomPlayerBuildDownload.
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this CustomPlayerBuildDownload.

        Until this date the download link is valid and can be downloaded.

        :param expires_at: The expires_at of this CustomPlayerBuildDownload.
        :type: datetime
        """

        if expires_at is not None:
            if not isinstance(expires_at, datetime):
                raise TypeError("Invalid type for `expires_at`, type has to be `datetime`")

            self._expires_at = expires_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

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
            if issubclass(CustomPlayerBuildDownload, dict):
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
        if not isinstance(other, CustomPlayerBuildDownload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
