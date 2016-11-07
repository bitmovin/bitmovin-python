import enum


class ACLPermission(enum.Enum):
    PUBLIC_READ = 'PUBLIC_READ'
    PRIVATE = 'PRIVATE'

    @staticmethod
    def default():
        return ACLPermission.PUBLIC_READ
