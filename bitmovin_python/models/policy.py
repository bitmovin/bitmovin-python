# coding: utf-8
from enum import Enum


class Policy(Enum):
    """
    allowed enum values
    """
    ALLOW = "ALLOW"
    DENY = "DENY"
