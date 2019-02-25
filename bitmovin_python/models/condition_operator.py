# coding: utf-8
from enum import Enum


class ConditionOperator(Enum):
    """
    allowed enum values
    """
    EQUAL = "=="
    NOT_EQUAL = "!="
    LESS_THAN_OR_EQUAL = "<="
    LESS_THAN = "<"
    GREATER_THAN = ">"
    GREATER_THAN_OR_EQUAL = ">="
