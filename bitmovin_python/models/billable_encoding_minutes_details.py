# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class BillableEncodingMinutesDetails(object):
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
            'unknown': 'int',
            'audio': 'int',
            'sd': 'int',
            'hd': 'int',
            'uhd': 'int'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'unknown': 'UNKNOWN',
            'audio': 'AUDIO',
            'sd': 'SD',
            'hd': 'HD',
            'uhd': 'UHD'
        }
        return attributes

    def __init__(self, unknown=None, audio=None, sd=None, hd=None, uhd=None, *args, **kwargs):

        self._unknown = None
        self._audio = None
        self._sd = None
        self._hd = None
        self._uhd = None
        self.discriminator = None

        if unknown is not None:
            self.unknown = unknown
        if audio is not None:
            self.audio = audio
        if sd is not None:
            self.sd = sd
        if hd is not None:
            self.hd = hd
        if uhd is not None:
            self.uhd = uhd

    @property
    def unknown(self):
        """Gets the unknown of this BillableEncodingMinutesDetails.

        Only set if resolution information is not present.

        :return: The unknown of this BillableEncodingMinutesDetails.
        :rtype: int
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        """Sets the unknown of this BillableEncodingMinutesDetails.

        Only set if resolution information is not present.

        :param unknown: The unknown of this BillableEncodingMinutesDetails.
        :type: int
        """

        if unknown is not None:
            if not isinstance(unknown, int):
                raise TypeError("Invalid type for `unknown`, type has to be `int`")

            self._unknown = unknown


    @property
    def audio(self):
        """Gets the audio of this BillableEncodingMinutesDetails.

        Billable minutes for audio. Available if stream is an audio stream.

        :return: The audio of this BillableEncodingMinutesDetails.
        :rtype: int
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this BillableEncodingMinutesDetails.

        Billable minutes for audio. Available if stream is an audio stream.

        :param audio: The audio of this BillableEncodingMinutesDetails.
        :type: int
        """

        if audio is not None:
            if not isinstance(audio, int):
                raise TypeError("Invalid type for `audio`, type has to be `int`")

            self._audio = audio


    @property
    def sd(self):
        """Gets the sd of this BillableEncodingMinutesDetails.

        Billable minutes for SD resolutions.

        :return: The sd of this BillableEncodingMinutesDetails.
        :rtype: int
        """
        return self._sd

    @sd.setter
    def sd(self, sd):
        """Sets the sd of this BillableEncodingMinutesDetails.

        Billable minutes for SD resolutions.

        :param sd: The sd of this BillableEncodingMinutesDetails.
        :type: int
        """

        if sd is not None:
            if not isinstance(sd, int):
                raise TypeError("Invalid type for `sd`, type has to be `int`")

            self._sd = sd


    @property
    def hd(self):
        """Gets the hd of this BillableEncodingMinutesDetails.

        Billable minutes for HD resolutions.

        :return: The hd of this BillableEncodingMinutesDetails.
        :rtype: int
        """
        return self._hd

    @hd.setter
    def hd(self, hd):
        """Sets the hd of this BillableEncodingMinutesDetails.

        Billable minutes for HD resolutions.

        :param hd: The hd of this BillableEncodingMinutesDetails.
        :type: int
        """

        if hd is not None:
            if not isinstance(hd, int):
                raise TypeError("Invalid type for `hd`, type has to be `int`")

            self._hd = hd


    @property
    def uhd(self):
        """Gets the uhd of this BillableEncodingMinutesDetails.

        Billable minutes for UHD resolutions.

        :return: The uhd of this BillableEncodingMinutesDetails.
        :rtype: int
        """
        return self._uhd

    @uhd.setter
    def uhd(self, uhd):
        """Sets the uhd of this BillableEncodingMinutesDetails.

        Billable minutes for UHD resolutions.

        :param uhd: The uhd of this BillableEncodingMinutesDetails.
        :type: int
        """

        if uhd is not None:
            if not isinstance(uhd, int):
                raise TypeError("Invalid type for `uhd`, type has to be `int`")

            self._uhd = uhd

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
            if issubclass(BillableEncodingMinutesDetails, dict):
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
        if not isinstance(other, BillableEncodingMinutesDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
