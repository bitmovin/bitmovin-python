# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from enum import Enum


class SmoothStreamingRepresentation(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(SmoothStreamingRepresentation, self).openapi_types
        types.update({
            'encoding_id': 'str',
            'muxing_id': 'str',
            'media_file': 'str',
            'language': 'str',
            'track_name': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(SmoothStreamingRepresentation, self).attribute_map
        attributes.update({
            'encoding_id': 'encodingId',
            'muxing_id': 'muxingId',
            'media_file': 'mediaFile',
            'language': 'language',
            'track_name': 'trackName'
        })
        return attributes

    def __init__(self, encoding_id=None, muxing_id=None, media_file=None, language=None, track_name=None, *args, **kwargs):
        super(SmoothStreamingRepresentation, self).__init__(*args, **kwargs)

        self._encoding_id = None
        self._muxing_id = None
        self._media_file = None
        self._language = None
        self._track_name = None
        self.discriminator = None

        self.encoding_id = encoding_id
        self.muxing_id = muxing_id
        self.media_file = media_file
        if language is not None:
            self.language = language
        if track_name is not None:
            self.track_name = track_name

    @property
    def encoding_id(self):
        """Gets the encoding_id of this SmoothStreamingRepresentation.

        Id of the encoding

        :return: The encoding_id of this SmoothStreamingRepresentation.
        :rtype: str
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        """Sets the encoding_id of this SmoothStreamingRepresentation.

        Id of the encoding

        :param encoding_id: The encoding_id of this SmoothStreamingRepresentation.
        :type: str
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, str):
                raise TypeError("Invalid type for `encoding_id`, type has to be `str`")

            self._encoding_id = encoding_id


    @property
    def muxing_id(self):
        """Gets the muxing_id of this SmoothStreamingRepresentation.

        Id of the muxing.

        :return: The muxing_id of this SmoothStreamingRepresentation.
        :rtype: str
        """
        return self._muxing_id

    @muxing_id.setter
    def muxing_id(self, muxing_id):
        """Sets the muxing_id of this SmoothStreamingRepresentation.

        Id of the muxing.

        :param muxing_id: The muxing_id of this SmoothStreamingRepresentation.
        :type: str
        """

        if muxing_id is not None:
            if not isinstance(muxing_id, str):
                raise TypeError("Invalid type for `muxing_id`, type has to be `str`")

            self._muxing_id = muxing_id


    @property
    def media_file(self):
        """Gets the media_file of this SmoothStreamingRepresentation.

        The Smooth Streaming ismv or isma file that will be referenced in the manifest.

        :return: The media_file of this SmoothStreamingRepresentation.
        :rtype: str
        """
        return self._media_file

    @media_file.setter
    def media_file(self, media_file):
        """Sets the media_file of this SmoothStreamingRepresentation.

        The Smooth Streaming ismv or isma file that will be referenced in the manifest.

        :param media_file: The media_file of this SmoothStreamingRepresentation.
        :type: str
        """

        if media_file is not None:
            if not isinstance(media_file, str):
                raise TypeError("Invalid type for `media_file`, type has to be `str`")

            self._media_file = media_file


    @property
    def language(self):
        """Gets the language of this SmoothStreamingRepresentation.

        Language of the MP4 file

        :return: The language of this SmoothStreamingRepresentation.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SmoothStreamingRepresentation.

        Language of the MP4 file

        :param language: The language of this SmoothStreamingRepresentation.
        :type: str
        """

        if language is not None:
            if not isinstance(language, str):
                raise TypeError("Invalid type for `language`, type has to be `str`")

            self._language = language


    @property
    def track_name(self):
        """Gets the track_name of this SmoothStreamingRepresentation.

        Track where this MP4 shoudl be added

        :return: The track_name of this SmoothStreamingRepresentation.
        :rtype: str
        """
        return self._track_name

    @track_name.setter
    def track_name(self, track_name):
        """Sets the track_name of this SmoothStreamingRepresentation.

        Track where this MP4 shoudl be added

        :param track_name: The track_name of this SmoothStreamingRepresentation.
        :type: str
        """

        if track_name is not None:
            if not isinstance(track_name, str):
                raise TypeError("Invalid type for `track_name`, type has to be `str`")

            self._track_name = track_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(SmoothStreamingRepresentation, self).to_dict()

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
            if issubclass(SmoothStreamingRepresentation, dict):
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
        if not isinstance(other, SmoothStreamingRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
