from .AbstractConjunction import AbstractConjunction
from .ConditionType import ConditionType


class OrConjunction(AbstractConjunction):

    def __init__(self, conditions):
        super().__init__(type=ConditionType.Or.value, conditions=conditions)

    @classmethod
    def parse_from_json_object(cls, json_object):
        conditions_json = json_object.get('conditions')
        return OrConjunction(conditions=conditions_json)
