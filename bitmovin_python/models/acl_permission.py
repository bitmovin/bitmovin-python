# coding: utf-8
from enum import Enum


class AclPermission(Enum):
    """
    allowed enum values
    """
    PUBLIC_READ = "PUBLIC_READ"
    PRIVATE = "PRIVATE"
