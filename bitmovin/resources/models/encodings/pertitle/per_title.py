from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable
from .h264_per_title_configuration import H264PerTitleConfiguration


class PerTitle(Serializable):
    def __init__(self, h264_configuration=None):
        super().__init__()

        self._h264_configuration = None
        self.h264_configuration = h264_configuration

    @property
    def h264_configuration(self):
        return self._h264_configuration

    @h264_configuration.setter
    def h264_configuration(self, new_h264_configuration):
        if new_h264_configuration is None:
            self._h264_configuration = None
            return
        if not isinstance(new_h264_configuration, H264PerTitleConfiguration):
            raise InvalidTypeError(
                'Invalid type {} for h264_configuration: must be H264PerTitleConfiguration!'.format(
                    type(new_h264_configuration)))

        self._h264_configuration = new_h264_configuration

    def serialize(self):
        serialized = super().serialize()
        serialized['h264Configuration'] = self.h264_configuration

        return serialized
