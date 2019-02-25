# coding: utf-8
from enum import Enum


class AdaptationSetRole(Enum):
    """
    allowed enum values
    """
    ALTERNATE = "ALTERNATE"
    CAPTION = "CAPTION"
    COMMENTARY = "COMMENTARY"
    DUB = "DUB"
    MAIN = "MAIN"
    SUBTITLE = "SUBTITLE"
    SUPPLEMENTARY = "SUPPLEMENTARY"
