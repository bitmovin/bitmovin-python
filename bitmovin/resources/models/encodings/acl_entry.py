from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import ACLPermission
from bitmovin.utils import Serializable
from bitmovin.resources import AbstractIdResource


class ACLEntry(AbstractIdResource, Serializable):

    def __init__(self, permission, scope=None, id_=None):
        super().__init__(id_=id_)
        self.scope = scope
        self._permission = None
        self.permission = permission

    @property
    def permission(self):
        if self._permission is not None:
            return self._permission
        else:
            return ACLPermission.default().value

    @permission.setter
    def permission(self, new_permission):
        if new_permission is None:
            return
        if isinstance(new_permission, str):
            self._permission = new_permission
        elif isinstance(new_permission, ACLPermission):
            self._permission = new_permission.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for permission: must be either str or ACLPermission!'.format(type(new_permission)))

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        permission = json_object['permission']
        scope = json_object.get('scope')

        acl_entry = ACLEntry(scope=scope, permission=permission, id_=id_)
        return acl_entry

    def serialize(self):
        serialized = super().serialize()
        serialized['permission'] = self.permission
        return serialized
