# coding: utf-8
from enum import Enum


class Vp8NoiseSensitivity(Enum):
    """
    allowed enum values
    """
    OFF = "OFF"
    ON_Y_ONLY = "ON_Y_ONLY"
    ON_YUV = "ON_YUV"
    ON_YUV_AGGRESSIVE = "ON_YUV_AGGRESSIVE"
    ADAPTIVE = "ADAPTIVE"
