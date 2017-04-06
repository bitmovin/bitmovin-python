from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import H264Profile, H264Level, MVPredictionMode
from bitmovin.utils import Serializable
from .video_codec_configuration import VideoCodecConfiguration


class H264CodecConfiguration(VideoCodecConfiguration, Serializable):

    def __init__(self, name, bitrate, profile, rate=None, id_=None, description=None, custom_data=None, width=None,
                 height=None, bframes=None, ref_frames=None, qp_min=None, qp_max=None, mv_prediction_mode=None,
                 mv_search_range_max=None, cabac=None, max_bitrate=None, min_bitrate=None, bufsize=None,
                 min_gop=None, max_gop=None, level=None):

        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description, bitrate=bitrate,
                         rate=rate, width=width, height=height)

        self._profile = None
        self.profile = profile
        self.bframes = bframes
        self.refFrames = ref_frames
        self.qpMin = qp_min
        self.qpMax = qp_max
        self._mvPredictionMode = None
        self.mvPredictionMode = mv_prediction_mode
        self.mvSearchRangeMax = mv_search_range_max
        self.cabac = cabac
        self.maxBitrate = max_bitrate
        self.minBitrate = min_bitrate
        self.bufsize = bufsize
        self.minGop = min_gop
        self.maxGop = max_gop
        self._level = None
        self.level = level

    @property
    def profile(self):
        return self._profile

    @profile.setter
    def profile(self, new_profile):
        if new_profile is None:
            return
        if isinstance(new_profile, str):
            self._profile = new_profile
        elif isinstance(new_profile, H264Profile):
            self._profile = new_profile.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for profile: must be either str or H264Profile!'.format(type(new_profile)))

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):
        if new_level is None:
            return
        if isinstance(new_level, str):
            self._level = new_level
        elif isinstance(new_level, H264Level):
            self._level = new_level.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for level: must be either str or H264Level!'.format(type(new_level)))

    @property
    def mvPredictionMode(self):
        if self._mvPredictionMode is not None:
            return self._mvPredictionMode
        else:
            return MVPredictionMode.default().value

    @mvPredictionMode.setter
    def mvPredictionMode(self, new_mode):
        if new_mode is None:
            return
        if isinstance(new_mode, str):
            self._mvPredictionMode = new_mode
        elif isinstance(new_mode, MVPredictionMode):
            self._mvPredictionMode = new_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for mvPredictionMode: must be either str or H264Level!'.format(type(new_mode)))

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

        profile = json_object.get('profile')
        bframes = json_object.get('bframes')
        ref_frames = json_object.get('refFrames')
        qp_min = json_object.get('qpMin')
        qp_max = json_object.get('qpMax')
        mv_prediction_mode = json_object.get('mvPredictionMode')
        mv_search_range_max = json_object.get('mvSearchRangeMax')
        cabac = json_object.get('cabac')
        max_bitrate = json_object.get('maxBitrate')
        min_bitrate = json_object.get('minBitrate')
        bufsize = json_object.get('bufsize')
        min_gop = json_object.get('minGop')
        max_gop = json_object.get('maxGop')
        level = json_object.get('level')

        h264_codec_configuration = H264CodecConfiguration(name=name, bitrate=bitrate, rate=rate, profile=profile,
                                                          id_=id_, description=description, custom_data=custom_data,
                                                          width=width, height=height, bframes=bframes,
                                                          ref_frames=ref_frames, qp_min=qp_min, qp_max=qp_max,
                                                          mv_prediction_mode=mv_prediction_mode,
                                                          mv_search_range_max=mv_search_range_max,
                                                          cabac=cabac, max_bitrate=max_bitrate, min_bitrate=min_bitrate,
                                                          bufsize=bufsize, min_gop=min_gop, max_gop=max_gop,
                                                          level=level)

        return h264_codec_configuration

    def serialize(self):
        serialized = super().serialize()
        serialized['profile'] = self.profile
        serialized['level'] = self.level
        serialized['mvPredictionMode'] = self.mvPredictionMode
        return serialized
