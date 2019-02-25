# coding: utf-8

from bitmovin_python.models.encoding_output import EncodingOutput
from bitmovin_python.models.ignoring import Ignoring
from bitmovin_python.models.muxing import Muxing
from bitmovin_python.models.muxing_stream import MuxingStream
from bitmovin_python.models.muxing_type import MuxingType
from bitmovin_python.models.stream_conditions_mode import StreamConditionsMode
import pprint
import six
from datetime import datetime
from enum import Enum


class Mp3Muxing(Muxing):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Mp3Muxing, self).openapi_types
        types.update({
            'filename': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Mp3Muxing, self).attribute_map
        attributes.update({
            'filename': 'filename'
        })
        return attributes

    def __init__(self, filename=None, *args, **kwargs):
        super(Mp3Muxing, self).__init__(*args, **kwargs)

        self._filename = None
        self.discriminator = None

        self.filename = filename

    @property
    def filename(self):
        """Gets the filename of this Mp3Muxing.

        Name of the new file

        :return: The filename of this Mp3Muxing.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Mp3Muxing.

        Name of the new file

        :param filename: The filename of this Mp3Muxing.
        :type: str
        """

        if filename is not None:
            if not isinstance(filename, str):
                raise TypeError("Invalid type for `filename`, type has to be `str`")

            self._filename = filename

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Mp3Muxing, self).to_dict()

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
            if issubclass(Mp3Muxing, dict):
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
        if not isinstance(other, Mp3Muxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
