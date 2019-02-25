# coding: utf-8
from enum import Enum


class Vp9ArnrType(Enum):
    """
    allowed enum values
    """
    BACKWARD = "BACKWARD"
    FORWARD = "FORWARD"
    CENTERED = "CENTERED"
