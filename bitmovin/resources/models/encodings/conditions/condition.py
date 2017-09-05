from .abstract_condition import AbstractCondition
from .condition_type import ConditionType


class Condition(AbstractCondition):

    def __init__(self, attribute, operator, value):
        super().__init__(type_=ConditionType.CONDITION.value)
        self.attribute = attribute
        self.operator = operator
        self.value = value

    @classmethod
    def parse_from_json_object(cls, json_object):
        attribute = json_object.get('attribute')
        operator = json_object.get('operator')
        value = json_object.get('value')
        return Condition(attribute=attribute, operator=operator, value=value)

    def serialize(self):
        serialized = super().serialize()
        return serialized
