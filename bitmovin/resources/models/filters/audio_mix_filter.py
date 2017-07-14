from . import AbstractFilter
from bitmovin.utils import Serializable
from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import AudioMixFilterChannelLayout
from . import AudioMixChannel


class AudioMixFilter(AbstractFilter, Serializable):
    def __init__(self, name=None, channel_layout=None, audio_mix_channels=None, id_=None,
                 custom_data=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self._channel_layout = None
        self._audio_mix_channels = None

        self.channel_layout = channel_layout
        self.audio_mix_channels = audio_mix_channels

    @property
    def channel_layout(self):
        return self._channel_layout

    @channel_layout.setter
    def channel_layout(self, new_value):
        if new_value is None:
            return
        if isinstance(new_value, str):
            self._channel_layout = new_value
        elif isinstance(new_value, AudioMixFilterChannelLayout):
            self._channel_layout = new_value.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for channelLayout: must be either str or AudioMixFilterChannelLayout!'.format(
                    type(new_value)))

    @property
    def audio_mix_channels(self):
        return self._audio_mix_channels

    @audio_mix_channels.setter
    def audio_mix_channels(self, new_value):
        if new_value is None:
            return

        if not isinstance(new_value, list):
            raise InvalidTypeError('partitions has to be a list of AudioMixChannel enums')

        if all(isinstance(output, AudioMixChannel) for output in new_value):
            audio_mix_channels = []
            for item in new_value:
                audio_mix_channels.append(item)
            self._audio_mix_channels = audio_mix_channels
        else:
            self._audio_mix_channels = new_value

    def serialize(self):
        serialized = super().serialize()
        serialized['channelLayout'] = self.channel_layout
        serialized['audioMixChannels'] = self.audio_mix_channels
        return serialized

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        channel_layout = json_object.get('channelLayout')
        audio_mix_channels = json_object.get('audioMixChannels')
        name = json_object.get('name')
        description = json_object.get('description')
        audio_mix_filter = AudioMixFilter(channel_layout=channel_layout, audio_mix_channels=audio_mix_channels,
                                          id_=id_, name=name, description=description)
        return audio_mix_filter
