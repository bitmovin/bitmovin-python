# coding: utf-8
from enum import Enum


class RaiUnit(Enum):
    """
    allowed enum values
    """
    NONE = "NONE"
    ALL_PES_PACKETS = "ALL_PES_PACKETS"
    ACQUISITION_POINT_PACKETS = "ACQUISITION_POINT_PACKETS"
    ACCORDING_TO_INPUT = "ACCORDING_TO_INPUT"
