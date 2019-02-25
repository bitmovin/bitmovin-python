# coding: utf-8

from bitmovin_python.models.auto_restart_configuration import AutoRestartConfiguration
from bitmovin_python.models.encoding_mode import EncodingMode
from bitmovin_python.models.live_dash_manifest import LiveDashManifest
from bitmovin_python.models.live_hls_manifest import LiveHlsManifest
from bitmovin_python.models.reupload_settings import ReuploadSettings
import pprint
import six
from datetime import datetime
from enum import Enum


class StartLiveEncodingRequest(object):
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
            'stream_key': 'str',
            'hls_manifests': 'list[LiveHlsManifest]',
            'dash_manifests': 'list[LiveDashManifest]',
            'live_encoding_mode': 'EncodingMode',
            'reupload_settings': 'ReuploadSettings',
            'auto_restart_configuration': 'AutoRestartConfiguration'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'stream_key': 'streamKey',
            'hls_manifests': 'hlsManifests',
            'dash_manifests': 'dashManifests',
            'live_encoding_mode': 'liveEncodingMode',
            'reupload_settings': 'reuploadSettings',
            'auto_restart_configuration': 'autoRestartConfiguration'
        }
        return attributes

    def __init__(self, stream_key=None, hls_manifests=None, dash_manifests=None, live_encoding_mode=None, reupload_settings=None, auto_restart_configuration=None, *args, **kwargs):

        self._stream_key = None
        self._hls_manifests = None
        self._dash_manifests = None
        self._live_encoding_mode = None
        self._reupload_settings = None
        self._auto_restart_configuration = None
        self.discriminator = None

        self.stream_key = stream_key
        if hls_manifests is not None:
            self.hls_manifests = hls_manifests
        if dash_manifests is not None:
            self.dash_manifests = dash_manifests
        if live_encoding_mode is not None:
            self.live_encoding_mode = live_encoding_mode
        if reupload_settings is not None:
            self.reupload_settings = reupload_settings
        if auto_restart_configuration is not None:
            self.auto_restart_configuration = auto_restart_configuration

    @property
    def stream_key(self):
        """Gets the stream_key of this StartLiveEncodingRequest.

        Key for the stream. (a-zA-Z, 3-20 characters)

        :return: The stream_key of this StartLiveEncodingRequest.
        :rtype: str
        """
        return self._stream_key

    @stream_key.setter
    def stream_key(self, stream_key):
        """Sets the stream_key of this StartLiveEncodingRequest.

        Key for the stream. (a-zA-Z, 3-20 characters)

        :param stream_key: The stream_key of this StartLiveEncodingRequest.
        :type: str
        """

        if stream_key is not None:
            if not isinstance(stream_key, str):
                raise TypeError("Invalid type for `stream_key`, type has to be `str`")

            self._stream_key = stream_key


    @property
    def hls_manifests(self):
        """Gets the hls_manifests of this StartLiveEncodingRequest.

        List of Hls manifests to use for this live encoding

        :return: The hls_manifests of this StartLiveEncodingRequest.
        :rtype: list[LiveHlsManifest]
        """
        return self._hls_manifests

    @hls_manifests.setter
    def hls_manifests(self, hls_manifests):
        """Sets the hls_manifests of this StartLiveEncodingRequest.

        List of Hls manifests to use for this live encoding

        :param hls_manifests: The hls_manifests of this StartLiveEncodingRequest.
        :type: list[LiveHlsManifest]
        """

        if hls_manifests is not None:
            if not isinstance(hls_manifests, list):
                raise TypeError("Invalid type for `hls_manifests`, type has to be `list[LiveHlsManifest]`")

            self._hls_manifests = hls_manifests


    @property
    def dash_manifests(self):
        """Gets the dash_manifests of this StartLiveEncodingRequest.

        List of Dash manifests to use for this live encoding

        :return: The dash_manifests of this StartLiveEncodingRequest.
        :rtype: list[LiveDashManifest]
        """
        return self._dash_manifests

    @dash_manifests.setter
    def dash_manifests(self, dash_manifests):
        """Sets the dash_manifests of this StartLiveEncodingRequest.

        List of Dash manifests to use for this live encoding

        :param dash_manifests: The dash_manifests of this StartLiveEncodingRequest.
        :type: list[LiveDashManifest]
        """

        if dash_manifests is not None:
            if not isinstance(dash_manifests, list):
                raise TypeError("Invalid type for `dash_manifests`, type has to be `list[LiveDashManifest]`")

            self._dash_manifests = dash_manifests


    @property
    def live_encoding_mode(self):
        """Gets the live_encoding_mode of this StartLiveEncodingRequest.

        The pass mode of the encoding

        :return: The live_encoding_mode of this StartLiveEncodingRequest.
        :rtype: EncodingMode
        """
        return self._live_encoding_mode

    @live_encoding_mode.setter
    def live_encoding_mode(self, live_encoding_mode):
        """Sets the live_encoding_mode of this StartLiveEncodingRequest.

        The pass mode of the encoding

        :param live_encoding_mode: The live_encoding_mode of this StartLiveEncodingRequest.
        :type: EncodingMode
        """

        if live_encoding_mode is not None:
            if not isinstance(live_encoding_mode, EncodingMode):
                raise TypeError("Invalid type for `live_encoding_mode`, type has to be `EncodingMode`")

            self._live_encoding_mode = live_encoding_mode


    @property
    def reupload_settings(self):
        """Gets the reupload_settings of this StartLiveEncodingRequest.

        Reupload specific files during a live encoding. This can be helpful if an automatic life cycle policy is enabled on the output storage

        :return: The reupload_settings of this StartLiveEncodingRequest.
        :rtype: ReuploadSettings
        """
        return self._reupload_settings

    @reupload_settings.setter
    def reupload_settings(self, reupload_settings):
        """Sets the reupload_settings of this StartLiveEncodingRequest.

        Reupload specific files during a live encoding. This can be helpful if an automatic life cycle policy is enabled on the output storage

        :param reupload_settings: The reupload_settings of this StartLiveEncodingRequest.
        :type: ReuploadSettings
        """

        if reupload_settings is not None:
            if not isinstance(reupload_settings, ReuploadSettings):
                raise TypeError("Invalid type for `reupload_settings`, type has to be `ReuploadSettings`")

            self._reupload_settings = reupload_settings


    @property
    def auto_restart_configuration(self):
        """Gets the auto_restart_configuration of this StartLiveEncodingRequest.

        Configuration for auto restarting the live encoding

        :return: The auto_restart_configuration of this StartLiveEncodingRequest.
        :rtype: AutoRestartConfiguration
        """
        return self._auto_restart_configuration

    @auto_restart_configuration.setter
    def auto_restart_configuration(self, auto_restart_configuration):
        """Sets the auto_restart_configuration of this StartLiveEncodingRequest.

        Configuration for auto restarting the live encoding

        :param auto_restart_configuration: The auto_restart_configuration of this StartLiveEncodingRequest.
        :type: AutoRestartConfiguration
        """

        if auto_restart_configuration is not None:
            if not isinstance(auto_restart_configuration, AutoRestartConfiguration):
                raise TypeError("Invalid type for `auto_restart_configuration`, type has to be `AutoRestartConfiguration`")

            self._auto_restart_configuration = auto_restart_configuration

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
            if issubclass(StartLiveEncodingRequest, dict):
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
        if not isinstance(other, StartLiveEncodingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
