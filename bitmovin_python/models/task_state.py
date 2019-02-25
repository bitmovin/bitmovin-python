# coding: utf-8
from enum import Enum


class TaskState(Enum):
    """
    allowed enum values
    """
    ENQUEUED = "ENQUEUED"
    ASSIGNED = "ASSIGNED"
    PREPARED = "PREPARED"
    INPROGRESS = "INPROGRESS"
    FINISHED = "FINISHED"
    ERROR = "ERROR"
    DEQUEUED = "DEQUEUED"
