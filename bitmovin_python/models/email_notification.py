# coding: utf-8

from bitmovin_python.models.notification import Notification
import pprint
import six
from datetime import datetime
from enum import Enum


class EmailNotification(Notification):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(EmailNotification, self).openapi_types
        types.update({
            'emails': 'list[str]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(EmailNotification, self).attribute_map
        attributes.update({
            'emails': 'emails'
        })
        return attributes

    def __init__(self, emails=None, *args, **kwargs):
        super(EmailNotification, self).__init__(*args, **kwargs)

        self._emails = None
        self.discriminator = None

        self.emails = emails

    @property
    def emails(self):
        """Gets the emails of this EmailNotification.


        :return: The emails of this EmailNotification.
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this EmailNotification.


        :param emails: The emails of this EmailNotification.
        :type: list[str]
        """

        if emails is not None:
            if not isinstance(emails, list):
                raise TypeError("Invalid type for `emails`, type has to be `list[str]`")

            self._emails = emails

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(EmailNotification, self).to_dict()

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
            if issubclass(EmailNotification, dict):
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
        if not isinstance(other, EmailNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
