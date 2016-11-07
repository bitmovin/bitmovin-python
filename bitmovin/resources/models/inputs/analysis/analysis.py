from bitmovin.errors import InvalidTypeError
from bitmovin.resources import AbstractCustomDataResource, CloudRegion
from bitmovin.utils import Serializable


class Analysis(AbstractCustomDataResource, Serializable):

    def __init__(self, path, cloud_region, custom_data=None):
        super().__init__(custom_data=custom_data)
        self.path = path
        self._cloudRegion = None
        self.cloudRegion = cloud_region

    @property
    def cloudRegion(self):
        if self._cloudRegion is not None:
            return self._cloudRegion
        else:
            return CloudRegion.default().value

    @cloudRegion.setter
    def cloudRegion(self, new_region):
        if new_region is None:
            return
        if isinstance(new_region, str):
            self._cloudRegion = new_region
        elif isinstance(new_region, CloudRegion):
            self._cloudRegion = new_region.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for cloudRegion: must be either str or CloudRegion!'.format(type(new_region)))

    @classmethod
    def parse_from_json_object(cls, json_object):
        raise NotImplementedError()

    def serialize(self):
        serialized = super().serialize()
        serialized['cloudRegion'] = self.cloudRegion
        return serialized
