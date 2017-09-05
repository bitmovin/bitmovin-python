from .abstract_conjunction import AbstractConjunction
from .condition_type import ConditionType


class OrConjunction(AbstractConjunction):

    def __init__(self, conditions):
        super().__init__(type_=ConditionType.OR.value, conditions=conditions)
