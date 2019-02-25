# coding: utf-8
from enum import Enum


class QuantizationGroupSize(Enum):
    """
    allowed enum values
    """
    QGS_8x8 = "QGS_8x8"
    QGS_16x16 = "QGS_16x16"
    QGS_32x32 = "QGS_32x32"
    QGS_64x64 = "QGS_64x64"
