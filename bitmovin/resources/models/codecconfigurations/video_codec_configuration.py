from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums.pixel_format import PixelFormat
from bitmovin.utils import Serializable

from .abstract_codec_configuration import AbstractCodecConfiguration

class VideoCodecConfiguration(AbstractCodecConfiguration, Serializable):

    def __init__(self, id_, name, bitrate, rate, width=None, height=None, description=None, custom_data=None,
                 pixel_format=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self._pixel_format = None
        self.pixelFormat = pixel_format
        self.bitrate = bitrate
        self.rate = rate
        self.width = width
        self.height = height

    @property
    def pixelFormat(self):
        return self._pixel_format

    @pixelFormat.setter
    def pixelFormat(self, new_format):
        if new_format is None:
            return
        if isinstance(new_format, str):
            self._pixel_format = new_format
        elif isinstance(new_format, PixelFormat):
            self._pixel_format = new_format.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for pixelFormat: must be either str or PixelFormat!'.format(type(new_format)))

    @classmethod
    def parse_from_json_object(cls, json_object):
        abstract_codec_configuration = AbstractCodecConfiguration.parse_from_json_object(json_object=json_object)
        id_ = abstract_codec_configuration.id
        name = abstract_codec_configuration.name
        description = abstract_codec_configuration.description
        custom_data = abstract_codec_configuration.customData
        rate = json_object.get('rate')
        bitrate = json_object.get('bitrate')
        width = json_object.get('width')
        height = json_object.get('height')
        pixel_format = json_object.get('pixelFormat')

        video_codec_configuration = VideoCodecConfiguration(id_=id_, name=name, description=description,
                                                            custom_data=custom_data, bitrate=bitrate, rate=rate,
                                                            width=width, height=height, pixel_format=pixel_format)

        return video_codec_configuration

    def serialize(self):
        serialized = super().serialize()
        serialized['pixelFormat'] = self.pixelFormat
        return serialized
