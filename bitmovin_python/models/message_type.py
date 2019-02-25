# coding: utf-8
from enum import Enum


class MessageType(Enum):
    """
    allowed enum values
    """
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"
    TRACE = "TRACE"
