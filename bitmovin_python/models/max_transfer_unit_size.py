# coding: utf-8
from enum import Enum


class MaxTransferUnitSize(Enum):
    """
    allowed enum values
    """
    MTU_4x4 = "MTU_4x4"
    MTU_8x8 = "MTU_8x8"
    MTU_16x16 = "MTU_16x16"
    MTU_32x32 = "MTU_32x32"
