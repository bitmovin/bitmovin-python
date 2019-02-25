# coding: utf-8

from bitmovin_python.models.adaptive_quant_mode import AdaptiveQuantMode
from bitmovin_python.models.b_adapt import BAdapt
from bitmovin_python.models.codec_config_type import CodecConfigType
from bitmovin_python.models.color_config import ColorConfig
from bitmovin_python.models.encoding_mode import EncodingMode
from bitmovin_python.models.force_flush_mode import ForceFlushMode
from bitmovin_python.models.level_h265 import LevelH265
from bitmovin_python.models.limit_references import LimitReferences
from bitmovin_python.models.limit_transfer_unit_depth_recursion_mode import LimitTransferUnitDepthRecursionMode
from bitmovin_python.models.max_ctu_size import MaxCtuSize
from bitmovin_python.models.max_transfer_unit_size import MaxTransferUnitSize
from bitmovin_python.models.min_coding_unit_size import MinCodingUnitSize
from bitmovin_python.models.motion_search import MotionSearch
from bitmovin_python.models.pixel_format import PixelFormat
from bitmovin_python.models.profile_h265 import ProfileH265
from bitmovin_python.models.quantization_group_size import QuantizationGroupSize
from bitmovin_python.models.rate_distortion_level_for_quantization import RateDistortionLevelForQuantization
from bitmovin_python.models.rate_distortion_penalty_mode import RateDistortionPenaltyMode
from bitmovin_python.models.transform_skip_mode import TransformSkipMode
from bitmovin_python.models.tu_inter_depth import TuInterDepth
from bitmovin_python.models.tu_intra_depth import TuIntraDepth
from bitmovin_python.models.video_configuration import VideoConfiguration
from bitmovin_python.models.video_format import VideoFormat
import pprint
import six
from datetime import datetime
from enum import Enum


class H265VideoConfiguration(VideoConfiguration):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(H265VideoConfiguration, self).openapi_types
        types.update({
            'crf': 'float',
            'profile': 'ProfileH265',
            'bframes': 'int',
            'ref_frames': 'int',
            'qp': 'int',
            'max_bitrate': 'int',
            'min_bitrate': 'int',
            'bufsize': 'int',
            'min_gop': 'int',
            'max_gop': 'int',
            'open_gop': 'bool',
            'min_keyframe_interval': 'float',
            'max_keyframe_interval': 'float',
            'level': 'LevelH265',
            'rc_lookahead': 'int',
            'b_adapt': 'BAdapt',
            'max_ctu_size': 'MaxCtuSize',
            'tu_intra_depth': 'TuIntraDepth',
            'tu_inter_depth': 'TuInterDepth',
            'motion_search': 'MotionSearch',
            'sub_me': 'int',
            'motion_search_range': 'int',
            'weight_prediction_on_p_slice': 'bool',
            'weight_prediction_on_b_slice': 'bool',
            'sao': 'bool',
            'master_display': 'str',
            'max_content_light_level': 'str',
            'max_average_light_level': 'int',
            'hdr': 'bool',
            'scene_cut_threshold': 'int',
            'adaptive_quantization_mode': 'AdaptiveQuantMode',
            'enable_hlg_signaling': 'bool',
            'video_format': 'VideoFormat',
            'psy_rate_distortion_optimization': 'float',
            'psy_rate_distortion_optimized_quantization': 'float',
            'enable_hrd_signaling': 'bool',
            'cutree': 'bool',
            'min_coding_unit_size': 'MinCodingUnitSize',
            'lookahead_slices': 'int',
            'limit_references': 'LimitReferences',
            'rectangular_motion_partitions_analysis': 'bool',
            'asymetric_motion_partitions_analysis': 'bool',
            'limit_modes': 'bool',
            'max_merge': 'int',
            'early_skip': 'bool',
            'recursion_skip': 'bool',
            'fast_search_for_angular_intra_predictions': 'bool',
            'evaluation_of_intra_modes_in_b_slices': 'bool',
            'sign_hide': 'bool',
            'rate_distortion_level_for_mode_decision': 'int',
            'rate_distortion_level_for_quantization': 'RateDistortionLevelForQuantization',
            'qp_min': 'int',
            'qp_max': 'int',
            'wavefront_parallel_processing': 'bool',
            'parallel_mode_decision': 'bool',
            'parallel_motion_estimation': 'bool',
            'slices': 'int',
            'copy_picture': 'bool',
            'level_high_tier': 'bool',
            'skip_split_rate_distortion_analysis': 'bool',
            'coding_unit_lossless': 'bool',
            'transform_skip': 'TransformSkipMode',
            'refine_rate_distortion_cost': 'bool',
            'limit_transfer_unit_depth_recursion': 'LimitTransferUnitDepthRecursionMode',
            'noise_reduction_intra': 'int',
            'noise_reduction_inter': 'int',
            'rate_distortion_penalty': 'RateDistortionPenaltyMode',
            'maximum_transfer_unit_size': 'MaxTransferUnitSize',
            'dynamic_rate_distortion_strength': 'int',
            'ssim_rate_distortion_optimization': 'bool',
            'temporal_motion_vector_predictors': 'bool',
            'analyze_source_frame_pixels': 'bool',
            'strong_intra_smoothing': 'bool',
            'constrained_intra_prediction': 'bool',
            'scenecut_bias': 'float',
            'allowed_radl_before_idr': 'int',
            'gop_lookahead': 'int',
            'bframe_bias': 'int',
            'force_flush': 'ForceFlushMode',
            'adaptive_quantization_strength': 'float',
            'adaptive_quantization_motion': 'bool',
            'quantization_group_size': 'QuantizationGroupSize',
            'strict_cbr': 'bool',
            'qp_offset_chroma_cb': 'int',
            'qp_offset_chroma_cr': 'int',
            'ip_ratio': 'float',
            'pb_ratio': 'float',
            'quantizer_curve_compression_factor': 'float',
            'qp_step': 'int',
            'grain_optimized_rate_control': 'bool',
            'blur_quants': 'float',
            'blur_complexity': 'float',
            'sao_non_deblock': 'bool',
            'limit_sao': 'bool',
            'lowpass_dct': 'bool'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(H265VideoConfiguration, self).attribute_map
        attributes.update({
            'crf': 'crf',
            'profile': 'profile',
            'bframes': 'bframes',
            'ref_frames': 'refFrames',
            'qp': 'qp',
            'max_bitrate': 'maxBitrate',
            'min_bitrate': 'minBitrate',
            'bufsize': 'bufsize',
            'min_gop': 'minGop',
            'max_gop': 'maxGop',
            'open_gop': 'openGop',
            'min_keyframe_interval': 'minKeyframeInterval',
            'max_keyframe_interval': 'maxKeyframeInterval',
            'level': 'level',
            'rc_lookahead': 'rcLookahead',
            'b_adapt': 'bAdapt',
            'max_ctu_size': 'maxCTUSize',
            'tu_intra_depth': 'tuIntraDepth',
            'tu_inter_depth': 'tuInterDepth',
            'motion_search': 'motionSearch',
            'sub_me': 'subMe',
            'motion_search_range': 'motionSearchRange',
            'weight_prediction_on_p_slice': 'weightPredictionOnPSlice',
            'weight_prediction_on_b_slice': 'weightPredictionOnBSlice',
            'sao': 'sao',
            'master_display': 'masterDisplay',
            'max_content_light_level': 'maxContentLightLevel',
            'max_average_light_level': 'maxAverageLightLevel',
            'hdr': 'hdr',
            'scene_cut_threshold': 'sceneCutThreshold',
            'adaptive_quantization_mode': 'adaptiveQuantizationMode',
            'enable_hlg_signaling': 'enableHlgSignaling',
            'video_format': 'videoFormat',
            'psy_rate_distortion_optimization': 'psyRateDistortionOptimization',
            'psy_rate_distortion_optimized_quantization': 'psyRateDistortionOptimizedQuantization',
            'enable_hrd_signaling': 'enableHrdSignaling',
            'cutree': 'cutree',
            'min_coding_unit_size': 'minCodingUnitSize',
            'lookahead_slices': 'lookaheadSlices',
            'limit_references': 'limitReferences',
            'rectangular_motion_partitions_analysis': 'rectangularMotionPartitionsAnalysis',
            'asymetric_motion_partitions_analysis': 'asymetricMotionPartitionsAnalysis',
            'limit_modes': 'limitModes',
            'max_merge': 'maxMerge',
            'early_skip': 'earlySkip',
            'recursion_skip': 'recursionSkip',
            'fast_search_for_angular_intra_predictions': 'fastSearchForAngularIntraPredictions',
            'evaluation_of_intra_modes_in_b_slices': 'evaluationOfIntraModesInBSlices',
            'sign_hide': 'signHide',
            'rate_distortion_level_for_mode_decision': 'rateDistortionLevelForModeDecision',
            'rate_distortion_level_for_quantization': 'rateDistortionLevelForQuantization',
            'qp_min': 'qpMin',
            'qp_max': 'qpMax',
            'wavefront_parallel_processing': 'wavefrontParallelProcessing',
            'parallel_mode_decision': 'parallelModeDecision',
            'parallel_motion_estimation': 'parallelMotionEstimation',
            'slices': 'slices',
            'copy_picture': 'copyPicture',
            'level_high_tier': 'levelHighTier',
            'skip_split_rate_distortion_analysis': 'skipSplitRateDistortionAnalysis',
            'coding_unit_lossless': 'codingUnitLossless',
            'transform_skip': 'transformSkip',
            'refine_rate_distortion_cost': 'refineRateDistortionCost',
            'limit_transfer_unit_depth_recursion': 'limitTransferUnitDepthRecursion',
            'noise_reduction_intra': 'noiseReductionIntra',
            'noise_reduction_inter': 'noiseReductionInter',
            'rate_distortion_penalty': 'rateDistortionPenalty',
            'maximum_transfer_unit_size': 'maximumTransferUnitSize',
            'dynamic_rate_distortion_strength': 'dynamicRateDistortionStrength',
            'ssim_rate_distortion_optimization': 'ssimRateDistortionOptimization',
            'temporal_motion_vector_predictors': 'temporalMotionVectorPredictors',
            'analyze_source_frame_pixels': 'analyzeSourceFramePixels',
            'strong_intra_smoothing': 'strongIntraSmoothing',
            'constrained_intra_prediction': 'constrainedIntraPrediction',
            'scenecut_bias': 'scenecutBias',
            'allowed_radl_before_idr': 'allowedRADLBeforeIDR',
            'gop_lookahead': 'gopLookahead',
            'bframe_bias': 'bframeBias',
            'force_flush': 'forceFlush',
            'adaptive_quantization_strength': 'adaptiveQuantizationStrength',
            'adaptive_quantization_motion': 'adaptiveQuantizationMotion',
            'quantization_group_size': 'quantizationGroupSize',
            'strict_cbr': 'strictCbr',
            'qp_offset_chroma_cb': 'qpOffsetChromaCb',
            'qp_offset_chroma_cr': 'qpOffsetChromaCr',
            'ip_ratio': 'ipRatio',
            'pb_ratio': 'pbRatio',
            'quantizer_curve_compression_factor': 'quantizerCurveCompressionFactor',
            'qp_step': 'qpStep',
            'grain_optimized_rate_control': 'grainOptimizedRateControl',
            'blur_quants': 'blurQuants',
            'blur_complexity': 'blurComplexity',
            'sao_non_deblock': 'saoNonDeblock',
            'limit_sao': 'limitSao',
            'lowpass_dct': 'lowpassDct'
        })
        return attributes

    def __init__(self, crf=None, profile=None, bframes=None, ref_frames=None, qp=None, max_bitrate=None, min_bitrate=None, bufsize=None, min_gop=None, max_gop=None, open_gop=None, min_keyframe_interval=None, max_keyframe_interval=None, level=None, rc_lookahead=None, b_adapt=None, max_ctu_size=None, tu_intra_depth=None, tu_inter_depth=None, motion_search=None, sub_me=None, motion_search_range=None, weight_prediction_on_p_slice=None, weight_prediction_on_b_slice=None, sao=None, master_display=None, max_content_light_level=None, max_average_light_level=None, hdr=None, scene_cut_threshold=None, adaptive_quantization_mode=None, enable_hlg_signaling=None, video_format=None, psy_rate_distortion_optimization=None, psy_rate_distortion_optimized_quantization=None, enable_hrd_signaling=None, cutree=None, min_coding_unit_size=None, lookahead_slices=None, limit_references=None, rectangular_motion_partitions_analysis=None, asymetric_motion_partitions_analysis=None, limit_modes=None, max_merge=None, early_skip=None, recursion_skip=None, fast_search_for_angular_intra_predictions=None, evaluation_of_intra_modes_in_b_slices=None, sign_hide=None, rate_distortion_level_for_mode_decision=None, rate_distortion_level_for_quantization=None, qp_min=None, qp_max=None, wavefront_parallel_processing=None, parallel_mode_decision=None, parallel_motion_estimation=None, slices=None, copy_picture=None, level_high_tier=None, skip_split_rate_distortion_analysis=None, coding_unit_lossless=None, transform_skip=None, refine_rate_distortion_cost=None, limit_transfer_unit_depth_recursion=None, noise_reduction_intra=None, noise_reduction_inter=None, rate_distortion_penalty=None, maximum_transfer_unit_size=None, dynamic_rate_distortion_strength=None, ssim_rate_distortion_optimization=None, temporal_motion_vector_predictors=None, analyze_source_frame_pixels=None, strong_intra_smoothing=None, constrained_intra_prediction=None, scenecut_bias=None, allowed_radl_before_idr=None, gop_lookahead=None, bframe_bias=None, force_flush=None, adaptive_quantization_strength=None, adaptive_quantization_motion=None, quantization_group_size=None, strict_cbr=None, qp_offset_chroma_cb=None, qp_offset_chroma_cr=None, ip_ratio=None, pb_ratio=None, quantizer_curve_compression_factor=None, qp_step=None, grain_optimized_rate_control=None, blur_quants=None, blur_complexity=None, sao_non_deblock=None, limit_sao=None, lowpass_dct=None, *args, **kwargs):
        super(H265VideoConfiguration, self).__init__(*args, **kwargs)

        self._crf = None
        self._profile = None
        self._bframes = None
        self._ref_frames = None
        self._qp = None
        self._max_bitrate = None
        self._min_bitrate = None
        self._bufsize = None
        self._min_gop = None
        self._max_gop = None
        self._open_gop = None
        self._min_keyframe_interval = None
        self._max_keyframe_interval = None
        self._level = None
        self._rc_lookahead = None
        self._b_adapt = None
        self._max_ctu_size = None
        self._tu_intra_depth = None
        self._tu_inter_depth = None
        self._motion_search = None
        self._sub_me = None
        self._motion_search_range = None
        self._weight_prediction_on_p_slice = None
        self._weight_prediction_on_b_slice = None
        self._sao = None
        self._master_display = None
        self._max_content_light_level = None
        self._max_average_light_level = None
        self._hdr = None
        self._scene_cut_threshold = None
        self._adaptive_quantization_mode = None
        self._enable_hlg_signaling = None
        self._video_format = None
        self._psy_rate_distortion_optimization = None
        self._psy_rate_distortion_optimized_quantization = None
        self._enable_hrd_signaling = None
        self._cutree = None
        self._min_coding_unit_size = None
        self._lookahead_slices = None
        self._limit_references = None
        self._rectangular_motion_partitions_analysis = None
        self._asymetric_motion_partitions_analysis = None
        self._limit_modes = None
        self._max_merge = None
        self._early_skip = None
        self._recursion_skip = None
        self._fast_search_for_angular_intra_predictions = None
        self._evaluation_of_intra_modes_in_b_slices = None
        self._sign_hide = None
        self._rate_distortion_level_for_mode_decision = None
        self._rate_distortion_level_for_quantization = None
        self._qp_min = None
        self._qp_max = None
        self._wavefront_parallel_processing = None
        self._parallel_mode_decision = None
        self._parallel_motion_estimation = None
        self._slices = None
        self._copy_picture = None
        self._level_high_tier = None
        self._skip_split_rate_distortion_analysis = None
        self._coding_unit_lossless = None
        self._transform_skip = None
        self._refine_rate_distortion_cost = None
        self._limit_transfer_unit_depth_recursion = None
        self._noise_reduction_intra = None
        self._noise_reduction_inter = None
        self._rate_distortion_penalty = None
        self._maximum_transfer_unit_size = None
        self._dynamic_rate_distortion_strength = None
        self._ssim_rate_distortion_optimization = None
        self._temporal_motion_vector_predictors = None
        self._analyze_source_frame_pixels = None
        self._strong_intra_smoothing = None
        self._constrained_intra_prediction = None
        self._scenecut_bias = None
        self._allowed_radl_before_idr = None
        self._gop_lookahead = None
        self._bframe_bias = None
        self._force_flush = None
        self._adaptive_quantization_strength = None
        self._adaptive_quantization_motion = None
        self._quantization_group_size = None
        self._strict_cbr = None
        self._qp_offset_chroma_cb = None
        self._qp_offset_chroma_cr = None
        self._ip_ratio = None
        self._pb_ratio = None
        self._quantizer_curve_compression_factor = None
        self._qp_step = None
        self._grain_optimized_rate_control = None
        self._blur_quants = None
        self._blur_complexity = None
        self._sao_non_deblock = None
        self._limit_sao = None
        self._lowpass_dct = None
        self.discriminator = None

        if crf is not None:
            self.crf = crf
        self.profile = profile
        if bframes is not None:
            self.bframes = bframes
        if ref_frames is not None:
            self.ref_frames = ref_frames
        if qp is not None:
            self.qp = qp
        if max_bitrate is not None:
            self.max_bitrate = max_bitrate
        if min_bitrate is not None:
            self.min_bitrate = min_bitrate
        if bufsize is not None:
            self.bufsize = bufsize
        if min_gop is not None:
            self.min_gop = min_gop
        if max_gop is not None:
            self.max_gop = max_gop
        if open_gop is not None:
            self.open_gop = open_gop
        if min_keyframe_interval is not None:
            self.min_keyframe_interval = min_keyframe_interval
        if max_keyframe_interval is not None:
            self.max_keyframe_interval = max_keyframe_interval
        if level is not None:
            self.level = level
        if rc_lookahead is not None:
            self.rc_lookahead = rc_lookahead
        if b_adapt is not None:
            self.b_adapt = b_adapt
        if max_ctu_size is not None:
            self.max_ctu_size = max_ctu_size
        if tu_intra_depth is not None:
            self.tu_intra_depth = tu_intra_depth
        if tu_inter_depth is not None:
            self.tu_inter_depth = tu_inter_depth
        if motion_search is not None:
            self.motion_search = motion_search
        if sub_me is not None:
            self.sub_me = sub_me
        if motion_search_range is not None:
            self.motion_search_range = motion_search_range
        if weight_prediction_on_p_slice is not None:
            self.weight_prediction_on_p_slice = weight_prediction_on_p_slice
        if weight_prediction_on_b_slice is not None:
            self.weight_prediction_on_b_slice = weight_prediction_on_b_slice
        if sao is not None:
            self.sao = sao
        if master_display is not None:
            self.master_display = master_display
        if max_content_light_level is not None:
            self.max_content_light_level = max_content_light_level
        if max_average_light_level is not None:
            self.max_average_light_level = max_average_light_level
        if hdr is not None:
            self.hdr = hdr
        if scene_cut_threshold is not None:
            self.scene_cut_threshold = scene_cut_threshold
        if adaptive_quantization_mode is not None:
            self.adaptive_quantization_mode = adaptive_quantization_mode
        if enable_hlg_signaling is not None:
            self.enable_hlg_signaling = enable_hlg_signaling
        if video_format is not None:
            self.video_format = video_format
        if psy_rate_distortion_optimization is not None:
            self.psy_rate_distortion_optimization = psy_rate_distortion_optimization
        if psy_rate_distortion_optimized_quantization is not None:
            self.psy_rate_distortion_optimized_quantization = psy_rate_distortion_optimized_quantization
        if enable_hrd_signaling is not None:
            self.enable_hrd_signaling = enable_hrd_signaling
        if cutree is not None:
            self.cutree = cutree
        if min_coding_unit_size is not None:
            self.min_coding_unit_size = min_coding_unit_size
        if lookahead_slices is not None:
            self.lookahead_slices = lookahead_slices
        if limit_references is not None:
            self.limit_references = limit_references
        if rectangular_motion_partitions_analysis is not None:
            self.rectangular_motion_partitions_analysis = rectangular_motion_partitions_analysis
        if asymetric_motion_partitions_analysis is not None:
            self.asymetric_motion_partitions_analysis = asymetric_motion_partitions_analysis
        if limit_modes is not None:
            self.limit_modes = limit_modes
        if max_merge is not None:
            self.max_merge = max_merge
        if early_skip is not None:
            self.early_skip = early_skip
        if recursion_skip is not None:
            self.recursion_skip = recursion_skip
        if fast_search_for_angular_intra_predictions is not None:
            self.fast_search_for_angular_intra_predictions = fast_search_for_angular_intra_predictions
        if evaluation_of_intra_modes_in_b_slices is not None:
            self.evaluation_of_intra_modes_in_b_slices = evaluation_of_intra_modes_in_b_slices
        if sign_hide is not None:
            self.sign_hide = sign_hide
        if rate_distortion_level_for_mode_decision is not None:
            self.rate_distortion_level_for_mode_decision = rate_distortion_level_for_mode_decision
        if rate_distortion_level_for_quantization is not None:
            self.rate_distortion_level_for_quantization = rate_distortion_level_for_quantization
        if qp_min is not None:
            self.qp_min = qp_min
        if qp_max is not None:
            self.qp_max = qp_max
        if wavefront_parallel_processing is not None:
            self.wavefront_parallel_processing = wavefront_parallel_processing
        if parallel_mode_decision is not None:
            self.parallel_mode_decision = parallel_mode_decision
        if parallel_motion_estimation is not None:
            self.parallel_motion_estimation = parallel_motion_estimation
        if slices is not None:
            self.slices = slices
        if copy_picture is not None:
            self.copy_picture = copy_picture
        if level_high_tier is not None:
            self.level_high_tier = level_high_tier
        if skip_split_rate_distortion_analysis is not None:
            self.skip_split_rate_distortion_analysis = skip_split_rate_distortion_analysis
        if coding_unit_lossless is not None:
            self.coding_unit_lossless = coding_unit_lossless
        if transform_skip is not None:
            self.transform_skip = transform_skip
        if refine_rate_distortion_cost is not None:
            self.refine_rate_distortion_cost = refine_rate_distortion_cost
        if limit_transfer_unit_depth_recursion is not None:
            self.limit_transfer_unit_depth_recursion = limit_transfer_unit_depth_recursion
        if noise_reduction_intra is not None:
            self.noise_reduction_intra = noise_reduction_intra
        if noise_reduction_inter is not None:
            self.noise_reduction_inter = noise_reduction_inter
        if rate_distortion_penalty is not None:
            self.rate_distortion_penalty = rate_distortion_penalty
        if maximum_transfer_unit_size is not None:
            self.maximum_transfer_unit_size = maximum_transfer_unit_size
        if dynamic_rate_distortion_strength is not None:
            self.dynamic_rate_distortion_strength = dynamic_rate_distortion_strength
        if ssim_rate_distortion_optimization is not None:
            self.ssim_rate_distortion_optimization = ssim_rate_distortion_optimization
        if temporal_motion_vector_predictors is not None:
            self.temporal_motion_vector_predictors = temporal_motion_vector_predictors
        if analyze_source_frame_pixels is not None:
            self.analyze_source_frame_pixels = analyze_source_frame_pixels
        if strong_intra_smoothing is not None:
            self.strong_intra_smoothing = strong_intra_smoothing
        if constrained_intra_prediction is not None:
            self.constrained_intra_prediction = constrained_intra_prediction
        if scenecut_bias is not None:
            self.scenecut_bias = scenecut_bias
        if allowed_radl_before_idr is not None:
            self.allowed_radl_before_idr = allowed_radl_before_idr
        if gop_lookahead is not None:
            self.gop_lookahead = gop_lookahead
        if bframe_bias is not None:
            self.bframe_bias = bframe_bias
        if force_flush is not None:
            self.force_flush = force_flush
        if adaptive_quantization_strength is not None:
            self.adaptive_quantization_strength = adaptive_quantization_strength
        if adaptive_quantization_motion is not None:
            self.adaptive_quantization_motion = adaptive_quantization_motion
        if quantization_group_size is not None:
            self.quantization_group_size = quantization_group_size
        if strict_cbr is not None:
            self.strict_cbr = strict_cbr
        if qp_offset_chroma_cb is not None:
            self.qp_offset_chroma_cb = qp_offset_chroma_cb
        if qp_offset_chroma_cr is not None:
            self.qp_offset_chroma_cr = qp_offset_chroma_cr
        if ip_ratio is not None:
            self.ip_ratio = ip_ratio
        if pb_ratio is not None:
            self.pb_ratio = pb_ratio
        if quantizer_curve_compression_factor is not None:
            self.quantizer_curve_compression_factor = quantizer_curve_compression_factor
        if qp_step is not None:
            self.qp_step = qp_step
        if grain_optimized_rate_control is not None:
            self.grain_optimized_rate_control = grain_optimized_rate_control
        if blur_quants is not None:
            self.blur_quants = blur_quants
        if blur_complexity is not None:
            self.blur_complexity = blur_complexity
        if sao_non_deblock is not None:
            self.sao_non_deblock = sao_non_deblock
        if limit_sao is not None:
            self.limit_sao = limit_sao
        if lowpass_dct is not None:
            self.lowpass_dct = lowpass_dct

    @property
    def crf(self):
        """Gets the crf of this H265VideoConfiguration.

        Sets the constant rate factor for quality-based variable bitrate. Either bitrate or crf is required.

        :return: The crf of this H265VideoConfiguration.
        :rtype: float
        """
        return self._crf

    @crf.setter
    def crf(self, crf):
        """Sets the crf of this H265VideoConfiguration.

        Sets the constant rate factor for quality-based variable bitrate. Either bitrate or crf is required.

        :param crf: The crf of this H265VideoConfiguration.
        :type: float
        """

        if crf is not None:
            if crf is not None and crf > 51:
                raise ValueError("Invalid value for `crf`, must be a value less than or equal to `51`")
            if crf is not None and crf < 0:
                raise ValueError("Invalid value for `crf`, must be a value greater than or equal to `0`")
            if not isinstance(crf, float):
                raise TypeError("Invalid type for `crf`, type has to be `float`")

            self._crf = crf


    @property
    def profile(self):
        """Gets the profile of this H265VideoConfiguration.


        :return: The profile of this H265VideoConfiguration.
        :rtype: ProfileH265
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this H265VideoConfiguration.


        :param profile: The profile of this H265VideoConfiguration.
        :type: ProfileH265
        """

        if profile is not None:
            if not isinstance(profile, ProfileH265):
                raise TypeError("Invalid type for `profile`, type has to be `ProfileH265`")

            self._profile = profile


    @property
    def bframes(self):
        """Gets the bframes of this H265VideoConfiguration.

        Sets the amount of b frames

        :return: The bframes of this H265VideoConfiguration.
        :rtype: int
        """
        return self._bframes

    @bframes.setter
    def bframes(self, bframes):
        """Sets the bframes of this H265VideoConfiguration.

        Sets the amount of b frames

        :param bframes: The bframes of this H265VideoConfiguration.
        :type: int
        """

        if bframes is not None:
            if bframes is not None and bframes > 16:
                raise ValueError("Invalid value for `bframes`, must be a value less than or equal to `16`")
            if bframes is not None and bframes < 0:
                raise ValueError("Invalid value for `bframes`, must be a value greater than or equal to `0`")
            if not isinstance(bframes, int):
                raise TypeError("Invalid type for `bframes`, type has to be `int`")

            self._bframes = bframes


    @property
    def ref_frames(self):
        """Gets the ref_frames of this H265VideoConfiguration.

        Sets the amount of reference frames

        :return: The ref_frames of this H265VideoConfiguration.
        :rtype: int
        """
        return self._ref_frames

    @ref_frames.setter
    def ref_frames(self, ref_frames):
        """Sets the ref_frames of this H265VideoConfiguration.

        Sets the amount of reference frames

        :param ref_frames: The ref_frames of this H265VideoConfiguration.
        :type: int
        """

        if ref_frames is not None:
            if ref_frames is not None and ref_frames > 16:
                raise ValueError("Invalid value for `ref_frames`, must be a value less than or equal to `16`")
            if ref_frames is not None and ref_frames < 0:
                raise ValueError("Invalid value for `ref_frames`, must be a value greater than or equal to `0`")
            if not isinstance(ref_frames, int):
                raise TypeError("Invalid type for `ref_frames`, type has to be `int`")

            self._ref_frames = ref_frames


    @property
    def qp(self):
        """Gets the qp of this H265VideoConfiguration.

        Sets the quantization factor

        :return: The qp of this H265VideoConfiguration.
        :rtype: int
        """
        return self._qp

    @qp.setter
    def qp(self, qp):
        """Sets the qp of this H265VideoConfiguration.

        Sets the quantization factor

        :param qp: The qp of this H265VideoConfiguration.
        :type: int
        """

        if qp is not None:
            if qp is not None and qp > 51:
                raise ValueError("Invalid value for `qp`, must be a value less than or equal to `51`")
            if qp is not None and qp < 0:
                raise ValueError("Invalid value for `qp`, must be a value greater than or equal to `0`")
            if not isinstance(qp, int):
                raise TypeError("Invalid type for `qp`, type has to be `int`")

            self._qp = qp


    @property
    def max_bitrate(self):
        """Gets the max_bitrate of this H265VideoConfiguration.

        Maximum Bitrate

        :return: The max_bitrate of this H265VideoConfiguration.
        :rtype: int
        """
        return self._max_bitrate

    @max_bitrate.setter
    def max_bitrate(self, max_bitrate):
        """Sets the max_bitrate of this H265VideoConfiguration.

        Maximum Bitrate

        :param max_bitrate: The max_bitrate of this H265VideoConfiguration.
        :type: int
        """

        if max_bitrate is not None:
            if not isinstance(max_bitrate, int):
                raise TypeError("Invalid type for `max_bitrate`, type has to be `int`")

            self._max_bitrate = max_bitrate


    @property
    def min_bitrate(self):
        """Gets the min_bitrate of this H265VideoConfiguration.

        Minimum Bitrate

        :return: The min_bitrate of this H265VideoConfiguration.
        :rtype: int
        """
        return self._min_bitrate

    @min_bitrate.setter
    def min_bitrate(self, min_bitrate):
        """Sets the min_bitrate of this H265VideoConfiguration.

        Minimum Bitrate

        :param min_bitrate: The min_bitrate of this H265VideoConfiguration.
        :type: int
        """

        if min_bitrate is not None:
            if not isinstance(min_bitrate, int):
                raise TypeError("Invalid type for `min_bitrate`, type has to be `int`")

            self._min_bitrate = min_bitrate


    @property
    def bufsize(self):
        """Gets the bufsize of this H265VideoConfiguration.

        Specify the size of the VBV buffer (kbits)

        :return: The bufsize of this H265VideoConfiguration.
        :rtype: int
        """
        return self._bufsize

    @bufsize.setter
    def bufsize(self, bufsize):
        """Sets the bufsize of this H265VideoConfiguration.

        Specify the size of the VBV buffer (kbits)

        :param bufsize: The bufsize of this H265VideoConfiguration.
        :type: int
        """

        if bufsize is not None:
            if not isinstance(bufsize, int):
                raise TypeError("Invalid type for `bufsize`, type has to be `int`")

            self._bufsize = bufsize


    @property
    def min_gop(self):
        """Gets the min_gop of this H265VideoConfiguration.

        Minimum GOP length, the minimum distance between I-frames

        :return: The min_gop of this H265VideoConfiguration.
        :rtype: int
        """
        return self._min_gop

    @min_gop.setter
    def min_gop(self, min_gop):
        """Sets the min_gop of this H265VideoConfiguration.

        Minimum GOP length, the minimum distance between I-frames

        :param min_gop: The min_gop of this H265VideoConfiguration.
        :type: int
        """

        if min_gop is not None:
            if not isinstance(min_gop, int):
                raise TypeError("Invalid type for `min_gop`, type has to be `int`")

            self._min_gop = min_gop


    @property
    def max_gop(self):
        """Gets the max_gop of this H265VideoConfiguration.

        Maximum GOP length, the maximum distance between I-frames

        :return: The max_gop of this H265VideoConfiguration.
        :rtype: int
        """
        return self._max_gop

    @max_gop.setter
    def max_gop(self, max_gop):
        """Sets the max_gop of this H265VideoConfiguration.

        Maximum GOP length, the maximum distance between I-frames

        :param max_gop: The max_gop of this H265VideoConfiguration.
        :type: int
        """

        if max_gop is not None:
            if not isinstance(max_gop, int):
                raise TypeError("Invalid type for `max_gop`, type has to be `int`")

            self._max_gop = max_gop


    @property
    def open_gop(self):
        """Gets the open_gop of this H265VideoConfiguration.

        Enable open-gop, allows referencing frames from a previous gop

        :return: The open_gop of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._open_gop

    @open_gop.setter
    def open_gop(self, open_gop):
        """Sets the open_gop of this H265VideoConfiguration.

        Enable open-gop, allows referencing frames from a previous gop

        :param open_gop: The open_gop of this H265VideoConfiguration.
        :type: bool
        """

        if open_gop is not None:
            if not isinstance(open_gop, bool):
                raise TypeError("Invalid type for `open_gop`, type has to be `bool`")

            self._open_gop = open_gop


    @property
    def min_keyframe_interval(self):
        """Gets the min_keyframe_interval of this H265VideoConfiguration.

        Minimum interval in seconds between key frames

        :return: The min_keyframe_interval of this H265VideoConfiguration.
        :rtype: float
        """
        return self._min_keyframe_interval

    @min_keyframe_interval.setter
    def min_keyframe_interval(self, min_keyframe_interval):
        """Sets the min_keyframe_interval of this H265VideoConfiguration.

        Minimum interval in seconds between key frames

        :param min_keyframe_interval: The min_keyframe_interval of this H265VideoConfiguration.
        :type: float
        """

        if min_keyframe_interval is not None:
            if not isinstance(min_keyframe_interval, float):
                raise TypeError("Invalid type for `min_keyframe_interval`, type has to be `float`")

            self._min_keyframe_interval = min_keyframe_interval


    @property
    def max_keyframe_interval(self):
        """Gets the max_keyframe_interval of this H265VideoConfiguration.

        Maximum interval in seconds between key frames

        :return: The max_keyframe_interval of this H265VideoConfiguration.
        :rtype: float
        """
        return self._max_keyframe_interval

    @max_keyframe_interval.setter
    def max_keyframe_interval(self, max_keyframe_interval):
        """Sets the max_keyframe_interval of this H265VideoConfiguration.

        Maximum interval in seconds between key frames

        :param max_keyframe_interval: The max_keyframe_interval of this H265VideoConfiguration.
        :type: float
        """

        if max_keyframe_interval is not None:
            if not isinstance(max_keyframe_interval, float):
                raise TypeError("Invalid type for `max_keyframe_interval`, type has to be `float`")

            self._max_keyframe_interval = max_keyframe_interval


    @property
    def level(self):
        """Gets the level of this H265VideoConfiguration.


        :return: The level of this H265VideoConfiguration.
        :rtype: LevelH265
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this H265VideoConfiguration.


        :param level: The level of this H265VideoConfiguration.
        :type: LevelH265
        """

        if level is not None:
            if not isinstance(level, LevelH265):
                raise TypeError("Invalid type for `level`, type has to be `LevelH265`")

            self._level = level


    @property
    def rc_lookahead(self):
        """Gets the rc_lookahead of this H265VideoConfiguration.

        Number of frames for slice-type decision lookahead

        :return: The rc_lookahead of this H265VideoConfiguration.
        :rtype: int
        """
        return self._rc_lookahead

    @rc_lookahead.setter
    def rc_lookahead(self, rc_lookahead):
        """Sets the rc_lookahead of this H265VideoConfiguration.

        Number of frames for slice-type decision lookahead

        :param rc_lookahead: The rc_lookahead of this H265VideoConfiguration.
        :type: int
        """

        if rc_lookahead is not None:
            if rc_lookahead is not None and rc_lookahead > 250:
                raise ValueError("Invalid value for `rc_lookahead`, must be a value less than or equal to `250`")
            if rc_lookahead is not None and rc_lookahead < 1:
                raise ValueError("Invalid value for `rc_lookahead`, must be a value greater than or equal to `1`")
            if not isinstance(rc_lookahead, int):
                raise TypeError("Invalid type for `rc_lookahead`, type has to be `int`")

            self._rc_lookahead = rc_lookahead


    @property
    def b_adapt(self):
        """Gets the b_adapt of this H265VideoConfiguration.

        Set the level of effort in determining B frame placement

        :return: The b_adapt of this H265VideoConfiguration.
        :rtype: BAdapt
        """
        return self._b_adapt

    @b_adapt.setter
    def b_adapt(self, b_adapt):
        """Sets the b_adapt of this H265VideoConfiguration.

        Set the level of effort in determining B frame placement

        :param b_adapt: The b_adapt of this H265VideoConfiguration.
        :type: BAdapt
        """

        if b_adapt is not None:
            if not isinstance(b_adapt, BAdapt):
                raise TypeError("Invalid type for `b_adapt`, type has to be `BAdapt`")

            self._b_adapt = b_adapt


    @property
    def max_ctu_size(self):
        """Gets the max_ctu_size of this H265VideoConfiguration.


        :return: The max_ctu_size of this H265VideoConfiguration.
        :rtype: MaxCtuSize
        """
        return self._max_ctu_size

    @max_ctu_size.setter
    def max_ctu_size(self, max_ctu_size):
        """Sets the max_ctu_size of this H265VideoConfiguration.


        :param max_ctu_size: The max_ctu_size of this H265VideoConfiguration.
        :type: MaxCtuSize
        """

        if max_ctu_size is not None:
            if not isinstance(max_ctu_size, MaxCtuSize):
                raise TypeError("Invalid type for `max_ctu_size`, type has to be `MaxCtuSize`")

            self._max_ctu_size = max_ctu_size


    @property
    def tu_intra_depth(self):
        """Gets the tu_intra_depth of this H265VideoConfiguration.


        :return: The tu_intra_depth of this H265VideoConfiguration.
        :rtype: TuIntraDepth
        """
        return self._tu_intra_depth

    @tu_intra_depth.setter
    def tu_intra_depth(self, tu_intra_depth):
        """Sets the tu_intra_depth of this H265VideoConfiguration.


        :param tu_intra_depth: The tu_intra_depth of this H265VideoConfiguration.
        :type: TuIntraDepth
        """

        if tu_intra_depth is not None:
            if not isinstance(tu_intra_depth, TuIntraDepth):
                raise TypeError("Invalid type for `tu_intra_depth`, type has to be `TuIntraDepth`")

            self._tu_intra_depth = tu_intra_depth


    @property
    def tu_inter_depth(self):
        """Gets the tu_inter_depth of this H265VideoConfiguration.


        :return: The tu_inter_depth of this H265VideoConfiguration.
        :rtype: TuInterDepth
        """
        return self._tu_inter_depth

    @tu_inter_depth.setter
    def tu_inter_depth(self, tu_inter_depth):
        """Sets the tu_inter_depth of this H265VideoConfiguration.


        :param tu_inter_depth: The tu_inter_depth of this H265VideoConfiguration.
        :type: TuInterDepth
        """

        if tu_inter_depth is not None:
            if not isinstance(tu_inter_depth, TuInterDepth):
                raise TypeError("Invalid type for `tu_inter_depth`, type has to be `TuInterDepth`")

            self._tu_inter_depth = tu_inter_depth


    @property
    def motion_search(self):
        """Gets the motion_search of this H265VideoConfiguration.


        :return: The motion_search of this H265VideoConfiguration.
        :rtype: MotionSearch
        """
        return self._motion_search

    @motion_search.setter
    def motion_search(self, motion_search):
        """Sets the motion_search of this H265VideoConfiguration.


        :param motion_search: The motion_search of this H265VideoConfiguration.
        :type: MotionSearch
        """

        if motion_search is not None:
            if not isinstance(motion_search, MotionSearch):
                raise TypeError("Invalid type for `motion_search`, type has to be `MotionSearch`")

            self._motion_search = motion_search


    @property
    def sub_me(self):
        """Gets the sub_me of this H265VideoConfiguration.

        Set the amount of subpel refinement to perform.

        :return: The sub_me of this H265VideoConfiguration.
        :rtype: int
        """
        return self._sub_me

    @sub_me.setter
    def sub_me(self, sub_me):
        """Sets the sub_me of this H265VideoConfiguration.

        Set the amount of subpel refinement to perform.

        :param sub_me: The sub_me of this H265VideoConfiguration.
        :type: int
        """

        if sub_me is not None:
            if sub_me is not None and sub_me > 7:
                raise ValueError("Invalid value for `sub_me`, must be a value less than or equal to `7`")
            if sub_me is not None and sub_me < 0:
                raise ValueError("Invalid value for `sub_me`, must be a value greater than or equal to `0`")
            if not isinstance(sub_me, int):
                raise TypeError("Invalid type for `sub_me`, type has to be `int`")

            self._sub_me = sub_me


    @property
    def motion_search_range(self):
        """Gets the motion_search_range of this H265VideoConfiguration.

        Set the Motion search range.

        :return: The motion_search_range of this H265VideoConfiguration.
        :rtype: int
        """
        return self._motion_search_range

    @motion_search_range.setter
    def motion_search_range(self, motion_search_range):
        """Sets the motion_search_range of this H265VideoConfiguration.

        Set the Motion search range.

        :param motion_search_range: The motion_search_range of this H265VideoConfiguration.
        :type: int
        """

        if motion_search_range is not None:
            if motion_search_range is not None and motion_search_range > 32768:
                raise ValueError("Invalid value for `motion_search_range`, must be a value less than or equal to `32768`")
            if motion_search_range is not None and motion_search_range < 0:
                raise ValueError("Invalid value for `motion_search_range`, must be a value greater than or equal to `0`")
            if not isinstance(motion_search_range, int):
                raise TypeError("Invalid type for `motion_search_range`, type has to be `int`")

            self._motion_search_range = motion_search_range


    @property
    def weight_prediction_on_p_slice(self):
        """Gets the weight_prediction_on_p_slice of this H265VideoConfiguration.

        Enable weighted prediction in P slices

        :return: The weight_prediction_on_p_slice of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._weight_prediction_on_p_slice

    @weight_prediction_on_p_slice.setter
    def weight_prediction_on_p_slice(self, weight_prediction_on_p_slice):
        """Sets the weight_prediction_on_p_slice of this H265VideoConfiguration.

        Enable weighted prediction in P slices

        :param weight_prediction_on_p_slice: The weight_prediction_on_p_slice of this H265VideoConfiguration.
        :type: bool
        """

        if weight_prediction_on_p_slice is not None:
            if not isinstance(weight_prediction_on_p_slice, bool):
                raise TypeError("Invalid type for `weight_prediction_on_p_slice`, type has to be `bool`")

            self._weight_prediction_on_p_slice = weight_prediction_on_p_slice


    @property
    def weight_prediction_on_b_slice(self):
        """Gets the weight_prediction_on_b_slice of this H265VideoConfiguration.

        Enable weighted prediction in B slices

        :return: The weight_prediction_on_b_slice of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._weight_prediction_on_b_slice

    @weight_prediction_on_b_slice.setter
    def weight_prediction_on_b_slice(self, weight_prediction_on_b_slice):
        """Sets the weight_prediction_on_b_slice of this H265VideoConfiguration.

        Enable weighted prediction in B slices

        :param weight_prediction_on_b_slice: The weight_prediction_on_b_slice of this H265VideoConfiguration.
        :type: bool
        """

        if weight_prediction_on_b_slice is not None:
            if not isinstance(weight_prediction_on_b_slice, bool):
                raise TypeError("Invalid type for `weight_prediction_on_b_slice`, type has to be `bool`")

            self._weight_prediction_on_b_slice = weight_prediction_on_b_slice


    @property
    def sao(self):
        """Gets the sao of this H265VideoConfiguration.

        Toggle sample adaptive offset loop filter

        :return: The sao of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._sao

    @sao.setter
    def sao(self, sao):
        """Sets the sao of this H265VideoConfiguration.

        Toggle sample adaptive offset loop filter

        :param sao: The sao of this H265VideoConfiguration.
        :type: bool
        """

        if sao is not None:
            if not isinstance(sao, bool):
                raise TypeError("Invalid type for `sao`, type has to be `bool`")

            self._sao = sao


    @property
    def master_display(self):
        """Gets the master_display of this H265VideoConfiguration.

        Set the mastering display color volume SEI info (SMPTE ST 2086). For example `G(13250,34500)B(7500,3000)R(34000,16000)WP(15635,16450)L(10000000,1)` describes a P3D65 1000-nits monitor, where G(x=0.265, y=0.690), B(x=0.150, y=0.060), R(x=0.680, y=0.320), WP(x=0.3127, y=0.3290), L(max=1000, min=0.0001). Part of HDR-10 metadata.

        :return: The master_display of this H265VideoConfiguration.
        :rtype: str
        """
        return self._master_display

    @master_display.setter
    def master_display(self, master_display):
        """Sets the master_display of this H265VideoConfiguration.

        Set the mastering display color volume SEI info (SMPTE ST 2086). For example `G(13250,34500)B(7500,3000)R(34000,16000)WP(15635,16450)L(10000000,1)` describes a P3D65 1000-nits monitor, where G(x=0.265, y=0.690), B(x=0.150, y=0.060), R(x=0.680, y=0.320), WP(x=0.3127, y=0.3290), L(max=1000, min=0.0001). Part of HDR-10 metadata.

        :param master_display: The master_display of this H265VideoConfiguration.
        :type: str
        """

        if master_display is not None:
            if not isinstance(master_display, str):
                raise TypeError("Invalid type for `master_display`, type has to be `str`")

            self._master_display = master_display


    @property
    def max_content_light_level(self):
        """Gets the max_content_light_level of this H265VideoConfiguration.

        Set the max content light level (MaxCLL). Use together with maxPictureAverageLightLevel (which will be 0 if not set). Part of HDR-10 metadata.

        :return: The max_content_light_level of this H265VideoConfiguration.
        :rtype: str
        """
        return self._max_content_light_level

    @max_content_light_level.setter
    def max_content_light_level(self, max_content_light_level):
        """Sets the max_content_light_level of this H265VideoConfiguration.

        Set the max content light level (MaxCLL). Use together with maxPictureAverageLightLevel (which will be 0 if not set). Part of HDR-10 metadata.

        :param max_content_light_level: The max_content_light_level of this H265VideoConfiguration.
        :type: str
        """

        if max_content_light_level is not None:
            if not isinstance(max_content_light_level, str):
                raise TypeError("Invalid type for `max_content_light_level`, type has to be `str`")

            self._max_content_light_level = max_content_light_level


    @property
    def max_average_light_level(self):
        """Gets the max_average_light_level of this H265VideoConfiguration.

        Set the maximum picture average light level (MaxFALL). Use together with maxContentLightLevel (which will be 0 if not set). Part of HDR-10 metadata.

        :return: The max_average_light_level of this H265VideoConfiguration.
        :rtype: int
        """
        return self._max_average_light_level

    @max_average_light_level.setter
    def max_average_light_level(self, max_average_light_level):
        """Sets the max_average_light_level of this H265VideoConfiguration.

        Set the maximum picture average light level (MaxFALL). Use together with maxContentLightLevel (which will be 0 if not set). Part of HDR-10 metadata.

        :param max_average_light_level: The max_average_light_level of this H265VideoConfiguration.
        :type: int
        """

        if max_average_light_level is not None:
            if not isinstance(max_average_light_level, int):
                raise TypeError("Invalid type for `max_average_light_level`, type has to be `int`")

            self._max_average_light_level = max_average_light_level


    @property
    def hdr(self):
        """Gets the hdr of this H265VideoConfiguration.

        Force signaling of HDR parameters in SEI packets. Enabled automatically when masterDisplay or maxContentLightLevel/maxPictureAverageLightLevel are set. Useful when there is a desire to signal 0 values for maxContentLightLevel and maxPictureAverageLightLevel.

        :return: The hdr of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._hdr

    @hdr.setter
    def hdr(self, hdr):
        """Sets the hdr of this H265VideoConfiguration.

        Force signaling of HDR parameters in SEI packets. Enabled automatically when masterDisplay or maxContentLightLevel/maxPictureAverageLightLevel are set. Useful when there is a desire to signal 0 values for maxContentLightLevel and maxPictureAverageLightLevel.

        :param hdr: The hdr of this H265VideoConfiguration.
        :type: bool
        """

        if hdr is not None:
            if not isinstance(hdr, bool):
                raise TypeError("Invalid type for `hdr`, type has to be `bool`")

            self._hdr = hdr


    @property
    def scene_cut_threshold(self):
        """Gets the scene_cut_threshold of this H265VideoConfiguration.

        Scene Change sensitivity. The higher the value, the more likely an I-Frame will be inserted. Set to 0 to disable it.

        :return: The scene_cut_threshold of this H265VideoConfiguration.
        :rtype: int
        """
        return self._scene_cut_threshold

    @scene_cut_threshold.setter
    def scene_cut_threshold(self, scene_cut_threshold):
        """Sets the scene_cut_threshold of this H265VideoConfiguration.

        Scene Change sensitivity. The higher the value, the more likely an I-Frame will be inserted. Set to 0 to disable it.

        :param scene_cut_threshold: The scene_cut_threshold of this H265VideoConfiguration.
        :type: int
        """

        if scene_cut_threshold is not None:
            if scene_cut_threshold is not None and scene_cut_threshold < 0:
                raise ValueError("Invalid value for `scene_cut_threshold`, must be a value greater than or equal to `0`")
            if not isinstance(scene_cut_threshold, int):
                raise TypeError("Invalid type for `scene_cut_threshold`, type has to be `int`")

            self._scene_cut_threshold = scene_cut_threshold


    @property
    def adaptive_quantization_mode(self):
        """Gets the adaptive_quantization_mode of this H265VideoConfiguration.

        Controls the adaptive quantization algorithm

        :return: The adaptive_quantization_mode of this H265VideoConfiguration.
        :rtype: AdaptiveQuantMode
        """
        return self._adaptive_quantization_mode

    @adaptive_quantization_mode.setter
    def adaptive_quantization_mode(self, adaptive_quantization_mode):
        """Sets the adaptive_quantization_mode of this H265VideoConfiguration.

        Controls the adaptive quantization algorithm

        :param adaptive_quantization_mode: The adaptive_quantization_mode of this H265VideoConfiguration.
        :type: AdaptiveQuantMode
        """

        if adaptive_quantization_mode is not None:
            if not isinstance(adaptive_quantization_mode, AdaptiveQuantMode):
                raise TypeError("Invalid type for `adaptive_quantization_mode`, type has to be `AdaptiveQuantMode`")

            self._adaptive_quantization_mode = adaptive_quantization_mode


    @property
    def enable_hlg_signaling(self):
        """Gets the enable_hlg_signaling of this H265VideoConfiguration.

        By enabling this video stream will be signaled as HLG

        :return: The enable_hlg_signaling of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._enable_hlg_signaling

    @enable_hlg_signaling.setter
    def enable_hlg_signaling(self, enable_hlg_signaling):
        """Sets the enable_hlg_signaling of this H265VideoConfiguration.

        By enabling this video stream will be signaled as HLG

        :param enable_hlg_signaling: The enable_hlg_signaling of this H265VideoConfiguration.
        :type: bool
        """

        if enable_hlg_signaling is not None:
            if not isinstance(enable_hlg_signaling, bool):
                raise TypeError("Invalid type for `enable_hlg_signaling`, type has to be `bool`")

            self._enable_hlg_signaling = enable_hlg_signaling


    @property
    def video_format(self):
        """Gets the video_format of this H265VideoConfiguration.

        Specifies the source format of the original analog video prior to digitizing and encoding

        :return: The video_format of this H265VideoConfiguration.
        :rtype: VideoFormat
        """
        return self._video_format

    @video_format.setter
    def video_format(self, video_format):
        """Sets the video_format of this H265VideoConfiguration.

        Specifies the source format of the original analog video prior to digitizing and encoding

        :param video_format: The video_format of this H265VideoConfiguration.
        :type: VideoFormat
        """

        if video_format is not None:
            if not isinstance(video_format, VideoFormat):
                raise TypeError("Invalid type for `video_format`, type has to be `VideoFormat`")

            self._video_format = video_format


    @property
    def psy_rate_distortion_optimization(self):
        """Gets the psy_rate_distortion_optimization of this H265VideoConfiguration.

        Psycho-visual rate-distortion retains fine details like film grain at the expense of more blocking artifacts. Higher values make the video appear sharper and more detailed but with a higher risk of blocking artifacts. Needs to have subMe with RD_IP, RD_ALL, RD_REF_IP, RD_REF_ALL, QPRD or FULL_RD

        :return: The psy_rate_distortion_optimization of this H265VideoConfiguration.
        :rtype: float
        """
        return self._psy_rate_distortion_optimization

    @psy_rate_distortion_optimization.setter
    def psy_rate_distortion_optimization(self, psy_rate_distortion_optimization):
        """Sets the psy_rate_distortion_optimization of this H265VideoConfiguration.

        Psycho-visual rate-distortion retains fine details like film grain at the expense of more blocking artifacts. Higher values make the video appear sharper and more detailed but with a higher risk of blocking artifacts. Needs to have subMe with RD_IP, RD_ALL, RD_REF_IP, RD_REF_ALL, QPRD or FULL_RD

        :param psy_rate_distortion_optimization: The psy_rate_distortion_optimization of this H265VideoConfiguration.
        :type: float
        """

        if psy_rate_distortion_optimization is not None:
            if not isinstance(psy_rate_distortion_optimization, float):
                raise TypeError("Invalid type for `psy_rate_distortion_optimization`, type has to be `float`")

            self._psy_rate_distortion_optimization = psy_rate_distortion_optimization


    @property
    def psy_rate_distortion_optimized_quantization(self):
        """Gets the psy_rate_distortion_optimized_quantization of this H265VideoConfiguration.

        Strength of psycho-visual optimizations in quantization. Only has an effect in presets which use RDOQ (rd-levels 4 and 5). The value must be between 0 and 50, 1.0 is typical

        :return: The psy_rate_distortion_optimized_quantization of this H265VideoConfiguration.
        :rtype: float
        """
        return self._psy_rate_distortion_optimized_quantization

    @psy_rate_distortion_optimized_quantization.setter
    def psy_rate_distortion_optimized_quantization(self, psy_rate_distortion_optimized_quantization):
        """Sets the psy_rate_distortion_optimized_quantization of this H265VideoConfiguration.

        Strength of psycho-visual optimizations in quantization. Only has an effect in presets which use RDOQ (rd-levels 4 and 5). The value must be between 0 and 50, 1.0 is typical

        :param psy_rate_distortion_optimized_quantization: The psy_rate_distortion_optimized_quantization of this H265VideoConfiguration.
        :type: float
        """

        if psy_rate_distortion_optimized_quantization is not None:
            if not isinstance(psy_rate_distortion_optimized_quantization, float):
                raise TypeError("Invalid type for `psy_rate_distortion_optimized_quantization`, type has to be `float`")

            self._psy_rate_distortion_optimized_quantization = psy_rate_distortion_optimized_quantization


    @property
    def enable_hrd_signaling(self):
        """Gets the enable_hrd_signaling of this H265VideoConfiguration.

        Signal hypothetical reference decoder (HRD) information

        :return: The enable_hrd_signaling of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._enable_hrd_signaling

    @enable_hrd_signaling.setter
    def enable_hrd_signaling(self, enable_hrd_signaling):
        """Sets the enable_hrd_signaling of this H265VideoConfiguration.

        Signal hypothetical reference decoder (HRD) information

        :param enable_hrd_signaling: The enable_hrd_signaling of this H265VideoConfiguration.
        :type: bool
        """

        if enable_hrd_signaling is not None:
            if not isinstance(enable_hrd_signaling, bool):
                raise TypeError("Invalid type for `enable_hrd_signaling`, type has to be `bool`")

            self._enable_hrd_signaling = enable_hrd_signaling


    @property
    def cutree(self):
        """Gets the cutree of this H265VideoConfiguration.

        Enables the use of lookahead’s lowres motion vector fields to determine the amount of reuse of each block to tune adaptive quantization factors.

        :return: The cutree of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._cutree

    @cutree.setter
    def cutree(self, cutree):
        """Sets the cutree of this H265VideoConfiguration.

        Enables the use of lookahead’s lowres motion vector fields to determine the amount of reuse of each block to tune adaptive quantization factors.

        :param cutree: The cutree of this H265VideoConfiguration.
        :type: bool
        """

        if cutree is not None:
            if not isinstance(cutree, bool):
                raise TypeError("Invalid type for `cutree`, type has to be `bool`")

            self._cutree = cutree


    @property
    def min_coding_unit_size(self):
        """Gets the min_coding_unit_size of this H265VideoConfiguration.

        Minimum CU size (width and height). By using 16 or 32 the encoder will not analyze the cost of CUs below that minimum threshold, saving considerable amounts of compute with a predictable increase in bitrate. This setting has a large effect on performance on the faster presets.

        :return: The min_coding_unit_size of this H265VideoConfiguration.
        :rtype: MinCodingUnitSize
        """
        return self._min_coding_unit_size

    @min_coding_unit_size.setter
    def min_coding_unit_size(self, min_coding_unit_size):
        """Sets the min_coding_unit_size of this H265VideoConfiguration.

        Minimum CU size (width and height). By using 16 or 32 the encoder will not analyze the cost of CUs below that minimum threshold, saving considerable amounts of compute with a predictable increase in bitrate. This setting has a large effect on performance on the faster presets.

        :param min_coding_unit_size: The min_coding_unit_size of this H265VideoConfiguration.
        :type: MinCodingUnitSize
        """

        if min_coding_unit_size is not None:
            if not isinstance(min_coding_unit_size, MinCodingUnitSize):
                raise TypeError("Invalid type for `min_coding_unit_size`, type has to be `MinCodingUnitSize`")

            self._min_coding_unit_size = min_coding_unit_size


    @property
    def lookahead_slices(self):
        """Gets the lookahead_slices of this H265VideoConfiguration.

        Use multiple worker threads to measure the estimated cost of each frame within the lookahead. The higher this parameter, the less accurate the frame costs will be which will result in less accurate B-frame and scene-cut decisions. Valid range: 0 - 16

        :return: The lookahead_slices of this H265VideoConfiguration.
        :rtype: int
        """
        return self._lookahead_slices

    @lookahead_slices.setter
    def lookahead_slices(self, lookahead_slices):
        """Sets the lookahead_slices of this H265VideoConfiguration.

        Use multiple worker threads to measure the estimated cost of each frame within the lookahead. The higher this parameter, the less accurate the frame costs will be which will result in less accurate B-frame and scene-cut decisions. Valid range: 0 - 16

        :param lookahead_slices: The lookahead_slices of this H265VideoConfiguration.
        :type: int
        """

        if lookahead_slices is not None:
            if not isinstance(lookahead_slices, int):
                raise TypeError("Invalid type for `lookahead_slices`, type has to be `int`")

            self._lookahead_slices = lookahead_slices


    @property
    def limit_references(self):
        """Gets the limit_references of this H265VideoConfiguration.

        If enabled, limit references per depth, CU or both.

        :return: The limit_references of this H265VideoConfiguration.
        :rtype: LimitReferences
        """
        return self._limit_references

    @limit_references.setter
    def limit_references(self, limit_references):
        """Sets the limit_references of this H265VideoConfiguration.

        If enabled, limit references per depth, CU or both.

        :param limit_references: The limit_references of this H265VideoConfiguration.
        :type: LimitReferences
        """

        if limit_references is not None:
            if not isinstance(limit_references, LimitReferences):
                raise TypeError("Invalid type for `limit_references`, type has to be `LimitReferences`")

            self._limit_references = limit_references


    @property
    def rectangular_motion_partitions_analysis(self):
        """Gets the rectangular_motion_partitions_analysis of this H265VideoConfiguration.

        Enable analysis of rectangular motion partitions Nx2N and 2NxN.

        :return: The rectangular_motion_partitions_analysis of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._rectangular_motion_partitions_analysis

    @rectangular_motion_partitions_analysis.setter
    def rectangular_motion_partitions_analysis(self, rectangular_motion_partitions_analysis):
        """Sets the rectangular_motion_partitions_analysis of this H265VideoConfiguration.

        Enable analysis of rectangular motion partitions Nx2N and 2NxN.

        :param rectangular_motion_partitions_analysis: The rectangular_motion_partitions_analysis of this H265VideoConfiguration.
        :type: bool
        """

        if rectangular_motion_partitions_analysis is not None:
            if not isinstance(rectangular_motion_partitions_analysis, bool):
                raise TypeError("Invalid type for `rectangular_motion_partitions_analysis`, type has to be `bool`")

            self._rectangular_motion_partitions_analysis = rectangular_motion_partitions_analysis


    @property
    def asymetric_motion_partitions_analysis(self):
        """Gets the asymetric_motion_partitions_analysis of this H265VideoConfiguration.

        Enable analysis of asymmetric motion partitions.

        :return: The asymetric_motion_partitions_analysis of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._asymetric_motion_partitions_analysis

    @asymetric_motion_partitions_analysis.setter
    def asymetric_motion_partitions_analysis(self, asymetric_motion_partitions_analysis):
        """Sets the asymetric_motion_partitions_analysis of this H265VideoConfiguration.

        Enable analysis of asymmetric motion partitions.

        :param asymetric_motion_partitions_analysis: The asymetric_motion_partitions_analysis of this H265VideoConfiguration.
        :type: bool
        """

        if asymetric_motion_partitions_analysis is not None:
            if not isinstance(asymetric_motion_partitions_analysis, bool):
                raise TypeError("Invalid type for `asymetric_motion_partitions_analysis`, type has to be `bool`")

            self._asymetric_motion_partitions_analysis = asymetric_motion_partitions_analysis


    @property
    def limit_modes(self):
        """Gets the limit_modes of this H265VideoConfiguration.

        When enabled, will limit modes analyzed for each CU using cost metrics from the 4 sub-CUs. This can significantly improve performance when `rectangularMotionPartitionsAnalysis` and/or `asymetricMotionPartitionsAnalysis` are enabled at minimal compression efficiency loss.

        :return: The limit_modes of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._limit_modes

    @limit_modes.setter
    def limit_modes(self, limit_modes):
        """Sets the limit_modes of this H265VideoConfiguration.

        When enabled, will limit modes analyzed for each CU using cost metrics from the 4 sub-CUs. This can significantly improve performance when `rectangularMotionPartitionsAnalysis` and/or `asymetricMotionPartitionsAnalysis` are enabled at minimal compression efficiency loss.

        :param limit_modes: The limit_modes of this H265VideoConfiguration.
        :type: bool
        """

        if limit_modes is not None:
            if not isinstance(limit_modes, bool):
                raise TypeError("Invalid type for `limit_modes`, type has to be `bool`")

            self._limit_modes = limit_modes


    @property
    def max_merge(self):
        """Gets the max_merge of this H265VideoConfiguration.

        Maximum number of neighbor (spatial and temporal) candidate blocks that the encoder may consider for merging motion predictions. Valid range: 1 - 5

        :return: The max_merge of this H265VideoConfiguration.
        :rtype: int
        """
        return self._max_merge

    @max_merge.setter
    def max_merge(self, max_merge):
        """Sets the max_merge of this H265VideoConfiguration.

        Maximum number of neighbor (spatial and temporal) candidate blocks that the encoder may consider for merging motion predictions. Valid range: 1 - 5

        :param max_merge: The max_merge of this H265VideoConfiguration.
        :type: int
        """

        if max_merge is not None:
            if not isinstance(max_merge, int):
                raise TypeError("Invalid type for `max_merge`, type has to be `int`")

            self._max_merge = max_merge


    @property
    def early_skip(self):
        """Gets the early_skip of this H265VideoConfiguration.

        Measure 2Nx2N merge candidates first; if no residual is found, additional modes at that depth are not analysed.

        :return: The early_skip of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._early_skip

    @early_skip.setter
    def early_skip(self, early_skip):
        """Sets the early_skip of this H265VideoConfiguration.

        Measure 2Nx2N merge candidates first; if no residual is found, additional modes at that depth are not analysed.

        :param early_skip: The early_skip of this H265VideoConfiguration.
        :type: bool
        """

        if early_skip is not None:
            if not isinstance(early_skip, bool):
                raise TypeError("Invalid type for `early_skip`, type has to be `bool`")

            self._early_skip = early_skip


    @property
    def recursion_skip(self):
        """Gets the recursion_skip of this H265VideoConfiguration.

        If enabled exits early from CU depth recursion. When a skip CU is found, additional heuristics are used to decide whether to terminate recursion.

        :return: The recursion_skip of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._recursion_skip

    @recursion_skip.setter
    def recursion_skip(self, recursion_skip):
        """Sets the recursion_skip of this H265VideoConfiguration.

        If enabled exits early from CU depth recursion. When a skip CU is found, additional heuristics are used to decide whether to terminate recursion.

        :param recursion_skip: The recursion_skip of this H265VideoConfiguration.
        :type: bool
        """

        if recursion_skip is not None:
            if not isinstance(recursion_skip, bool):
                raise TypeError("Invalid type for `recursion_skip`, type has to be `bool`")

            self._recursion_skip = recursion_skip


    @property
    def fast_search_for_angular_intra_predictions(self):
        """Gets the fast_search_for_angular_intra_predictions of this H265VideoConfiguration.

        Enable faster search method for angular intra predictions.

        :return: The fast_search_for_angular_intra_predictions of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._fast_search_for_angular_intra_predictions

    @fast_search_for_angular_intra_predictions.setter
    def fast_search_for_angular_intra_predictions(self, fast_search_for_angular_intra_predictions):
        """Sets the fast_search_for_angular_intra_predictions of this H265VideoConfiguration.

        Enable faster search method for angular intra predictions.

        :param fast_search_for_angular_intra_predictions: The fast_search_for_angular_intra_predictions of this H265VideoConfiguration.
        :type: bool
        """

        if fast_search_for_angular_intra_predictions is not None:
            if not isinstance(fast_search_for_angular_intra_predictions, bool):
                raise TypeError("Invalid type for `fast_search_for_angular_intra_predictions`, type has to be `bool`")

            self._fast_search_for_angular_intra_predictions = fast_search_for_angular_intra_predictions


    @property
    def evaluation_of_intra_modes_in_b_slices(self):
        """Gets the evaluation_of_intra_modes_in_b_slices of this H265VideoConfiguration.

        Enables the evaluation of intra modes in B slices.

        :return: The evaluation_of_intra_modes_in_b_slices of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._evaluation_of_intra_modes_in_b_slices

    @evaluation_of_intra_modes_in_b_slices.setter
    def evaluation_of_intra_modes_in_b_slices(self, evaluation_of_intra_modes_in_b_slices):
        """Sets the evaluation_of_intra_modes_in_b_slices of this H265VideoConfiguration.

        Enables the evaluation of intra modes in B slices.

        :param evaluation_of_intra_modes_in_b_slices: The evaluation_of_intra_modes_in_b_slices of this H265VideoConfiguration.
        :type: bool
        """

        if evaluation_of_intra_modes_in_b_slices is not None:
            if not isinstance(evaluation_of_intra_modes_in_b_slices, bool):
                raise TypeError("Invalid type for `evaluation_of_intra_modes_in_b_slices`, type has to be `bool`")

            self._evaluation_of_intra_modes_in_b_slices = evaluation_of_intra_modes_in_b_slices


    @property
    def sign_hide(self):
        """Gets the sign_hide of this H265VideoConfiguration.

        Hide sign bit of one coefficient per coding tree unit.

        :return: The sign_hide of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._sign_hide

    @sign_hide.setter
    def sign_hide(self, sign_hide):
        """Sets the sign_hide of this H265VideoConfiguration.

        Hide sign bit of one coefficient per coding tree unit.

        :param sign_hide: The sign_hide of this H265VideoConfiguration.
        :type: bool
        """

        if sign_hide is not None:
            if not isinstance(sign_hide, bool):
                raise TypeError("Invalid type for `sign_hide`, type has to be `bool`")

            self._sign_hide = sign_hide


    @property
    def rate_distortion_level_for_mode_decision(self):
        """Gets the rate_distortion_level_for_mode_decision of this H265VideoConfiguration.

        Level of rate-distortion optimization in mode decision. The lower the value the faster the encode, the higher the value higher the compression efficiency. Valid range: 0 - 6

        :return: The rate_distortion_level_for_mode_decision of this H265VideoConfiguration.
        :rtype: int
        """
        return self._rate_distortion_level_for_mode_decision

    @rate_distortion_level_for_mode_decision.setter
    def rate_distortion_level_for_mode_decision(self, rate_distortion_level_for_mode_decision):
        """Sets the rate_distortion_level_for_mode_decision of this H265VideoConfiguration.

        Level of rate-distortion optimization in mode decision. The lower the value the faster the encode, the higher the value higher the compression efficiency. Valid range: 0 - 6

        :param rate_distortion_level_for_mode_decision: The rate_distortion_level_for_mode_decision of this H265VideoConfiguration.
        :type: int
        """

        if rate_distortion_level_for_mode_decision is not None:
            if not isinstance(rate_distortion_level_for_mode_decision, int):
                raise TypeError("Invalid type for `rate_distortion_level_for_mode_decision`, type has to be `int`")

            self._rate_distortion_level_for_mode_decision = rate_distortion_level_for_mode_decision


    @property
    def rate_distortion_level_for_quantization(self):
        """Gets the rate_distortion_level_for_quantization of this H265VideoConfiguration.

        Specify the amount of rate-distortion analysis to use within quantization.

        :return: The rate_distortion_level_for_quantization of this H265VideoConfiguration.
        :rtype: RateDistortionLevelForQuantization
        """
        return self._rate_distortion_level_for_quantization

    @rate_distortion_level_for_quantization.setter
    def rate_distortion_level_for_quantization(self, rate_distortion_level_for_quantization):
        """Sets the rate_distortion_level_for_quantization of this H265VideoConfiguration.

        Specify the amount of rate-distortion analysis to use within quantization.

        :param rate_distortion_level_for_quantization: The rate_distortion_level_for_quantization of this H265VideoConfiguration.
        :type: RateDistortionLevelForQuantization
        """

        if rate_distortion_level_for_quantization is not None:
            if not isinstance(rate_distortion_level_for_quantization, RateDistortionLevelForQuantization):
                raise TypeError("Invalid type for `rate_distortion_level_for_quantization`, type has to be `RateDistortionLevelForQuantization`")

            self._rate_distortion_level_for_quantization = rate_distortion_level_for_quantization


    @property
    def qp_min(self):
        """Gets the qp_min of this H265VideoConfiguration.

        Sets the minimum of quantization factor. Valid value range: 0 - 69

        :return: The qp_min of this H265VideoConfiguration.
        :rtype: int
        """
        return self._qp_min

    @qp_min.setter
    def qp_min(self, qp_min):
        """Sets the qp_min of this H265VideoConfiguration.

        Sets the minimum of quantization factor. Valid value range: 0 - 69

        :param qp_min: The qp_min of this H265VideoConfiguration.
        :type: int
        """

        if qp_min is not None:
            if not isinstance(qp_min, int):
                raise TypeError("Invalid type for `qp_min`, type has to be `int`")

            self._qp_min = qp_min


    @property
    def qp_max(self):
        """Gets the qp_max of this H265VideoConfiguration.

        Sets the maximum of quantization factor. Valid value range: 0 - 69

        :return: The qp_max of this H265VideoConfiguration.
        :rtype: int
        """
        return self._qp_max

    @qp_max.setter
    def qp_max(self, qp_max):
        """Sets the qp_max of this H265VideoConfiguration.

        Sets the maximum of quantization factor. Valid value range: 0 - 69

        :param qp_max: The qp_max of this H265VideoConfiguration.
        :type: int
        """

        if qp_max is not None:
            if not isinstance(qp_max, int):
                raise TypeError("Invalid type for `qp_max`, type has to be `int`")

            self._qp_max = qp_max


    @property
    def wavefront_parallel_processing(self):
        """Gets the wavefront_parallel_processing of this H265VideoConfiguration.

        The encoder may begin encoding a row as soon as the row above it is at least two CTUs ahead in the encode process. Default is enabled.

        :return: The wavefront_parallel_processing of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._wavefront_parallel_processing

    @wavefront_parallel_processing.setter
    def wavefront_parallel_processing(self, wavefront_parallel_processing):
        """Sets the wavefront_parallel_processing of this H265VideoConfiguration.

        The encoder may begin encoding a row as soon as the row above it is at least two CTUs ahead in the encode process. Default is enabled.

        :param wavefront_parallel_processing: The wavefront_parallel_processing of this H265VideoConfiguration.
        :type: bool
        """

        if wavefront_parallel_processing is not None:
            if not isinstance(wavefront_parallel_processing, bool):
                raise TypeError("Invalid type for `wavefront_parallel_processing`, type has to be `bool`")

            self._wavefront_parallel_processing = wavefront_parallel_processing


    @property
    def parallel_mode_decision(self):
        """Gets the parallel_mode_decision of this H265VideoConfiguration.

        When enabled the encoder will distribute the analysis work of each CU (merge, inter, intra) across multiple worker threads. Default is disabled.

        :return: The parallel_mode_decision of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._parallel_mode_decision

    @parallel_mode_decision.setter
    def parallel_mode_decision(self, parallel_mode_decision):
        """Sets the parallel_mode_decision of this H265VideoConfiguration.

        When enabled the encoder will distribute the analysis work of each CU (merge, inter, intra) across multiple worker threads. Default is disabled.

        :param parallel_mode_decision: The parallel_mode_decision of this H265VideoConfiguration.
        :type: bool
        """

        if parallel_mode_decision is not None:
            if not isinstance(parallel_mode_decision, bool):
                raise TypeError("Invalid type for `parallel_mode_decision`, type has to be `bool`")

            self._parallel_mode_decision = parallel_mode_decision


    @property
    def parallel_motion_estimation(self):
        """Gets the parallel_motion_estimation of this H265VideoConfiguration.

        When enabled the encoder will distribute motion estimation across multiple worker threads when more than two references require motion searches for a given CU. Default is disabled.

        :return: The parallel_motion_estimation of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._parallel_motion_estimation

    @parallel_motion_estimation.setter
    def parallel_motion_estimation(self, parallel_motion_estimation):
        """Sets the parallel_motion_estimation of this H265VideoConfiguration.

        When enabled the encoder will distribute motion estimation across multiple worker threads when more than two references require motion searches for a given CU. Default is disabled.

        :param parallel_motion_estimation: The parallel_motion_estimation of this H265VideoConfiguration.
        :type: bool
        """

        if parallel_motion_estimation is not None:
            if not isinstance(parallel_motion_estimation, bool):
                raise TypeError("Invalid type for `parallel_motion_estimation`, type has to be `bool`")

            self._parallel_motion_estimation = parallel_motion_estimation


    @property
    def slices(self):
        """Gets the slices of this H265VideoConfiguration.

        Encode each incoming frame as multiple parallel slices that may be decoded independently. Default is 1.

        :return: The slices of this H265VideoConfiguration.
        :rtype: int
        """
        return self._slices

    @slices.setter
    def slices(self, slices):
        """Sets the slices of this H265VideoConfiguration.

        Encode each incoming frame as multiple parallel slices that may be decoded independently. Default is 1.

        :param slices: The slices of this H265VideoConfiguration.
        :type: int
        """

        if slices is not None:
            if not isinstance(slices, int):
                raise TypeError("Invalid type for `slices`, type has to be `int`")

            self._slices = slices


    @property
    def copy_picture(self):
        """Gets the copy_picture of this H265VideoConfiguration.

        Copy buffers of input picture in frame. Default is enabled.

        :return: The copy_picture of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._copy_picture

    @copy_picture.setter
    def copy_picture(self, copy_picture):
        """Sets the copy_picture of this H265VideoConfiguration.

        Copy buffers of input picture in frame. Default is enabled.

        :param copy_picture: The copy_picture of this H265VideoConfiguration.
        :type: bool
        """

        if copy_picture is not None:
            if not isinstance(copy_picture, bool):
                raise TypeError("Invalid type for `copy_picture`, type has to be `bool`")

            self._copy_picture = copy_picture


    @property
    def level_high_tier(self):
        """Gets the level_high_tier of this H265VideoConfiguration.

        If high tier is disabled the encoder will attempt to encode only at the main tier. Default is enabled.

        :return: The level_high_tier of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._level_high_tier

    @level_high_tier.setter
    def level_high_tier(self, level_high_tier):
        """Sets the level_high_tier of this H265VideoConfiguration.

        If high tier is disabled the encoder will attempt to encode only at the main tier. Default is enabled.

        :param level_high_tier: The level_high_tier of this H265VideoConfiguration.
        :type: bool
        """

        if level_high_tier is not None:
            if not isinstance(level_high_tier, bool):
                raise TypeError("Invalid type for `level_high_tier`, type has to be `bool`")

            self._level_high_tier = level_high_tier


    @property
    def skip_split_rate_distortion_analysis(self):
        """Gets the skip_split_rate_distortion_analysis of this H265VideoConfiguration.

        Enable skipping split rate distortion analysis when sum of split CU RD cost larger than one split CU RD cost for intra CU. Default disabled.

        :return: The skip_split_rate_distortion_analysis of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._skip_split_rate_distortion_analysis

    @skip_split_rate_distortion_analysis.setter
    def skip_split_rate_distortion_analysis(self, skip_split_rate_distortion_analysis):
        """Sets the skip_split_rate_distortion_analysis of this H265VideoConfiguration.

        Enable skipping split rate distortion analysis when sum of split CU RD cost larger than one split CU RD cost for intra CU. Default disabled.

        :param skip_split_rate_distortion_analysis: The skip_split_rate_distortion_analysis of this H265VideoConfiguration.
        :type: bool
        """

        if skip_split_rate_distortion_analysis is not None:
            if not isinstance(skip_split_rate_distortion_analysis, bool):
                raise TypeError("Invalid type for `skip_split_rate_distortion_analysis`, type has to be `bool`")

            self._skip_split_rate_distortion_analysis = skip_split_rate_distortion_analysis


    @property
    def coding_unit_lossless(self):
        """Gets the coding_unit_lossless of this H265VideoConfiguration.

        If enabled, consider lossless mode in CU RDO decisions. Default is disabled.

        :return: The coding_unit_lossless of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._coding_unit_lossless

    @coding_unit_lossless.setter
    def coding_unit_lossless(self, coding_unit_lossless):
        """Sets the coding_unit_lossless of this H265VideoConfiguration.

        If enabled, consider lossless mode in CU RDO decisions. Default is disabled.

        :param coding_unit_lossless: The coding_unit_lossless of this H265VideoConfiguration.
        :type: bool
        """

        if coding_unit_lossless is not None:
            if not isinstance(coding_unit_lossless, bool):
                raise TypeError("Invalid type for `coding_unit_lossless`, type has to be `bool`")

            self._coding_unit_lossless = coding_unit_lossless


    @property
    def transform_skip(self):
        """Gets the transform_skip of this H265VideoConfiguration.

        Enable evaluation of transform skip (bypass DCT but still use quantization) coding for 4x4 TU coded blocks. Default is NONE.

        :return: The transform_skip of this H265VideoConfiguration.
        :rtype: TransformSkipMode
        """
        return self._transform_skip

    @transform_skip.setter
    def transform_skip(self, transform_skip):
        """Sets the transform_skip of this H265VideoConfiguration.

        Enable evaluation of transform skip (bypass DCT but still use quantization) coding for 4x4 TU coded blocks. Default is NONE.

        :param transform_skip: The transform_skip of this H265VideoConfiguration.
        :type: TransformSkipMode
        """

        if transform_skip is not None:
            if not isinstance(transform_skip, TransformSkipMode):
                raise TypeError("Invalid type for `transform_skip`, type has to be `TransformSkipMode`")

            self._transform_skip = transform_skip


    @property
    def refine_rate_distortion_cost(self):
        """Gets the refine_rate_distortion_cost of this H265VideoConfiguration.

        Enable QP based rate distortion refinement. Default is disabled.

        :return: The refine_rate_distortion_cost of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._refine_rate_distortion_cost

    @refine_rate_distortion_cost.setter
    def refine_rate_distortion_cost(self, refine_rate_distortion_cost):
        """Sets the refine_rate_distortion_cost of this H265VideoConfiguration.

        Enable QP based rate distortion refinement. Default is disabled.

        :param refine_rate_distortion_cost: The refine_rate_distortion_cost of this H265VideoConfiguration.
        :type: bool
        """

        if refine_rate_distortion_cost is not None:
            if not isinstance(refine_rate_distortion_cost, bool):
                raise TypeError("Invalid type for `refine_rate_distortion_cost`, type has to be `bool`")

            self._refine_rate_distortion_cost = refine_rate_distortion_cost


    @property
    def limit_transfer_unit_depth_recursion(self):
        """Gets the limit_transfer_unit_depth_recursion of this H265VideoConfiguration.

        Enables early exit from transfer unit depth recursion, for inter coded blocks. Default is DISABLED.

        :return: The limit_transfer_unit_depth_recursion of this H265VideoConfiguration.
        :rtype: LimitTransferUnitDepthRecursionMode
        """
        return self._limit_transfer_unit_depth_recursion

    @limit_transfer_unit_depth_recursion.setter
    def limit_transfer_unit_depth_recursion(self, limit_transfer_unit_depth_recursion):
        """Sets the limit_transfer_unit_depth_recursion of this H265VideoConfiguration.

        Enables early exit from transfer unit depth recursion, for inter coded blocks. Default is DISABLED.

        :param limit_transfer_unit_depth_recursion: The limit_transfer_unit_depth_recursion of this H265VideoConfiguration.
        :type: LimitTransferUnitDepthRecursionMode
        """

        if limit_transfer_unit_depth_recursion is not None:
            if not isinstance(limit_transfer_unit_depth_recursion, LimitTransferUnitDepthRecursionMode):
                raise TypeError("Invalid type for `limit_transfer_unit_depth_recursion`, type has to be `LimitTransferUnitDepthRecursionMode`")

            self._limit_transfer_unit_depth_recursion = limit_transfer_unit_depth_recursion


    @property
    def noise_reduction_intra(self):
        """Gets the noise_reduction_intra of this H265VideoConfiguration.

        An integer value, which denotes strength of noise reduction in intra CUs. Default 0.

        :return: The noise_reduction_intra of this H265VideoConfiguration.
        :rtype: int
        """
        return self._noise_reduction_intra

    @noise_reduction_intra.setter
    def noise_reduction_intra(self, noise_reduction_intra):
        """Sets the noise_reduction_intra of this H265VideoConfiguration.

        An integer value, which denotes strength of noise reduction in intra CUs. Default 0.

        :param noise_reduction_intra: The noise_reduction_intra of this H265VideoConfiguration.
        :type: int
        """

        if noise_reduction_intra is not None:
            if noise_reduction_intra is not None and noise_reduction_intra > 2000:
                raise ValueError("Invalid value for `noise_reduction_intra`, must be a value less than or equal to `2000`")
            if noise_reduction_intra is not None and noise_reduction_intra < 0:
                raise ValueError("Invalid value for `noise_reduction_intra`, must be a value greater than or equal to `0`")
            if not isinstance(noise_reduction_intra, int):
                raise TypeError("Invalid type for `noise_reduction_intra`, type has to be `int`")

            self._noise_reduction_intra = noise_reduction_intra


    @property
    def noise_reduction_inter(self):
        """Gets the noise_reduction_inter of this H265VideoConfiguration.

        An integer value, which denotes strength of noise reduction in inter CUs. Default 0.

        :return: The noise_reduction_inter of this H265VideoConfiguration.
        :rtype: int
        """
        return self._noise_reduction_inter

    @noise_reduction_inter.setter
    def noise_reduction_inter(self, noise_reduction_inter):
        """Sets the noise_reduction_inter of this H265VideoConfiguration.

        An integer value, which denotes strength of noise reduction in inter CUs. Default 0.

        :param noise_reduction_inter: The noise_reduction_inter of this H265VideoConfiguration.
        :type: int
        """

        if noise_reduction_inter is not None:
            if noise_reduction_inter is not None and noise_reduction_inter > 2000:
                raise ValueError("Invalid value for `noise_reduction_inter`, must be a value less than or equal to `2000`")
            if noise_reduction_inter is not None and noise_reduction_inter < 0:
                raise ValueError("Invalid value for `noise_reduction_inter`, must be a value greater than or equal to `0`")
            if not isinstance(noise_reduction_inter, int):
                raise TypeError("Invalid type for `noise_reduction_inter`, type has to be `int`")

            self._noise_reduction_inter = noise_reduction_inter


    @property
    def rate_distortion_penalty(self):
        """Gets the rate_distortion_penalty of this H265VideoConfiguration.

        Penalty for 32x32 intra transfer units in non-I slices. Default DISABLED.

        :return: The rate_distortion_penalty of this H265VideoConfiguration.
        :rtype: RateDistortionPenaltyMode
        """
        return self._rate_distortion_penalty

    @rate_distortion_penalty.setter
    def rate_distortion_penalty(self, rate_distortion_penalty):
        """Sets the rate_distortion_penalty of this H265VideoConfiguration.

        Penalty for 32x32 intra transfer units in non-I slices. Default DISABLED.

        :param rate_distortion_penalty: The rate_distortion_penalty of this H265VideoConfiguration.
        :type: RateDistortionPenaltyMode
        """

        if rate_distortion_penalty is not None:
            if not isinstance(rate_distortion_penalty, RateDistortionPenaltyMode):
                raise TypeError("Invalid type for `rate_distortion_penalty`, type has to be `RateDistortionPenaltyMode`")

            self._rate_distortion_penalty = rate_distortion_penalty


    @property
    def maximum_transfer_unit_size(self):
        """Gets the maximum_transfer_unit_size of this H265VideoConfiguration.

        Penalty for 32x32 intra transfer units in non-I slices. Default DISABLED.

        :return: The maximum_transfer_unit_size of this H265VideoConfiguration.
        :rtype: MaxTransferUnitSize
        """
        return self._maximum_transfer_unit_size

    @maximum_transfer_unit_size.setter
    def maximum_transfer_unit_size(self, maximum_transfer_unit_size):
        """Sets the maximum_transfer_unit_size of this H265VideoConfiguration.

        Penalty for 32x32 intra transfer units in non-I slices. Default DISABLED.

        :param maximum_transfer_unit_size: The maximum_transfer_unit_size of this H265VideoConfiguration.
        :type: MaxTransferUnitSize
        """

        if maximum_transfer_unit_size is not None:
            if not isinstance(maximum_transfer_unit_size, MaxTransferUnitSize):
                raise TypeError("Invalid type for `maximum_transfer_unit_size`, type has to be `MaxTransferUnitSize`")

            self._maximum_transfer_unit_size = maximum_transfer_unit_size


    @property
    def dynamic_rate_distortion_strength(self):
        """Gets the dynamic_rate_distortion_strength of this H265VideoConfiguration.

        Increases the RD level at points where quality drops due to VBV rate control enforcement. Default 0.

        :return: The dynamic_rate_distortion_strength of this H265VideoConfiguration.
        :rtype: int
        """
        return self._dynamic_rate_distortion_strength

    @dynamic_rate_distortion_strength.setter
    def dynamic_rate_distortion_strength(self, dynamic_rate_distortion_strength):
        """Sets the dynamic_rate_distortion_strength of this H265VideoConfiguration.

        Increases the RD level at points where quality drops due to VBV rate control enforcement. Default 0.

        :param dynamic_rate_distortion_strength: The dynamic_rate_distortion_strength of this H265VideoConfiguration.
        :type: int
        """

        if dynamic_rate_distortion_strength is not None:
            if dynamic_rate_distortion_strength is not None and dynamic_rate_distortion_strength > 4:
                raise ValueError("Invalid value for `dynamic_rate_distortion_strength`, must be a value less than or equal to `4`")
            if dynamic_rate_distortion_strength is not None and dynamic_rate_distortion_strength < 0:
                raise ValueError("Invalid value for `dynamic_rate_distortion_strength`, must be a value greater than or equal to `0`")
            if not isinstance(dynamic_rate_distortion_strength, int):
                raise TypeError("Invalid type for `dynamic_rate_distortion_strength`, type has to be `int`")

            self._dynamic_rate_distortion_strength = dynamic_rate_distortion_strength


    @property
    def ssim_rate_distortion_optimization(self):
        """Gets the ssim_rate_distortion_optimization of this H265VideoConfiguration.

        It is used for mode selection during analysis of CTUs and can achieve significant gain in terms of objective quality metrics SSIM and PSNR. Default false.

        :return: The ssim_rate_distortion_optimization of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._ssim_rate_distortion_optimization

    @ssim_rate_distortion_optimization.setter
    def ssim_rate_distortion_optimization(self, ssim_rate_distortion_optimization):
        """Sets the ssim_rate_distortion_optimization of this H265VideoConfiguration.

        It is used for mode selection during analysis of CTUs and can achieve significant gain in terms of objective quality metrics SSIM and PSNR. Default false.

        :param ssim_rate_distortion_optimization: The ssim_rate_distortion_optimization of this H265VideoConfiguration.
        :type: bool
        """

        if ssim_rate_distortion_optimization is not None:
            if not isinstance(ssim_rate_distortion_optimization, bool):
                raise TypeError("Invalid type for `ssim_rate_distortion_optimization`, type has to be `bool`")

            self._ssim_rate_distortion_optimization = ssim_rate_distortion_optimization


    @property
    def temporal_motion_vector_predictors(self):
        """Gets the temporal_motion_vector_predictors of this H265VideoConfiguration.

        Enable temporal motion vector predictors in P and B slices. Default true.

        :return: The temporal_motion_vector_predictors of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._temporal_motion_vector_predictors

    @temporal_motion_vector_predictors.setter
    def temporal_motion_vector_predictors(self, temporal_motion_vector_predictors):
        """Sets the temporal_motion_vector_predictors of this H265VideoConfiguration.

        Enable temporal motion vector predictors in P and B slices. Default true.

        :param temporal_motion_vector_predictors: The temporal_motion_vector_predictors of this H265VideoConfiguration.
        :type: bool
        """

        if temporal_motion_vector_predictors is not None:
            if not isinstance(temporal_motion_vector_predictors, bool):
                raise TypeError("Invalid type for `temporal_motion_vector_predictors`, type has to be `bool`")

            self._temporal_motion_vector_predictors = temporal_motion_vector_predictors


    @property
    def analyze_source_frame_pixels(self):
        """Gets the analyze_source_frame_pixels of this H265VideoConfiguration.

        Enable motion estimation with source frame pixels, in this mode, motion estimation can be computed independently. Default false.

        :return: The analyze_source_frame_pixels of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._analyze_source_frame_pixels

    @analyze_source_frame_pixels.setter
    def analyze_source_frame_pixels(self, analyze_source_frame_pixels):
        """Sets the analyze_source_frame_pixels of this H265VideoConfiguration.

        Enable motion estimation with source frame pixels, in this mode, motion estimation can be computed independently. Default false.

        :param analyze_source_frame_pixels: The analyze_source_frame_pixels of this H265VideoConfiguration.
        :type: bool
        """

        if analyze_source_frame_pixels is not None:
            if not isinstance(analyze_source_frame_pixels, bool):
                raise TypeError("Invalid type for `analyze_source_frame_pixels`, type has to be `bool`")

            self._analyze_source_frame_pixels = analyze_source_frame_pixels


    @property
    def strong_intra_smoothing(self):
        """Gets the strong_intra_smoothing of this H265VideoConfiguration.

        Enable strong intra smoothing for 32x32 intra blocks. Default true.

        :return: The strong_intra_smoothing of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._strong_intra_smoothing

    @strong_intra_smoothing.setter
    def strong_intra_smoothing(self, strong_intra_smoothing):
        """Sets the strong_intra_smoothing of this H265VideoConfiguration.

        Enable strong intra smoothing for 32x32 intra blocks. Default true.

        :param strong_intra_smoothing: The strong_intra_smoothing of this H265VideoConfiguration.
        :type: bool
        """

        if strong_intra_smoothing is not None:
            if not isinstance(strong_intra_smoothing, bool):
                raise TypeError("Invalid type for `strong_intra_smoothing`, type has to be `bool`")

            self._strong_intra_smoothing = strong_intra_smoothing


    @property
    def constrained_intra_prediction(self):
        """Gets the constrained_intra_prediction of this H265VideoConfiguration.

        When generating intra predictions for blocks in inter slices, only intra-coded reference pixels are used. Default false.

        :return: The constrained_intra_prediction of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._constrained_intra_prediction

    @constrained_intra_prediction.setter
    def constrained_intra_prediction(self, constrained_intra_prediction):
        """Sets the constrained_intra_prediction of this H265VideoConfiguration.

        When generating intra predictions for blocks in inter slices, only intra-coded reference pixels are used. Default false.

        :param constrained_intra_prediction: The constrained_intra_prediction of this H265VideoConfiguration.
        :type: bool
        """

        if constrained_intra_prediction is not None:
            if not isinstance(constrained_intra_prediction, bool):
                raise TypeError("Invalid type for `constrained_intra_prediction`, type has to be `bool`")

            self._constrained_intra_prediction = constrained_intra_prediction


    @property
    def scenecut_bias(self):
        """Gets the scenecut_bias of this H265VideoConfiguration.

        This value represents the percentage difference between the inter cost and intra cost of a frame used in scenecut detection. Default 5.0.

        :return: The scenecut_bias of this H265VideoConfiguration.
        :rtype: float
        """
        return self._scenecut_bias

    @scenecut_bias.setter
    def scenecut_bias(self, scenecut_bias):
        """Sets the scenecut_bias of this H265VideoConfiguration.

        This value represents the percentage difference between the inter cost and intra cost of a frame used in scenecut detection. Default 5.0.

        :param scenecut_bias: The scenecut_bias of this H265VideoConfiguration.
        :type: float
        """

        if scenecut_bias is not None:
            if scenecut_bias is not None and scenecut_bias > 100:
                raise ValueError("Invalid value for `scenecut_bias`, must be a value less than or equal to `100`")
            if scenecut_bias is not None and scenecut_bias < 0:
                raise ValueError("Invalid value for `scenecut_bias`, must be a value greater than or equal to `0`")
            if not isinstance(scenecut_bias, float):
                raise TypeError("Invalid type for `scenecut_bias`, type has to be `float`")

            self._scenecut_bias = scenecut_bias


    @property
    def allowed_radl_before_idr(self):
        """Gets the allowed_radl_before_idr of this H265VideoConfiguration.

        Number of RADL pictures allowed infront of IDR. Requires fixed keyframe interval. Valid values 0 - `bframes`. Default 0.

        :return: The allowed_radl_before_idr of this H265VideoConfiguration.
        :rtype: int
        """
        return self._allowed_radl_before_idr

    @allowed_radl_before_idr.setter
    def allowed_radl_before_idr(self, allowed_radl_before_idr):
        """Sets the allowed_radl_before_idr of this H265VideoConfiguration.

        Number of RADL pictures allowed infront of IDR. Requires fixed keyframe interval. Valid values 0 - `bframes`. Default 0.

        :param allowed_radl_before_idr: The allowed_radl_before_idr of this H265VideoConfiguration.
        :type: int
        """

        if allowed_radl_before_idr is not None:
            if not isinstance(allowed_radl_before_idr, int):
                raise TypeError("Invalid type for `allowed_radl_before_idr`, type has to be `int`")

            self._allowed_radl_before_idr = allowed_radl_before_idr


    @property
    def gop_lookahead(self):
        """Gets the gop_lookahead of this H265VideoConfiguration.

        Number of frames for GOP boundary decision lookahead. Valid values 0 - `rcLookahead`. Default 0

        :return: The gop_lookahead of this H265VideoConfiguration.
        :rtype: int
        """
        return self._gop_lookahead

    @gop_lookahead.setter
    def gop_lookahead(self, gop_lookahead):
        """Sets the gop_lookahead of this H265VideoConfiguration.

        Number of frames for GOP boundary decision lookahead. Valid values 0 - `rcLookahead`. Default 0

        :param gop_lookahead: The gop_lookahead of this H265VideoConfiguration.
        :type: int
        """

        if gop_lookahead is not None:
            if not isinstance(gop_lookahead, int):
                raise TypeError("Invalid type for `gop_lookahead`, type has to be `int`")

            self._gop_lookahead = gop_lookahead


    @property
    def bframe_bias(self):
        """Gets the bframe_bias of this H265VideoConfiguration.

        Bias towards B frames in slicetype decision. The higher the bias the more likely the encoder is to use B frames. Default 0

        :return: The bframe_bias of this H265VideoConfiguration.
        :rtype: int
        """
        return self._bframe_bias

    @bframe_bias.setter
    def bframe_bias(self, bframe_bias):
        """Sets the bframe_bias of this H265VideoConfiguration.

        Bias towards B frames in slicetype decision. The higher the bias the more likely the encoder is to use B frames. Default 0

        :param bframe_bias: The bframe_bias of this H265VideoConfiguration.
        :type: int
        """

        if bframe_bias is not None:
            if bframe_bias is not None and bframe_bias > 100:
                raise ValueError("Invalid value for `bframe_bias`, must be a value less than or equal to `100`")
            if bframe_bias is not None and bframe_bias < -90:
                raise ValueError("Invalid value for `bframe_bias`, must be a value greater than or equal to `-90`")
            if not isinstance(bframe_bias, int):
                raise TypeError("Invalid type for `bframe_bias`, type has to be `int`")

            self._bframe_bias = bframe_bias


    @property
    def force_flush(self):
        """Gets the force_flush of this H265VideoConfiguration.

        Force the encoder to flush frames. Default is DISABLED.

        :return: The force_flush of this H265VideoConfiguration.
        :rtype: ForceFlushMode
        """
        return self._force_flush

    @force_flush.setter
    def force_flush(self, force_flush):
        """Sets the force_flush of this H265VideoConfiguration.

        Force the encoder to flush frames. Default is DISABLED.

        :param force_flush: The force_flush of this H265VideoConfiguration.
        :type: ForceFlushMode
        """

        if force_flush is not None:
            if not isinstance(force_flush, ForceFlushMode):
                raise TypeError("Invalid type for `force_flush`, type has to be `ForceFlushMode`")

            self._force_flush = force_flush


    @property
    def adaptive_quantization_strength(self):
        """Gets the adaptive_quantization_strength of this H265VideoConfiguration.

        Adjust the strength of the adaptive quantization offsets. Default 1.0.

        :return: The adaptive_quantization_strength of this H265VideoConfiguration.
        :rtype: float
        """
        return self._adaptive_quantization_strength

    @adaptive_quantization_strength.setter
    def adaptive_quantization_strength(self, adaptive_quantization_strength):
        """Sets the adaptive_quantization_strength of this H265VideoConfiguration.

        Adjust the strength of the adaptive quantization offsets. Default 1.0.

        :param adaptive_quantization_strength: The adaptive_quantization_strength of this H265VideoConfiguration.
        :type: float
        """

        if adaptive_quantization_strength is not None:
            if adaptive_quantization_strength is not None and adaptive_quantization_strength > 3:
                raise ValueError("Invalid value for `adaptive_quantization_strength`, must be a value less than or equal to `3`")
            if adaptive_quantization_strength is not None and adaptive_quantization_strength < 0:
                raise ValueError("Invalid value for `adaptive_quantization_strength`, must be a value greater than or equal to `0`")
            if not isinstance(adaptive_quantization_strength, float):
                raise TypeError("Invalid type for `adaptive_quantization_strength`, type has to be `float`")

            self._adaptive_quantization_strength = adaptive_quantization_strength


    @property
    def adaptive_quantization_motion(self):
        """Gets the adaptive_quantization_motion of this H265VideoConfiguration.

        Adjust the AQ offsets based on the relative motion of each block with respect to the motion of the frame. Default false.

        :return: The adaptive_quantization_motion of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._adaptive_quantization_motion

    @adaptive_quantization_motion.setter
    def adaptive_quantization_motion(self, adaptive_quantization_motion):
        """Sets the adaptive_quantization_motion of this H265VideoConfiguration.

        Adjust the AQ offsets based on the relative motion of each block with respect to the motion of the frame. Default false.

        :param adaptive_quantization_motion: The adaptive_quantization_motion of this H265VideoConfiguration.
        :type: bool
        """

        if adaptive_quantization_motion is not None:
            if not isinstance(adaptive_quantization_motion, bool):
                raise TypeError("Invalid type for `adaptive_quantization_motion`, type has to be `bool`")

            self._adaptive_quantization_motion = adaptive_quantization_motion


    @property
    def quantization_group_size(self):
        """Gets the quantization_group_size of this H265VideoConfiguration.

        Enable adaptive quantization for sub-CTUs. This parameter specifies the minimum CU size at which QP can be adjusted. Default is same as `maxCTUSize`.

        :return: The quantization_group_size of this H265VideoConfiguration.
        :rtype: QuantizationGroupSize
        """
        return self._quantization_group_size

    @quantization_group_size.setter
    def quantization_group_size(self, quantization_group_size):
        """Sets the quantization_group_size of this H265VideoConfiguration.

        Enable adaptive quantization for sub-CTUs. This parameter specifies the minimum CU size at which QP can be adjusted. Default is same as `maxCTUSize`.

        :param quantization_group_size: The quantization_group_size of this H265VideoConfiguration.
        :type: QuantizationGroupSize
        """

        if quantization_group_size is not None:
            if not isinstance(quantization_group_size, QuantizationGroupSize):
                raise TypeError("Invalid type for `quantization_group_size`, type has to be `QuantizationGroupSize`")

            self._quantization_group_size = quantization_group_size


    @property
    def strict_cbr(self):
        """Gets the strict_cbr of this H265VideoConfiguration.

        Enables stricter conditions to control bitrate deviance from the target bitrate in ABR mode. Bit rate adherence is prioritised over quality. Default false.

        :return: The strict_cbr of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._strict_cbr

    @strict_cbr.setter
    def strict_cbr(self, strict_cbr):
        """Sets the strict_cbr of this H265VideoConfiguration.

        Enables stricter conditions to control bitrate deviance from the target bitrate in ABR mode. Bit rate adherence is prioritised over quality. Default false.

        :param strict_cbr: The strict_cbr of this H265VideoConfiguration.
        :type: bool
        """

        if strict_cbr is not None:
            if not isinstance(strict_cbr, bool):
                raise TypeError("Invalid type for `strict_cbr`, type has to be `bool`")

            self._strict_cbr = strict_cbr


    @property
    def qp_offset_chroma_cb(self):
        """Gets the qp_offset_chroma_cb of this H265VideoConfiguration.

        Offset of Cb chroma QP from the luma QP selected by rate control. This is a general way to spend more or less bits on the chroma channel. Default 0

        :return: The qp_offset_chroma_cb of this H265VideoConfiguration.
        :rtype: int
        """
        return self._qp_offset_chroma_cb

    @qp_offset_chroma_cb.setter
    def qp_offset_chroma_cb(self, qp_offset_chroma_cb):
        """Sets the qp_offset_chroma_cb of this H265VideoConfiguration.

        Offset of Cb chroma QP from the luma QP selected by rate control. This is a general way to spend more or less bits on the chroma channel. Default 0

        :param qp_offset_chroma_cb: The qp_offset_chroma_cb of this H265VideoConfiguration.
        :type: int
        """

        if qp_offset_chroma_cb is not None:
            if qp_offset_chroma_cb is not None and qp_offset_chroma_cb > 12:
                raise ValueError("Invalid value for `qp_offset_chroma_cb`, must be a value less than or equal to `12`")
            if qp_offset_chroma_cb is not None and qp_offset_chroma_cb < -12:
                raise ValueError("Invalid value for `qp_offset_chroma_cb`, must be a value greater than or equal to `-12`")
            if not isinstance(qp_offset_chroma_cb, int):
                raise TypeError("Invalid type for `qp_offset_chroma_cb`, type has to be `int`")

            self._qp_offset_chroma_cb = qp_offset_chroma_cb


    @property
    def qp_offset_chroma_cr(self):
        """Gets the qp_offset_chroma_cr of this H265VideoConfiguration.

        Offset of Cr chroma QP from the luma QP selected by rate control. This is a general way to spend more or less bits on the chroma channel. Default 0

        :return: The qp_offset_chroma_cr of this H265VideoConfiguration.
        :rtype: int
        """
        return self._qp_offset_chroma_cr

    @qp_offset_chroma_cr.setter
    def qp_offset_chroma_cr(self, qp_offset_chroma_cr):
        """Sets the qp_offset_chroma_cr of this H265VideoConfiguration.

        Offset of Cr chroma QP from the luma QP selected by rate control. This is a general way to spend more or less bits on the chroma channel. Default 0

        :param qp_offset_chroma_cr: The qp_offset_chroma_cr of this H265VideoConfiguration.
        :type: int
        """

        if qp_offset_chroma_cr is not None:
            if qp_offset_chroma_cr is not None and qp_offset_chroma_cr > 12:
                raise ValueError("Invalid value for `qp_offset_chroma_cr`, must be a value less than or equal to `12`")
            if qp_offset_chroma_cr is not None and qp_offset_chroma_cr < -12:
                raise ValueError("Invalid value for `qp_offset_chroma_cr`, must be a value greater than or equal to `-12`")
            if not isinstance(qp_offset_chroma_cr, int):
                raise TypeError("Invalid type for `qp_offset_chroma_cr`, type has to be `int`")

            self._qp_offset_chroma_cr = qp_offset_chroma_cr


    @property
    def ip_ratio(self):
        """Gets the ip_ratio of this H265VideoConfiguration.

        QP ratio factor between I and P slices. This ratio is used in all of the rate control modes. Default 1.4

        :return: The ip_ratio of this H265VideoConfiguration.
        :rtype: float
        """
        return self._ip_ratio

    @ip_ratio.setter
    def ip_ratio(self, ip_ratio):
        """Sets the ip_ratio of this H265VideoConfiguration.

        QP ratio factor between I and P slices. This ratio is used in all of the rate control modes. Default 1.4

        :param ip_ratio: The ip_ratio of this H265VideoConfiguration.
        :type: float
        """

        if ip_ratio is not None:
            if not isinstance(ip_ratio, float):
                raise TypeError("Invalid type for `ip_ratio`, type has to be `float`")

            self._ip_ratio = ip_ratio


    @property
    def pb_ratio(self):
        """Gets the pb_ratio of this H265VideoConfiguration.

        QP ratio factor between P and B slices. This ratio is used in all of the rate control modes. Default 1.3

        :return: The pb_ratio of this H265VideoConfiguration.
        :rtype: float
        """
        return self._pb_ratio

    @pb_ratio.setter
    def pb_ratio(self, pb_ratio):
        """Sets the pb_ratio of this H265VideoConfiguration.

        QP ratio factor between P and B slices. This ratio is used in all of the rate control modes. Default 1.3

        :param pb_ratio: The pb_ratio of this H265VideoConfiguration.
        :type: float
        """

        if pb_ratio is not None:
            if not isinstance(pb_ratio, float):
                raise TypeError("Invalid type for `pb_ratio`, type has to be `float`")

            self._pb_ratio = pb_ratio


    @property
    def quantizer_curve_compression_factor(self):
        """Gets the quantizer_curve_compression_factor of this H265VideoConfiguration.

        Sets the quantizer curve compression factor. It weights the frame quantizer based on the complexity of residual (measured by lookahead). Default 0.6

        :return: The quantizer_curve_compression_factor of this H265VideoConfiguration.
        :rtype: float
        """
        return self._quantizer_curve_compression_factor

    @quantizer_curve_compression_factor.setter
    def quantizer_curve_compression_factor(self, quantizer_curve_compression_factor):
        """Sets the quantizer_curve_compression_factor of this H265VideoConfiguration.

        Sets the quantizer curve compression factor. It weights the frame quantizer based on the complexity of residual (measured by lookahead). Default 0.6

        :param quantizer_curve_compression_factor: The quantizer_curve_compression_factor of this H265VideoConfiguration.
        :type: float
        """

        if quantizer_curve_compression_factor is not None:
            if quantizer_curve_compression_factor is not None and quantizer_curve_compression_factor > 1:
                raise ValueError("Invalid value for `quantizer_curve_compression_factor`, must be a value less than or equal to `1`")
            if quantizer_curve_compression_factor is not None and quantizer_curve_compression_factor < 0.5:
                raise ValueError("Invalid value for `quantizer_curve_compression_factor`, must be a value greater than or equal to `0.5`")
            if not isinstance(quantizer_curve_compression_factor, float):
                raise TypeError("Invalid type for `quantizer_curve_compression_factor`, type has to be `float`")

            self._quantizer_curve_compression_factor = quantizer_curve_compression_factor


    @property
    def qp_step(self):
        """Gets the qp_step of this H265VideoConfiguration.

        The maximum single adjustment in QP allowed to rate control. Default 4

        :return: The qp_step of this H265VideoConfiguration.
        :rtype: int
        """
        return self._qp_step

    @qp_step.setter
    def qp_step(self, qp_step):
        """Sets the qp_step of this H265VideoConfiguration.

        The maximum single adjustment in QP allowed to rate control. Default 4

        :param qp_step: The qp_step of this H265VideoConfiguration.
        :type: int
        """

        if qp_step is not None:
            if not isinstance(qp_step, int):
                raise TypeError("Invalid type for `qp_step`, type has to be `int`")

            self._qp_step = qp_step


    @property
    def grain_optimized_rate_control(self):
        """Gets the grain_optimized_rate_control of this H265VideoConfiguration.

        Enables a specialised ratecontrol algorithm for film grain content. Default false.

        :return: The grain_optimized_rate_control of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._grain_optimized_rate_control

    @grain_optimized_rate_control.setter
    def grain_optimized_rate_control(self, grain_optimized_rate_control):
        """Sets the grain_optimized_rate_control of this H265VideoConfiguration.

        Enables a specialised ratecontrol algorithm for film grain content. Default false.

        :param grain_optimized_rate_control: The grain_optimized_rate_control of this H265VideoConfiguration.
        :type: bool
        """

        if grain_optimized_rate_control is not None:
            if not isinstance(grain_optimized_rate_control, bool):
                raise TypeError("Invalid type for `grain_optimized_rate_control`, type has to be `bool`")

            self._grain_optimized_rate_control = grain_optimized_rate_control


    @property
    def blur_quants(self):
        """Gets the blur_quants of this H265VideoConfiguration.

        Temporally blur quants. Default 0.5

        :return: The blur_quants of this H265VideoConfiguration.
        :rtype: float
        """
        return self._blur_quants

    @blur_quants.setter
    def blur_quants(self, blur_quants):
        """Sets the blur_quants of this H265VideoConfiguration.

        Temporally blur quants. Default 0.5

        :param blur_quants: The blur_quants of this H265VideoConfiguration.
        :type: float
        """

        if blur_quants is not None:
            if not isinstance(blur_quants, float):
                raise TypeError("Invalid type for `blur_quants`, type has to be `float`")

            self._blur_quants = blur_quants


    @property
    def blur_complexity(self):
        """Gets the blur_complexity of this H265VideoConfiguration.

        Temporally blur complexity. Default 20.0

        :return: The blur_complexity of this H265VideoConfiguration.
        :rtype: float
        """
        return self._blur_complexity

    @blur_complexity.setter
    def blur_complexity(self, blur_complexity):
        """Sets the blur_complexity of this H265VideoConfiguration.

        Temporally blur complexity. Default 20.0

        :param blur_complexity: The blur_complexity of this H265VideoConfiguration.
        :type: float
        """

        if blur_complexity is not None:
            if not isinstance(blur_complexity, float):
                raise TypeError("Invalid type for `blur_complexity`, type has to be `float`")

            self._blur_complexity = blur_complexity


    @property
    def sao_non_deblock(self):
        """Gets the sao_non_deblock of this H265VideoConfiguration.

        Specify how to handle depencency between SAO and deblocking filter. When enabled, non-deblocked pixels are used for SAO analysis. When disabled, SAO analysis skips the right/bottom boundary areas. Default false.

        :return: The sao_non_deblock of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._sao_non_deblock

    @sao_non_deblock.setter
    def sao_non_deblock(self, sao_non_deblock):
        """Sets the sao_non_deblock of this H265VideoConfiguration.

        Specify how to handle depencency between SAO and deblocking filter. When enabled, non-deblocked pixels are used for SAO analysis. When disabled, SAO analysis skips the right/bottom boundary areas. Default false.

        :param sao_non_deblock: The sao_non_deblock of this H265VideoConfiguration.
        :type: bool
        """

        if sao_non_deblock is not None:
            if not isinstance(sao_non_deblock, bool):
                raise TypeError("Invalid type for `sao_non_deblock`, type has to be `bool`")

            self._sao_non_deblock = sao_non_deblock


    @property
    def limit_sao(self):
        """Gets the limit_sao of this H265VideoConfiguration.

        Limit SAO filter computation by early terminating SAO process based on inter prediction mode, CTU spatial-domain correlations, and relations between luma and chroma. Default false.

        :return: The limit_sao of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._limit_sao

    @limit_sao.setter
    def limit_sao(self, limit_sao):
        """Sets the limit_sao of this H265VideoConfiguration.

        Limit SAO filter computation by early terminating SAO process based on inter prediction mode, CTU spatial-domain correlations, and relations between luma and chroma. Default false.

        :param limit_sao: The limit_sao of this H265VideoConfiguration.
        :type: bool
        """

        if limit_sao is not None:
            if not isinstance(limit_sao, bool):
                raise TypeError("Invalid type for `limit_sao`, type has to be `bool`")

            self._limit_sao = limit_sao


    @property
    def lowpass_dct(self):
        """Gets the lowpass_dct of this H265VideoConfiguration.

        Will use low-pass subband dct approximation instead of the standard dct for 16x16 and 32x32 blocks. Default false.

        :return: The lowpass_dct of this H265VideoConfiguration.
        :rtype: bool
        """
        return self._lowpass_dct

    @lowpass_dct.setter
    def lowpass_dct(self, lowpass_dct):
        """Sets the lowpass_dct of this H265VideoConfiguration.

        Will use low-pass subband dct approximation instead of the standard dct for 16x16 and 32x32 blocks. Default false.

        :param lowpass_dct: The lowpass_dct of this H265VideoConfiguration.
        :type: bool
        """

        if lowpass_dct is not None:
            if not isinstance(lowpass_dct, bool):
                raise TypeError("Invalid type for `lowpass_dct`, type has to be `bool`")

            self._lowpass_dct = lowpass_dct

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(H265VideoConfiguration, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(H265VideoConfiguration, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, H265VideoConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
