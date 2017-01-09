from .abstract_codec_configuration import AbstractCodecConfiguration


class AudioCodecConfiguration(AbstractCodecConfiguration):

    def __init__(self, id_, name, bitrate, rate, description=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.bitrate = bitrate
        self.rate = rate

    @classmethod
    def parse_from_json_object(cls, json_object):
        abstract_codec_configuration = AbstractCodecConfiguration.parse_from_json_object(json_object=json_object)
        id_ = abstract_codec_configuration.id
        name = abstract_codec_configuration.name
        description = abstract_codec_configuration.description
        custom_data = abstract_codec_configuration.customData
        rate = json_object.get('rate')
        bitrate = json_object['bitrate']

        audio_codec_configuration = AudioCodecConfiguration(id_=id_, name=name, description=description,
                                                            custom_data=custom_data, bitrate=bitrate, rate=rate)

        return audio_codec_configuration
