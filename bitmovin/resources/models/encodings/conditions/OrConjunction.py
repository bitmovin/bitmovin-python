from .AbstractConjunction import AbstractConjunction
from .ConditionType import ConditionType

class OrConjunction(AbstractConjunction):

    def __init__(self, conditions):
        super().__init__(type=ConditionType.OR.value, conditions=conditions)
