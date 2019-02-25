# coding: utf-8
from enum import Enum


class ChromaLocation(Enum):
    """
    allowed enum values
    """
    UNSPECIFIED = "UNSPECIFIED"
    LEFT = "LEFT"
    CENTER = "CENTER"
    TOPLEFT = "TOPLEFT"
    TOP = "TOP"
    BOTTOMLEFT = "BOTTOMLEFT"
    BOTTOM = "BOTTOM"
