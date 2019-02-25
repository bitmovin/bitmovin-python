# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.codec_config_type import CodecConfigType
import pprint
import six
from datetime import datetime
from enum import Enum


class CodecConfiguration(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(CodecConfiguration, self).openapi_types
        types.update({
            'type': 'CodecConfigType'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(CodecConfiguration, self).attribute_map
        attributes.update({
            'type': 'type'
        })
        return attributes

    discriminator_value_class_map = {
        'AAC': 'AacAudioConfiguration',
        'HE_AAC_V1': 'HeAacV1AudioConfiguration',
        'HE_AAC_V2': 'HeAacV2AudioConfiguration',
        'H264': 'H264VideoConfiguration',
        'H265': 'H265VideoConfiguration',
        'VP9': 'Vp9VideoConfiguration',
        'VP8': 'Vp8VideoConfiguration',
        'MP2': 'Mp2AudioConfiguration',
        'MP3': 'Mp3AudioConfiguration',
        'AC3': 'Ac3AudioConfiguration',
        'EAC3': 'Eac3AudioConfiguration',
        'OPUS': 'OpusAudioConfiguration',
        'VORBIS': 'VorbisAudioConfiguration',
        'MJPEG': 'MjpegVideoConfiguration',
        'AV1': 'Av1VideoConfiguration'
    }

    def __init__(self, type=None, *args, **kwargs):
        super(CodecConfiguration, self).__init__(*args, **kwargs)

        self._type = None
        self.discriminator = 'type'

        if type is not None:
            self.type = type

    @property
    def type(self):
        """Gets the type of this CodecConfiguration.

        The type of the codec configuration

        :return: The type of this CodecConfiguration.
        :rtype: CodecConfigType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CodecConfiguration.

        The type of the codec configuration

        :param type: The type of this CodecConfiguration.
        :type: CodecConfigType
        """

        if type is not None:
            if not isinstance(type, CodecConfigType):
                raise TypeError("Invalid type for `type`, type has to be `CodecConfigType`")

            self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator]
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(CodecConfiguration, self).to_dict()

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
            if issubclass(CodecConfiguration, dict):
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
        if not isinstance(other, CodecConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
