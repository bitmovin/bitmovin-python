# coding: utf-8

from bitmovin_python.models.bitmovin_response import BitmovinResponse
import pprint
import six
from datetime import datetime
from enum import Enum


class Notification(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Notification, self).openapi_types
        types.update({
            'resolve': 'bool',
            'resource_id': 'str',
            'triggered_at': 'datetime',
            'type': 'str',
            'event_type': 'str',
            'category': 'str',
            'resource_type': 'str',
            'muted': 'bool'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Notification, self).attribute_map
        attributes.update({
            'resolve': 'resolve',
            'resource_id': 'resourceId',
            'triggered_at': 'triggeredAt',
            'type': 'type',
            'event_type': 'eventType',
            'category': 'category',
            'resource_type': 'resourceType',
            'muted': 'muted'
        })
        return attributes

    def __init__(self, resolve=None, resource_id=None, triggered_at=None, type=None, event_type=None, category=None, resource_type=None, muted=None, *args, **kwargs):
        super(Notification, self).__init__(*args, **kwargs)

        self._resolve = None
        self._resource_id = None
        self._triggered_at = None
        self._type = None
        self._event_type = None
        self._category = None
        self._resource_type = None
        self._muted = None
        self.discriminator = None

        if resolve is not None:
            self.resolve = resolve
        if resource_id is not None:
            self.resource_id = resource_id
        if triggered_at is not None:
            self.triggered_at = triggered_at
        if type is not None:
            self.type = type
        if event_type is not None:
            self.event_type = event_type
        if category is not None:
            self.category = category
        if resource_type is not None:
            self.resource_type = resource_type
        if muted is not None:
            self.muted = muted

    @property
    def resolve(self):
        """Gets the resolve of this Notification.

        Notify when condition resolves after it was met

        :return: The resolve of this Notification.
        :rtype: bool
        """
        return self._resolve

    @resolve.setter
    def resolve(self, resolve):
        """Sets the resolve of this Notification.

        Notify when condition resolves after it was met

        :param resolve: The resolve of this Notification.
        :type: bool
        """

        if resolve is not None:
            if not isinstance(resolve, bool):
                raise TypeError("Invalid type for `resolve`, type has to be `bool`")

            self._resolve = resolve


    @property
    def resource_id(self):
        """Gets the resource_id of this Notification.

        Specific resource, e.g. encoding id

        :return: The resource_id of this Notification.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Notification.

        Specific resource, e.g. encoding id

        :param resource_id: The resource_id of this Notification.
        :type: str
        """

        if resource_id is not None:
            if not isinstance(resource_id, str):
                raise TypeError("Invalid type for `resource_id`, type has to be `str`")

            self._resource_id = resource_id


    @property
    def triggered_at(self):
        """Gets the triggered_at of this Notification.

        Last time the notification was triggered

        :return: The triggered_at of this Notification.
        :rtype: datetime
        """
        return self._triggered_at

    @triggered_at.setter
    def triggered_at(self, triggered_at):
        """Sets the triggered_at of this Notification.

        Last time the notification was triggered

        :param triggered_at: The triggered_at of this Notification.
        :type: datetime
        """

        if triggered_at is not None:
            if not isinstance(triggered_at, datetime):
                raise TypeError("Invalid type for `triggered_at`, type has to be `datetime`")

            self._triggered_at = triggered_at


    @property
    def type(self):
        """Gets the type of this Notification.


        :return: The type of this Notification.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Notification.


        :param type: The type of this Notification.
        :type: str
        """

        if type is not None:
            if not isinstance(type, str):
                raise TypeError("Invalid type for `type`, type has to be `str`")

            self._type = type


    @property
    def event_type(self):
        """Gets the event_type of this Notification.


        :return: The event_type of this Notification.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this Notification.


        :param event_type: The event_type of this Notification.
        :type: str
        """

        if event_type is not None:
            if not isinstance(event_type, str):
                raise TypeError("Invalid type for `event_type`, type has to be `str`")

            self._event_type = event_type


    @property
    def category(self):
        """Gets the category of this Notification.


        :return: The category of this Notification.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Notification.


        :param category: The category of this Notification.
        :type: str
        """

        if category is not None:
            if not isinstance(category, str):
                raise TypeError("Invalid type for `category`, type has to be `str`")

            self._category = category


    @property
    def resource_type(self):
        """Gets the resource_type of this Notification.


        :return: The resource_type of this Notification.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Notification.


        :param resource_type: The resource_type of this Notification.
        :type: str
        """

        if resource_type is not None:
            if not isinstance(resource_type, str):
                raise TypeError("Invalid type for `resource_type`, type has to be `str`")

            self._resource_type = resource_type


    @property
    def muted(self):
        """Gets the muted of this Notification.


        :return: The muted of this Notification.
        :rtype: bool
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        """Sets the muted of this Notification.


        :param muted: The muted of this Notification.
        :type: bool
        """

        if muted is not None:
            if not isinstance(muted, bool):
                raise TypeError("Invalid type for `muted`, type has to be `bool`")

            self._muted = muted

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Notification, self).to_dict()

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
            if issubclass(Notification, dict):
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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
