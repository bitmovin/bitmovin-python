# coding: utf-8
from enum import Enum


class DeinterlaceMode(Enum):
    """
    allowed enum values
    """
    FRAME = "FRAME"
    FIELD = "FIELD"
    FRAME_NOSPATIAL = "FRAME_NOSPATIAL"
    FIELD_NOSPATIAL = "FIELD_NOSPATIAL"
