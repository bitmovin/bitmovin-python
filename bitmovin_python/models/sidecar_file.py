# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.encoding_output import EncodingOutput
import pprint
import six
from datetime import datetime
from enum import Enum


class SidecarFile(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(SidecarFile, self).openapi_types
        types.update({
            'input_id': 'str',
            'input_path': 'str',
            'outputs': 'list[EncodingOutput]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(SidecarFile, self).attribute_map
        attributes.update({
            'input_id': 'inputId',
            'input_path': 'inputPath',
            'outputs': 'outputs'
        })
        return attributes

    def __init__(self, input_id=None, input_path=None, outputs=None, *args, **kwargs):
        super(SidecarFile, self).__init__(*args, **kwargs)

        self._input_id = None
        self._input_path = None
        self._outputs = None
        self.discriminator = None

        self.input_id = input_id
        self.input_path = input_path
        if outputs is not None:
            self.outputs = outputs

    @property
    def input_id(self):
        """Gets the input_id of this SidecarFile.

        Id of input

        :return: The input_id of this SidecarFile.
        :rtype: str
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        """Sets the input_id of this SidecarFile.

        Id of input

        :param input_id: The input_id of this SidecarFile.
        :type: str
        """

        if input_id is not None:
            if not isinstance(input_id, str):
                raise TypeError("Invalid type for `input_id`, type has to be `str`")

            self._input_id = input_id


    @property
    def input_path(self):
        """Gets the input_path of this SidecarFile.

        Path to sidecar file

        :return: The input_path of this SidecarFile.
        :rtype: str
        """
        return self._input_path

    @input_path.setter
    def input_path(self, input_path):
        """Sets the input_path of this SidecarFile.

        Path to sidecar file

        :param input_path: The input_path of this SidecarFile.
        :type: str
        """

        if input_path is not None:
            if not isinstance(input_path, str):
                raise TypeError("Invalid type for `input_path`, type has to be `str`")

            self._input_path = input_path


    @property
    def outputs(self):
        """Gets the outputs of this SidecarFile.


        :return: The outputs of this SidecarFile.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this SidecarFile.


        :param outputs: The outputs of this SidecarFile.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

            self._outputs = outputs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(SidecarFile, self).to_dict()

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
            if issubclass(SidecarFile, dict):
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
        if not isinstance(other, SidecarFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
