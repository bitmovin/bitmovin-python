# coding: utf-8

from bitmovin_python.models.link import Link
from bitmovin_python.models.message import Message
import pprint
import six
from datetime import datetime
from enum import Enum


class ResponseErrorData(object):
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
            'code': 'int',
            'message': 'str',
            'developer_message': 'str',
            'links': 'list[Link]',
            'details': 'list[Message]'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'code': 'code',
            'message': 'message',
            'developer_message': 'developerMessage',
            'links': 'links',
            'details': 'details'
        }
        return attributes

    def __init__(self, code=None, message=None, developer_message=None, links=None, details=None, *args, **kwargs):

        self._code = None
        self._message = None
        self._developer_message = None
        self._links = None
        self._details = None
        self.discriminator = None

        self.code = code
        self.message = message
        self.developer_message = developer_message
        if links is not None:
            self.links = links
        if details is not None:
            self.details = details

    @property
    def code(self):
        """Gets the code of this ResponseErrorData.

        Contains an error code as defined in https://bitmovin.com/encoding-documentation/bitmovin-api/#/introduction/api-error-codes 

        :return: The code of this ResponseErrorData.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ResponseErrorData.

        Contains an error code as defined in https://bitmovin.com/encoding-documentation/bitmovin-api/#/introduction/api-error-codes 

        :param code: The code of this ResponseErrorData.
        :type: int
        """

        if code is not None:
            if not isinstance(code, int):
                raise TypeError("Invalid type for `code`, type has to be `int`")

            self._code = code


    @property
    def message(self):
        """Gets the message of this ResponseErrorData.

        General error message

        :return: The message of this ResponseErrorData.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ResponseErrorData.

        General error message

        :param message: The message of this ResponseErrorData.
        :type: str
        """

        if message is not None:
            if not isinstance(message, str):
                raise TypeError("Invalid type for `message`, type has to be `str`")

            self._message = message


    @property
    def developer_message(self):
        """Gets the developer_message of this ResponseErrorData.

        More detailed message meant for developers

        :return: The developer_message of this ResponseErrorData.
        :rtype: str
        """
        return self._developer_message

    @developer_message.setter
    def developer_message(self, developer_message):
        """Sets the developer_message of this ResponseErrorData.

        More detailed message meant for developers

        :param developer_message: The developer_message of this ResponseErrorData.
        :type: str
        """

        if developer_message is not None:
            if not isinstance(developer_message, str):
                raise TypeError("Invalid type for `developer_message`, type has to be `str`")

            self._developer_message = developer_message


    @property
    def links(self):
        """Gets the links of this ResponseErrorData.

        collection of links to webpages containing further information on the topic

        :return: The links of this ResponseErrorData.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ResponseErrorData.

        collection of links to webpages containing further information on the topic

        :param links: The links of this ResponseErrorData.
        :type: list[Link]
        """

        if links is not None:
            if not isinstance(links, list):
                raise TypeError("Invalid type for `links`, type has to be `list[Link]`")

            self._links = links


    @property
    def details(self):
        """Gets the details of this ResponseErrorData.

        collection of messages containing more detailed information on the cause of the error

        :return: The details of this ResponseErrorData.
        :rtype: list[Message]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ResponseErrorData.

        collection of messages containing more detailed information on the cause of the error

        :param details: The details of this ResponseErrorData.
        :type: list[Message]
        """

        if details is not None:
            if not isinstance(details, list):
                raise TypeError("Invalid type for `details`, type has to be `list[Message]`")

            self._details = details

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
            if issubclass(ResponseErrorData, dict):
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
        if not isinstance(other, ResponseErrorData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
