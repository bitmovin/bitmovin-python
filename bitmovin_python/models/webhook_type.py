# coding: utf-8
from enum import Enum


class WebhookType(Enum):
    """
    allowed enum values
    """
    FINISHED = "ENCODING_FINISHED"
    ERROR = "ENCODING_ERROR"
