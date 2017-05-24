from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import H264Profile, H264Level, MVPredictionMode
from bitmovin.resources.enums.h264_Preset import H264Preset
from bitmovin.resources.enums.h264_interlace_mode import H264InterlaceMode
from bitmovin.resources.enums.h264_motion_estimation_method import H264MotionEstimationMethod
from bitmovin.resources.enums.h264_partition import H264Partition
from bitmovin.resources.enums.h264_sub_me import H264SubMe
from bitmovin.resources.enums.badapt import BAdapt
from bitmovin.resources.enums.h264_trellis import H264Trellis

from bitmovin.utils import Serializable
from .video_codec_configuration import VideoCodecConfiguration


class H264CodecConfiguration(VideoCodecConfiguration, Serializable):

    def __init__(self, name, rate, profile, bitrate=None, id_=None, description=None, custom_data=None, width=None,
                 height=None, bframes=None, ref_frames=None, qp_min=None, qp_max=None, mv_prediction_mode=None,
                 mv_search_range_max=None, cabac=None, max_bitrate=None, min_bitrate=None, bufsize=None,
                 min_gop=None, max_gop=None, level=None, rc_lookahead=None, b_adapt=None, sub_me=None, motion_estimation_method=None,
                 partitions=None, trellis=None, slices=None, interlaceMode=None, crf=None):

        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description, bitrate=bitrate,
                         rate=rate, width=width, height=height)

        self._b_adapt = None
        self._level = None
        self._mvPredictionMode = None
        self._motion_estimation_method = None
        self._partitions = None
        self._profile = None
        self._sub_me = None
        self._trellis = None
        self._interlaceMode = None
        self._crf = None

        self.b_adapt = b_adapt
        self.bframes = bframes
        self.bufsize = bufsize
        self.cabac = cabac
        self.level = level
        self.interlaceMode = interlaceMode
        self.maxBitrate = max_bitrate
        self.maxGop = max_gop
        self.minBitrate = min_bitrate
        self.minGop = min_gop
        self.mvPredictionMode = mv_prediction_mode
        self.mvSearchRangeMax = mv_search_range_max
        self.motion_estimation_method = motion_estimation_method
        self.partitions = partitions
        self.profile = profile
        self.qpMin = qp_min
        self.qpMax = qp_max
        self.rc_lookahead = rc_lookahead
        self.refFrames = ref_frames
        self.slices = slices
        self.sub_me = sub_me
        self.trellis = trellis
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

    @property
    def b_adapt(self):
        return self._b_adapt

    @b_adapt.setter
    def b_adapt(self, new_value):
        if new_value is None:
            return
        if isinstance(new_value, str):
            self._b_adapt = new_value
        elif isinstance(new_value, BAdapt):
            self._b_adapt = new_value.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for b_adapt: must be either str or BAdapt!'.format(type(new_value)))

    @property
    def sub_me(self):
        return self._sub_me

    @sub_me.setter
    def sub_me(self, new_value):
        if new_value is None:
            return
        if isinstance(new_value, str):
            self._sub_me = new_value
        elif isinstance(new_value, H264SubMe):
            self._sub_me = new_value.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for sub_me: must be either str or H264SubMe!'.format(type(new_value)))

    @property
    def motion_estimation_method(self):
        return self._motion_estimation_method

    @motion_estimation_method.setter
    def motion_estimation_method(self, new_value):
        if new_value is None:
            return
        if isinstance(new_value, str):
            self._motion_estimation_method = new_value
        elif isinstance(new_value, H264MotionEstimationMethod):
            self._motion_estimation_method = new_value.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for motion_estimation_method: must be either str or H264MotionEstimationMethod!'.format(type(new_value)))

    @property
    def interlaceMode(self):
        return self._interlaceMode

    @interlaceMode.setter
    def interlaceMode(self, new_value):
        if new_value is None:
            return
        if isinstance(new_value, str):
            self._interlaceMode = new_value
        elif isinstance(new_value, H264InterlaceMode):
            self._interlaceMode = new_value.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for interlaceMode: must be either str or H264MInterlaceMode!'.format(type(new_value)))

    @property
    def trellis(self):
        return self._trellis

    @trellis.setter
    def trellis(self, new_value):
        if new_value is None:
            return
        if isinstance(new_value, str):
            self._trellis = new_value
        elif isinstance(new_value, H264Trellis):
            self._trellis = new_value.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for trellis: must be either str or H264Trellis!'.format(type(new_value)))

    @property
    def partitions(self):
        return self._partitions

    @partitions.setter
    def partitions(self, new_value):
        if new_value is None:
            return

        if not isinstance(new_value, list):
            raise InvalidTypeError('partitions has to be a list of Partition enums')

        if all(isinstance(output, H264Partition) for output in new_value):
            partitions = []
            for part in new_value:
                partitions.append(part.value)
            self._partitions = partitions
        else:
            self._partitions = new_value

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
        rc_lookahead = json_object.get('rcLookahead')
        sub_me = json_object.get('subMe')
        motion_estimation_method = json_object.get('motionEstimationMethod')
        b_adapt = json_object.get('bAdaptiveStrategy')
        partitions = json_object.get('partitions')
        trellis = json_object.get('trellis')
        slices = json_object.get('slices')
        interlaceMode = json_object.get('interlaceMode')
        crf = json_object.get('crf')

        h264_codec_configuration = H264CodecConfiguration(name=name, bitrate=bitrate, rate=rate, profile=profile,
                                                          id_=id_, description=description, custom_data=custom_data,
                                                          width=width, height=height, bframes=bframes,
                                                          ref_frames=ref_frames, qp_min=qp_min, qp_max=qp_max,
                                                          mv_prediction_mode=mv_prediction_mode,
                                                          mv_search_range_max=mv_search_range_max,
                                                          cabac=cabac, max_bitrate=max_bitrate, min_bitrate=min_bitrate,
                                                          bufsize=bufsize, min_gop=min_gop, max_gop=max_gop,
                                                          level=level, rc_lookahead=rc_lookahead, sub_me=sub_me,
                                                          motion_estimation_method=motion_estimation_method, b_adapt=b_adapt,
                                                          partitions=partitions, trellis=trellis, slices=slices,
                                                          interlaceMode=interlaceMode, crf=crf)

        return h264_codec_configuration

    def serialize(self):
        serialized = super().serialize()
        serialized['bAdaptiveStrategy'] = self.b_adapt
        serialized['interlaceMode'] = self.interlaceMode
        serialized['level'] = self.level
        serialized['mvPredictionMode'] = self.mvPredictionMode
        serialized['motionEstimationMethod'] = self.motion_estimation_method
        serialized['partitions'] = self.partitions
        serialized['profile'] = self.profile
        serialized['rcLookahead'] = self.rc_lookahead
        serialized['subMe'] = self.sub_me
        serialized['trellis'] = self.trellis
        serialized['crf'] = self.crf
        return serialized


