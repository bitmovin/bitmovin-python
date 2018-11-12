from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable
from .auto_representation import AutoRepresentation


class PerTitleConfiguration(Serializable):
    def __init__(self, min_bitrate=None, max_bitrate=None, min_bitrate_step_size=None, max_bitrate_step_size=None,
                 auto_representations=None):
        super().__init__()
        self.minBitrate = min_bitrate
        self.maxBitrate = max_bitrate
        self.minBitrateStepSize = min_bitrate_step_size
        self.maxBitrateStepSize = max_bitrate_step_size

        self._autoRepresentations = None
        self.autoRepresentations = auto_representations

    @property
    def autoRepresentations(self):
        return self._autoRepresentations

    @autoRepresentations.setter
    def autoRepresentations(self, new_auto_representations):
        if new_auto_representations is None:
            self._autoRepresentations = None
            return

        if not isinstance(new_auto_representations, AutoRepresentation):
            raise InvalidTypeError(
                'Invalid type {} for auto_representations: must be AutoRepresentation!'.format(
                    type(new_auto_representations)))

        self._autoRepresentations = new_auto_representations

    def serialize(self):
        serialized = super().serialize()
        serialized['autoRepresentations'] = self.autoRepresentations
        return serialized
