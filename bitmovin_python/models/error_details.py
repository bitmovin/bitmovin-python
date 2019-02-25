# coding: utf-8

from bitmovin_python.models.retry_hint import RetryHint
import pprint
import six
from datetime import datetime
from enum import Enum


class ErrorDetails(object):
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
            'category': 'str',
            'text': 'str',
            'retry_hint': 'RetryHint'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'code': 'code',
            'category': 'category',
            'text': 'text',
            'retry_hint': 'retryHint'
        }
        return attributes

    def __init__(self, code=None, category=None, text=None, retry_hint=None, *args, **kwargs):

        self._code = None
        self._category = None
        self._text = None
        self._retry_hint = None
        self.discriminator = None

        self.code = code
        self.category = category
        self.text = text
        self.retry_hint = retry_hint

    @property
    def code(self):
        """Gets the code of this ErrorDetails.

        Specific error code

        :return: The code of this ErrorDetails.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorDetails.

        Specific error code

        :param code: The code of this ErrorDetails.
        :type: int
        """

        if code is not None:
            if not isinstance(code, int):
                raise TypeError("Invalid type for `code`, type has to be `int`")

            self._code = code


    @property
    def category(self):
        """Gets the category of this ErrorDetails.

        Error group name

        :return: The category of this ErrorDetails.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ErrorDetails.

        Error group name

        :param category: The category of this ErrorDetails.
        :type: str
        """

        if category is not None:
            if not isinstance(category, str):
                raise TypeError("Invalid type for `category`, type has to be `str`")

            self._category = category


    @property
    def text(self):
        """Gets the text of this ErrorDetails.

        Detailed error message

        :return: The text of this ErrorDetails.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ErrorDetails.

        Detailed error message

        :param text: The text of this ErrorDetails.
        :type: str
        """

        if text is not None:
            if not isinstance(text, str):
                raise TypeError("Invalid type for `text`, type has to be `str`")

            self._text = text


    @property
    def retry_hint(self):
        """Gets the retry_hint of this ErrorDetails.

        Information if the encoding could potentially succeed when retrying.

        :return: The retry_hint of this ErrorDetails.
        :rtype: RetryHint
        """
        return self._retry_hint

    @retry_hint.setter
    def retry_hint(self, retry_hint):
        """Sets the retry_hint of this ErrorDetails.

        Information if the encoding could potentially succeed when retrying.

        :param retry_hint: The retry_hint of this ErrorDetails.
        :type: RetryHint
        """

        if retry_hint is not None:
            if not isinstance(retry_hint, RetryHint):
                raise TypeError("Invalid type for `retry_hint`, type has to be `RetryHint`")

            self._retry_hint = retry_hint

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
            if issubclass(ErrorDetails, dict):
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
        if not isinstance(other, ErrorDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
