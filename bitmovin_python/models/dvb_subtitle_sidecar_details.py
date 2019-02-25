# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.input_stream import InputStream
from bitmovin_python.models.output import Output
import pprint
import six
from datetime import datetime
from enum import Enum


class DvbSubtitleSidecarDetails(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(DvbSubtitleSidecarDetails, self).openapi_types
        types.update({
            'input_stream': 'InputStream',
            'outputs': 'list[Output]',
            'image_file_naming': 'str',
            'index_filename': 'str',
            'image_format': 'str',
            'output_format': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(DvbSubtitleSidecarDetails, self).attribute_map
        attributes.update({
            'input_stream': 'inputStream',
            'outputs': 'outputs',
            'image_file_naming': 'imageFileNaming',
            'index_filename': 'indexFilename',
            'image_format': 'imageFormat',
            'output_format': 'outputFormat'
        })
        return attributes

    def __init__(self, input_stream=None, outputs=None, image_file_naming=None, index_filename=None, image_format=None, output_format=None, *args, **kwargs):
        super(DvbSubtitleSidecarDetails, self).__init__(*args, **kwargs)

        self._input_stream = None
        self._outputs = None
        self._image_file_naming = None
        self._index_filename = None
        self._image_format = None
        self._output_format = None
        self.discriminator = None

        self.input_stream = input_stream
        if outputs is not None:
            self.outputs = outputs
        if image_file_naming is not None:
            self.image_file_naming = image_file_naming
        if index_filename is not None:
            self.index_filename = index_filename
        if image_format is not None:
            self.image_format = image_format
        if output_format is not None:
            self.output_format = output_format

    @property
    def input_stream(self):
        """Gets the input_stream of this DvbSubtitleSidecarDetails.

        The input stream to extract the subtitle from

        :return: The input_stream of this DvbSubtitleSidecarDetails.
        :rtype: InputStream
        """
        return self._input_stream

    @input_stream.setter
    def input_stream(self, input_stream):
        """Sets the input_stream of this DvbSubtitleSidecarDetails.

        The input stream to extract the subtitle from

        :param input_stream: The input_stream of this DvbSubtitleSidecarDetails.
        :type: InputStream
        """

        if input_stream is not None:
            if not isinstance(input_stream, InputStream):
                raise TypeError("Invalid type for `input_stream`, type has to be `InputStream`")

            self._input_stream = input_stream


    @property
    def outputs(self):
        """Gets the outputs of this DvbSubtitleSidecarDetails.

        The output where the extracted subtitle should be written to

        :return: The outputs of this DvbSubtitleSidecarDetails.
        :rtype: list[Output]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this DvbSubtitleSidecarDetails.

        The output where the extracted subtitle should be written to

        :param outputs: The outputs of this DvbSubtitleSidecarDetails.
        :type: list[Output]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[Output]`")

            self._outputs = outputs


    @property
    def image_file_naming(self):
        """Gets the image_file_naming of this DvbSubtitleSidecarDetails.

        Naming strategy for the image files

        :return: The image_file_naming of this DvbSubtitleSidecarDetails.
        :rtype: str
        """
        return self._image_file_naming

    @image_file_naming.setter
    def image_file_naming(self, image_file_naming):
        """Sets the image_file_naming of this DvbSubtitleSidecarDetails.

        Naming strategy for the image files

        :param image_file_naming: The image_file_naming of this DvbSubtitleSidecarDetails.
        :type: str
        """

        if image_file_naming is not None:
            if not isinstance(image_file_naming, str):
                raise TypeError("Invalid type for `image_file_naming`, type has to be `str`")

            self._image_file_naming = image_file_naming


    @property
    def index_filename(self):
        """Gets the index_filename of this DvbSubtitleSidecarDetails.

        Name of the index file

        :return: The index_filename of this DvbSubtitleSidecarDetails.
        :rtype: str
        """
        return self._index_filename

    @index_filename.setter
    def index_filename(self, index_filename):
        """Sets the index_filename of this DvbSubtitleSidecarDetails.

        Name of the index file

        :param index_filename: The index_filename of this DvbSubtitleSidecarDetails.
        :type: str
        """

        if index_filename is not None:
            if not isinstance(index_filename, str):
                raise TypeError("Invalid type for `index_filename`, type has to be `str`")

            self._index_filename = index_filename


    @property
    def image_format(self):
        """Gets the image_format of this DvbSubtitleSidecarDetails.

        Specify the format of the generated images

        :return: The image_format of this DvbSubtitleSidecarDetails.
        :rtype: str
        """
        return self._image_format

    @image_format.setter
    def image_format(self, image_format):
        """Sets the image_format of this DvbSubtitleSidecarDetails.

        Specify the format of the generated images

        :param image_format: The image_format of this DvbSubtitleSidecarDetails.
        :type: str
        """

        if image_format is not None:
            if not isinstance(image_format, str):
                raise TypeError("Invalid type for `image_format`, type has to be `str`")

            self._image_format = image_format


    @property
    def output_format(self):
        """Gets the output_format of this DvbSubtitleSidecarDetails.


        :return: The output_format of this DvbSubtitleSidecarDetails.
        :rtype: str
        """
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        """Sets the output_format of this DvbSubtitleSidecarDetails.


        :param output_format: The output_format of this DvbSubtitleSidecarDetails.
        :type: str
        """

        if output_format is not None:
            if not isinstance(output_format, str):
                raise TypeError("Invalid type for `output_format`, type has to be `str`")

            self._output_format = output_format

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(DvbSubtitleSidecarDetails, self).to_dict()

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
            if issubclass(DvbSubtitleSidecarDetails, dict):
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
        if not isinstance(other, DvbSubtitleSidecarDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
