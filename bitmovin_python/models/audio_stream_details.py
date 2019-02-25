# coding: utf-8

from bitmovin_python.models.stream_details import StreamDetails
import pprint
import six
from datetime import datetime
from enum import Enum


class AudioStreamDetails(StreamDetails):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AudioStreamDetails, self).openapi_types
        types.update({
            'sample_rate': 'int',
            'bitrate': 'int',
            'language': 'str',
            'hearing_impaired': 'bool'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AudioStreamDetails, self).attribute_map
        attributes.update({
            'sample_rate': 'sampleRate',
            'bitrate': 'bitrate',
            'language': 'language',
            'hearing_impaired': 'hearingImpaired'
        })
        return attributes

    def __init__(self, sample_rate=None, bitrate=None, language=None, hearing_impaired=None, *args, **kwargs):
        super(AudioStreamDetails, self).__init__(*args, **kwargs)

        self._sample_rate = None
        self._bitrate = None
        self._language = None
        self._hearing_impaired = None
        self.discriminator = None

        if sample_rate is not None:
            self.sample_rate = sample_rate
        if bitrate is not None:
            self.bitrate = bitrate
        if language is not None:
            self.language = language
        if hearing_impaired is not None:
            self.hearing_impaired = hearing_impaired

    @property
    def sample_rate(self):
        """Gets the sample_rate of this AudioStreamDetails.


        :return: The sample_rate of this AudioStreamDetails.
        :rtype: int
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this AudioStreamDetails.


        :param sample_rate: The sample_rate of this AudioStreamDetails.
        :type: int
        """

        if sample_rate is not None:
            if not isinstance(sample_rate, int):
                raise TypeError("Invalid type for `sample_rate`, type has to be `int`")

            self._sample_rate = sample_rate


    @property
    def bitrate(self):
        """Gets the bitrate of this AudioStreamDetails.


        :return: The bitrate of this AudioStreamDetails.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this AudioStreamDetails.


        :param bitrate: The bitrate of this AudioStreamDetails.
        :type: int
        """

        if bitrate is not None:
            if not isinstance(bitrate, int):
                raise TypeError("Invalid type for `bitrate`, type has to be `int`")

            self._bitrate = bitrate


    @property
    def language(self):
        """Gets the language of this AudioStreamDetails.


        :return: The language of this AudioStreamDetails.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AudioStreamDetails.


        :param language: The language of this AudioStreamDetails.
        :type: str
        """

        if language is not None:
            if not isinstance(language, str):
                raise TypeError("Invalid type for `language`, type has to be `str`")

            self._language = language


    @property
    def hearing_impaired(self):
        """Gets the hearing_impaired of this AudioStreamDetails.


        :return: The hearing_impaired of this AudioStreamDetails.
        :rtype: bool
        """
        return self._hearing_impaired

    @hearing_impaired.setter
    def hearing_impaired(self, hearing_impaired):
        """Sets the hearing_impaired of this AudioStreamDetails.


        :param hearing_impaired: The hearing_impaired of this AudioStreamDetails.
        :type: bool
        """

        if hearing_impaired is not None:
            if not isinstance(hearing_impaired, bool):
                raise TypeError("Invalid type for `hearing_impaired`, type has to be `bool`")

            self._hearing_impaired = hearing_impaired

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AudioStreamDetails, self).to_dict()

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
            if issubclass(AudioStreamDetails, dict):
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
        if not isinstance(other, AudioStreamDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
