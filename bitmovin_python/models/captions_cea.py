# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.encoding_output import EncodingOutput
from bitmovin_python.models.input_stream import InputStream
from bitmovin_python.models.output_format import OutputFormat
import pprint
import six
from datetime import datetime
from enum import Enum


class CaptionsCea(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(CaptionsCea, self).openapi_types
        types.update({
            'channel': 'int',
            'input_stream': 'InputStream',
            'output_format': 'OutputFormat',
            'filename': 'str',
            'outputs': 'list[EncodingOutput]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(CaptionsCea, self).attribute_map
        attributes.update({
            'channel': 'channel',
            'input_stream': 'inputStream',
            'output_format': 'outputFormat',
            'filename': 'filename',
            'outputs': 'outputs'
        })
        return attributes

    def __init__(self, channel=None, input_stream=None, output_format=None, filename=None, outputs=None, *args, **kwargs):
        super(CaptionsCea, self).__init__(*args, **kwargs)

        self._channel = None
        self._input_stream = None
        self._output_format = None
        self._filename = None
        self._outputs = None
        self.discriminator = None

        if channel is not None:
            self.channel = channel
        self.input_stream = input_stream
        self.output_format = output_format
        if filename is not None:
            self.filename = filename
        self.outputs = outputs

    @property
    def channel(self):
        """Gets the channel of this CaptionsCea.

        Select the channel for the caption information

        :return: The channel of this CaptionsCea.
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this CaptionsCea.

        Select the channel for the caption information

        :param channel: The channel of this CaptionsCea.
        :type: int
        """

        if channel is not None:
            if not isinstance(channel, int):
                raise TypeError("Invalid type for `channel`, type has to be `int`")

            self._channel = channel


    @property
    def input_stream(self):
        """Gets the input_stream of this CaptionsCea.

        The input stream to extract the subtitle from

        :return: The input_stream of this CaptionsCea.
        :rtype: InputStream
        """
        return self._input_stream

    @input_stream.setter
    def input_stream(self, input_stream):
        """Sets the input_stream of this CaptionsCea.

        The input stream to extract the subtitle from

        :param input_stream: The input_stream of this CaptionsCea.
        :type: InputStream
        """

        if input_stream is not None:
            if not isinstance(input_stream, InputStream):
                raise TypeError("Invalid type for `input_stream`, type has to be `InputStream`")

            self._input_stream = input_stream


    @property
    def output_format(self):
        """Gets the output_format of this CaptionsCea.


        :return: The output_format of this CaptionsCea.
        :rtype: OutputFormat
        """
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        """Sets the output_format of this CaptionsCea.


        :param output_format: The output_format of this CaptionsCea.
        :type: OutputFormat
        """

        if output_format is not None:
            if not isinstance(output_format, OutputFormat):
                raise TypeError("Invalid type for `output_format`, type has to be `OutputFormat`")

            self._output_format = output_format


    @property
    def filename(self):
        """Gets the filename of this CaptionsCea.

        Name of the captions file

        :return: The filename of this CaptionsCea.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this CaptionsCea.

        Name of the captions file

        :param filename: The filename of this CaptionsCea.
        :type: str
        """

        if filename is not None:
            if not isinstance(filename, str):
                raise TypeError("Invalid type for `filename`, type has to be `str`")

            self._filename = filename


    @property
    def outputs(self):
        """Gets the outputs of this CaptionsCea.


        :return: The outputs of this CaptionsCea.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this CaptionsCea.


        :param outputs: The outputs of this CaptionsCea.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

            self._outputs = outputs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(CaptionsCea, self).to_dict()

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
            if issubclass(CaptionsCea, dict):
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
        if not isinstance(other, CaptionsCea):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
