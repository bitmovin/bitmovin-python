# coding: utf-8
from enum import Enum


class InputType(Enum):
    """
    allowed enum values
    """
    AKAMAI_NETSTORAGE = "AKAMAI_NETSTORAGE"
    ASPERA = "ASPERA"
    AZURE = "AZURE"
    REDUNDANT_RTMP = "REDUNDANT_RTMP"
    FTP = "FTP"
    GENERIC_S3 = "GENERIC_S3"
    GCS = "GCS"
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    LOCAL = "LOCAL"
    RTMP = "RTMP"
    S3 = "S3"
    S3_ROLE_BASED = "S3_ROLE_BASED"
    SFTP = "SFTP"
    ZIXI = "ZIXI"
