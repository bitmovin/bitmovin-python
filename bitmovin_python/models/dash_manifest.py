# coding: utf-8

from bitmovin_python.models.dash_profile import DashProfile
from bitmovin_python.models.encoding_output import EncodingOutput
from bitmovin_python.models.manifest import Manifest
from bitmovin_python.models.manifest_type import ManifestType
from bitmovin_python.models.utc_timing import UtcTiming
from bitmovin_python.models.xml_namespace import XmlNamespace
import pprint
import six
from datetime import datetime
from enum import Enum


class DashManifest(Manifest):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(DashManifest, self).openapi_types
        types.update({
            'profile': 'DashProfile',
            'manifest_name': 'str',
            'namespaces': 'list[XmlNamespace]',
            'utc_timings': 'list[UtcTiming]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(DashManifest, self).attribute_map
        attributes.update({
            'profile': 'profile',
            'manifest_name': 'manifestName',
            'namespaces': 'namespaces',
            'utc_timings': 'utcTimings'
        })
        return attributes

    def __init__(self, profile=None, manifest_name=None, namespaces=None, utc_timings=None, *args, **kwargs):
        super(DashManifest, self).__init__(*args, **kwargs)

        self._profile = None
        self._manifest_name = None
        self._namespaces = None
        self._utc_timings = None
        self.discriminator = None

        if profile is not None:
            self.profile = profile
        if manifest_name is not None:
            self.manifest_name = manifest_name
        if namespaces is not None:
            self.namespaces = namespaces
        if utc_timings is not None:
            self.utc_timings = utc_timings

    @property
    def profile(self):
        """Gets the profile of this DashManifest.


        :return: The profile of this DashManifest.
        :rtype: DashProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this DashManifest.


        :param profile: The profile of this DashManifest.
        :type: DashProfile
        """

        if profile is not None:
            if not isinstance(profile, DashProfile):
                raise TypeError("Invalid type for `profile`, type has to be `DashProfile`")

            self._profile = profile


    @property
    def manifest_name(self):
        """Gets the manifest_name of this DashManifest.

        The filename of your manifest

        :return: The manifest_name of this DashManifest.
        :rtype: str
        """
        return self._manifest_name

    @manifest_name.setter
    def manifest_name(self, manifest_name):
        """Sets the manifest_name of this DashManifest.

        The filename of your manifest

        :param manifest_name: The manifest_name of this DashManifest.
        :type: str
        """

        if manifest_name is not None:
            if not isinstance(manifest_name, str):
                raise TypeError("Invalid type for `manifest_name`, type has to be `str`")

            self._manifest_name = manifest_name


    @property
    def namespaces(self):
        """Gets the namespaces of this DashManifest.

        List of additional XML namespaces to add to the DASH Manifest

        :return: The namespaces of this DashManifest.
        :rtype: list[XmlNamespace]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this DashManifest.

        List of additional XML namespaces to add to the DASH Manifest

        :param namespaces: The namespaces of this DashManifest.
        :type: list[XmlNamespace]
        """

        if namespaces is not None:
            if not isinstance(namespaces, list):
                raise TypeError("Invalid type for `namespaces`, type has to be `list[XmlNamespace]`")

            self._namespaces = namespaces


    @property
    def utc_timings(self):
        """Gets the utc_timings of this DashManifest.

        List of UTC Timings to use for live streaming

        :return: The utc_timings of this DashManifest.
        :rtype: list[UtcTiming]
        """
        return self._utc_timings

    @utc_timings.setter
    def utc_timings(self, utc_timings):
        """Sets the utc_timings of this DashManifest.

        List of UTC Timings to use for live streaming

        :param utc_timings: The utc_timings of this DashManifest.
        :type: list[UtcTiming]
        """

        if utc_timings is not None:
            if not isinstance(utc_timings, list):
                raise TypeError("Invalid type for `utc_timings`, type has to be `list[UtcTiming]`")

            self._utc_timings = utc_timings

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(DashManifest, self).to_dict()

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
            if issubclass(DashManifest, dict):
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
        if not isinstance(other, DashManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
