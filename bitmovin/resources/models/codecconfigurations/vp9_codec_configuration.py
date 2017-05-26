from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums.vp9_aq_mode import VP9AQMode
from bitmovin.resources.enums.vp9_arnr_type import VP9ARNRType
from bitmovin.resources.enums.vp9_quality import VP9Quality

from bitmovin.utils import Serializable
from .video_codec_configuration import VideoCodecConfiguration


class VP9CodecConfiguration(VideoCodecConfiguration, Serializable):

    def __init__(self, name, bitrate, rate, id_=None, description=None, custom_data=None, width=None,
                 height=None, lag_in_frames=None, tile_columns=None, tile_rows=None, frame_parallel=None,
                 max_intra_rate=None, qp_min=None, qp_max=None, crf=None, rate_undershoot_pct=None,
                 rate_overshoot_pct=None, cpu_used=None, noise_sensitivity=None, quality=None,
                 lossless=None, static_thresh=None, aq_mode=None, arnr_max_frames=None, 
                 arnr_strength=None, arnr_type=None):

        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description, bitrate=bitrate,
                         rate=rate, width=width, height=height)

        self.lagInFrames = lag_in_frames
        self.tileColumns = tile_columns
        self.tileRows = tile_rows
        self.frameParallel = frame_parallel
        self.maxIntraRate = max_intra_rate
        self.qpMin = qp_min
        self.qpMax = qp_max
        self.crf = crf
        self.rateUndershootPct = rate_undershoot_pct
        self.rateOvershootPct = rate_overshoot_pct
        self.cpuUsed = cpu_used
        self.noiseSensitivity = noise_sensitivity
        self._quality = None
        self.quality = quality
        self.lossless = lossless
        self.staticThresh = static_thresh
        self._aqMode = None
        self.aqMode = aq_mode
        self.arnrMaxFrames = arnr_max_frames
        self.arnrStrength = arnr_strength
        self._arnrType = None
        self.arnrType = arnr_type
        
        

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, new_quality):
        if new_quality is None:
            return
        if isinstance(new_quality, str):
            self._quality = new_quality
        elif isinstance(new_quality, VP9Quality):
            self._quality = new_quality.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for profile: must be either str or VP9Quality!'.format(type(new_quality)))

    @property
    def aqMode(self):
        return self._aqMode

    @aqMode.setter
    def aqMode(self, new_aqMode):
        if new_aqMode is None:
            return
        if isinstance(new_aqMode, str):
            self._aqMode = new_aqMode
        elif isinstance(new_aqMode, VP9AQMode):
            self._aqMode = new_aqMode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for aqMode: must be either str or VP9AQMode!'.format(type(new_aqMode)))

    @property
    def arnrType(self):
        return self._arnrType

    @arnrType.setter
    def arnrType(self, new_arnrType):
        if new_arnrType is None:
            return
        if isinstance(new_arnrType, str):
            self._arnrType = new_arnrType
        elif isinstance(new_arnrType, VP9ARNRType):
            self._arnrType = new_arnrType.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for arnrType: must be either str or VP9ARNRType!'.format(type(new_arnrType)))

    @classmethod
    def parse_from_json_object(cls, json_object):
        video_codec_configuration = VideoCodecConfiguration.parse_from_json_object(json_object=json_object)

        id_ = video_codec_configuration.id
        custom_data = video_codec_configuration.customData
        name = video_codec_configuration.name
        description = video_codec_configuration.description
        width = video_codec_configuration.width
        height = video_codec_configuration.height
        bitrate = video_codec_configuration.bitrate
        rate = video_codec_configuration.rate

        lag_in_frames = json_object.get('lagInFrames')
        tile_columns = json_object.get('tileColumns')
        tile_rows = json_object.get('tileRows')
        frame_parallel = json_object.get('frameParallel')
        max_intra_rate = json_object.get('maxIntraRate')
        qp_min = json_object.get('qpMin')
        qp_max = json_object.get('qpMax')
        crf = json_object.get('crf')
        rate_undershoot_pct = json_object.get('rateUndershootPct')
        rate_overshoot_pct = json_object.get('rateOvershootPct')
        cpu_used = json_object.get('cpuUsed')
        noise_sensitivity = json_object.get('noiseSensitivity')
        quality = json_object.get('quality')
        lossless = json_object.get('lossless')
        static_thresh = json_object.get('staticThresh')
        aq_mode = json_object.get('aqMode')
        arnr_max_frames = json_object.get('arnrMaxFrames')
        arnr_strength = json_object.get('arnrStrength')
        arnr_type = json_object.get('arnrType')

        

        vp9_codec_configuration = VP9CodecConfiguration(name=name, bitrate=bitrate, rate=rate, id_=id_, 
                                                        description=description, custom_data=custom_data, width=width, 
                                                        height=height, lag_in_frames=lag_in_frames, 
                                                        tile_columns=tile_columns, tile_rows=tile_rows, 
                                                        frame_parallel=frame_parallel, max_intra_rate=max_intra_rate, 
                                                        qp_min=qp_min, qp_max=qp_max, crf=crf, 
                                                        rate_undershoot_pct=rate_undershoot_pct, 
                                                        rate_overshoot_pct=rate_overshoot_pct, cpu_used=cpu_used, 
                                                        noise_sensitivity=noise_sensitivity, quality=quality, 
                                                        lossless=lossless, static_thresh=static_thresh, 
                                                        aq_mode=aq_mode, arnr_max_frames=arnr_max_frames, 
                                                        arnr_strength=arnr_strength, arnr_type=arnr_type)

        return vp9_codec_configuration

    def serialize(self):
        serialized = super().serialize()
        serialized['quality'] = self.quality
        serialized['aqMode'] = self.aqMode
        serialized['arnrType'] = self.arnrType
        return serialized
