from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable


class Scheduling(Serializable):

    def __init__(self, priority=None, prewarmed_instance_pool_ids=None):
        super().__init__()
        self._prewarmed_instance_pool_ids = None
        self.priority = priority
        self.prewarmedInstancePoolIds = prewarmed_instance_pool_ids

    @property
    def prewarmedInstancePoolIds(self):
        return self._prewarmed_instance_pool_ids

    @prewarmedInstancePoolIds.setter
    def prewarmedInstancePoolIds(self, new_prewarmed_instance_pool_ids):
        if new_prewarmed_instance_pool_ids is None:
            self._prewarmed_instance_pool_ids = None
            return

        if not isinstance(new_prewarmed_instance_pool_ids, list):
            raise InvalidTypeError('prewarmedInstancePoolIds has to be a list of strings')

        if all(isinstance(pool_id, str) for pool_id in new_prewarmed_instance_pool_ids):
            self._prewarmed_instance_pool_ids = new_prewarmed_instance_pool_ids
        else:
            raise InvalidTypeError('prewarmedInstancePoolIds has to be a list of strings')

    def serialize(self):
        serialized = super().serialize()
        serialized['prewarmedInstancePoolIds'] = self.prewarmedInstancePoolIds
        return serialized
