# coding: utf-8

from bitmovin_python.models.basic_media_info import BasicMediaInfo
import pprint
import six
from datetime import datetime
from enum import Enum


class VttMediaInfo(BasicMediaInfo):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(VttMediaInfo, self).openapi_types
        types.update({
            'vtt_url': 'str',
            'uri': 'str',
            'forced': 'bool'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(VttMediaInfo, self).attribute_map
        attributes.update({
            'vtt_url': 'vttUrl',
            'uri': 'uri',
            'forced': 'forced'
        })
        return attributes

    def __init__(self, vtt_url=None, uri=None, forced=None, *args, **kwargs):
        super(VttMediaInfo, self).__init__(*args, **kwargs)

        self._vtt_url = None
        self._uri = None
        self._forced = None
        self.discriminator = None

        self.vtt_url = vtt_url
        self.uri = uri
        if forced is not None:
            self.forced = forced

    @property
    def vtt_url(self):
        """Gets the vtt_url of this VttMediaInfo.

        The URL of the referenced VTT file

        :return: The vtt_url of this VttMediaInfo.
        :rtype: str
        """
        return self._vtt_url

    @vtt_url.setter
    def vtt_url(self, vtt_url):
        """Sets the vtt_url of this VttMediaInfo.

        The URL of the referenced VTT file

        :param vtt_url: The vtt_url of this VttMediaInfo.
        :type: str
        """

        if vtt_url is not None:
            if not isinstance(vtt_url, str):
                raise TypeError("Invalid type for `vtt_url`, type has to be `str`")

            self._vtt_url = vtt_url


    @property
    def uri(self):
        """Gets the uri of this VttMediaInfo.

        The URI of the Rendition

        :return: The uri of this VttMediaInfo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this VttMediaInfo.

        The URI of the Rendition

        :param uri: The uri of this VttMediaInfo.
        :type: str
        """

        if uri is not None:
            if not isinstance(uri, str):
                raise TypeError("Invalid type for `uri`, type has to be `str`")

            self._uri = uri


    @property
    def forced(self):
        """Gets the forced of this VttMediaInfo.

        A value of true indicates that the Rendition contains content which is considered essential to play.

        :return: The forced of this VttMediaInfo.
        :rtype: bool
        """
        return self._forced

    @forced.setter
    def forced(self, forced):
        """Sets the forced of this VttMediaInfo.

        A value of true indicates that the Rendition contains content which is considered essential to play.

        :param forced: The forced of this VttMediaInfo.
        :type: bool
        """

        if forced is not None:
            if not isinstance(forced, bool):
                raise TypeError("Invalid type for `forced`, type has to be `bool`")

            self._forced = forced

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(VttMediaInfo, self).to_dict()

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
            if issubclass(VttMediaInfo, dict):
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
        if not isinstance(other, VttMediaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
