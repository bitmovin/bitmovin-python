# coding: utf-8

from bitmovin_python.models.encoding_stream_input_details import EncodingStreamInputDetails
import pprint
import six
from datetime import datetime
from enum import Enum


class EncodingStreamInput(object):
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
            'input_id': 'str',
            'input_path': 'str',
            'details': 'EncodingStreamInputDetails'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'input_id': 'inputId',
            'input_path': 'inputPath',
            'details': 'details'
        }
        return attributes

    def __init__(self, input_id=None, input_path=None, details=None, *args, **kwargs):

        self._input_id = None
        self._input_path = None
        self._details = None
        self.discriminator = None

        self.input_id = input_id
        self.input_path = input_path
        self.details = details

    @property
    def input_id(self):
        """Gets the input_id of this EncodingStreamInput.

        Input id

        :return: The input_id of this EncodingStreamInput.
        :rtype: str
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        """Sets the input_id of this EncodingStreamInput.

        Input id

        :param input_id: The input_id of this EncodingStreamInput.
        :type: str
        """

        if input_id is not None:
            if not isinstance(input_id, str):
                raise TypeError("Invalid type for `input_id`, type has to be `str`")

            self._input_id = input_id


    @property
    def input_path(self):
        """Gets the input_path of this EncodingStreamInput.

        Path to media file

        :return: The input_path of this EncodingStreamInput.
        :rtype: str
        """
        return self._input_path

    @input_path.setter
    def input_path(self, input_path):
        """Sets the input_path of this EncodingStreamInput.

        Path to media file

        :param input_path: The input_path of this EncodingStreamInput.
        :type: str
        """

        if input_path is not None:
            if not isinstance(input_path, str):
                raise TypeError("Invalid type for `input_path`, type has to be `str`")

            self._input_path = input_path


    @property
    def details(self):
        """Gets the details of this EncodingStreamInput.


        :return: The details of this EncodingStreamInput.
        :rtype: EncodingStreamInputDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this EncodingStreamInput.


        :param details: The details of this EncodingStreamInput.
        :type: EncodingStreamInputDetails
        """

        if details is not None:
            if not isinstance(details, EncodingStreamInputDetails):
                raise TypeError("Invalid type for `details`, type has to be `EncodingStreamInputDetails`")

            self._details = details

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
            if issubclass(EncodingStreamInput, dict):
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
        if not isinstance(other, EncodingStreamInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
