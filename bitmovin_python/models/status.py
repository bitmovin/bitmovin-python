# coding: utf-8
from enum import Enum


class Status(Enum):
    """
    allowed enum values
    """
    CREATED = "CREATED"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    FINISHED = "FINISHED"
    ERROR = "ERROR"
