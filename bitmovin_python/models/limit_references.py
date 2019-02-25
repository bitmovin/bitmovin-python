# coding: utf-8
from enum import Enum


class LimitReferences(Enum):
    """
    allowed enum values
    """
    DISABLED = "DISABLED"
    DEPTH = "DEPTH"
    CU = "CU"
    DEPTH_AND_CU = "DEPTH_AND_CU"
