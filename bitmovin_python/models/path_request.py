# coding: utf-8

from bitmovin_python.models.cloud_region import CloudRegion
import pprint
import six
from datetime import datetime
from enum import Enum


class PathRequest(object):
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
            'path': 'str',
            'recursive': 'bool',
            'cloud_region': 'CloudRegion'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'path': 'path',
            'recursive': 'recursive',
            'cloud_region': 'cloudRegion'
        }
        return attributes

    def __init__(self, path=None, recursive=None, cloud_region=None, *args, **kwargs):

        self._path = None
        self._recursive = None
        self._cloud_region = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if recursive is not None:
            self.recursive = recursive
        if cloud_region is not None:
            self.cloud_region = cloud_region

    @property
    def path(self):
        """Gets the path of this PathRequest.


        :return: The path of this PathRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PathRequest.


        :param path: The path of this PathRequest.
        :type: str
        """

        if path is not None:
            if not isinstance(path, str):
                raise TypeError("Invalid type for `path`, type has to be `str`")

            self._path = path


    @property
    def recursive(self):
        """Gets the recursive of this PathRequest.


        :return: The recursive of this PathRequest.
        :rtype: bool
        """
        return self._recursive

    @recursive.setter
    def recursive(self, recursive):
        """Sets the recursive of this PathRequest.


        :param recursive: The recursive of this PathRequest.
        :type: bool
        """

        if recursive is not None:
            if not isinstance(recursive, bool):
                raise TypeError("Invalid type for `recursive`, type has to be `bool`")

            self._recursive = recursive


    @property
    def cloud_region(self):
        """Gets the cloud_region of this PathRequest.


        :return: The cloud_region of this PathRequest.
        :rtype: CloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        """Sets the cloud_region of this PathRequest.


        :param cloud_region: The cloud_region of this PathRequest.
        :type: CloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, CloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `CloudRegion`")

            self._cloud_region = cloud_region

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
            if issubclass(PathRequest, dict):
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
        if not isinstance(other, PathRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
