from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable
from bitmovin.resources.enums import AudioVideoSyncMode


class Tweaks(Serializable):

    def __init__(self, audio_video_sync_mode=None):
        super().__init__()
        self._audio_video_sync_mode = None
        self.audioVideoSyncMode = audio_video_sync_mode

    @property
    def audioVideoSyncMode(self):
        return self._audio_video_sync_mode

    @audioVideoSyncMode.setter
    def audioVideoSyncMode(self, new_audio_video_sync_mode):
        if new_audio_video_sync_mode is None:
            self._audio_video_sync_mode = None
            return
        if isinstance(new_audio_video_sync_mode, str):
            self._audio_video_sync_mode = new_audio_video_sync_mode
        elif isinstance(new_audio_video_sync_mode, AudioVideoSyncMode):
            self._audio_video_sync_mode = new_audio_video_sync_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for audioVideoSyncMode: ' +
                'must be either str or AudioVideoSyncMode!'.format(type(new_audio_video_sync_mode)))

    def serialize(self):
        serialized = super().serialize()
        serialized['audioVideoSyncMode'] = self.audioVideoSyncMode
        return serialized
