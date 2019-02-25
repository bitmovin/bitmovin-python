# coding: utf-8

from bitmovin_python.models.cloud_region import CloudRegion
import pprint
import six
from datetime import datetime
from enum import Enum


class AnalysisStartRequest(object):
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
            'cloud_region': 'CloudRegion'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'path': 'path',
            'cloud_region': 'cloudRegion'
        }
        return attributes

    def __init__(self, path=None, cloud_region=None, *args, **kwargs):

        self._path = None
        self._cloud_region = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if cloud_region is not None:
            self.cloud_region = cloud_region

    @property
    def path(self):
        """Gets the path of this AnalysisStartRequest.


        :return: The path of this AnalysisStartRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this AnalysisStartRequest.


        :param path: The path of this AnalysisStartRequest.
        :type: str
        """

        if path is not None:
            if not isinstance(path, str):
                raise TypeError("Invalid type for `path`, type has to be `str`")

            self._path = path


    @property
    def cloud_region(self):
        """Gets the cloud_region of this AnalysisStartRequest.


        :return: The cloud_region of this AnalysisStartRequest.
        :rtype: CloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        """Sets the cloud_region of this AnalysisStartRequest.


        :param cloud_region: The cloud_region of this AnalysisStartRequest.
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
            if issubclass(AnalysisStartRequest, dict):
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
        if not isinstance(other, AnalysisStartRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
