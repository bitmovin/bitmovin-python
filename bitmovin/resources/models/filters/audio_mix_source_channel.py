from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import AudioMixFilterChannelType
from bitmovin.utils import Serializable


class AudioMixSourceChannel(Serializable):
    def __init__(self, channel_type, channel_number, gain=1.0):
        super().__init__()
        self._channel_type = None

        self.channelNumber = channel_number
        self.gain = gain
        self.channel_type = channel_type

    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, new_value):
        if new_value is None:
            return
        if isinstance(new_value, str):
            self._channel_type = new_value
        elif isinstance(new_value, AudioMixFilterChannelType):
            self._channel_type = new_value.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for channelType: must be either str or AudioMixFilterChannelType!'.format(
                    type(new_value)))

    def serialize(self):
        serialized = super().serialize()
        serialized['type'] = self.channel_type
        return serialized

    @classmethod
    def parse_from_json_object(cls, json_object):
        channel_type = json_object.get('type')
        channel_number = json_object.get('channelNumber')
        gain = json_object.get('gain')
        audio_mix_channel = AudioMixSourceChannel(channel_type=channel_type, channel_number=channel_number, gain=gain)
        return audio_mix_channel
