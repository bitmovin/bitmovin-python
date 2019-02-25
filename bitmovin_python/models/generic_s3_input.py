# coding: utf-8

from bitmovin_python.models.input import Input
from bitmovin_python.models.input_type import InputType
from bitmovin_python.models.s3_signature_version import S3SignatureVersion
import pprint
import six
from datetime import datetime
from enum import Enum


class GenericS3Input(Input):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(GenericS3Input, self).openapi_types
        types.update({
            'bucket_name': 'str',
            'host': 'str',
            'port': 'int',
            'ssl': 'bool',
            'signature_version': 'S3SignatureVersion',
            'access_key': 'str',
            'secret_key': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(GenericS3Input, self).attribute_map
        attributes.update({
            'bucket_name': 'bucketName',
            'host': 'host',
            'port': 'port',
            'ssl': 'ssl',
            'signature_version': 'signatureVersion',
            'access_key': 'accessKey',
            'secret_key': 'secretKey'
        })
        return attributes

    def __init__(self, bucket_name=None, host=None, port=None, ssl=None, signature_version=None, access_key=None, secret_key=None, *args, **kwargs):
        super(GenericS3Input, self).__init__(*args, **kwargs)

        self._bucket_name = None
        self._host = None
        self._port = None
        self._ssl = None
        self._signature_version = None
        self._access_key = None
        self._secret_key = None
        self.discriminator = None

        self.bucket_name = bucket_name
        self.host = host
        if port is not None:
            self.port = port
        if ssl is not None:
            self.ssl = ssl
        if signature_version is not None:
            self.signature_version = signature_version
        self.access_key = access_key
        self.secret_key = secret_key

    @property
    def bucket_name(self):
        """Gets the bucket_name of this GenericS3Input.

        Your generic S3 bucket name

        :return: The bucket_name of this GenericS3Input.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this GenericS3Input.

        Your generic S3 bucket name

        :param bucket_name: The bucket_name of this GenericS3Input.
        :type: str
        """

        if bucket_name is not None:
            if not isinstance(bucket_name, str):
                raise TypeError("Invalid type for `bucket_name`, type has to be `str`")

            self._bucket_name = bucket_name


    @property
    def host(self):
        """Gets the host of this GenericS3Input.

        The generic S3 server hostname (or IP address)

        :return: The host of this GenericS3Input.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this GenericS3Input.

        The generic S3 server hostname (or IP address)

        :param host: The host of this GenericS3Input.
        :type: str
        """

        if host is not None:
            if not isinstance(host, str):
                raise TypeError("Invalid type for `host`, type has to be `str`")

            self._host = host


    @property
    def port(self):
        """Gets the port of this GenericS3Input.

        The port on which the generic S3 server is running on (if not provided 8000 will be used)

        :return: The port of this GenericS3Input.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this GenericS3Input.

        The port on which the generic S3 server is running on (if not provided 8000 will be used)

        :param port: The port of this GenericS3Input.
        :type: int
        """

        if port is not None:
            if not isinstance(port, int):
                raise TypeError("Invalid type for `port`, type has to be `int`")

            self._port = port


    @property
    def ssl(self):
        """Gets the ssl of this GenericS3Input.

        Controls whether SSL is used or not

        :return: The ssl of this GenericS3Input.
        :rtype: bool
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """Sets the ssl of this GenericS3Input.

        Controls whether SSL is used or not

        :param ssl: The ssl of this GenericS3Input.
        :type: bool
        """

        if ssl is not None:
            if not isinstance(ssl, bool):
                raise TypeError("Invalid type for `ssl`, type has to be `bool`")

            self._ssl = ssl


    @property
    def signature_version(self):
        """Gets the signature_version of this GenericS3Input.

        Specifies the method used for authentication

        :return: The signature_version of this GenericS3Input.
        :rtype: S3SignatureVersion
        """
        return self._signature_version

    @signature_version.setter
    def signature_version(self, signature_version):
        """Sets the signature_version of this GenericS3Input.

        Specifies the method used for authentication

        :param signature_version: The signature_version of this GenericS3Input.
        :type: S3SignatureVersion
        """

        if signature_version is not None:
            if not isinstance(signature_version, S3SignatureVersion):
                raise TypeError("Invalid type for `signature_version`, type has to be `S3SignatureVersion`")

            self._signature_version = signature_version


    @property
    def access_key(self):
        """Gets the access_key of this GenericS3Input.

        Your generic S3 access key

        :return: The access_key of this GenericS3Input.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this GenericS3Input.

        Your generic S3 access key

        :param access_key: The access_key of this GenericS3Input.
        :type: str
        """

        if access_key is not None:
            if not isinstance(access_key, str):
                raise TypeError("Invalid type for `access_key`, type has to be `str`")

            self._access_key = access_key


    @property
    def secret_key(self):
        """Gets the secret_key of this GenericS3Input.

        Your generic S3 secret key

        :return: The secret_key of this GenericS3Input.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this GenericS3Input.

        Your generic S3 secret key

        :param secret_key: The secret_key of this GenericS3Input.
        :type: str
        """

        if secret_key is not None:
            if not isinstance(secret_key, str):
                raise TypeError("Invalid type for `secret_key`, type has to be `str`")

            self._secret_key = secret_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(GenericS3Input, self).to_dict()

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
            if issubclass(GenericS3Input, dict):
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
        if not isinstance(other, GenericS3Input):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
