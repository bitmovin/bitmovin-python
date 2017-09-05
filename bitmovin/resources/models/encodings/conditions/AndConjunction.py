from .ConditionType import ConditionType
from .AbstractConjunction import AbstractConjunction


class AndConjunction(AbstractConjunction):

    def __init__(self, conditions):
        super().__init__(type_=ConditionType.AND.value, conditions=conditions)
