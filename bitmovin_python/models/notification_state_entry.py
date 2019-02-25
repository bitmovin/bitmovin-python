# coding: utf-8

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.notification_states import NotificationStates
import pprint
import six
from datetime import datetime
from enum import Enum


class NotificationStateEntry(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(NotificationStateEntry, self).openapi_types
        types.update({
            'state': 'NotificationStates',
            'muted': 'bool',
            'notification_id': 'str',
            'resource_id': 'str',
            'triggered_at': 'datetime'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(NotificationStateEntry, self).attribute_map
        attributes.update({
            'state': 'state',
            'muted': 'muted',
            'notification_id': 'notificationId',
            'resource_id': 'resourceId',
            'triggered_at': 'triggeredAt'
        })
        return attributes

    def __init__(self, state=None, muted=None, notification_id=None, resource_id=None, triggered_at=None, *args, **kwargs):
        super(NotificationStateEntry, self).__init__(*args, **kwargs)

        self._state = None
        self._muted = None
        self._notification_id = None
        self._resource_id = None
        self._triggered_at = None
        self.discriminator = None

        self.state = state
        self.muted = muted
        self.notification_id = notification_id
        self.resource_id = resource_id
        self.triggered_at = triggered_at

    @property
    def state(self):
        """Gets the state of this NotificationStateEntry.


        :return: The state of this NotificationStateEntry.
        :rtype: NotificationStates
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this NotificationStateEntry.


        :param state: The state of this NotificationStateEntry.
        :type: NotificationStates
        """

        if state is not None:
            if not isinstance(state, NotificationStates):
                raise TypeError("Invalid type for `state`, type has to be `NotificationStates`")

            self._state = state


    @property
    def muted(self):
        """Gets the muted of this NotificationStateEntry.

        Indicate if notification was sent

        :return: The muted of this NotificationStateEntry.
        :rtype: bool
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        """Sets the muted of this NotificationStateEntry.

        Indicate if notification was sent

        :param muted: The muted of this NotificationStateEntry.
        :type: bool
        """

        if muted is not None:
            if not isinstance(muted, bool):
                raise TypeError("Invalid type for `muted`, type has to be `bool`")

            self._muted = muted


    @property
    def notification_id(self):
        """Gets the notification_id of this NotificationStateEntry.

        The notification this state belongs to

        :return: The notification_id of this NotificationStateEntry.
        :rtype: str
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """Sets the notification_id of this NotificationStateEntry.

        The notification this state belongs to

        :param notification_id: The notification_id of this NotificationStateEntry.
        :type: str
        """

        if notification_id is not None:
            if not isinstance(notification_id, str):
                raise TypeError("Invalid type for `notification_id`, type has to be `str`")

            self._notification_id = notification_id


    @property
    def resource_id(self):
        """Gets the resource_id of this NotificationStateEntry.

        Indicate if triggered for specific resource

        :return: The resource_id of this NotificationStateEntry.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this NotificationStateEntry.

        Indicate if triggered for specific resource

        :param resource_id: The resource_id of this NotificationStateEntry.
        :type: str
        """

        if resource_id is not None:
            if not isinstance(resource_id, str):
                raise TypeError("Invalid type for `resource_id`, type has to be `str`")

            self._resource_id = resource_id


    @property
    def triggered_at(self):
        """Gets the triggered_at of this NotificationStateEntry.


        :return: The triggered_at of this NotificationStateEntry.
        :rtype: datetime
        """
        return self._triggered_at

    @triggered_at.setter
    def triggered_at(self, triggered_at):
        """Sets the triggered_at of this NotificationStateEntry.


        :param triggered_at: The triggered_at of this NotificationStateEntry.
        :type: datetime
        """

        if triggered_at is not None:
            if not isinstance(triggered_at, datetime):
                raise TypeError("Invalid type for `triggered_at`, type has to be `datetime`")

            self._triggered_at = triggered_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(NotificationStateEntry, self).to_dict()

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
            if issubclass(NotificationStateEntry, dict):
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
        if not isinstance(other, NotificationStateEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
