# coding: utf-8
from enum import Enum


class EncodingMode(Enum):
    """
    allowed enum values
    """
    STANDARD = "STANDARD"
    SINGLE_PASS = "SINGLE_PASS"
    TWO_PASS = "TWO_PASS"
    THREE_PASS = "THREE_PASS"
