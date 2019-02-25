# coding: utf-8

from bitmovin_python.models.stream_details import StreamDetails
import pprint
import six
from datetime import datetime
from enum import Enum


class SubtitleStreamDetails(StreamDetails):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(SubtitleStreamDetails, self).openapi_types
        types.update({
            'language': 'str',
            'hearing_impaired': 'bool'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(SubtitleStreamDetails, self).attribute_map
        attributes.update({
            'language': 'language',
            'hearing_impaired': 'hearingImpaired'
        })
        return attributes

    def __init__(self, language=None, hearing_impaired=None, *args, **kwargs):
        super(SubtitleStreamDetails, self).__init__(*args, **kwargs)

        self._language = None
        self._hearing_impaired = None
        self.discriminator = None

        if language is not None:
            self.language = language
        if hearing_impaired is not None:
            self.hearing_impaired = hearing_impaired

    @property
    def language(self):
        """Gets the language of this SubtitleStreamDetails.


        :return: The language of this SubtitleStreamDetails.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SubtitleStreamDetails.


        :param language: The language of this SubtitleStreamDetails.
        :type: str
        """

        if language is not None:
            if not isinstance(language, str):
                raise TypeError("Invalid type for `language`, type has to be `str`")

            self._language = language


    @property
    def hearing_impaired(self):
        """Gets the hearing_impaired of this SubtitleStreamDetails.


        :return: The hearing_impaired of this SubtitleStreamDetails.
        :rtype: bool
        """
        return self._hearing_impaired

    @hearing_impaired.setter
    def hearing_impaired(self, hearing_impaired):
        """Sets the hearing_impaired of this SubtitleStreamDetails.


        :param hearing_impaired: The hearing_impaired of this SubtitleStreamDetails.
        :type: bool
        """

        if hearing_impaired is not None:
            if not isinstance(hearing_impaired, bool):
                raise TypeError("Invalid type for `hearing_impaired`, type has to be `bool`")

            self._hearing_impaired = hearing_impaired

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(SubtitleStreamDetails, self).to_dict()

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
            if issubclass(SubtitleStreamDetails, dict):
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
        if not isinstance(other, SubtitleStreamDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
