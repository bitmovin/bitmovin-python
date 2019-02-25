# coding: utf-8
from enum import Enum


class S3SignatureVersion(Enum):
    """
    allowed enum values
    """
    V2 = "S3_V2"
    V4 = "S3_V4"
