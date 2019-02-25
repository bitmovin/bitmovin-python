# coding: utf-8

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.message import Message
from bitmovin_python.models.status import Status
import pprint
import six
from datetime import datetime
from enum import Enum


class Subtask(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Subtask, self).openapi_types
        types.update({
            'status': 'Status',
            'progress': 'int',
            'name': 'str',
            'messages': 'list[Message]',
            'created_at': 'datetime',
            'updated_at': 'datetime',
            'started_at': 'datetime',
            'queued_at': 'datetime',
            'running_at': 'datetime',
            'finished_at': 'datetime',
            'error_at': 'datetime'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Subtask, self).attribute_map
        attributes.update({
            'status': 'status',
            'progress': 'progress',
            'name': 'name',
            'messages': 'messages',
            'created_at': 'createdAt',
            'updated_at': 'updatedAt',
            'started_at': 'startedAt',
            'queued_at': 'queuedAt',
            'running_at': 'runningAt',
            'finished_at': 'finishedAt',
            'error_at': 'errorAt'
        })
        return attributes

    def __init__(self, status=None, progress=None, name=None, messages=None, created_at=None, updated_at=None, started_at=None, queued_at=None, running_at=None, finished_at=None, error_at=None, *args, **kwargs):
        super(Subtask, self).__init__(*args, **kwargs)

        self._status = None
        self._progress = None
        self._name = None
        self._messages = None
        self._created_at = None
        self._updated_at = None
        self._started_at = None
        self._queued_at = None
        self._running_at = None
        self._finished_at = None
        self._error_at = None
        self.discriminator = None

        self.status = status
        if progress is not None:
            self.progress = progress
        self.name = name
        if messages is not None:
            self.messages = messages
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if started_at is not None:
            self.started_at = started_at
        if queued_at is not None:
            self.queued_at = queued_at
        if running_at is not None:
            self.running_at = running_at
        if finished_at is not None:
            self.finished_at = finished_at
        if error_at is not None:
            self.error_at = error_at

    @property
    def status(self):
        """Gets the status of this Subtask.

        Current status

        :return: The status of this Subtask.
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Subtask.

        Current status

        :param status: The status of this Subtask.
        :type: Status
        """

        if status is not None:
            if not isinstance(status, Status):
                raise TypeError("Invalid type for `status`, type has to be `Status`")

            self._status = status


    @property
    def progress(self):
        """Gets the progress of this Subtask.

        Progress in percent

        :return: The progress of this Subtask.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this Subtask.

        Progress in percent

        :param progress: The progress of this Subtask.
        :type: int
        """

        if progress is not None:
            if not isinstance(progress, int):
                raise TypeError("Invalid type for `progress`, type has to be `int`")

            self._progress = progress


    @property
    def name(self):
        """Gets the name of this Subtask.

        Name of the subtask

        :return: The name of this Subtask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Subtask.

        Name of the subtask

        :param name: The name of this Subtask.
        :type: str
        """

        if name is not None:
            if not isinstance(name, str):
                raise TypeError("Invalid type for `name`, type has to be `str`")

            self._name = name


    @property
    def messages(self):
        """Gets the messages of this Subtask.

        Task specific messages

        :return: The messages of this Subtask.
        :rtype: list[Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this Subtask.

        Task specific messages

        :param messages: The messages of this Subtask.
        :type: list[Message]
        """

        if messages is not None:
            if not isinstance(messages, list):
                raise TypeError("Invalid type for `messages`, type has to be `list[Message]`")

            self._messages = messages


    @property
    def created_at(self):
        """Gets the created_at of this Subtask.

        Timestamp when the subtask was created, expressed in UTC: YYYY-MM-DDThh:mm:ssZ 

        :return: The created_at of this Subtask.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Subtask.

        Timestamp when the subtask was created, expressed in UTC: YYYY-MM-DDThh:mm:ssZ 

        :param created_at: The created_at of this Subtask.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

            self._created_at = created_at


    @property
    def updated_at(self):
        """Gets the updated_at of this Subtask.

        Timestamp when the subtask was last updated, expressed in UTC: YYYY-MM-DDThh:mm:ssZ 

        :return: The updated_at of this Subtask.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Subtask.

        Timestamp when the subtask was last updated, expressed in UTC: YYYY-MM-DDThh:mm:ssZ 

        :param updated_at: The updated_at of this Subtask.
        :type: datetime
        """

        if updated_at is not None:
            if not isinstance(updated_at, datetime):
                raise TypeError("Invalid type for `updated_at`, type has to be `datetime`")

            self._updated_at = updated_at


    @property
    def started_at(self):
        """Gets the started_at of this Subtask.

        Timestamp when the subtask was started, expressed in UTC: YYYY-MM-DDThh:mm:ssZ 

        :return: The started_at of this Subtask.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this Subtask.

        Timestamp when the subtask was started, expressed in UTC: YYYY-MM-DDThh:mm:ssZ 

        :param started_at: The started_at of this Subtask.
        :type: datetime
        """

        if started_at is not None:
            if not isinstance(started_at, datetime):
                raise TypeError("Invalid type for `started_at`, type has to be `datetime`")

            self._started_at = started_at


    @property
    def queued_at(self):
        """Gets the queued_at of this Subtask.

        Timestamp when the subtask status changed to 'QUEUED', expressed in UTC: YYYY-MM-DDThh:mm:ssZ 

        :return: The queued_at of this Subtask.
        :rtype: datetime
        """
        return self._queued_at

    @queued_at.setter
    def queued_at(self, queued_at):
        """Sets the queued_at of this Subtask.

        Timestamp when the subtask status changed to 'QUEUED', expressed in UTC: YYYY-MM-DDThh:mm:ssZ 

        :param queued_at: The queued_at of this Subtask.
        :type: datetime
        """

        if queued_at is not None:
            if not isinstance(queued_at, datetime):
                raise TypeError("Invalid type for `queued_at`, type has to be `datetime`")

            self._queued_at = queued_at


    @property
    def running_at(self):
        """Gets the running_at of this Subtask.

        Timestamp when the subtask status changed to to 'RUNNING', expressed in UTC: YYYY-MM-DDThh:mm:ssZ 

        :return: The running_at of this Subtask.
        :rtype: datetime
        """
        return self._running_at

    @running_at.setter
    def running_at(self, running_at):
        """Sets the running_at of this Subtask.

        Timestamp when the subtask status changed to to 'RUNNING', expressed in UTC: YYYY-MM-DDThh:mm:ssZ 

        :param running_at: The running_at of this Subtask.
        :type: datetime
        """

        if running_at is not None:
            if not isinstance(running_at, datetime):
                raise TypeError("Invalid type for `running_at`, type has to be `datetime`")

            self._running_at = running_at


    @property
    def finished_at(self):
        """Gets the finished_at of this Subtask.

        Timestamp when the subtask status changed to 'FINISHED', expressed in UTC: YYYY-MM-DDThh:mm:ssZ 

        :return: The finished_at of this Subtask.
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this Subtask.

        Timestamp when the subtask status changed to 'FINISHED', expressed in UTC: YYYY-MM-DDThh:mm:ssZ 

        :param finished_at: The finished_at of this Subtask.
        :type: datetime
        """

        if finished_at is not None:
            if not isinstance(finished_at, datetime):
                raise TypeError("Invalid type for `finished_at`, type has to be `datetime`")

            self._finished_at = finished_at


    @property
    def error_at(self):
        """Gets the error_at of this Subtask.

        Timestamp when the subtask status changed to 'ERROR', expressed in UTC: YYYY-MM-DDThh:mm:ssZ 

        :return: The error_at of this Subtask.
        :rtype: datetime
        """
        return self._error_at

    @error_at.setter
    def error_at(self, error_at):
        """Sets the error_at of this Subtask.

        Timestamp when the subtask status changed to 'ERROR', expressed in UTC: YYYY-MM-DDThh:mm:ssZ 

        :param error_at: The error_at of this Subtask.
        :type: datetime
        """

        if error_at is not None:
            if not isinstance(error_at, datetime):
                raise TypeError("Invalid type for `error_at`, type has to be `datetime`")

            self._error_at = error_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Subtask, self).to_dict()

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
            if issubclass(Subtask, dict):
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
        if not isinstance(other, Subtask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
