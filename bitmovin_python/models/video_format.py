# coding: utf-8
from enum import Enum


class VideoFormat(Enum):
    """
    allowed enum values
    """
    UNDEFINED = "UNDEFINED"
    COMPONENT = "COMPONENT"
    PAL = "PAL"
    NTSC = "NTSC"
    SECAM = "SECAM"
    MAC = "MAC"
