# coding: utf-8
from enum import Enum


class LiveEncodingStatus(Enum):
    """
    allowed enum values
    """
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
    WAITING_FOR_FIRST_CONNECT = "WAITING_FOR_FIRST_CONNECT"
    ERROR = "ERROR"
    NOT_AVAILABLE = "NOT_AVAILABLE"
    FINISHED = "FINISHED"
