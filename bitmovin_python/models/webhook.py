# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.webhook_encryption import WebhookEncryption
from bitmovin_python.models.webhook_http_method import WebhookHttpMethod
from bitmovin_python.models.webhook_signature import WebhookSignature
import pprint
import six
from datetime import datetime
from enum import Enum


class Webhook(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Webhook, self).openapi_types
        types.update({
            'url': 'str',
            'method': 'WebhookHttpMethod',
            'insecure_ssl': 'bool',
            'encryption': 'WebhookEncryption',
            'signature': 'WebhookSignature'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Webhook, self).attribute_map
        attributes.update({
            'url': 'url',
            'method': 'method',
            'insecure_ssl': 'insecureSsl',
            'encryption': 'encryption',
            'signature': 'signature'
        })
        return attributes

    def __init__(self, url=None, method=None, insecure_ssl=None, encryption=None, signature=None, *args, **kwargs):
        super(Webhook, self).__init__(*args, **kwargs)

        self._url = None
        self._method = None
        self._insecure_ssl = None
        self._encryption = None
        self._signature = None
        self.discriminator = None

        self.url = url
        if method is not None:
            self.method = method
        if insecure_ssl is not None:
            self.insecure_ssl = insecure_ssl
        if encryption is not None:
            self.encryption = encryption
        if signature is not None:
            self.signature = signature

    @property
    def url(self):
        """Gets the url of this Webhook.

        Webhook url

        :return: The url of this Webhook.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Webhook.

        Webhook url

        :param url: The url of this Webhook.
        :type: str
        """

        if url is not None:
            if not isinstance(url, str):
                raise TypeError("Invalid type for `url`, type has to be `str`")

            self._url = url


    @property
    def method(self):
        """Gets the method of this Webhook.

        HTTP method used for the webhook

        :return: The method of this Webhook.
        :rtype: WebhookHttpMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Webhook.

        HTTP method used for the webhook

        :param method: The method of this Webhook.
        :type: WebhookHttpMethod
        """

        if method is not None:
            if not isinstance(method, WebhookHttpMethod):
                raise TypeError("Invalid type for `method`, type has to be `WebhookHttpMethod`")

            self._method = method


    @property
    def insecure_ssl(self):
        """Gets the insecure_ssl of this Webhook.

        Whether to skip SSL certification verification or not

        :return: The insecure_ssl of this Webhook.
        :rtype: bool
        """
        return self._insecure_ssl

    @insecure_ssl.setter
    def insecure_ssl(self, insecure_ssl):
        """Sets the insecure_ssl of this Webhook.

        Whether to skip SSL certification verification or not

        :param insecure_ssl: The insecure_ssl of this Webhook.
        :type: bool
        """

        if insecure_ssl is not None:
            if not isinstance(insecure_ssl, bool):
                raise TypeError("Invalid type for `insecure_ssl`, type has to be `bool`")

            self._insecure_ssl = insecure_ssl


    @property
    def encryption(self):
        """Gets the encryption of this Webhook.

        Encryption used for the webhook

        :return: The encryption of this Webhook.
        :rtype: WebhookEncryption
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this Webhook.

        Encryption used for the webhook

        :param encryption: The encryption of this Webhook.
        :type: WebhookEncryption
        """

        if encryption is not None:
            if not isinstance(encryption, WebhookEncryption):
                raise TypeError("Invalid type for `encryption`, type has to be `WebhookEncryption`")

            self._encryption = encryption


    @property
    def signature(self):
        """Gets the signature of this Webhook.

        Signature used for the webhook

        :return: The signature of this Webhook.
        :rtype: WebhookSignature
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this Webhook.

        Signature used for the webhook

        :param signature: The signature of this Webhook.
        :type: WebhookSignature
        """

        if signature is not None:
            if not isinstance(signature, WebhookSignature):
                raise TypeError("Invalid type for `signature`, type has to be `WebhookSignature`")

            self._signature = signature

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Webhook, self).to_dict()

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
            if issubclass(Webhook, dict):
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
        if not isinstance(other, Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
