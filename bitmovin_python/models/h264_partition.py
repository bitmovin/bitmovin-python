# coding: utf-8
from enum import Enum


class H264Partition(Enum):
    """
    allowed enum values
    """
    NONE = "NONE"
    P8X8 = "P8X8"
    P4X4 = "P4X4"
    B8X8 = "B8X8"
    I8X8 = "I8X8"
    I4X4 = "I4X4"
    ALL = "ALL"
