# coding: utf-8
from enum import Enum


class H264Trellis(Enum):
    """
    allowed enum values
    """
    DISABLED = "DISABLED"
    ENABLED_FINAL_MB = "ENABLED_FINAL_MB"
    ENABLED_ALL = "ENABLED_ALL"
