from bitmovin.errors import InvalidTypeError
from .ignored_by_type import IgnoredByType
from bitmovin.utils import Serializable


class IgnoredBy(Serializable):

    def __init__(self, ignored_by, ignored_by_description):
        super().__init__()
        self._ignoredBy = None
        self.ignored_by = ignored_by
        self.ignoredByDescription = ignored_by_description

    @property
    def ignored_by(self):
        return self._ignoredBy

    @ignored_by.setter
    def ignored_by(self, new_type):
        if new_type is None:
            return
        if isinstance(new_type, str):
            self._ignoredBy = new_type
        elif isinstance(new_type, IgnoredByType):
            self._ignoredBy = new_type.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for type: must be either str or IgnoredByType!'.format(type(new_type)))

    @classmethod
    def parse_from_json_object(cls, json_object):
        ignored_by = json_object['ignoredBy']
        ignored_by_description = json_object.get('ignoredByDescription')

        obj = IgnoredBy(ignored_by=ignored_by, ignored_by_description=ignored_by_description)
        return obj

    def serialize(self):
        serialized = super().serialize()
        serialized['type'] = self._ignoredBy
        return serialized
