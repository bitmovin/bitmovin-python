# coding: utf-8
from enum import Enum


class DashMuxingType(Enum):
    """
    allowed enum values
    """
    TEMPLATE = "TEMPLATE"
    LIST = "LIST"
    TIMELINE = "TIMELINE"
