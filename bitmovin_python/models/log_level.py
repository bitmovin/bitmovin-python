# coding: utf-8
from enum import Enum


class LogLevel(Enum):
    """
    allowed enum values
    """
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"
    OFF = "OFF"
