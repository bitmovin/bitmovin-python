# coding: utf-8
from enum import Enum


class RetryHint(Enum):
    """
    allowed enum values
    """
    RETRY = "RETRY"
    RETRY_IN_DIFFERENT_REGION = "RETRY_IN_DIFFERENT_REGION"
    NO_RETRY = "NO_RETRY"
