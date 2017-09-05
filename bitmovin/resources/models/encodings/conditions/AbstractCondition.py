from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable
from .ConditionType import ConditionType


class AbstractCondition(Serializable):

    def __init__(self, type_):
        super().__init__()

        self._type = None
        self.type = type_

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, new_type):
        if new_type is None:
            return
        if isinstance(new_type, str):
            self._type = new_type
        elif isinstance(new_type, ConditionType):
            self._type = new_type.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for type: must be either str or ConditionType!'.format(type(new_type)))

    def serialize(self):
        serialized = super().serialize()
        serialized['type'] = self._type
        return serialized

