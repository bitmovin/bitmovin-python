# coding: utf-8
from enum import Enum


class ColorSpace(Enum):
    """
    allowed enum values
    """
    UNSPECIFIED = "UNSPECIFIED"
    RGB = "RGB"
    BT709 = "BT709"
    FCC = "FCC"
    BT470BG = "BT470BG"
    SMPTE170M = "SMPTE170M"
    SMPTE240M = "SMPTE240M"
    YCGCO = "YCGCO"
    YCOCG = "YCOCG"
    BT2020_NCL = "BT2020_NCL"
    BT2020_CL = "BT2020_CL"
    SMPTE2085 = "SMPTE2085"
