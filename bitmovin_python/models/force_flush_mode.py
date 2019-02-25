# coding: utf-8
from enum import Enum


class ForceFlushMode(Enum):
    """
    allowed enum values
    """
    DISABLED = "DISABLED"
    ALL_FRAMES = "ALL_FRAMES"
    SLICE_TYPE = "SLICE_TYPE"
