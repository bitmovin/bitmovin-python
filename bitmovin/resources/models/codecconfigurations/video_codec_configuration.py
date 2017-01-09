from .abstract_codec_configuration import AbstractCodecConfiguration


class VideoCodecConfiguration(AbstractCodecConfiguration):

    def __init__(self, id_, name, bitrate, rate, width=None, height=None, description=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.bitrate = bitrate
        self.rate = rate
        self.width = width
        self.height = height

    @classmethod
    def parse_from_json_object(cls, json_object):
        abstract_codec_configuration = AbstractCodecConfiguration.parse_from_json_object(json_object=json_object)
        id_ = abstract_codec_configuration.id
        name = abstract_codec_configuration.name
        description = abstract_codec_configuration.description
        custom_data = abstract_codec_configuration.customData
        rate = json_object.get('rate')
        bitrate = json_object['bitrate']
        width = json_object.get('width')
        height = json_object.get('height')

        video_codec_configuration = VideoCodecConfiguration(id_=id_, name=name, description=description,
                                                            custom_data=custom_data, bitrate=bitrate, rate=rate,
                                                            width=width, height=height)

        return video_codec_configuration
