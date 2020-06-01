from bitmovin.utils import Serializable
from bitmovin.resources.enums import BitrateSelectionMode

class StreamPerTitleFixedResolutionAndBitrateSettings(Serializable):
    def __init__(self, min_bitrate=None, max_bitrate=None, selection_mode=None, low_complexity_boundary=None, high_complexity_boundary=None):
        self.minBitrate = min_bitrate
        self.maxBitrate = max_bitrate
        self._bitrateSelectionMode = None
        self.bitrateSelectionMode = selection_mode
        self.lowComplexityBoundaryForMaxBitrate = low_complexity_boundary 
        self.highComplexityBoundaryForMaxBitrate = high_complexity_boundary

    @property
    def bitrateSelectionMode(self):
        return self._bitrateSelectionMode

    @bitrateSelectionMode.setter
    def bitrateSelectionMode(self, new_selection_mode):
        if new_selection_mode is None:
            self._bitrateSelectionMode = None
            return
        if isinstance(new_selection_mode, str):
            self._bitrateSelectionMode = new_selection_mode
        elif isinstance(new_selection_mode, BitrateSelectionMode):
            self._bitrateSelectionMode = new_selection_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for bitrateSelectionMode: must be either str or BitrateSelectionMode!'.format(type(new_forced_rendition_calculation_mode)))

    @classmethod
    def parse_from_json_object(cls, json_object):
        min_bitrate = json_object.get('minBitrate')
        max_bitrate = json_object.get('maxBitrate')
        selection_mode = json_object.get('bitrateSelectionMode')
        low_complexity_boundary = json_object.get('lowComplexityBoundaryForMaxBitrate')
        high_complexity_boundary = json_object.get('highComplexityBoundaryForMaxBitrate')
        stream_per_title_fixed_resolution_and_bitrate_settings = StreamPerTitleFixedResolutionAndBitrateSettings(min_bitrate=min_bitrate,
                                                                                                                 max_bitrate=max_bitrate,
                                                                                                                 selection_mode=selection_mode,
                                                                                                                 low_complexity_boundary=low_complexity_boundary,
                                                                                                                 high_complexity_boundary=high_complexity_boundary)
        return stream_per_title_fixed_resolution_and_bitrate_settings
    
    def serialize(self):
        serialized = super().serialize()
        serialized['bitrateSelectionMode'] = self.bitrateSelectionMode
        return serialized
    