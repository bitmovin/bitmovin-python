# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class LiveDashManifest(object):
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
            'manifest_id': 'str',
            'timeshift': 'float',
            'live_edge_offset': 'float'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'manifest_id': 'manifestId',
            'timeshift': 'timeshift',
            'live_edge_offset': 'liveEdgeOffset'
        }
        return attributes

    def __init__(self, manifest_id=None, timeshift=None, live_edge_offset=None, *args, **kwargs):

        self._manifest_id = None
        self._timeshift = None
        self._live_edge_offset = None
        self.discriminator = None

        self.manifest_id = manifest_id
        if timeshift is not None:
            self.timeshift = timeshift
        if live_edge_offset is not None:
            self.live_edge_offset = live_edge_offset

    @property
    def manifest_id(self):
        """Gets the manifest_id of this LiveDashManifest.

        Dash manifest ids

        :return: The manifest_id of this LiveDashManifest.
        :rtype: str
        """
        return self._manifest_id

    @manifest_id.setter
    def manifest_id(self, manifest_id):
        """Sets the manifest_id of this LiveDashManifest.

        Dash manifest ids

        :param manifest_id: The manifest_id of this LiveDashManifest.
        :type: str
        """

        if manifest_id is not None:
            if not isinstance(manifest_id, str):
                raise TypeError("Invalid type for `manifest_id`, type has to be `str`")

            self._manifest_id = manifest_id


    @property
    def timeshift(self):
        """Gets the timeshift of this LiveDashManifest.

        Timeshift in seconds

        :return: The timeshift of this LiveDashManifest.
        :rtype: float
        """
        return self._timeshift

    @timeshift.setter
    def timeshift(self, timeshift):
        """Sets the timeshift of this LiveDashManifest.

        Timeshift in seconds

        :param timeshift: The timeshift of this LiveDashManifest.
        :type: float
        """

        if timeshift is not None:
            if not isinstance(timeshift, float):
                raise TypeError("Invalid type for `timeshift`, type has to be `float`")

            self._timeshift = timeshift


    @property
    def live_edge_offset(self):
        """Gets the live_edge_offset of this LiveDashManifest.

        Live edge offset in seconds

        :return: The live_edge_offset of this LiveDashManifest.
        :rtype: float
        """
        return self._live_edge_offset

    @live_edge_offset.setter
    def live_edge_offset(self, live_edge_offset):
        """Sets the live_edge_offset of this LiveDashManifest.

        Live edge offset in seconds

        :param live_edge_offset: The live_edge_offset of this LiveDashManifest.
        :type: float
        """

        if live_edge_offset is not None:
            if not isinstance(live_edge_offset, float):
                raise TypeError("Invalid type for `live_edge_offset`, type has to be `float`")

            self._live_edge_offset = live_edge_offset

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
            if issubclass(LiveDashManifest, dict):
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
        if not isinstance(other, LiveDashManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
