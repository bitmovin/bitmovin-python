# coding: utf-8

from bitmovin_python.models.acl_entry import AclEntry
import pprint
import six
from datetime import datetime
from enum import Enum


class EncodingOutput(object):
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
            'output_id': 'str',
            'output_path': 'str',
            'acl': 'list[AclEntry]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'output_id': 'outputId',
            'output_path': 'outputPath',
            'acl': 'acl'
        }
        return attributes

    def __init__(self, output_id=None, output_path=None, acl=None, *args, **kwargs):

        self._output_id = None
        self._output_path = None
        self._acl = None
        self.discriminator = None

        self.output_id = output_id
        self.output_path = output_path
        if acl is not None:
            self.acl = acl

    @property
    def output_id(self):
        """Gets the output_id of this EncodingOutput.

        Id of the corresponding output

        :return: The output_id of this EncodingOutput.
        :rtype: str
        """
        return self._output_id

    @output_id.setter
    def output_id(self, output_id):
        """Sets the output_id of this EncodingOutput.

        Id of the corresponding output

        :param output_id: The output_id of this EncodingOutput.
        :type: str
        """

        if output_id is not None:
            if not isinstance(output_id, str):
                raise TypeError("Invalid type for `output_id`, type has to be `str`")

            self._output_id = output_id


    @property
    def output_path(self):
        """Gets the output_path of this EncodingOutput.

        Subdirectory where to save the files to

        :return: The output_path of this EncodingOutput.
        :rtype: str
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        """Sets the output_path of this EncodingOutput.

        Subdirectory where to save the files to

        :param output_path: The output_path of this EncodingOutput.
        :type: str
        """

        if output_path is not None:
            if not isinstance(output_path, str):
                raise TypeError("Invalid type for `output_path`, type has to be `str`")

            self._output_path = output_path


    @property
    def acl(self):
        """Gets the acl of this EncodingOutput.


        :return: The acl of this EncodingOutput.
        :rtype: list[AclEntry]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this EncodingOutput.


        :param acl: The acl of this EncodingOutput.
        :type: list[AclEntry]
        """

        if acl is not None:
            if not isinstance(acl, list):
                raise TypeError("Invalid type for `acl`, type has to be `list[AclEntry]`")

            self._acl = acl

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
            if issubclass(EncodingOutput, dict):
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
        if not isinstance(other, EncodingOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
