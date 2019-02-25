# coding: utf-8
from enum import Enum


class CodecConfigType(Enum):
    """
    allowed enum values
    """
    AAC = "AAC"
    HE_AAC_V1 = "HE_AAC_V1"
    HE_AAC_V2 = "HE_AAC_V2"
    H264 = "H264"
    H265 = "H265"
    VP9 = "VP9"
    VP8 = "VP8"
    MP2 = "MP2"
    MP3 = "MP3"
    AC3 = "AC3"
    EAC3 = "EAC3"
    OPUS = "OPUS"
    VORBIS = "VORBIS"
    MJPEG = "MJPEG"
    AV1 = "AV1"
