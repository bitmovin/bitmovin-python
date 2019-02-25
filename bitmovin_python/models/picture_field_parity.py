# coding: utf-8
from enum import Enum


class PictureFieldParity(Enum):
    """
    allowed enum values
    """
    AUTO = "AUTO"
    TOP_FIELD_FIRST = "TOP_FIELD_FIRST"
    BOTTOM_FIELD_FIRST = "BOTTOM_FIELD_FIRST"
