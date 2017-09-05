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
            conditions_list = conditions_json.get('conditions')
            conditions_parsed = ConditionJsonConverter.parse_conditions_list(conditions_list)
            return AndConjunction(conditions=conditions_parsed)
        if condition_type == ConditionType.OR.value:
            conditions_list = conditions_json.get('conditions')
            conditions_parsed = ConditionJsonConverter.parse_conditions_list(conditions_list)
            return OrConjunction(conditions=conditions_parsed)

        raise InvalidTypeError('unknown ConditionType {}'.format(condition_type))


    @classmethod
    def parse_conditions_list(cls, conditions_list):
        if(conditions_list is None):
            return None

        if not isinstance(conditions_list, list):
            raise InvalidTypeError('conditions_list has to be a list')

        conditions = []
        for condition_json in conditions_list:
            condition = ConditionJsonConverter.parse_conditions(condition_json)
            conditions.append(condition)
        return conditions

