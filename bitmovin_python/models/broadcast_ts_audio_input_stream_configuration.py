# coding: utf-8

from bitmovin_python.models.broadcast_ts_input_stream_configuration import BroadcastTsInputStreamConfiguration
from bitmovin_python.models.rai_unit import RaiUnit
import pprint
import six
from datetime import datetime
from enum import Enum


class BroadcastTsAudioInputStreamConfiguration(BroadcastTsInputStreamConfiguration):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(BroadcastTsAudioInputStreamConfiguration, self).openapi_types
        types.update({
            'use_atsc_buffer_model': 'bool',
            'language': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(BroadcastTsAudioInputStreamConfiguration, self).attribute_map
        attributes.update({
            'use_atsc_buffer_model': 'useATSCBufferModel',
            'language': 'language'
        })
        return attributes

    def __init__(self, use_atsc_buffer_model=None, language=None, *args, **kwargs):
        super(BroadcastTsAudioInputStreamConfiguration, self).__init__(*args, **kwargs)

        self._use_atsc_buffer_model = None
        self._language = None
        self.discriminator = None

        if use_atsc_buffer_model is not None:
            self.use_atsc_buffer_model = use_atsc_buffer_model
        if language is not None:
            self.language = language

    @property
    def use_atsc_buffer_model(self):
        """Gets the use_atsc_buffer_model of this BroadcastTsAudioInputStreamConfiguration.

        Use ATSC buffer model for AC-3. If true, use the ATSC version of the T-STD buffer model is used. This parameter applies to AC-3 streams only.

        :return: The use_atsc_buffer_model of this BroadcastTsAudioInputStreamConfiguration.
        :rtype: bool
        """
        return self._use_atsc_buffer_model

    @use_atsc_buffer_model.setter
    def use_atsc_buffer_model(self, use_atsc_buffer_model):
        """Sets the use_atsc_buffer_model of this BroadcastTsAudioInputStreamConfiguration.

        Use ATSC buffer model for AC-3. If true, use the ATSC version of the T-STD buffer model is used. This parameter applies to AC-3 streams only.

        :param use_atsc_buffer_model: The use_atsc_buffer_model of this BroadcastTsAudioInputStreamConfiguration.
        :type: bool
        """

        if use_atsc_buffer_model is not None:
            if not isinstance(use_atsc_buffer_model, bool):
                raise TypeError("Invalid type for `use_atsc_buffer_model`, type has to be `bool`")

            self._use_atsc_buffer_model = use_atsc_buffer_model


    @property
    def language(self):
        """Gets the language of this BroadcastTsAudioInputStreamConfiguration.

        Language of the audio stream. Specified according to the ISO 639-2 alpha code for the language descriptor.

        :return: The language of this BroadcastTsAudioInputStreamConfiguration.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this BroadcastTsAudioInputStreamConfiguration.

        Language of the audio stream. Specified according to the ISO 639-2 alpha code for the language descriptor.

        :param language: The language of this BroadcastTsAudioInputStreamConfiguration.
        :type: str
        """

        if language is not None:
            if not isinstance(language, str):
                raise TypeError("Invalid type for `language`, type has to be `str`")

            self._language = language

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(BroadcastTsAudioInputStreamConfiguration, self).to_dict()

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
            if issubclass(BroadcastTsAudioInputStreamConfiguration, dict):
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
        if not isinstance(other, BroadcastTsAudioInputStreamConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
