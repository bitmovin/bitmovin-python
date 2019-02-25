# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class ReuploadSettings(object):
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
            'dash_manifest_interval': 'float',
            'hls_manifest_interval': 'float',
            'muxing_init_file_interval': 'float'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'dash_manifest_interval': 'dashManifestInterval',
            'hls_manifest_interval': 'hlsManifestInterval',
            'muxing_init_file_interval': 'muxingInitFileInterval'
        }
        return attributes

    def __init__(self, dash_manifest_interval=None, hls_manifest_interval=None, muxing_init_file_interval=None, *args, **kwargs):

        self._dash_manifest_interval = None
        self._hls_manifest_interval = None
        self._muxing_init_file_interval = None
        self.discriminator = None

        if dash_manifest_interval is not None:
            self.dash_manifest_interval = dash_manifest_interval
        if hls_manifest_interval is not None:
            self.hls_manifest_interval = hls_manifest_interval
        if muxing_init_file_interval is not None:
            self.muxing_init_file_interval = muxing_init_file_interval

    @property
    def dash_manifest_interval(self):
        """Gets the dash_manifest_interval of this ReuploadSettings.

        Interval in seconds to reupload the DASH manifest (minimum value: 30)

        :return: The dash_manifest_interval of this ReuploadSettings.
        :rtype: float
        """
        return self._dash_manifest_interval

    @dash_manifest_interval.setter
    def dash_manifest_interval(self, dash_manifest_interval):
        """Sets the dash_manifest_interval of this ReuploadSettings.

        Interval in seconds to reupload the DASH manifest (minimum value: 30)

        :param dash_manifest_interval: The dash_manifest_interval of this ReuploadSettings.
        :type: float
        """

        if dash_manifest_interval is not None:
            if dash_manifest_interval is not None and dash_manifest_interval < 30:
                raise ValueError("Invalid value for `dash_manifest_interval`, must be a value greater than or equal to `30`")
            if not isinstance(dash_manifest_interval, float):
                raise TypeError("Invalid type for `dash_manifest_interval`, type has to be `float`")

            self._dash_manifest_interval = dash_manifest_interval


    @property
    def hls_manifest_interval(self):
        """Gets the hls_manifest_interval of this ReuploadSettings.

        Interval in seconds to reupload the HLS master file. This is currently not used, as the master file will always be uploaded when one of the playlist files has changed (minimum value: 30)

        :return: The hls_manifest_interval of this ReuploadSettings.
        :rtype: float
        """
        return self._hls_manifest_interval

    @hls_manifest_interval.setter
    def hls_manifest_interval(self, hls_manifest_interval):
        """Sets the hls_manifest_interval of this ReuploadSettings.

        Interval in seconds to reupload the HLS master file. This is currently not used, as the master file will always be uploaded when one of the playlist files has changed (minimum value: 30)

        :param hls_manifest_interval: The hls_manifest_interval of this ReuploadSettings.
        :type: float
        """

        if hls_manifest_interval is not None:
            if hls_manifest_interval is not None and hls_manifest_interval < 30:
                raise ValueError("Invalid value for `hls_manifest_interval`, must be a value greater than or equal to `30`")
            if not isinstance(hls_manifest_interval, float):
                raise TypeError("Invalid type for `hls_manifest_interval`, type has to be `float`")

            self._hls_manifest_interval = hls_manifest_interval


    @property
    def muxing_init_file_interval(self):
        """Gets the muxing_init_file_interval of this ReuploadSettings.

        The interval in seconds to reupload the init file for segmented muxings (e.g. fMP4, WebM) (minimum value: 30)

        :return: The muxing_init_file_interval of this ReuploadSettings.
        :rtype: float
        """
        return self._muxing_init_file_interval

    @muxing_init_file_interval.setter
    def muxing_init_file_interval(self, muxing_init_file_interval):
        """Sets the muxing_init_file_interval of this ReuploadSettings.

        The interval in seconds to reupload the init file for segmented muxings (e.g. fMP4, WebM) (minimum value: 30)

        :param muxing_init_file_interval: The muxing_init_file_interval of this ReuploadSettings.
        :type: float
        """

        if muxing_init_file_interval is not None:
            if muxing_init_file_interval is not None and muxing_init_file_interval < 30:
                raise ValueError("Invalid value for `muxing_init_file_interval`, must be a value greater than or equal to `30`")
            if not isinstance(muxing_init_file_interval, float):
                raise TypeError("Invalid type for `muxing_init_file_interval`, type has to be `float`")

            self._muxing_init_file_interval = muxing_init_file_interval

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
            if issubclass(ReuploadSettings, dict):
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
        if not isinstance(other, ReuploadSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
