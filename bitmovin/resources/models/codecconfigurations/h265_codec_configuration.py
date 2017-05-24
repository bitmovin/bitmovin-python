from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import H265Profile, H265Level, BAdapt, MaxCTUSize, TUInterDepth, TUIntraDepth, \
    MotionSearch
from bitmovin.utils import Serializable
from .video_codec_configuration import VideoCodecConfiguration


class H265CodecConfiguration(VideoCodecConfiguration, Serializable):

    def __init__(self, name, rate, profile, bitrate=None, id_=None, description=None, custom_data=None, width=None,
                 height=None, bframes=None, ref_frames=None, qp=None, max_bitrate=None, min_bitrate=None, bufsize=None,
                 min_gop=None, max_gop=None, level=None, rc_lookahead=None, b_adapt=None, max_ctu_size=None,
                 tu_intra_depth=None, tu_inter_depth=None, motion_search=None, sub_me=None, motion_search_range=None,
                 weight_prediction_on_p_slice=None, weight_prediction_on_b_slice=None, sao=None, crf=None):

        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description, bitrate=bitrate,
                         rate=rate, width=width, height=height)

        self._profile = None
        self.profile = profile
        self.bframes = bframes
        self.refFrames = ref_frames
        self.qp = qp
        self.maxBitrate = max_bitrate
        self.minBitrate = min_bitrate
        self.bufsize = bufsize
        self.minGop = min_gop
        self.maxGop = max_gop
        self._level = None
        self.level = level
        self.rcLookahead = rc_lookahead
        self._bAdapt = None
        self.bAdapt = b_adapt
        self._maxCTUSize = None
        self.maxCTUSize = max_ctu_size
        self._tuIntraDepth = None
        self.tuIntraDepth = tu_intra_depth
        self._tuInterDepth = None
        self.tuInterDepth = tu_inter_depth
        self._motionSearch = None
        self.motionSearch = motion_search
        self.subMe = sub_me
        self.motionSearchRange = motion_search_range
        self.weightPredictionOnPSlice = weight_prediction_on_p_slice
        self.weightPredictionOnBSlice = weight_prediction_on_b_slice
        self.sao = sao
        self._crf = None
        self.crf = crf

    @property
    def profile(self):
        return self._profile

    @profile.setter
    def profile(self, new_profile):
        if new_profile is None:
            return
        if isinstance(new_profile, str):
            self._profile = new_profile
        elif isinstance(new_profile, H265Profile):
            self._profile = new_profile.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for profile: must be either str or H265Profile!'.format(type(new_profile)))

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):
        if new_level is None:
            return
        if isinstance(new_level, str):
            self._level = new_level
        elif isinstance(new_level, H265Level):
            self._level = new_level.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for level: must be either str or H265Level!'.format(type(new_level)))

    @property
    def bAdapt(self):
        if self._bAdapt is not None:
            return self._bAdapt
        else:
            return BAdapt.default().value

    @bAdapt.setter
    def bAdapt(self, new_badapt):
        if new_badapt is None:
            return
        if isinstance(new_badapt, str):
            self._bAdapt = new_badapt
        elif isinstance(new_badapt, BAdapt):
            self._bAdapt = new_badapt.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for bAdapt: must be either str or BAdapt!'.format(type(new_badapt)))

    @property
    def maxCTUSize(self):
        if self._maxCTUSize is not None:
            return self._maxCTUSize
        else:
            return MaxCTUSize.default().value

    @maxCTUSize.setter
    def maxCTUSize(self, new_max_ctu_size):
        if new_max_ctu_size is None:
            return
        if isinstance(new_max_ctu_size, str):
            self._maxCTUSize = new_max_ctu_size
        elif isinstance(new_max_ctu_size, MaxCTUSize):
            self._maxCTUSize = new_max_ctu_size.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for maxCTUSize: must be either str or MaxCTUSize!'.format(type(new_max_ctu_size)))

    @property
    def tuIntraDepth(self):
        if self._tuIntraDepth is not None:
            return self._tuIntraDepth
        else:
            return TUIntraDepth.default().value

    @tuIntraDepth.setter
    def tuIntraDepth(self, new_tu_intra_depth):
        if new_tu_intra_depth is None:
            return
        if isinstance(new_tu_intra_depth, str):
            self._tuIntraDepth = new_tu_intra_depth
        elif isinstance(new_tu_intra_depth, TUIntraDepth):
            self._tuIntraDepth = new_tu_intra_depth.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for tuIntraDepth: must be either str or TUIntraDepth!'.format(
                    type(new_tu_intra_depth)))
        
    @property
    def tuInterDepth(self):
        if self._tuInterDepth is not None:
            return self._tuInterDepth
        else:
            return TUInterDepth.default().value

    @tuInterDepth.setter
    def tuInterDepth(self, new_tu_inter_depth):
        if new_tu_inter_depth is None:
            return
        if isinstance(new_tu_inter_depth, str):
            self._tuInterDepth = new_tu_inter_depth
        elif isinstance(new_tu_inter_depth, TUInterDepth):
            self._tuInterDepth = new_tu_inter_depth.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for tuInterDepth: must be either str or TUInterDepth!'.format(
                    type(new_tu_inter_depth)))

    @property
    def motionSearch(self):
        if self._motionSearch is not None:
            return self._motionSearch
        else:
            return MotionSearch.default().value

    @motionSearch.setter
    def motionSearch(self, new_motion_search):
        if new_motion_search is None:
            return
        if isinstance(new_motion_search, str):
            self._motionSearch = new_motion_search
        elif isinstance(new_motion_search, MotionSearch):
            self._motionSearch = new_motion_search.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for motionSearch: must be either str or MotionSearch!'.format(type(new_motion_search)))

    @property
    def crf(self):
        return self._crf

    @crf.setter
    def crf(self, new_value):
        if new_value is None:
            return
        if not isinstance(new_value, float):
            raise InvalidTypeError('crf has to be a float value')
        else:
            self._crf = new_value

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
        qp = json_object.get('qp')
        max_bitrate = json_object.get('maxBitrate')
        min_bitrate = json_object.get('minBitrate')
        bufsize = json_object.get('bufsize')
        min_gop = json_object.get('minGop')
        max_gop = json_object.get('maxGop')
        level = json_object.get('level')
        rc_lookahead = json_object.get('rcLookahead')
        b_adapt = json_object.get('bAdapt')
        max_ctu_size = json_object.get('maxCTUSize')
        tu_intra_depth = json_object.get('tuIntraDepth')
        tu_inter_depth = json_object.get('tuInterDepth')
        motion_search = json_object.get('motionSearch')
        sub_me = json_object.get('subMe')
        motion_search_range = json_object.get('motionSearchRange')
        weight_prediction_on_p_slice = json_object.get('weightPredictionOnPSlice')
        weight_prediction_on_b_slice = json_object.get('weightPredictionOnBSlice')
        sao = json_object.get('sao')
        crf = json_object.get('crf')

        h265_codec_configuration = H265CodecConfiguration(name=name, bitrate=bitrate, rate=rate, profile=profile,
                                                          id_=id_, description=description, custom_data=custom_data,
                                                          width=width, height=height, bframes=bframes,
                                                          ref_frames=ref_frames, qp=qp, max_bitrate=max_bitrate,
                                                          min_bitrate=min_bitrate, bufsize=bufsize, min_gop=min_gop,
                                                          max_gop=max_gop, level=level, rc_lookahead=rc_lookahead,
                                                          b_adapt=b_adapt, max_ctu_size=max_ctu_size,
                                                          tu_intra_depth=tu_intra_depth, tu_inter_depth=tu_inter_depth,
                                                          motion_search=motion_search, sub_me=sub_me,
                                                          motion_search_range=motion_search_range,
                                                          weight_prediction_on_p_slice=weight_prediction_on_p_slice,
                                                          weight_prediction_on_b_slice=weight_prediction_on_b_slice,
                                                          sao=sao, crf=crf)

        return h265_codec_configuration

    def serialize(self):
        serialized = super().serialize()
        serialized['profile'] = self.profile
        serialized['level'] = self.level
        serialized['bAdapt'] = self.bAdapt
        serialized['maxCTUSize'] = self.maxCTUSize
        serialized['tuIntraDepth'] = self.tuIntraDepth
        serialized['tuInterDepth'] = self.tuInterDepth
        serialized['motionSearch'] = self.motionSearch
        return serialized
