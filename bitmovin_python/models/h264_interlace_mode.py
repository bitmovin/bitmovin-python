# coding: utf-8
from enum import Enum


class H264InterlaceMode(Enum):
    """
    allowed enum values
    """
    NONE = "NONE"
    TOP_FIELD_FIRST = "TOP_FIELD_FIRST"
    BOTTOM_FIELD_FIRST = "BOTTOM_FIELD_FIRST"
