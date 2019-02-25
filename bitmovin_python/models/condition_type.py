# coding: utf-8
from enum import Enum


class ConditionType(Enum):
    """
    allowed enum values
    """
    CONDITION = "CONDITION"
    AND = "AND"
    OR = "OR"
