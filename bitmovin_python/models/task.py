# coding: utf-8

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.error_details import ErrorDetails
from bitmovin_python.models.message import Message
from bitmovin_python.models.status import Status
from bitmovin_python.models.subtask import Subtask
import pprint
import six
from datetime import datetime
from enum import Enum


class Task(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Task, self).openapi_types
        types.update({
            'status': 'Status',
            'eta': 'int',
            'progress': 'int',
            'subtasks': 'list[Subtask]',
            'messages': 'list[Message]',
            'created_at': 'datetime',
            'queued_at': 'datetime',
            'running_at': 'datetime',
            'finished_at': 'datetime',
            'error_at': 'datetime',
            'error': 'ErrorDetails'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Task, self).attribute_map
        attributes.update({
            'status': 'status',
            'eta': 'eta',
            'progress': 'progress',
            'subtasks': 'subtasks',
            'messages': 'messages',
            'created_at': 'createdAt',
            'queued_at': 'queuedAt',
            'running_at': 'runningAt',
            'finished_at': 'finishedAt',
            'error_at': 'errorAt',
            'error': 'error'
        })
        return attributes

    def __init__(self, status=None, eta=None, progress=None, subtasks=None, messages=None, created_at=None, queued_at=None, running_at=None, finished_at=None, error_at=None, error=None, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)

        self._status = None
        self._eta = None
        self._progress = None
        self._subtasks = None
        self._messages = None
        self._created_at = None
        self._queued_at = None
        self._running_at = None
        self._finished_at = None
        self._error_at = None
        self._error = None
        self.discriminator = None

        self.status = status
        if eta is not None:
            self.eta = eta
        if progress is not None:
            self.progress = progress
        if subtasks is not None:
            self.subtasks = subtasks
        if messages is not None:
            self.messages = messages
        if created_at is not None:
            self.created_at = created_at
        if queued_at is not None:
            self.queued_at = queued_at
        if running_at is not None:
            self.running_at = running_at
        if finished_at is not None:
            self.finished_at = finished_at
        if error_at is not None:
            self.error_at = error_at
        if error is not None:
            self.error = error

    @property
    def status(self):
        """Gets the status of this Task.

        Current status

        :return: The status of this Task.
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Task.

        Current status

        :param status: The status of this Task.
        :type: Status
        """

        if status is not None:
            if not isinstance(status, Status):
                raise TypeError("Invalid type for `status`, type has to be `Status`")

            self._status = status


    @property
    def eta(self):
        """Gets the eta of this Task.

        Estimated ETA in seconds

        :return: The eta of this Task.
        :rtype: int
        """
        return self._eta

    @eta.setter
    def eta(self, eta):
        """Sets the eta of this Task.

        Estimated ETA in seconds

        :param eta: The eta of this Task.
        :type: int
        """

        if eta is not None:
            if not isinstance(eta, int):
                raise TypeError("Invalid type for `eta`, type has to be `int`")

            self._eta = eta


    @property
    def progress(self):
        """Gets the progress of this Task.

        Progress in percent

        :return: The progress of this Task.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this Task.

        Progress in percent

        :param progress: The progress of this Task.
        :type: int
        """

        if progress is not None:
            if not isinstance(progress, int):
                raise TypeError("Invalid type for `progress`, type has to be `int`")

            self._progress = progress


    @property
    def subtasks(self):
        """Gets the subtasks of this Task.

        List of subtasks

        :return: The subtasks of this Task.
        :rtype: list[Subtask]
        """
        return self._subtasks

    @subtasks.setter
    def subtasks(self, subtasks):
        """Sets the subtasks of this Task.

        List of subtasks

        :param subtasks: The subtasks of this Task.
        :type: list[Subtask]
        """

        if subtasks is not None:
            if not isinstance(subtasks, list):
                raise TypeError("Invalid type for `subtasks`, type has to be `list[Subtask]`")

            self._subtasks = subtasks


    @property
    def messages(self):
        """Gets the messages of this Task.

        Task specific messages

        :return: The messages of this Task.
        :rtype: list[Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this Task.

        Task specific messages

        :param messages: The messages of this Task.
        :type: list[Message]
        """

        if messages is not None:
            if not isinstance(messages, list):
                raise TypeError("Invalid type for `messages`, type has to be `list[Message]`")

            self._messages = messages


    @property
    def created_at(self):
        """Gets the created_at of this Task.

        Timestamp when the task was created, expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :return: The created_at of this Task.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Task.

        Timestamp when the task was created, expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :param created_at: The created_at of this Task.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

            self._created_at = created_at


    @property
    def queued_at(self):
        """Gets the queued_at of this Task.

        Timestamp when the task status changed to \"QUEUED\", expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :return: The queued_at of this Task.
        :rtype: datetime
        """
        return self._queued_at

    @queued_at.setter
    def queued_at(self, queued_at):
        """Sets the queued_at of this Task.

        Timestamp when the task status changed to \"QUEUED\", expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :param queued_at: The queued_at of this Task.
        :type: datetime
        """

        if queued_at is not None:
            if not isinstance(queued_at, datetime):
                raise TypeError("Invalid type for `queued_at`, type has to be `datetime`")

            self._queued_at = queued_at


    @property
    def running_at(self):
        """Gets the running_at of this Task.

        Timestamp when the task status changed to to \"RUNNING\", expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :return: The running_at of this Task.
        :rtype: datetime
        """
        return self._running_at

    @running_at.setter
    def running_at(self, running_at):
        """Sets the running_at of this Task.

        Timestamp when the task status changed to to \"RUNNING\", expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :param running_at: The running_at of this Task.
        :type: datetime
        """

        if running_at is not None:
            if not isinstance(running_at, datetime):
                raise TypeError("Invalid type for `running_at`, type has to be `datetime`")

            self._running_at = running_at


    @property
    def finished_at(self):
        """Gets the finished_at of this Task.

        Timestamp when the task status changed to \"FINISHED\", expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :return: The finished_at of this Task.
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this Task.

        Timestamp when the task status changed to \"FINISHED\", expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :param finished_at: The finished_at of this Task.
        :type: datetime
        """

        if finished_at is not None:
            if not isinstance(finished_at, datetime):
                raise TypeError("Invalid type for `finished_at`, type has to be `datetime`")

            self._finished_at = finished_at


    @property
    def error_at(self):
        """Gets the error_at of this Task.

        Timestamp when the task status changed to \"ERROR\", expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :return: The error_at of this Task.
        :rtype: datetime
        """
        return self._error_at

    @error_at.setter
    def error_at(self, error_at):
        """Sets the error_at of this Task.

        Timestamp when the task status changed to \"ERROR\", expressed in UTC: YYYY-MM-DDThh:mm:ssZ

        :param error_at: The error_at of this Task.
        :type: datetime
        """

        if error_at is not None:
            if not isinstance(error_at, datetime):
                raise TypeError("Invalid type for `error_at`, type has to be `datetime`")

            self._error_at = error_at


    @property
    def error(self):
        """Gets the error of this Task.

        Additional optional error details

        :return: The error of this Task.
        :rtype: ErrorDetails
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Task.

        Additional optional error details

        :param error: The error of this Task.
        :type: ErrorDetails
        """

        if error is not None:
            if not isinstance(error, ErrorDetails):
                raise TypeError("Invalid type for `error`, type has to be `ErrorDetails`")

            self._error = error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Task, self).to_dict()

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
            if issubclass(Task, dict):
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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
