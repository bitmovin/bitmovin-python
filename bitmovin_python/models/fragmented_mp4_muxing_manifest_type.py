# coding: utf-8
from enum import Enum


class FragmentedMp4MuxingManifestType(Enum):
    """
    allowed enum values
    """
    SMOOTH = "SMOOTH"
    DASH_ON_DEMAND = "DASH_ON_DEMAND"
    HLS_BYTE_RANGES = "HLS_BYTE_RANGES"
    NONE = "NONE"
    HLS_BYTE_RANGES_AND_IFRAME_PLAYLIST = "HLS_BYTE_RANGES_AND_IFRAME_PLAYLIST"
