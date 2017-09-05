from .condition_type import ConditionType
from .abstract_conjunction import AbstractConjunction


class AndConjunction(AbstractConjunction):

    def __init__(self, conditions):
        super().__init__(type_=ConditionType.AND.value, conditions=conditions)
