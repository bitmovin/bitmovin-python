from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable
from .auto_representation import AutoRepresentation
from .fixed_resolution_and_bitrate_configuration import PerTitleFixedResolutionAndBitrateConfiguration


class PerTitleConfiguration(Serializable):
    def __init__(self, min_bitrate=None, max_bitrate=None, min_bitrate_step_size=None, max_bitrate_step_size=None,
                 auto_representations=None, complexity_factor=None, fixed_resolution_and_bitrate_configuration=None):
        super().__init__()
        self.minBitrate = min_bitrate
        self.maxBitrate = max_bitrate
        self.minBitrateStepSize = min_bitrate_step_size
        self.maxBitrateStepSize = max_bitrate_step_size
        self.complexityFactor = complexity_factor

        self._auto_representations = None
        self.autoRepresentations = auto_representations
        
        self._fixedResolutionAndBitrateConfiguration = None
        self.fixedResolutionAndBitrateConfiguration = fixed_resolution_and_bitrate_configuration

    @property
    def autoRepresentations(self):
        return self._auto_representations

    @autoRepresentations.setter
    def autoRepresentations(self, new_auto_representations):
        if new_auto_representations is None:
            self._auto_representations = None
            return

        if not isinstance(new_auto_representations, AutoRepresentation):
            raise InvalidTypeError(
                'Invalid type {} for auto_representations: must be AutoRepresentation!'.format(
                    type(new_auto_representations)))

        self._auto_representations = new_auto_representations

    @property
    def fixedResolutionAndBitrateConfiguration(self):
        return self._fixedResolutionAndBitrateConfiguration

    @fixedResolutionAndBitrateConfiguration.setter
    def fixedResolutionAndBitrateConfiguration(self, new_fixed_resolution_and_bitrate_configuration):
        if new_fixed_resolution_and_bitrate_configuration is None:
            self._fixedResolutionAndBitrateConfiguration = None
            return

        if not isinstance(new_fixed_resolution_and_bitrate_configuration, PerTitleFixedResolutionAndBitrateConfiguration):
            raise InvalidTypeError(
                'Invalid type {} for fixed_resolution_and_bitrate_configuration: must be PerTitleFixedResolutionAndBitrateConfiguration!'.format(
                    type(new_fixed_resolution_and_bitrate_configuration)))

        self._fixedResolutionAndBitrateConfiguration = new_fixed_resolution_and_bitrate_configuration

    def serialize(self):
        serialized = super().serialize()
        serialized['autoRepresentations'] = self.autoRepresentations
        serialized['fixedResolutionAndBitrateConfiguration'] = self.fixedResolutionAndBitrateConfiguration
        return serialized
