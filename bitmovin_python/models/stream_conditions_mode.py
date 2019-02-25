# coding: utf-8
from enum import Enum


class StreamConditionsMode(Enum):
    """
    allowed enum values
    """
    DROP_MUXING = "DROP_MUXING"
    DROP_STREAM = "DROP_STREAM"
