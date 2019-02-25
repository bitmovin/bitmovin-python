# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.encoding_output import EncodingOutput
from bitmovin_python.models.input_stream import InputStream
import pprint
import six
from datetime import datetime
from enum import Enum


class WebVttExtract(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(WebVttExtract, self).openapi_types
        types.update({
            'input_stream': 'InputStream',
            'outputs': 'list[EncodingOutput]',
            'file_name': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(WebVttExtract, self).attribute_map
        attributes.update({
            'input_stream': 'inputStream',
            'outputs': 'outputs',
            'file_name': 'fileName'
        })
        return attributes

    def __init__(self, input_stream=None, outputs=None, file_name=None, *args, **kwargs):
        super(WebVttExtract, self).__init__(*args, **kwargs)

        self._input_stream = None
        self._outputs = None
        self._file_name = None
        self.discriminator = None

        self.input_stream = input_stream
        self.outputs = outputs
        if file_name is not None:
            self.file_name = file_name

    @property
    def input_stream(self):
        """Gets the input_stream of this WebVttExtract.

        The input stream to extract the subtitle from

        :return: The input_stream of this WebVttExtract.
        :rtype: InputStream
        """
        return self._input_stream

    @input_stream.setter
    def input_stream(self, input_stream):
        """Sets the input_stream of this WebVttExtract.

        The input stream to extract the subtitle from

        :param input_stream: The input_stream of this WebVttExtract.
        :type: InputStream
        """

        if input_stream is not None:
            if not isinstance(input_stream, InputStream):
                raise TypeError("Invalid type for `input_stream`, type has to be `InputStream`")

            self._input_stream = input_stream


    @property
    def outputs(self):
        """Gets the outputs of this WebVttExtract.


        :return: The outputs of this WebVttExtract.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this WebVttExtract.


        :param outputs: The outputs of this WebVttExtract.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

            self._outputs = outputs


    @property
    def file_name(self):
        """Gets the file_name of this WebVttExtract.

        Name of the captions file

        :return: The file_name of this WebVttExtract.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this WebVttExtract.

        Name of the captions file

        :param file_name: The file_name of this WebVttExtract.
        :type: str
        """

        if file_name is not None:
            if not isinstance(file_name, str):
                raise TypeError("Invalid type for `file_name`, type has to be `str`")

            self._file_name = file_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(WebVttExtract, self).to_dict()

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
            if issubclass(WebVttExtract, dict):
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
        if not isinstance(other, WebVttExtract):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
