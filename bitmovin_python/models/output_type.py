# coding: utf-8
from enum import Enum


class OutputType(Enum):
    """
    allowed enum values
    """
    AKAMAI_NETSTORAGE = "AKAMAI_NETSTORAGE"
    AZURE = "AZURE"
    GENERIC_S3 = "GENERIC_S3"
    GCS = "GCS"
    FTP = "FTP"
    LOCAL = "LOCAL"
    S3 = "S3"
    S3_ROLE_BASED = "S3_ROLE_BASED"
    SFTP = "SFTP"
