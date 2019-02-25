# coding: utf-8
from enum import Enum


class H264NalHrd(Enum):
    """
    allowed enum values
    """
    NONE = "NONE"
    VBR = "VBR"
    CBR = "CBR"
