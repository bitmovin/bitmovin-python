# coding: utf-8
from enum import Enum


class ManifestType(Enum):
    """
    allowed enum values
    """
    DASH = "DASH"
    HLS = "HLS"
    SMOOTH_STREAMING = "SMOOTH_STREAMING"
