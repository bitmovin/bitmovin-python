from .ConditionType import ConditionType
from .AbstractConjunction import AbstractConjunction


class AndConjunction(AbstractConjunction):

    def __init__(self, conditions):
        super().__init__(type=ConditionType.AND.value, conditions=conditions)

    @classmethod
    def parse_from_json_object(cls, json_object):
        conditions_json = json_object.get('conditions')
        return AndConjunction(conditions=conditions_json)
