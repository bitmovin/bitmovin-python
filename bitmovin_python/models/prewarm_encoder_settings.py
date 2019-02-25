# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.log_level import LogLevel
import pprint
import six
from datetime import datetime
from enum import Enum


class PrewarmEncoderSettings(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(PrewarmEncoderSettings, self).openapi_types
        types.update({
            'encoder_version': 'str',
            'min_prewarmed': 'int',
            'max_prewarmed': 'int',
            'log_level': 'LogLevel'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(PrewarmEncoderSettings, self).attribute_map
        attributes.update({
            'encoder_version': 'encoderVersion',
            'min_prewarmed': 'minPrewarmed',
            'max_prewarmed': 'maxPrewarmed',
            'log_level': 'logLevel'
        })
        return attributes

    def __init__(self, encoder_version=None, min_prewarmed=None, max_prewarmed=None, log_level=None, *args, **kwargs):
        super(PrewarmEncoderSettings, self).__init__(*args, **kwargs)

        self._encoder_version = None
        self._min_prewarmed = None
        self._max_prewarmed = None
        self._log_level = None
        self.discriminator = None

        self.encoder_version = encoder_version
        self.min_prewarmed = min_prewarmed
        if max_prewarmed is not None:
            self.max_prewarmed = max_prewarmed
        if log_level is not None:
            self.log_level = log_level

    @property
    def encoder_version(self):
        """Gets the encoder_version of this PrewarmEncoderSettings.

        Encoder Version to be prewarmed. Only one encoder of this version can be prewarmed per cluster.

        :return: The encoder_version of this PrewarmEncoderSettings.
        :rtype: str
        """
        return self._encoder_version

    @encoder_version.setter
    def encoder_version(self, encoder_version):
        """Sets the encoder_version of this PrewarmEncoderSettings.

        Encoder Version to be prewarmed. Only one encoder of this version can be prewarmed per cluster.

        :param encoder_version: The encoder_version of this PrewarmEncoderSettings.
        :type: str
        """

        if encoder_version is not None:
            if not isinstance(encoder_version, str):
                raise TypeError("Invalid type for `encoder_version`, type has to be `str`")

            self._encoder_version = encoder_version


    @property
    def min_prewarmed(self):
        """Gets the min_prewarmed of this PrewarmEncoderSettings.

        The minimum number of prewarmed encoders of this Version

        :return: The min_prewarmed of this PrewarmEncoderSettings.
        :rtype: int
        """
        return self._min_prewarmed

    @min_prewarmed.setter
    def min_prewarmed(self, min_prewarmed):
        """Sets the min_prewarmed of this PrewarmEncoderSettings.

        The minimum number of prewarmed encoders of this Version

        :param min_prewarmed: The min_prewarmed of this PrewarmEncoderSettings.
        :type: int
        """

        if min_prewarmed is not None:
            if not isinstance(min_prewarmed, int):
                raise TypeError("Invalid type for `min_prewarmed`, type has to be `int`")

            self._min_prewarmed = min_prewarmed


    @property
    def max_prewarmed(self):
        """Gets the max_prewarmed of this PrewarmEncoderSettings.

        The maximum number of concurrent prewarmed encoders of this Version

        :return: The max_prewarmed of this PrewarmEncoderSettings.
        :rtype: int
        """
        return self._max_prewarmed

    @max_prewarmed.setter
    def max_prewarmed(self, max_prewarmed):
        """Sets the max_prewarmed of this PrewarmEncoderSettings.

        The maximum number of concurrent prewarmed encoders of this Version

        :param max_prewarmed: The max_prewarmed of this PrewarmEncoderSettings.
        :type: int
        """

        if max_prewarmed is not None:
            if not isinstance(max_prewarmed, int):
                raise TypeError("Invalid type for `max_prewarmed`, type has to be `int`")

            self._max_prewarmed = max_prewarmed


    @property
    def log_level(self):
        """Gets the log_level of this PrewarmEncoderSettings.


        :return: The log_level of this PrewarmEncoderSettings.
        :rtype: LogLevel
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this PrewarmEncoderSettings.


        :param log_level: The log_level of this PrewarmEncoderSettings.
        :type: LogLevel
        """

        if log_level is not None:
            if not isinstance(log_level, LogLevel):
                raise TypeError("Invalid type for `log_level`, type has to be `LogLevel`")

            self._log_level = log_level

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(PrewarmEncoderSettings, self).to_dict()

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
            if issubclass(PrewarmEncoderSettings, dict):
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
        if not isinstance(other, PrewarmEncoderSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
