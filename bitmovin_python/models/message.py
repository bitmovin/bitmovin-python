# coding: utf-8

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.link import Link
from bitmovin_python.models.message_type import MessageType
import pprint
import six
from datetime import datetime
from enum import Enum


class Message(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Message, self).openapi_types
        types.update({
            'type': 'MessageType',
            'text': 'str',
            'field': 'str',
            'links': 'list[Link]',
            'more': 'object',
            'date': 'datetime'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Message, self).attribute_map
        attributes.update({
            'type': 'type',
            'text': 'text',
            'field': 'field',
            'links': 'links',
            'more': 'more',
            'date': 'date'
        })
        return attributes

    def __init__(self, type=None, text=None, field=None, links=None, more=None, date=None, *args, **kwargs):
        super(Message, self).__init__(*args, **kwargs)

        self._type = None
        self._text = None
        self._field = None
        self._links = None
        self._more = None
        self._date = None
        self.discriminator = None

        self.type = type
        self.text = text
        if field is not None:
            self.field = field
        if links is not None:
            self.links = links
        if more is not None:
            self.more = more
        if date is not None:
            self.date = date

    @property
    def type(self):
        """Gets the type of this Message.

        Message type giving a hint on the importance of the message (log level)

        :return: The type of this Message.
        :rtype: MessageType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Message.

        Message type giving a hint on the importance of the message (log level)

        :param type: The type of this Message.
        :type: MessageType
        """

        if type is not None:
            if not isinstance(type, MessageType):
                raise TypeError("Invalid type for `type`, type has to be `MessageType`")

            self._type = type


    @property
    def text(self):
        """Gets the text of this Message.

        Message text

        :return: The text of this Message.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Message.

        Message text

        :param text: The text of this Message.
        :type: str
        """

        if text is not None:
            if not isinstance(text, str):
                raise TypeError("Invalid type for `text`, type has to be `str`")

            self._text = text


    @property
    def field(self):
        """Gets the field of this Message.

        Name of the field to which the message is referring to

        :return: The field of this Message.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this Message.

        Name of the field to which the message is referring to

        :param field: The field of this Message.
        :type: str
        """

        if field is not None:
            if not isinstance(field, str):
                raise TypeError("Invalid type for `field`, type has to be `str`")

            self._field = field


    @property
    def links(self):
        """Gets the links of this Message.

        collection of links to webpages containing further information on the topic

        :return: The links of this Message.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Message.

        collection of links to webpages containing further information on the topic

        :param links: The links of this Message.
        :type: list[Link]
        """

        if links is not None:
            if not isinstance(links, list):
                raise TypeError("Invalid type for `links`, type has to be `list[Link]`")

            self._links = links


    @property
    def more(self):
        """Gets the more of this Message.

        Service-specific information

        :return: The more of this Message.
        :rtype: object
        """
        return self._more

    @more.setter
    def more(self, more):
        """Sets the more of this Message.

        Service-specific information

        :param more: The more of this Message.
        :type: object
        """

        if more is not None:
            if not isinstance(more, object):
                raise TypeError("Invalid type for `more`, type has to be `object`")

            self._more = more


    @property
    def date(self):
        """Gets the date of this Message.

        Timestamp when the message occured

        :return: The date of this Message.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Message.

        Timestamp when the message occured

        :param date: The date of this Message.
        :type: datetime
        """

        if date is not None:
            if not isinstance(date, datetime):
                raise TypeError("Invalid type for `date`, type has to be `datetime`")

            self._date = date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Message, self).to_dict()

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
            if issubclass(Message, dict):
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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
