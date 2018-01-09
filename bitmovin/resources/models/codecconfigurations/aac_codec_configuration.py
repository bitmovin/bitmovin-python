from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import AACChannelLayout
from bitmovin.utils import Serializable
from .audio_codec_configuration import AudioCodecConfiguration


class AACCodecConfiguration(AudioCodecConfiguration, Serializable):

    def __init__(self, name, bitrate, rate, id_=None, description=None, custom_data=None, channel_layout=None,
                 volume_adjust=None, normalize=None):

        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description, bitrate=bitrate,
                         rate=rate)

        self._channelLayout = None
        self.channelLayout = channel_layout
        self.normalize = normalize

    @property
    def channelLayout(self):
        if self._channelLayout is not None:
            return self._channelLayout
        else:
            return AACChannelLayout.default().value

    @channelLayout.setter
    def channelLayout(self, new_layout):
        if new_layout is None:
            return
        if isinstance(new_layout, str):
            self._channelLayout = new_layout
        elif isinstance(new_layout, AACChannelLayout):
            self._channelLayout = new_layout.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for channelLayout: must be either str or AACChannelLayout!'.format(type(new_layout)))

    @classmethod
    def parse_from_json_object(cls, json_object):
        audio_codec_configuration = AudioCodecConfiguration.parse_from_json_object(json_object=json_object)
        id_ = audio_codec_configuration.id
        name = audio_codec_configuration.name
        description = audio_codec_configuration.description
        custom_data = audio_codec_configuration.customData
        rate = audio_codec_configuration.rate
        bitrate = audio_codec_configuration.bitrate

        channel_layout = json_object.get('channelLayout')
        normalize = json_object.get('normalize')

        aac_codec_configuration = AACCodecConfiguration(id_=id_, name=name, description=description,
                                                        custom_data=custom_data, bitrate=bitrate, rate=rate,
                                                        channel_layout=channel_layout, volume_adjust=None,
                                                        normalize=normalize)

        return aac_codec_configuration

    def serialize(self):
        serialized = super().serialize()
        serialized['channelLayout'] = self.channelLayout
        return serialized
