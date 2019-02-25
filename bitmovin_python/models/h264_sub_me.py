# coding: utf-8
from enum import Enum


class H264SubMe(Enum):
    """
    allowed enum values
    """
    FULLPEL = "FULLPEL"
    SAD = "SAD"
    SATD = "SATD"
    QPEL3 = "QPEL3"
    QPEL4 = "QPEL4"
    QPEL5 = "QPEL5"
    RD_IP = "RD_IP"
    RD_ALL = "RD_ALL"
    RD_REF_IP = "RD_REF_IP"
    RD_REF_ALL = "RD_REF_ALL"
    QPRD = "QPRD"
    FULL_RD = "FULL_RD"
