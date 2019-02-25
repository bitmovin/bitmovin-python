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


class S3RoleBasedOutput(Output):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(S3RoleBasedOutput, self).openapi_types
        types.update({
            'bucket_name': 'str',
            'role_arn': 'str',
            'md5_meta_tag': 'str',
            'cloud_region': 'AwsCloudRegion',
            'signature_version': 'S3SignatureVersion'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(S3RoleBasedOutput, self).attribute_map
        attributes.update({
            'bucket_name': 'bucketName',
            'role_arn': 'roleArn',
            'md5_meta_tag': 'md5MetaTag',
            'cloud_region': 'cloudRegion',
            'signature_version': 'signatureVersion'
        })
        return attributes

    def __init__(self, bucket_name=None, role_arn=None, md5_meta_tag=None, cloud_region=None, signature_version=None, *args, **kwargs):
        super(S3RoleBasedOutput, self).__init__(*args, **kwargs)

        self._bucket_name = None
        self._role_arn = None
        self._md5_meta_tag = None
        self._cloud_region = None
        self._signature_version = None
        self.discriminator = None

        self.bucket_name = bucket_name
        self.role_arn = role_arn
        if md5_meta_tag is not None:
            self.md5_meta_tag = md5_meta_tag
        if cloud_region is not None:
            self.cloud_region = cloud_region
        if signature_version is not None:
            self.signature_version = signature_version

    @property
    def bucket_name(self):
        """Gets the bucket_name of this S3RoleBasedOutput.

        Amazon S3 bucket name

        :return: The bucket_name of this S3RoleBasedOutput.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this S3RoleBasedOutput.

        Amazon S3 bucket name

        :param bucket_name: The bucket_name of this S3RoleBasedOutput.
        :type: str
        """

        if bucket_name is not None:
            if not isinstance(bucket_name, str):
                raise TypeError("Invalid type for `bucket_name`, type has to be `str`")

            self._bucket_name = bucket_name


    @property
    def role_arn(self):
        """Gets the role_arn of this S3RoleBasedOutput.

        Amazon ARN of the Role that will be assumed for S3 access.

        :return: The role_arn of this S3RoleBasedOutput.
        :rtype: str
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        """Sets the role_arn of this S3RoleBasedOutput.

        Amazon ARN of the Role that will be assumed for S3 access.

        :param role_arn: The role_arn of this S3RoleBasedOutput.
        :type: str
        """

        if role_arn is not None:
            if not isinstance(role_arn, str):
                raise TypeError("Invalid type for `role_arn`, type has to be `str`")

            self._role_arn = role_arn


    @property
    def md5_meta_tag(self):
        """Gets the md5_meta_tag of this S3RoleBasedOutput.

        If set a user defined tag (x-amz-meta-) with that key will be used to store the MD5 hash of the file.

        :return: The md5_meta_tag of this S3RoleBasedOutput.
        :rtype: str
        """
        return self._md5_meta_tag

    @md5_meta_tag.setter
    def md5_meta_tag(self, md5_meta_tag):
        """Sets the md5_meta_tag of this S3RoleBasedOutput.

        If set a user defined tag (x-amz-meta-) with that key will be used to store the MD5 hash of the file.

        :param md5_meta_tag: The md5_meta_tag of this S3RoleBasedOutput.
        :type: str
        """

        if md5_meta_tag is not None:
            if not isinstance(md5_meta_tag, str):
                raise TypeError("Invalid type for `md5_meta_tag`, type has to be `str`")

            self._md5_meta_tag = md5_meta_tag


    @property
    def cloud_region(self):
        """Gets the cloud_region of this S3RoleBasedOutput.


        :return: The cloud_region of this S3RoleBasedOutput.
        :rtype: AwsCloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        """Sets the cloud_region of this S3RoleBasedOutput.


        :param cloud_region: The cloud_region of this S3RoleBasedOutput.
        :type: AwsCloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, AwsCloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `AwsCloudRegion`")

            self._cloud_region = cloud_region


    @property
    def signature_version(self):
        """Gets the signature_version of this S3RoleBasedOutput.

        Specifies the method used for authentication

        :return: The signature_version of this S3RoleBasedOutput.
        :rtype: S3SignatureVersion
        """
        return self._signature_version

    @signature_version.setter
    def signature_version(self, signature_version):
        """Sets the signature_version of this S3RoleBasedOutput.

        Specifies the method used for authentication

        :param signature_version: The signature_version of this S3RoleBasedOutput.
        :type: S3SignatureVersion
        """

        if signature_version is not None:
            if not isinstance(signature_version, S3SignatureVersion):
                raise TypeError("Invalid type for `signature_version`, type has to be `S3SignatureVersion`")

            self._signature_version = signature_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(S3RoleBasedOutput, self).to_dict()

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
            if issubclass(S3RoleBasedOutput, dict):
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
        if not isinstance(other, S3RoleBasedOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
