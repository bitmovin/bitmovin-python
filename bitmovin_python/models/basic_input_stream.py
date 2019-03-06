# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.input_stream_type import InputStreamType
import pprint
import six
from datetime import datetime
from enum import Enum


class BasicInputStream(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(BasicInputStream, self).openapi_types
        types.update({
            'type': 'InputStreamType'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(BasicInputStream, self).attribute_map
        attributes.update({
            'type': 'type'
        })
        return attributes

    discriminator_value_class_map = {
        'INGEST': 'IngestInputStream',
        'CONCATENATION': 'ConcatenationInputStream',
        'TRIMMING_TIME_BASED': 'TimeBasedTrimmingInputStream',
        'TRIMMING_TIME_CODE_TRACK': 'TimecodeTrackTrimmingInputStream',
        'TRIMMING_H264_PICTURE_TIMING': 'H264PictureTimingTrimmingInputStream'
    }

    def __init__(self, type=None, *args, **kwargs):
        super(BasicInputStream, self).__init__(*args, **kwargs)

        self._type = None
        self.discriminator = 'type'

        if type is not None:
            self.type = type

    @property
    def type(self):
        """Gets the type of this BasicInputStream.

        The input stream type

        :return: The type of this BasicInputStream.
        :rtype: InputStreamType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BasicInputStream.

        The input stream type

        :param type: The type of this BasicInputStream.
        :type: InputStreamType
        """

        if type is not None:
            if not isinstance(type, InputStreamType):
                raise TypeError("Invalid type for `type`, type has to be `InputStreamType`")

            self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator]
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(BasicInputStream, self).to_dict()

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
            if issubclass(BasicInputStream, dict):
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
        if not isinstance(other, BasicInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
