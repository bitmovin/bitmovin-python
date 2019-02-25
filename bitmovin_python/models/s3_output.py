# coding: utf-8

from bitmovin_python.models.acl_entry import AclEntry
from bitmovin_python.models.aws_cloud_region import AwsCloudRegion
from bitmovin_python.models.output import Output
from bitmovin_python.models.output_type import OutputType
from bitmovin_python.models.s3_signature_version import S3SignatureVersion
import pprint
import six
from datetime import datetime
from enum import Enum


class S3Output(Output):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(S3Output, self).openapi_types
        types.update({
            'bucket_name': 'str',
            'access_key': 'str',
            'secret_key': 'str',
            'md5_meta_tag': 'str',
            'cloud_region': 'AwsCloudRegion',
            'signature_version': 'S3SignatureVersion'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(S3Output, self).attribute_map
        attributes.update({
            'bucket_name': 'bucketName',
            'access_key': 'accessKey',
            'secret_key': 'secretKey',
            'md5_meta_tag': 'md5MetaTag',
            'cloud_region': 'cloudRegion',
            'signature_version': 'signatureVersion'
        })
        return attributes

    def __init__(self, bucket_name=None, access_key=None, secret_key=None, md5_meta_tag=None, cloud_region=None, signature_version=None, *args, **kwargs):
        super(S3Output, self).__init__(*args, **kwargs)

        self._bucket_name = None
        self._access_key = None
        self._secret_key = None
        self._md5_meta_tag = None
        self._cloud_region = None
        self._signature_version = None
        self.discriminator = None

        self.bucket_name = bucket_name
        self.access_key = access_key
        self.secret_key = secret_key
        if md5_meta_tag is not None:
            self.md5_meta_tag = md5_meta_tag
        if cloud_region is not None:
            self.cloud_region = cloud_region
        if signature_version is not None:
            self.signature_version = signature_version

    @property
    def bucket_name(self):
        """Gets the bucket_name of this S3Output.

        Amazon S3 bucket name

        :return: The bucket_name of this S3Output.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this S3Output.

        Amazon S3 bucket name

        :param bucket_name: The bucket_name of this S3Output.
        :type: str
        """

        if bucket_name is not None:
            if not isinstance(bucket_name, str):
                raise TypeError("Invalid type for `bucket_name`, type has to be `str`")

            self._bucket_name = bucket_name


    @property
    def access_key(self):
        """Gets the access_key of this S3Output.

        Amazon S3 access key

        :return: The access_key of this S3Output.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this S3Output.

        Amazon S3 access key

        :param access_key: The access_key of this S3Output.
        :type: str
        """

        if access_key is not None:
            if not isinstance(access_key, str):
                raise TypeError("Invalid type for `access_key`, type has to be `str`")

            self._access_key = access_key


    @property
    def secret_key(self):
        """Gets the secret_key of this S3Output.

        Amazon S3 secret key

        :return: The secret_key of this S3Output.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this S3Output.

        Amazon S3 secret key

        :param secret_key: The secret_key of this S3Output.
        :type: str
        """

        if secret_key is not None:
            if not isinstance(secret_key, str):
                raise TypeError("Invalid type for `secret_key`, type has to be `str`")

            self._secret_key = secret_key


    @property
    def md5_meta_tag(self):
        """Gets the md5_meta_tag of this S3Output.

        If set a user defined tag (x-amz-meta-) with that key will be used to store the MD5 hash of the file.

        :return: The md5_meta_tag of this S3Output.
        :rtype: str
        """
        return self._md5_meta_tag

    @md5_meta_tag.setter
    def md5_meta_tag(self, md5_meta_tag):
        """Sets the md5_meta_tag of this S3Output.

        If set a user defined tag (x-amz-meta-) with that key will be used to store the MD5 hash of the file.

        :param md5_meta_tag: The md5_meta_tag of this S3Output.
        :type: str
        """

        if md5_meta_tag is not None:
            if not isinstance(md5_meta_tag, str):
                raise TypeError("Invalid type for `md5_meta_tag`, type has to be `str`")

            self._md5_meta_tag = md5_meta_tag


    @property
    def cloud_region(self):
        """Gets the cloud_region of this S3Output.


        :return: The cloud_region of this S3Output.
        :rtype: AwsCloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        """Sets the cloud_region of this S3Output.


        :param cloud_region: The cloud_region of this S3Output.
        :type: AwsCloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, AwsCloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `AwsCloudRegion`")

            self._cloud_region = cloud_region


    @property
    def signature_version(self):
        """Gets the signature_version of this S3Output.


        :return: The signature_version of this S3Output.
        :rtype: S3SignatureVersion
        """
        return self._signature_version

    @signature_version.setter
    def signature_version(self, signature_version):
        """Sets the signature_version of this S3Output.


        :param signature_version: The signature_version of this S3Output.
        :type: S3SignatureVersion
        """

        if signature_version is not None:
            if not isinstance(signature_version, S3SignatureVersion):
                raise TypeError("Invalid type for `signature_version`, type has to be `S3SignatureVersion`")

            self._signature_version = signature_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(S3Output, self).to_dict()

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
            if issubclass(S3Output, dict):
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
        if not isinstance(other, S3Output):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
