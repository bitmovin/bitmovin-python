# coding: utf-8

from bitmovin_python.models.acl_entry import AclEntry
from bitmovin_python.models.google_cloud_region import GoogleCloudRegion
from bitmovin_python.models.output import Output
from bitmovin_python.models.output_type import OutputType
import pprint
import six
from datetime import datetime
from enum import Enum


class GcsOutput(Output):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(GcsOutput, self).openapi_types
        types.update({
            'access_key': 'str',
            'secret_key': 'str',
            'bucket_name': 'str',
            'cloud_region': 'GoogleCloudRegion'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(GcsOutput, self).attribute_map
        attributes.update({
            'access_key': 'accessKey',
            'secret_key': 'secretKey',
            'bucket_name': 'bucketName',
            'cloud_region': 'cloudRegion'
        })
        return attributes

    def __init__(self, access_key=None, secret_key=None, bucket_name=None, cloud_region=None, *args, **kwargs):
        super(GcsOutput, self).__init__(*args, **kwargs)

        self._access_key = None
        self._secret_key = None
        self._bucket_name = None
        self._cloud_region = None
        self.discriminator = None

        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name
        if cloud_region is not None:
            self.cloud_region = cloud_region

    @property
    def access_key(self):
        """Gets the access_key of this GcsOutput.

        GCS access key

        :return: The access_key of this GcsOutput.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this GcsOutput.

        GCS access key

        :param access_key: The access_key of this GcsOutput.
        :type: str
        """

        if access_key is not None:
            if not isinstance(access_key, str):
                raise TypeError("Invalid type for `access_key`, type has to be `str`")

            self._access_key = access_key


    @property
    def secret_key(self):
        """Gets the secret_key of this GcsOutput.

        GCS secret key

        :return: The secret_key of this GcsOutput.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this GcsOutput.

        GCS secret key

        :param secret_key: The secret_key of this GcsOutput.
        :type: str
        """

        if secret_key is not None:
            if not isinstance(secret_key, str):
                raise TypeError("Invalid type for `secret_key`, type has to be `str`")

            self._secret_key = secret_key


    @property
    def bucket_name(self):
        """Gets the bucket_name of this GcsOutput.

        Name of the bucket

        :return: The bucket_name of this GcsOutput.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this GcsOutput.

        Name of the bucket

        :param bucket_name: The bucket_name of this GcsOutput.
        :type: str
        """

        if bucket_name is not None:
            if not isinstance(bucket_name, str):
                raise TypeError("Invalid type for `bucket_name`, type has to be `str`")

            self._bucket_name = bucket_name


    @property
    def cloud_region(self):
        """Gets the cloud_region of this GcsOutput.


        :return: The cloud_region of this GcsOutput.
        :rtype: GoogleCloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        """Sets the cloud_region of this GcsOutput.


        :param cloud_region: The cloud_region of this GcsOutput.
        :type: GoogleCloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, GoogleCloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `GoogleCloudRegion`")

            self._cloud_region = cloud_region

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(GcsOutput, self).to_dict()

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
            if issubclass(GcsOutput, dict):
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
        if not isinstance(other, GcsOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
