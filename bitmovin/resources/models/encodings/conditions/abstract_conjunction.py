from bitmovin.errors import InvalidTypeError
from .abstract_condition import AbstractCondition


class AbstractConjunction(AbstractCondition):

    @property
    def conditions(self):
        return self._conditions

    def __init__(self, type_, conditions):
        super().__init__(type_=type_)
        self._conditions = None
        self.conditions=conditions

    @conditions.setter
    def conditions(self, new_conditions):
        if new_conditions is None:
            return

        if not isinstance(new_conditions, list):
            raise InvalidTypeError('new_conditions has to be a list')

        if all(isinstance(new_condition, AbstractCondition) for new_condition in new_conditions):
            self._conditions = new_conditions
        else:
            raise InvalidTypeError('Invalid type for conditions list')

    def serialize(self):
        serialized = super().serialize()
        serialized['conditions'] = self._conditions
        return serialized

