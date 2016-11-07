import abc


class Serializable:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def serialize(self):
        serialized = {}
        serialized.update(self.__dict__)
        underscored_keys = []

        for key in serialized.keys():
            if key.startswith('_'):
                underscored_keys.append(key)

        for underscored_key in underscored_keys:
            serialized.pop(underscored_key)

        return serialized
