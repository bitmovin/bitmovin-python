# coding: utf-8
from enum import Enum


class LiveEncodingEventName(Enum):
    """
    allowed enum values
    """
    FIRST_CONNECT = "FIRST_CONNECT"
    DISCONNECT = "DISCONNECT"
    RECONNECT = "RECONNECT"
    RESYNCING = "RESYNCING"
    IDLE = "IDLE"
    ERROR = "ERROR"
