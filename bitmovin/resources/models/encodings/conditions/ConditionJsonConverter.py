from bitmovin.errors import InvalidTypeError
from .OrConjunction import OrConjunction
from .AndConjunction import AndConjunction
from .ConditionType import ConditionType
from .Condition import Condition


class ConditionJsonConverter():

    @classmethod
    def parse_conditions(cls, conditions_json):
        if(conditions_json is None):
            return None

        condition_type = conditions_json.get('type')
        if condition_type is None:
            raise InvalidTypeError('type of condition is None')

        if condition_type == ConditionType.CONDITION.value:
            return Condition.parse_from_json_object(json_object=conditions_json)
        if condition_type == ConditionType.AND.value:
            return AndConjunction.parse_from_json_object(json_object=conditions_json)
        if condition_type == ConditionType.OR.value:
            return OrConjunction.parse_from_json_object(json_object=conditions_json)

        raise InvalidTypeError('unknown ConditionType {}'.format(condition_type))

