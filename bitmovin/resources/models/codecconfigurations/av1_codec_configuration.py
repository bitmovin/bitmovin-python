from bitmovin.resources.enums import AV1KeyPlacementMode
from bitmovin.resources.enums import AV1RateControlMode
from bitmovin.resources.enums import AV1AdaptiveQuantMode
from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable

from .video_codec_configuration import VideoCodecConfiguration
from .color_config import ColorConfig


class AV1CodecConfiguration(VideoCodecConfiguration, Serializable):

    def __init__(self, name, bitrate, rate, id_=None, width=None, height=None, description=None, custom_data=None,
                 pixel_format=None, color_config=None, key_placement_mode=None, rate_control_mode=None,
                 sample_aspect_ratio_numerator=None, sample_aspect_ratio_denominator=None, adaptive_quant_mode=None,
                 lag_in_frames=None, min_q=None, max_q=None, undershoot_pct=None, overshoot_pct=None,
                 client_buffer_size=None, client_initial_buffer_size=None, client_optimal_buffer_size=None,
                 tile_columns=None, tile_rows=None, automatic_alt_ref_frames_enabled=None, arnr_max_frames=None,
                 arnr_strength=None, cq_level=None, max_intra_rate=None, max_inter_rate=None, gf_cbr_boost=None,
                 lossless=None, frame_parallel=None, sharpness=None, frame_boost_enabled=None,
                 noise_sensitivity=None, min_gf_interval=None, max_gf_interval=None, num_tile_groups=None,
                 mtu_size=None):

        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description, bitrate=bitrate,
                         rate=rate, width=width, height=height, pixel_format=pixel_format)

        self._colorConfig = None
        self._keyPlacementMode = None
        self._rateControlMode = None
        self._adaptiveQuantMode = None

        self.colorConfig = color_config
        self.keyPlacementMode = key_placement_mode
        self.rateControlMode = rate_control_mode
        self.sampleAspectRatioNumerator = sample_aspect_ratio_numerator
        self.sampleAspectRatioDenominator = sample_aspect_ratio_denominator
        self.adaptiveQuantMode = adaptive_quant_mode
        self.lagInFrames = lag_in_frames
        self.minQ = min_q
        self.maxQ = max_q
        self.undershootPct = undershoot_pct
        self.overshootPct = overshoot_pct
        self.clientBufferSize = client_buffer_size
        self.clientInitialBufferSize = client_initial_buffer_size
        self.clientOptimalBufferSize = client_optimal_buffer_size
        self.tileColumns = tile_columns
        self.tileRows = tile_rows
        self.automaticAltRefFramesEnabled = automatic_alt_ref_frames_enabled
        self.arnrMaxFrames = arnr_max_frames
        self.arnrStrength = arnr_strength
        self.cqLevel = cq_level
        self.maxIntraRate = max_intra_rate
        self.maxInterRate = max_inter_rate
        self.gfCbrBoost = gf_cbr_boost
        self.lossless = lossless
        self.frameParallel = frame_parallel
        self.sharpness = sharpness
        self.frameBoostEnabled = frame_boost_enabled
        self.noiseSensitivity = noise_sensitivity
        self.minGfInterval = min_gf_interval
        self.maxGfInterval = max_gf_interval
        self.numTileGroups = num_tile_groups
        self.mtuSize = mtu_size

    @property
    def colorConfig(self):
        return self._colorConfig

    @colorConfig.setter
    def colorConfig(self, new_color_config):
        if new_color_config is None:
            self._colorConfig = None
        elif isinstance(new_color_config, ColorConfig):
            self._colorConfig = new_color_config
        else:
            raise InvalidTypeError('colorConfig has to be of type ColorConfig')

    @property
    def keyPlacementMode(self):
        return self._keyPlacementMode

    @keyPlacementMode.setter
    def keyPlacementMode(self, new_key_placement_mode):
        if new_key_placement_mode is None:
            return
        if isinstance(new_key_placement_mode, str):
            self._keyPlacementMode = new_key_placement_mode
        elif isinstance(new_key_placement_mode, AV1KeyPlacementMode):
            self._keyPlacementMode = new_key_placement_mode.value
        else:
            raise InvalidTypeError('Invalid type {} for keyPlacementMode: must be either str or AV1KeyPlacementMode.'
                                   .format(type(new_key_placement_mode)))

    @property
    def rateControlMode(self):
        return self._rateControlMode

    @rateControlMode.setter
    def rateControlMode(self, new_rate_control_mode):
        if new_rate_control_mode is None:
            return
        if isinstance(new_rate_control_mode, str):
            self._rateControlMode = new_rate_control_mode
        elif isinstance(new_rate_control_mode, AV1RateControlMode):
            self._rateControlMode = new_rate_control_mode.value
        else:
            raise InvalidTypeError('Invalid type {} for rateControlMode: must be either str or AV1RateControlMode.'
                                   .format(type(new_rate_control_mode)))

    @property
    def adaptiveQuantMode(self):
        return self._adaptiveQuantMode

    @adaptiveQuantMode.setter
    def adaptiveQuantMode(self, new_adaptive_quant_mode):
        if new_adaptive_quant_mode is None:
            return
        if isinstance(new_adaptive_quant_mode, str):
            self._adaptiveQuantMode = new_adaptive_quant_mode
        elif isinstance(new_adaptive_quant_mode, AV1AdaptiveQuantMode):
            self._adaptiveQuantMode = new_adaptive_quant_mode.value
        else:
            raise InvalidTypeError('Invalid type {} for adaptiveQuantMode: must be either str or AV1AdaptiveQuantMode.'
                                   .format(type(new_adaptive_quant_mode)))

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
        pixel_format = video_codec_configuration.pixelFormat

        key_placement_mode = json_object.get('keyPlacementMode')
        rate_control_mode = json_object.get('rateControlMode')
        sample_aspect_ratio_numerator = json_object.get('sampleAspectRatioNumerator')
        sample_aspect_ratio_denominator = json_object.get('sampleAspectRatioDenominator')
        adaptive_quant_mode = json_object.get('adaptiveQuantMode')
        lag_in_frames = json_object.get('lagInFrames')
        min_q = json_object.get('minQ')
        max_q = json_object.get('maxQ')
        undershoot_pct = json_object.get('undershootPct')
        overshoot_pct = json_object.get('overshootPct')
        client_buffer_size = json_object.get('clientBufferSize')
        client_initial_buffer_size = json_object.get('clientInitialBufferSize')
        client_optimal_buffer_size = json_object.get('clientOptimalBufferSize')
        tile_columns = json_object.get('tileColumns')
        tile_rows = json_object.get('tileRows')
        automatic_alt_ref_frames_enabled = json_object.get('automaticAltRefFramesEnabled')
        arnr_max_frames = json_object.get('arnrMaxFrames')
        arnr_strength = json_object.get('arnrStrength')
        cq_level = json_object.get('cqLevel')
        max_intra_rate = json_object.get('maxIntraRate')
        max_inter_rate = json_object.get('maxInterRate')
        gf_cbr_boost = json_object.get('gfCbrBoost')
        lossless = json_object.get('lossless')
        frame_parallel = json_object.get('frameParallel')
        sharpness = json_object.get('sharpness')
        frame_boost_enabled = json_object.get('frameBoostEnabled')
        noise_sensitivity = json_object.get('noiseSensitivity')
        min_gf_interval = json_object.get('minGfInterval')
        max_gf_interval = json_object.get('maxGfInterval')
        num_tile_groups = json_object.get('numTileGroups')
        mtu_size = json_object.get('mtuSize')

        color_config = None
        color_config_json = json_object.get('colorConfig')
        if color_config_json is not None:

            copy_chroma_location_flag = color_config_json.get('copyChromaLocationFlag')
            copy_color_space_flag = color_config_json.get('copyColorSpaceFlag')
            copy_color_primaries_flag = color_config_json.get('copyColorPrimariesFlag')
            copy_color_range_flag = color_config_json.get('copyColorRangeFlag')
            copy_color_transfer_flag = color_config_json.get('copyColorTransferFlag')
            chroma_location = color_config_json.get('chromaLocation')
            color_space = color_config_json.get('colorSpace')
            color_primaries = color_config_json.get('colorPrimaries')
            color_range = color_config_json.get('colorRange')
            color_transfer = color_config_json.get('colorTransfer')
            input_color_space = color_config_json.get('inputColorSpace')
            input_color_range = color_config_json.get('inputColorRange')
            color_config = ColorConfig(copy_chroma_location_flag=copy_chroma_location_flag,
                                       copy_color_space_flag=copy_color_space_flag,
                                       copy_color_primaries_flag=copy_color_primaries_flag,
                                       copy_color_range_flag=copy_color_range_flag,
                                       copy_color_transfer_flag=copy_color_transfer_flag,
                                       chroma_location=chroma_location, color_space=color_space,
                                       color_primaries=color_primaries, color_range=color_range,
                                       color_transfer=color_transfer, input_color_space=input_color_space,
                                       input_color_range=input_color_range)

        av1_codec_configuration = AV1CodecConfiguration(name=name, bitrate=bitrate, rate=rate, id_=id_,
                                                        description=description, custom_data=custom_data,
                                                        width=width, height=height, pixel_format=pixel_format,
                                                        color_config=color_config,
                                                        key_placement_mode=key_placement_mode,
                                                        rate_control_mode=rate_control_mode,
                                                        sample_aspect_ratio_numerator=sample_aspect_ratio_numerator,
                                                        sample_aspect_ratio_denominator=sample_aspect_ratio_denominator,
                                                        adaptive_quant_mode=adaptive_quant_mode,
                                                        lag_in_frames=lag_in_frames,
                                                        min_q=min_q,
                                                        max_q=max_q,
                                                        undershoot_pct=undershoot_pct,
                                                        overshoot_pct=overshoot_pct,
                                                        client_buffer_size=client_buffer_size,
                                                        client_initial_buffer_size=client_initial_buffer_size,
                                                        client_optimal_buffer_size=client_optimal_buffer_size,
                                                        tile_columns=tile_columns,
                                                        tile_rows=tile_rows,
                                                        automatic_alt_ref_frames_enabled=
                                                        automatic_alt_ref_frames_enabled,
                                                        arnr_max_frames=arnr_max_frames,
                                                        arnr_strength=arnr_strength,
                                                        cq_level=cq_level,
                                                        max_intra_rate=max_intra_rate,
                                                        max_inter_rate=max_inter_rate,
                                                        gf_cbr_boost=gf_cbr_boost,
                                                        lossless=lossless,
                                                        frame_parallel=frame_parallel,
                                                        sharpness=sharpness,
                                                        frame_boost_enabled=frame_boost_enabled,
                                                        noise_sensitivity=noise_sensitivity,
                                                        min_gf_interval=min_gf_interval,
                                                        max_gf_interval=max_gf_interval,
                                                        num_tile_groups=num_tile_groups,
                                                        mtu_size=mtu_size
                                                        )

        return av1_codec_configuration

    def serialize(self):
        serialized = super().serialize()
        serialized['keyPlacementMode'] = self.keyPlacementMode
        serialized['rateControlMode'] = self.rateControlMode
        serialized['sampleAspectRatioNumerator'] = self.sampleAspectRatioNumerator
        serialized['sampleAspectRatioDenominator'] = self.sampleAspectRatioDenominator
        serialized['adaptiveQuantMode'] = self.adaptiveQuantMode
        serialized['lagInFrames'] = self.lagInFrames
        serialized['minQ'] = self.minQ
        serialized['maxQ'] = self.maxQ
        serialized['undershootPct'] = self.undershootPct
        serialized['overshootPct'] = self.overshootPct
        serialized['clientBufferSize'] = self.clientBufferSize
        serialized['clientInitialBufferSize'] = self.clientInitialBufferSize
        serialized['clientOptimalBufferSize'] = self.clientOptimalBufferSize
        serialized['tileColumns'] = self.tileColumns
        serialized['tileRows'] = self.tileRows
        serialized['automaticAltRefFramesEnabled'] = self.automaticAltRefFramesEnabled
        serialized['arnrMaxFrames'] = self.arnrMaxFrames
        serialized['arnrStrength'] = self.arnrStrength
        serialized['cqLevel'] = self.cqLevel
        serialized['maxIntraRate'] = self.maxIntraRate
        serialized['maxInterRate'] = self.maxInterRate
        serialized['gfCbrBoost'] = self.gfCbrBoost
        serialized['lossless'] = self.lossless
        serialized['frameParallel'] = self.frameParallel
        serialized['sharpness'] = self.sharpness
        serialized['frameBoostEnabled'] = self.frameBoostEnabled
        serialized['noiseSensitivity'] = self.noiseSensitivity
        serialized['minGfInterval'] = self.minGfInterval
        serialized['maxGfInterval'] = self.maxGfInterval
        serialized['numTileGroups'] = self.numTileGroups
        serialized['mtuSize'] = self.mtuSize

        if isinstance(self.colorConfig, ColorConfig):
            serialized['colorConfig'] = self.colorConfig.serialize()

        return serialized
