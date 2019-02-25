# coding: utf-8
from enum import Enum


class H264MotionEstimationMethod(Enum):
    """
    allowed enum values
    """
    DIA = "DIA"
    HEX = "HEX"
    UMH = "UMH"
    ESA = "ESA"
    TESA = "TESA"
