# coding: utf-8
from enum import Enum


class DecodingErrorMode(Enum):
    """
    allowed enum values
    """
    FAIL_ON_ERROR = "FAIL_ON_ERROR"
    DUPLICATE_FRAMES = "DUPLICATE_FRAMES"
