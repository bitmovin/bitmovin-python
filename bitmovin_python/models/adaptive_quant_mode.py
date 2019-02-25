# coding: utf-8
from enum import Enum


class AdaptiveQuantMode(Enum):
    """
    allowed enum values
    """
    DISABLED = "DISABLED"
    VARIANCE = "VARIANCE"
    AUTO_VARIANCE = "AUTO_VARIANCE"
    AUTO_VARIANCE_DARK_SCENES = "AUTO_VARIANCE_DARK_SCENES"
