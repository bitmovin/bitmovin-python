from .abstract_codec_configuration import AbstractCodecConfiguration


class MJPEGCodecConfiguration(AbstractCodecConfiguration):
    def __init__(self, name, id_=None, description=None, custom_data=None, rate=None, width=None, height=None,
                 pixel_format=None, q_scale=None):

        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)

        self.width = width
        self.height = height
        self.pixel_format = pixel_format
        self.qScale = q_scale
        self.rate = rate

    @classmethod
    def parse_from_json_object(cls, json_object):
        codec_configuration = AbstractCodecConfiguration.parse_from_json_object(json_object=json_object)

        id_ = codec_configuration.id
        custom_data = codec_configuration.customData
        name = codec_configuration.name
        description = codec_configuration.description

        width = json_object.get('width')
        height = json_object.get('height')
        rate = json_object.get('rate')
        pixel_format = json_object.get('pixelFormat')
        q_scale = json_object.get('qScale')

        mjpeg_codec_config = MJPEGCodecConfiguration(name=name, id_=id_, description=description,
                                                     custom_data=custom_data, rate=rate, width=width, height=height,
                                                     pixel_format=pixel_format, q_scale=q_scale)

        return mjpeg_codec_config
