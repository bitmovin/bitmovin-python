from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable
from .stream_per_title_fixed_res_bitrate_settings import StreamPerTitleFixedResolutionAndBitrateSettings


class StreamPerTitleSettings(Serializable):
    def __init__(self, fixed_resolution_and_bitrate_settings=None):
        super().__init__()
        self._fixedResolutionAndBitrateSettings = None
        self.fixedResolutionAndBitrateSettings = fixed_resolution_and_bitrate_settings

    @property
    def fixedResolutionAndBitrateSettings(self):
        return self._fixedResolutionAndBitrateSettings

    @fixedResolutionAndBitrateSettings.setter
    def fixedResolutionAndBitrateSettings(self, new_fixed_resolution_and_bitrate_settings):
        if new_fixed_resolution_and_bitrate_settings is None:
            self._fixedResolutionAndBitrateSettings = None
            return

        if isinstance(new_fixed_resolution_and_bitrate_settings, StreamPerTitleFixedResolutionAndBitrateSettings):
            self._fixedResolutionAndBitrateSettings = new_fixed_resolution_and_bitrate_settings
        else:
            self._fixedResolutionAndBitrateSettings = StreamPerTitleFixedResolutionAndBitrateSettings.parse_from_json_object(new_fixed_resolution_and_bitrate_settings)

    @classmethod
    def parse_from_json_object(cls, json_object):
        fixed_resolution_and_bitrate_settings = json_object.get('fixedResolutionAndBitrateSettings')
        stream_per_title_settings = StreamPerTitleSettings(fixed_resolution_and_bitrate_settings=fixed_resolution_and_bitrate_settings)
        return stream_per_title_settings

    def serialize(self):
        serialized = super().serialize()
        serialized['fixedResolutionAndBitrateSettings'] = self.fixedResolutionAndBitrateSettings
        return serialized
