from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable
from .auto_representation import AutoRepresentation


class PerTitleConfiguration(Serializable):
    def __init__(self, min_bitrate=None, max_bitrate=None, min_bitrate_step_size=None, max_bitrate_step_size=None,
                 auto_representations=None):
        super().__init__()
        self.min_bitrate = min_bitrate
        self.max_bitrate = max_bitrate
        self.min_bitrate_step_size = min_bitrate_step_size
        self.max_bitrate_step_size = max_bitrate_step_size

        self._auto_representations = None
        self.auto_representations = auto_representations

    @property
    def auto_representations(self):
        return self._auto_representations

    @auto_representations.setter
    def auto_representations(self, new_auto_representations):
        if new_auto_representations is None:
            self._auto_representations = None
            return

        if not isinstance(new_auto_representations, AutoRepresentation):
            raise InvalidTypeError(
                'Invalid type {} for auto_representations: must be AutoRepresentation!'.format(
                    type(new_auto_representations)))

        self._auto_representations = new_auto_representations

    def serialize(self):
        serialized = super().serialize()
        serialized['autoRepresentations'] = self.auto_representations
        return serialized
