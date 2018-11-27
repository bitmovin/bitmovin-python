from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable
from .h264_per_title_configuration import H264PerTitleConfiguration
from .h265_per_title_configuration import H265PerTitleConfiguration
from .vp9_per_title_configuration import VP9PerTitleConfiguration

class PerTitle(Serializable):
    def __init__(self, h264_configuration=None, h265_configuration=None, vp9_configuration=None):
        super().__init__()

        self._h264_configuration = None
        self.h264_configuration = h264_configuration
        self._h265_configuration = None
        self.h265_configuration = h265_configuration
        self._vp9_configuration = None
        self.vp9_configuration = vp9_configuration

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
         
    @property
    def h265_configuration(self):
        return self._h265_configuration

    @h265_configuration.setter
    def h265_configuration(self, new_h265_configuration):
        if new_h265_configuration is None:
            self._h265_configuration = None
            return
        if not isinstance(new_h265_configuration, H265PerTitleConfiguration):
            raise InvalidTypeError(
                'Invalid type {} for h265_configuration: must be H265PerTitleConfiguration!'.format(
                    type(new_h265_configuration)))

        self._h265_configuration = new_h265_configuration
        
    @property
    def vp9_configuration(self):
        return self._vp9_configuration

    @vp9_configuration.setter
    def vp9_configuration(self, new_vp9_configuration):
        if new_vp9_configuration is None:
            self._vp9_configuration = None
            return
        if not isinstance(new_vp9_configuration, VP9PerTitleConfiguration):
            raise InvalidTypeError(
                'Invalid type {} for vp9_configuration: must be VP9PerTitleConfiguration!'.format(
                    type(new_vp9_configuration)))

        self._vp9_configuration = new_vp9_configuration

    def serialize(self):
        serialized = super().serialize()
        serialized['h264Configuration'] = self.h264_configuration
        serialized['h265Configuration'] = self.h265_configuration
        serialized['vp9Configuration'] = self.vp9_configuration

        return serialized
