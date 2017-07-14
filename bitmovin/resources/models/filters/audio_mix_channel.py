from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable
from . import AudioMixSourceChannel


class AudioMixChannel(Serializable):
    def __init__(self, channel_number, source_channels):
        super().__init__()
        self._source_channels = None

        self.channelNumber = channel_number
        self.source_channels = source_channels

    @property
    def source_channels(self):
        return self._source_channels

    @source_channels.setter
    def source_channels(self, new_value):
        if new_value is None:
            return

        if not isinstance(new_value, list):
            raise InvalidTypeError('source_channels has to be a list of AudioMixSourceChannel enums')

        if all(isinstance(output, AudioMixSourceChannel) for output in new_value):
            source_channels = []
            for item in new_value:
                source_channels.append(item)
            self._source_channels = source_channels
        else:
            self._source_channels = new_value

    def serialize(self):
        serialized = super().serialize()
        serialized['sourceChannels'] = self.source_channels
        return serialized

    @classmethod
    def parse_from_json_object(cls, json_object):
        channel_number = json_object.get('channelNumber')
        source_channels = json_object.get('sourceChannels')
        audio_mix_channel = AudioMixChannel(channel_number=channel_number, source_channels=source_channels)
        return audio_mix_channel
