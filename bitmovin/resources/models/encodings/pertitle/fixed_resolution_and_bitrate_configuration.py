from bitmovin.utils import Serializable
from bitmovin.resources.enums import PerTitleFixedResolutionAndBitrateCalculationMode

class PerTitleFixedResolutionAndBitrateConfiguration(Serializable):
    def __init__(self, forced_renditions, forced_rendition_factor, forced_rendition_calculation_mode):
        self.forcedRenditionAboveHighestFixedRepresentation = forced_renditions
        self.forcedRenditionAboveHighestFixedRepresentationFactor = forced_rendition_factor
        
        self._forced_rendition_calculation_mode = None
        self.forcedRenditionAboveHighestFixedRepresentationCalculationMode = forced_rendition_calculation_mode

    @property
    def forcedRenditionAboveHighestFixedRepresentationCalculationMode(self):
        return self._forced_rendition_calculation_mode

    @forcedRenditionAboveHighestFixedRepresentationCalculationMode.setter
    def forcedRenditionAboveHighestFixedRepresentationCalculationMode(self, new_forced_rendition_calculation_mode):
        if new_forced_rendition_calculation_mode is None:
            self._forced_rendition_calculation_mode = None
            return
        if isinstance(new_forced_rendition_calculation_mode, str):
            self._forced_rendition_calculation_mode = new_forced_rendition_calculation_mode
        elif isinstance(new_forced_rendition_calculation_mode, PerTitleFixedResolutionAndBitrateCalculationMode):
            self._forced_rendition_calculation_mode = new_forced_rendition_calculation_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for forcedRenditionAboveHighestFixedRepresentationCalculationMode: must be either str or PerTitleFixedResolutionAndBitrateCalculationMode!'.format(type(new_forced_rendition_calculation_mode)))
            
    def serialize(self):
        serialized = super().serialize()
        serialized['forcedRenditionAboveHighestFixedRepresentationCalculationMode'] = self.forcedRenditionAboveHighestFixedRepresentationCalculationMode
        return serialized