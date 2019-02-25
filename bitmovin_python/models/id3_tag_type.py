# coding: utf-8
from enum import Enum


class Id3TagType(Enum):
    """
    allowed enum values
    """
    RAW = "RAW"
    FRAME_ID = "FRAME_ID"
    PLAIN_TEXT = "PLAIN_TEXT"
