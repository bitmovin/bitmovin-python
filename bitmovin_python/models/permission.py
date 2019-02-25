# coding: utf-8
from enum import Enum


class Permission(Enum):
    """
    allowed enum values
    """
    GET = "GET"
    DELETE = "DELETE"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
