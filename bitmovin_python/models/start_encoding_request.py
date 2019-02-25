# coding: utf-8

from bitmovin_python.models.encoding_mode import EncodingMode
from bitmovin_python.models.manifest_resource import ManifestResource
from bitmovin_python.models.per_title import PerTitle
from bitmovin_python.models.scheduling import Scheduling
from bitmovin_python.models.trimming import Trimming
from bitmovin_python.models.tweaks import Tweaks
import pprint
import six
from datetime import datetime
from enum import Enum


class StartEncodingRequest(object):
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
            'trimming': 'Trimming',
            'scheduling': 'Scheduling',
            'tweaks': 'Tweaks',
            'handle_variable_input_fps': 'bool',
            'encoding_mode': 'EncodingMode',
            'preview_dash_manifests': 'list[ManifestResource]',
            'preview_hls_manifests': 'list[ManifestResource]',
            'vod_dash_manifests': 'list[ManifestResource]',
            'vod_hls_manifests': 'list[ManifestResource]',
            'per_title': 'PerTitle'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'trimming': 'trimming',
            'scheduling': 'scheduling',
            'tweaks': 'tweaks',
            'handle_variable_input_fps': 'handleVariableInputFps',
            'encoding_mode': 'encodingMode',
            'preview_dash_manifests': 'previewDashManifests',
            'preview_hls_manifests': 'previewHlsManifests',
            'vod_dash_manifests': 'vodDashManifests',
            'vod_hls_manifests': 'vodHlsManifests',
            'per_title': 'perTitle'
        }
        return attributes

    def __init__(self, trimming=None, scheduling=None, tweaks=None, handle_variable_input_fps=None, encoding_mode=None, preview_dash_manifests=None, preview_hls_manifests=None, vod_dash_manifests=None, vod_hls_manifests=None, per_title=None, *args, **kwargs):

        self._trimming = None
        self._scheduling = None
        self._tweaks = None
        self._handle_variable_input_fps = None
        self._encoding_mode = None
        self._preview_dash_manifests = None
        self._preview_hls_manifests = None
        self._vod_dash_manifests = None
        self._vod_hls_manifests = None
        self._per_title = None
        self.discriminator = None

        if trimming is not None:
            self.trimming = trimming
        if scheduling is not None:
            self.scheduling = scheduling
        if tweaks is not None:
            self.tweaks = tweaks
        if handle_variable_input_fps is not None:
            self.handle_variable_input_fps = handle_variable_input_fps
        if encoding_mode is not None:
            self.encoding_mode = encoding_mode
        if preview_dash_manifests is not None:
            self.preview_dash_manifests = preview_dash_manifests
        if preview_hls_manifests is not None:
            self.preview_hls_manifests = preview_hls_manifests
        if vod_dash_manifests is not None:
            self.vod_dash_manifests = vod_dash_manifests
        if vod_hls_manifests is not None:
            self.vod_hls_manifests = vod_hls_manifests
        if per_title is not None:
            self.per_title = per_title

    @property
    def trimming(self):
        """Gets the trimming of this StartEncodingRequest.

        Allows to encode only part of the input. Defines start (offset) and duration of the desired section.

        :return: The trimming of this StartEncodingRequest.
        :rtype: Trimming
        """
        return self._trimming

    @trimming.setter
    def trimming(self, trimming):
        """Sets the trimming of this StartEncodingRequest.

        Allows to encode only part of the input. Defines start (offset) and duration of the desired section.

        :param trimming: The trimming of this StartEncodingRequest.
        :type: Trimming
        """

        if trimming is not None:
            if not isinstance(trimming, Trimming):
                raise TypeError("Invalid type for `trimming`, type has to be `Trimming`")

            self._trimming = trimming


    @property
    def scheduling(self):
        """Gets the scheduling of this StartEncodingRequest.

        Set scheduling parameters of the encoding.

        :return: The scheduling of this StartEncodingRequest.
        :rtype: Scheduling
        """
        return self._scheduling

    @scheduling.setter
    def scheduling(self, scheduling):
        """Sets the scheduling of this StartEncodingRequest.

        Set scheduling parameters of the encoding.

        :param scheduling: The scheduling of this StartEncodingRequest.
        :type: Scheduling
        """

        if scheduling is not None:
            if not isinstance(scheduling, Scheduling):
                raise TypeError("Invalid type for `scheduling`, type has to be `Scheduling`")

            self._scheduling = scheduling


    @property
    def tweaks(self):
        """Gets the tweaks of this StartEncodingRequest.

        Set special tweaks for your encoding job.

        :return: The tweaks of this StartEncodingRequest.
        :rtype: Tweaks
        """
        return self._tweaks

    @tweaks.setter
    def tweaks(self, tweaks):
        """Sets the tweaks of this StartEncodingRequest.

        Set special tweaks for your encoding job.

        :param tweaks: The tweaks of this StartEncodingRequest.
        :type: Tweaks
        """

        if tweaks is not None:
            if not isinstance(tweaks, Tweaks):
                raise TypeError("Invalid type for `tweaks`, type has to be `Tweaks`")

            self._tweaks = tweaks


    @property
    def handle_variable_input_fps(self):
        """Gets the handle_variable_input_fps of this StartEncodingRequest.

        Enable frame dropping/duplication to handle variable frames per seconds of video input streams

        :return: The handle_variable_input_fps of this StartEncodingRequest.
        :rtype: bool
        """
        return self._handle_variable_input_fps

    @handle_variable_input_fps.setter
    def handle_variable_input_fps(self, handle_variable_input_fps):
        """Sets the handle_variable_input_fps of this StartEncodingRequest.

        Enable frame dropping/duplication to handle variable frames per seconds of video input streams

        :param handle_variable_input_fps: The handle_variable_input_fps of this StartEncodingRequest.
        :type: bool
        """

        if handle_variable_input_fps is not None:
            if not isinstance(handle_variable_input_fps, bool):
                raise TypeError("Invalid type for `handle_variable_input_fps`, type has to be `bool`")

            self._handle_variable_input_fps = handle_variable_input_fps


    @property
    def encoding_mode(self):
        """Gets the encoding_mode of this StartEncodingRequest.

        The pass mode of the encoding

        :return: The encoding_mode of this StartEncodingRequest.
        :rtype: EncodingMode
        """
        return self._encoding_mode

    @encoding_mode.setter
    def encoding_mode(self, encoding_mode):
        """Sets the encoding_mode of this StartEncodingRequest.

        The pass mode of the encoding

        :param encoding_mode: The encoding_mode of this StartEncodingRequest.
        :type: EncodingMode
        """

        if encoding_mode is not None:
            if not isinstance(encoding_mode, EncodingMode):
                raise TypeError("Invalid type for `encoding_mode`, type has to be `EncodingMode`")

            self._encoding_mode = encoding_mode


    @property
    def preview_dash_manifests(self):
        """Gets the preview_dash_manifests of this StartEncodingRequest.

        List of preview DASH manifests to be created

        :return: The preview_dash_manifests of this StartEncodingRequest.
        :rtype: list[ManifestResource]
        """
        return self._preview_dash_manifests

    @preview_dash_manifests.setter
    def preview_dash_manifests(self, preview_dash_manifests):
        """Sets the preview_dash_manifests of this StartEncodingRequest.

        List of preview DASH manifests to be created

        :param preview_dash_manifests: The preview_dash_manifests of this StartEncodingRequest.
        :type: list[ManifestResource]
        """

        if preview_dash_manifests is not None:
            if not isinstance(preview_dash_manifests, list):
                raise TypeError("Invalid type for `preview_dash_manifests`, type has to be `list[ManifestResource]`")

            self._preview_dash_manifests = preview_dash_manifests


    @property
    def preview_hls_manifests(self):
        """Gets the preview_hls_manifests of this StartEncodingRequest.

        List of preview HLS manifests to be created

        :return: The preview_hls_manifests of this StartEncodingRequest.
        :rtype: list[ManifestResource]
        """
        return self._preview_hls_manifests

    @preview_hls_manifests.setter
    def preview_hls_manifests(self, preview_hls_manifests):
        """Sets the preview_hls_manifests of this StartEncodingRequest.

        List of preview HLS manifests to be created

        :param preview_hls_manifests: The preview_hls_manifests of this StartEncodingRequest.
        :type: list[ManifestResource]
        """

        if preview_hls_manifests is not None:
            if not isinstance(preview_hls_manifests, list):
                raise TypeError("Invalid type for `preview_hls_manifests`, type has to be `list[ManifestResource]`")

            self._preview_hls_manifests = preview_hls_manifests


    @property
    def vod_dash_manifests(self):
        """Gets the vod_dash_manifests of this StartEncodingRequest.

        List of VoD DASH manifests to be created after encoding finished successfully

        :return: The vod_dash_manifests of this StartEncodingRequest.
        :rtype: list[ManifestResource]
        """
        return self._vod_dash_manifests

    @vod_dash_manifests.setter
    def vod_dash_manifests(self, vod_dash_manifests):
        """Sets the vod_dash_manifests of this StartEncodingRequest.

        List of VoD DASH manifests to be created after encoding finished successfully

        :param vod_dash_manifests: The vod_dash_manifests of this StartEncodingRequest.
        :type: list[ManifestResource]
        """

        if vod_dash_manifests is not None:
            if not isinstance(vod_dash_manifests, list):
                raise TypeError("Invalid type for `vod_dash_manifests`, type has to be `list[ManifestResource]`")

            self._vod_dash_manifests = vod_dash_manifests


    @property
    def vod_hls_manifests(self):
        """Gets the vod_hls_manifests of this StartEncodingRequest.

        List of VoD HLS manifests to be created after encoding finished successfully

        :return: The vod_hls_manifests of this StartEncodingRequest.
        :rtype: list[ManifestResource]
        """
        return self._vod_hls_manifests

    @vod_hls_manifests.setter
    def vod_hls_manifests(self, vod_hls_manifests):
        """Sets the vod_hls_manifests of this StartEncodingRequest.

        List of VoD HLS manifests to be created after encoding finished successfully

        :param vod_hls_manifests: The vod_hls_manifests of this StartEncodingRequest.
        :type: list[ManifestResource]
        """

        if vod_hls_manifests is not None:
            if not isinstance(vod_hls_manifests, list):
                raise TypeError("Invalid type for `vod_hls_manifests`, type has to be `list[ManifestResource]`")

            self._vod_hls_manifests = vod_hls_manifests


    @property
    def per_title(self):
        """Gets the per_title of this StartEncodingRequest.

        Per-Title settings

        :return: The per_title of this StartEncodingRequest.
        :rtype: PerTitle
        """
        return self._per_title

    @per_title.setter
    def per_title(self, per_title):
        """Sets the per_title of this StartEncodingRequest.

        Per-Title settings

        :param per_title: The per_title of this StartEncodingRequest.
        :type: PerTitle
        """

        if per_title is not None:
            if not isinstance(per_title, PerTitle):
                raise TypeError("Invalid type for `per_title`, type has to be `PerTitle`")

            self._per_title = per_title

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
            if issubclass(StartEncodingRequest, dict):
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
        if not isinstance(other, StartEncodingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
