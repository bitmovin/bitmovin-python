# coding: utf-8

from bitmovin_python.models.av1_adaptive_quant_mode import Av1AdaptiveQuantMode
from bitmovin_python.models.av1_key_placement_mode import Av1KeyPlacementMode
from bitmovin_python.models.codec_config_type import CodecConfigType
from bitmovin_python.models.color_config import ColorConfig
from bitmovin_python.models.encoding_mode import EncodingMode
from bitmovin_python.models.pixel_format import PixelFormat
from bitmovin_python.models.video_configuration import VideoConfiguration
import pprint
import six
from datetime import datetime
from enum import Enum


class Av1VideoConfiguration(VideoConfiguration):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Av1VideoConfiguration, self).openapi_types
        types.update({
            'key_placement_mode': 'Av1KeyPlacementMode',
            'adaptive_quant_mode': 'Av1AdaptiveQuantMode',
            'lag_in_frames': 'int',
            'min_q': 'int',
            'max_q': 'int',
            'undershoot_pct': 'int',
            'overshoot_pct': 'int',
            'client_buffer_size': 'int',
            'client_initial_buffer_size': 'int',
            'client_optimal_buffer_size': 'int',
            'tile_columns': 'int',
            'tile_rows': 'int',
            'is_automatic_alt_ref_frames_enabled': 'bool',
            'arnr_max_frames': 'int',
            'arnr_strength': 'int',
            'max_intra_rate': 'int',
            'is_lossless': 'bool',
            'is_frame_parallel': 'bool',
            'sharpness': 'int',
            'is_frame_boost_enabled': 'bool',
            'noise_sensitivity': 'bool',
            'min_gf_interval': 'int',
            'max_gf_interval': 'int',
            'num_tile_groups': 'int',
            'mtu_size': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Av1VideoConfiguration, self).attribute_map
        attributes.update({
            'key_placement_mode': 'keyPlacementMode',
            'adaptive_quant_mode': 'adaptiveQuantMode',
            'lag_in_frames': 'lagInFrames',
            'min_q': 'minQ',
            'max_q': 'maxQ',
            'undershoot_pct': 'undershootPct',
            'overshoot_pct': 'overshootPct',
            'client_buffer_size': 'clientBufferSize',
            'client_initial_buffer_size': 'clientInitialBufferSize',
            'client_optimal_buffer_size': 'clientOptimalBufferSize',
            'tile_columns': 'tileColumns',
            'tile_rows': 'tileRows',
            'is_automatic_alt_ref_frames_enabled': 'isAutomaticAltRefFramesEnabled',
            'arnr_max_frames': 'arnrMaxFrames',
            'arnr_strength': 'arnrStrength',
            'max_intra_rate': 'maxIntraRate',
            'is_lossless': 'isLossless',
            'is_frame_parallel': 'isFrameParallel',
            'sharpness': 'sharpness',
            'is_frame_boost_enabled': 'isFrameBoostEnabled',
            'noise_sensitivity': 'noiseSensitivity',
            'min_gf_interval': 'minGfInterval',
            'max_gf_interval': 'maxGfInterval',
            'num_tile_groups': 'numTileGroups',
            'mtu_size': 'mtuSize'
        })
        return attributes

    def __init__(self, key_placement_mode=None, adaptive_quant_mode=None, lag_in_frames=None, min_q=None, max_q=None, undershoot_pct=None, overshoot_pct=None, client_buffer_size=None, client_initial_buffer_size=None, client_optimal_buffer_size=None, tile_columns=None, tile_rows=None, is_automatic_alt_ref_frames_enabled=None, arnr_max_frames=None, arnr_strength=None, max_intra_rate=None, is_lossless=None, is_frame_parallel=None, sharpness=None, is_frame_boost_enabled=None, noise_sensitivity=None, min_gf_interval=None, max_gf_interval=None, num_tile_groups=None, mtu_size=None, *args, **kwargs):
        super(Av1VideoConfiguration, self).__init__(*args, **kwargs)

        self._key_placement_mode = None
        self._adaptive_quant_mode = None
        self._lag_in_frames = None
        self._min_q = None
        self._max_q = None
        self._undershoot_pct = None
        self._overshoot_pct = None
        self._client_buffer_size = None
        self._client_initial_buffer_size = None
        self._client_optimal_buffer_size = None
        self._tile_columns = None
        self._tile_rows = None
        self._is_automatic_alt_ref_frames_enabled = None
        self._arnr_max_frames = None
        self._arnr_strength = None
        self._max_intra_rate = None
        self._is_lossless = None
        self._is_frame_parallel = None
        self._sharpness = None
        self._is_frame_boost_enabled = None
        self._noise_sensitivity = None
        self._min_gf_interval = None
        self._max_gf_interval = None
        self._num_tile_groups = None
        self._mtu_size = None
        self.discriminator = None

        if key_placement_mode is not None:
            self.key_placement_mode = key_placement_mode
        if adaptive_quant_mode is not None:
            self.adaptive_quant_mode = adaptive_quant_mode
        if lag_in_frames is not None:
            self.lag_in_frames = lag_in_frames
        if min_q is not None:
            self.min_q = min_q
        if max_q is not None:
            self.max_q = max_q
        if undershoot_pct is not None:
            self.undershoot_pct = undershoot_pct
        if overshoot_pct is not None:
            self.overshoot_pct = overshoot_pct
        if client_buffer_size is not None:
            self.client_buffer_size = client_buffer_size
        if client_initial_buffer_size is not None:
            self.client_initial_buffer_size = client_initial_buffer_size
        if client_optimal_buffer_size is not None:
            self.client_optimal_buffer_size = client_optimal_buffer_size
        if tile_columns is not None:
            self.tile_columns = tile_columns
        if tile_rows is not None:
            self.tile_rows = tile_rows
        if is_automatic_alt_ref_frames_enabled is not None:
            self.is_automatic_alt_ref_frames_enabled = is_automatic_alt_ref_frames_enabled
        if arnr_max_frames is not None:
            self.arnr_max_frames = arnr_max_frames
        if arnr_strength is not None:
            self.arnr_strength = arnr_strength
        if max_intra_rate is not None:
            self.max_intra_rate = max_intra_rate
        if is_lossless is not None:
            self.is_lossless = is_lossless
        if is_frame_parallel is not None:
            self.is_frame_parallel = is_frame_parallel
        if sharpness is not None:
            self.sharpness = sharpness
        if is_frame_boost_enabled is not None:
            self.is_frame_boost_enabled = is_frame_boost_enabled
        if noise_sensitivity is not None:
            self.noise_sensitivity = noise_sensitivity
        if min_gf_interval is not None:
            self.min_gf_interval = min_gf_interval
        if max_gf_interval is not None:
            self.max_gf_interval = max_gf_interval
        if num_tile_groups is not None:
            self.num_tile_groups = num_tile_groups
        if mtu_size is not None:
            self.mtu_size = mtu_size

    @property
    def key_placement_mode(self):
        """Gets the key_placement_mode of this Av1VideoConfiguration.


        :return: The key_placement_mode of this Av1VideoConfiguration.
        :rtype: Av1KeyPlacementMode
        """
        return self._key_placement_mode

    @key_placement_mode.setter
    def key_placement_mode(self, key_placement_mode):
        """Sets the key_placement_mode of this Av1VideoConfiguration.


        :param key_placement_mode: The key_placement_mode of this Av1VideoConfiguration.
        :type: Av1KeyPlacementMode
        """

        if key_placement_mode is not None:
            if not isinstance(key_placement_mode, Av1KeyPlacementMode):
                raise TypeError("Invalid type for `key_placement_mode`, type has to be `Av1KeyPlacementMode`")

            self._key_placement_mode = key_placement_mode


    @property
    def adaptive_quant_mode(self):
        """Gets the adaptive_quant_mode of this Av1VideoConfiguration.


        :return: The adaptive_quant_mode of this Av1VideoConfiguration.
        :rtype: Av1AdaptiveQuantMode
        """
        return self._adaptive_quant_mode

    @adaptive_quant_mode.setter
    def adaptive_quant_mode(self, adaptive_quant_mode):
        """Sets the adaptive_quant_mode of this Av1VideoConfiguration.


        :param adaptive_quant_mode: The adaptive_quant_mode of this Av1VideoConfiguration.
        :type: Av1AdaptiveQuantMode
        """

        if adaptive_quant_mode is not None:
            if not isinstance(adaptive_quant_mode, Av1AdaptiveQuantMode):
                raise TypeError("Invalid type for `adaptive_quant_mode`, type has to be `Av1AdaptiveQuantMode`")

            self._adaptive_quant_mode = adaptive_quant_mode


    @property
    def lag_in_frames(self):
        """Gets the lag_in_frames of this Av1VideoConfiguration.

        Number of frames to look ahead for alternate reference frame selection

        :return: The lag_in_frames of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._lag_in_frames

    @lag_in_frames.setter
    def lag_in_frames(self, lag_in_frames):
        """Sets the lag_in_frames of this Av1VideoConfiguration.

        Number of frames to look ahead for alternate reference frame selection

        :param lag_in_frames: The lag_in_frames of this Av1VideoConfiguration.
        :type: int
        """

        if lag_in_frames is not None:
            if lag_in_frames is not None and lag_in_frames > 25:
                raise ValueError("Invalid value for `lag_in_frames`, must be a value less than or equal to `25`")
            if lag_in_frames is not None and lag_in_frames < 0:
                raise ValueError("Invalid value for `lag_in_frames`, must be a value greater than or equal to `0`")
            if not isinstance(lag_in_frames, int):
                raise TypeError("Invalid type for `lag_in_frames`, type has to be `int`")

            self._lag_in_frames = lag_in_frames


    @property
    def min_q(self):
        """Gets the min_q of this Av1VideoConfiguration.

        Minimum (best quality) quantizer

        :return: The min_q of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._min_q

    @min_q.setter
    def min_q(self, min_q):
        """Sets the min_q of this Av1VideoConfiguration.

        Minimum (best quality) quantizer

        :param min_q: The min_q of this Av1VideoConfiguration.
        :type: int
        """

        if min_q is not None:
            if not isinstance(min_q, int):
                raise TypeError("Invalid type for `min_q`, type has to be `int`")

            self._min_q = min_q


    @property
    def max_q(self):
        """Gets the max_q of this Av1VideoConfiguration.

        Maximum (worst quality) quantizer

        :return: The max_q of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._max_q

    @max_q.setter
    def max_q(self, max_q):
        """Sets the max_q of this Av1VideoConfiguration.

        Maximum (worst quality) quantizer

        :param max_q: The max_q of this Av1VideoConfiguration.
        :type: int
        """

        if max_q is not None:
            if not isinstance(max_q, int):
                raise TypeError("Invalid type for `max_q`, type has to be `int`")

            self._max_q = max_q


    @property
    def undershoot_pct(self):
        """Gets the undershoot_pct of this Av1VideoConfiguration.

        Rate control adaptation undershoot control

        :return: The undershoot_pct of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._undershoot_pct

    @undershoot_pct.setter
    def undershoot_pct(self, undershoot_pct):
        """Sets the undershoot_pct of this Av1VideoConfiguration.

        Rate control adaptation undershoot control

        :param undershoot_pct: The undershoot_pct of this Av1VideoConfiguration.
        :type: int
        """

        if undershoot_pct is not None:
            if undershoot_pct is not None and undershoot_pct > 1000:
                raise ValueError("Invalid value for `undershoot_pct`, must be a value less than or equal to `1000`")
            if undershoot_pct is not None and undershoot_pct < 0:
                raise ValueError("Invalid value for `undershoot_pct`, must be a value greater than or equal to `0`")
            if not isinstance(undershoot_pct, int):
                raise TypeError("Invalid type for `undershoot_pct`, type has to be `int`")

            self._undershoot_pct = undershoot_pct


    @property
    def overshoot_pct(self):
        """Gets the overshoot_pct of this Av1VideoConfiguration.

        Rate control adaptation overshoot control

        :return: The overshoot_pct of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._overshoot_pct

    @overshoot_pct.setter
    def overshoot_pct(self, overshoot_pct):
        """Sets the overshoot_pct of this Av1VideoConfiguration.

        Rate control adaptation overshoot control

        :param overshoot_pct: The overshoot_pct of this Av1VideoConfiguration.
        :type: int
        """

        if overshoot_pct is not None:
            if overshoot_pct is not None and overshoot_pct > 1000:
                raise ValueError("Invalid value for `overshoot_pct`, must be a value less than or equal to `1000`")
            if overshoot_pct is not None and overshoot_pct < 0:
                raise ValueError("Invalid value for `overshoot_pct`, must be a value greater than or equal to `0`")
            if not isinstance(overshoot_pct, int):
                raise TypeError("Invalid type for `overshoot_pct`, type has to be `int`")

            self._overshoot_pct = overshoot_pct


    @property
    def client_buffer_size(self):
        """Gets the client_buffer_size of this Av1VideoConfiguration.

        Decoder buffer size in milliseconds

        :return: The client_buffer_size of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._client_buffer_size

    @client_buffer_size.setter
    def client_buffer_size(self, client_buffer_size):
        """Sets the client_buffer_size of this Av1VideoConfiguration.

        Decoder buffer size in milliseconds

        :param client_buffer_size: The client_buffer_size of this Av1VideoConfiguration.
        :type: int
        """

        if client_buffer_size is not None:
            if not isinstance(client_buffer_size, int):
                raise TypeError("Invalid type for `client_buffer_size`, type has to be `int`")

            self._client_buffer_size = client_buffer_size


    @property
    def client_initial_buffer_size(self):
        """Gets the client_initial_buffer_size of this Av1VideoConfiguration.

        Decoder buffer initial size in milliseconds

        :return: The client_initial_buffer_size of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._client_initial_buffer_size

    @client_initial_buffer_size.setter
    def client_initial_buffer_size(self, client_initial_buffer_size):
        """Sets the client_initial_buffer_size of this Av1VideoConfiguration.

        Decoder buffer initial size in milliseconds

        :param client_initial_buffer_size: The client_initial_buffer_size of this Av1VideoConfiguration.
        :type: int
        """

        if client_initial_buffer_size is not None:
            if not isinstance(client_initial_buffer_size, int):
                raise TypeError("Invalid type for `client_initial_buffer_size`, type has to be `int`")

            self._client_initial_buffer_size = client_initial_buffer_size


    @property
    def client_optimal_buffer_size(self):
        """Gets the client_optimal_buffer_size of this Av1VideoConfiguration.

        Decoder buffer optimal size in milliseconds

        :return: The client_optimal_buffer_size of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._client_optimal_buffer_size

    @client_optimal_buffer_size.setter
    def client_optimal_buffer_size(self, client_optimal_buffer_size):
        """Sets the client_optimal_buffer_size of this Av1VideoConfiguration.

        Decoder buffer optimal size in milliseconds

        :param client_optimal_buffer_size: The client_optimal_buffer_size of this Av1VideoConfiguration.
        :type: int
        """

        if client_optimal_buffer_size is not None:
            if not isinstance(client_optimal_buffer_size, int):
                raise TypeError("Invalid type for `client_optimal_buffer_size`, type has to be `int`")

            self._client_optimal_buffer_size = client_optimal_buffer_size


    @property
    def tile_columns(self):
        """Gets the tile_columns of this Av1VideoConfiguration.

        Number of tile columns to use, log2

        :return: The tile_columns of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._tile_columns

    @tile_columns.setter
    def tile_columns(self, tile_columns):
        """Sets the tile_columns of this Av1VideoConfiguration.

        Number of tile columns to use, log2

        :param tile_columns: The tile_columns of this Av1VideoConfiguration.
        :type: int
        """

        if tile_columns is not None:
            if tile_columns is not None and tile_columns > 6:
                raise ValueError("Invalid value for `tile_columns`, must be a value less than or equal to `6`")
            if tile_columns is not None and tile_columns < 0:
                raise ValueError("Invalid value for `tile_columns`, must be a value greater than or equal to `0`")
            if not isinstance(tile_columns, int):
                raise TypeError("Invalid type for `tile_columns`, type has to be `int`")

            self._tile_columns = tile_columns


    @property
    def tile_rows(self):
        """Gets the tile_rows of this Av1VideoConfiguration.

        Number of tile rows to use, log2

        :return: The tile_rows of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._tile_rows

    @tile_rows.setter
    def tile_rows(self, tile_rows):
        """Sets the tile_rows of this Av1VideoConfiguration.

        Number of tile rows to use, log2

        :param tile_rows: The tile_rows of this Av1VideoConfiguration.
        :type: int
        """

        if tile_rows is not None:
            if tile_rows is not None and tile_rows > 2:
                raise ValueError("Invalid value for `tile_rows`, must be a value less than or equal to `2`")
            if tile_rows is not None and tile_rows < 0:
                raise ValueError("Invalid value for `tile_rows`, must be a value greater than or equal to `0`")
            if not isinstance(tile_rows, int):
                raise TypeError("Invalid type for `tile_rows`, type has to be `int`")

            self._tile_rows = tile_rows


    @property
    def is_automatic_alt_ref_frames_enabled(self):
        """Gets the is_automatic_alt_ref_frames_enabled of this Av1VideoConfiguration.

        Enable automatic set and use alf frames

        :return: The is_automatic_alt_ref_frames_enabled of this Av1VideoConfiguration.
        :rtype: bool
        """
        return self._is_automatic_alt_ref_frames_enabled

    @is_automatic_alt_ref_frames_enabled.setter
    def is_automatic_alt_ref_frames_enabled(self, is_automatic_alt_ref_frames_enabled):
        """Sets the is_automatic_alt_ref_frames_enabled of this Av1VideoConfiguration.

        Enable automatic set and use alf frames

        :param is_automatic_alt_ref_frames_enabled: The is_automatic_alt_ref_frames_enabled of this Av1VideoConfiguration.
        :type: bool
        """

        if is_automatic_alt_ref_frames_enabled is not None:
            if not isinstance(is_automatic_alt_ref_frames_enabled, bool):
                raise TypeError("Invalid type for `is_automatic_alt_ref_frames_enabled`, type has to be `bool`")

            self._is_automatic_alt_ref_frames_enabled = is_automatic_alt_ref_frames_enabled


    @property
    def arnr_max_frames(self):
        """Gets the arnr_max_frames of this Av1VideoConfiguration.

        The max number of frames to create arf

        :return: The arnr_max_frames of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._arnr_max_frames

    @arnr_max_frames.setter
    def arnr_max_frames(self, arnr_max_frames):
        """Sets the arnr_max_frames of this Av1VideoConfiguration.

        The max number of frames to create arf

        :param arnr_max_frames: The arnr_max_frames of this Av1VideoConfiguration.
        :type: int
        """

        if arnr_max_frames is not None:
            if not isinstance(arnr_max_frames, int):
                raise TypeError("Invalid type for `arnr_max_frames`, type has to be `int`")

            self._arnr_max_frames = arnr_max_frames


    @property
    def arnr_strength(self):
        """Gets the arnr_strength of this Av1VideoConfiguration.

        The filter strength for the arf

        :return: The arnr_strength of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._arnr_strength

    @arnr_strength.setter
    def arnr_strength(self, arnr_strength):
        """Sets the arnr_strength of this Av1VideoConfiguration.

        The filter strength for the arf

        :param arnr_strength: The arnr_strength of this Av1VideoConfiguration.
        :type: int
        """

        if arnr_strength is not None:
            if not isinstance(arnr_strength, int):
                raise TypeError("Invalid type for `arnr_strength`, type has to be `int`")

            self._arnr_strength = arnr_strength


    @property
    def max_intra_rate(self):
        """Gets the max_intra_rate of this Av1VideoConfiguration.

        Maximum data rate for intra frames, expressed as a percentage of the average per-frame bitrate. Default value 0 meaning unlimited

        :return: The max_intra_rate of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._max_intra_rate

    @max_intra_rate.setter
    def max_intra_rate(self, max_intra_rate):
        """Sets the max_intra_rate of this Av1VideoConfiguration.

        Maximum data rate for intra frames, expressed as a percentage of the average per-frame bitrate. Default value 0 meaning unlimited

        :param max_intra_rate: The max_intra_rate of this Av1VideoConfiguration.
        :type: int
        """

        if max_intra_rate is not None:
            if not isinstance(max_intra_rate, int):
                raise TypeError("Invalid type for `max_intra_rate`, type has to be `int`")

            self._max_intra_rate = max_intra_rate


    @property
    def is_lossless(self):
        """Gets the is_lossless of this Av1VideoConfiguration.

        Lossless encoding mode

        :return: The is_lossless of this Av1VideoConfiguration.
        :rtype: bool
        """
        return self._is_lossless

    @is_lossless.setter
    def is_lossless(self, is_lossless):
        """Sets the is_lossless of this Av1VideoConfiguration.

        Lossless encoding mode

        :param is_lossless: The is_lossless of this Av1VideoConfiguration.
        :type: bool
        """

        if is_lossless is not None:
            if not isinstance(is_lossless, bool):
                raise TypeError("Invalid type for `is_lossless`, type has to be `bool`")

            self._is_lossless = is_lossless


    @property
    def is_frame_parallel(self):
        """Gets the is_frame_parallel of this Av1VideoConfiguration.

        Enable frame parallel decoding feature

        :return: The is_frame_parallel of this Av1VideoConfiguration.
        :rtype: bool
        """
        return self._is_frame_parallel

    @is_frame_parallel.setter
    def is_frame_parallel(self, is_frame_parallel):
        """Sets the is_frame_parallel of this Av1VideoConfiguration.

        Enable frame parallel decoding feature

        :param is_frame_parallel: The is_frame_parallel of this Av1VideoConfiguration.
        :type: bool
        """

        if is_frame_parallel is not None:
            if not isinstance(is_frame_parallel, bool):
                raise TypeError("Invalid type for `is_frame_parallel`, type has to be `bool`")

            self._is_frame_parallel = is_frame_parallel


    @property
    def sharpness(self):
        """Gets the sharpness of this Av1VideoConfiguration.

        Sets the sharpness

        :return: The sharpness of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._sharpness

    @sharpness.setter
    def sharpness(self, sharpness):
        """Sets the sharpness of this Av1VideoConfiguration.

        Sets the sharpness

        :param sharpness: The sharpness of this Av1VideoConfiguration.
        :type: int
        """

        if sharpness is not None:
            if not isinstance(sharpness, int):
                raise TypeError("Invalid type for `sharpness`, type has to be `int`")

            self._sharpness = sharpness


    @property
    def is_frame_boost_enabled(self):
        """Gets the is_frame_boost_enabled of this Av1VideoConfiguration.

        Enable quality boost by lowering frame level Q periodically

        :return: The is_frame_boost_enabled of this Av1VideoConfiguration.
        :rtype: bool
        """
        return self._is_frame_boost_enabled

    @is_frame_boost_enabled.setter
    def is_frame_boost_enabled(self, is_frame_boost_enabled):
        """Sets the is_frame_boost_enabled of this Av1VideoConfiguration.

        Enable quality boost by lowering frame level Q periodically

        :param is_frame_boost_enabled: The is_frame_boost_enabled of this Av1VideoConfiguration.
        :type: bool
        """

        if is_frame_boost_enabled is not None:
            if not isinstance(is_frame_boost_enabled, bool):
                raise TypeError("Invalid type for `is_frame_boost_enabled`, type has to be `bool`")

            self._is_frame_boost_enabled = is_frame_boost_enabled


    @property
    def noise_sensitivity(self):
        """Gets the noise_sensitivity of this Av1VideoConfiguration.

        Enable noise sensitivity on Y channel

        :return: The noise_sensitivity of this Av1VideoConfiguration.
        :rtype: bool
        """
        return self._noise_sensitivity

    @noise_sensitivity.setter
    def noise_sensitivity(self, noise_sensitivity):
        """Sets the noise_sensitivity of this Av1VideoConfiguration.

        Enable noise sensitivity on Y channel

        :param noise_sensitivity: The noise_sensitivity of this Av1VideoConfiguration.
        :type: bool
        """

        if noise_sensitivity is not None:
            if not isinstance(noise_sensitivity, bool):
                raise TypeError("Invalid type for `noise_sensitivity`, type has to be `bool`")

            self._noise_sensitivity = noise_sensitivity


    @property
    def min_gf_interval(self):
        """Gets the min_gf_interval of this Av1VideoConfiguration.

        Minimum interval between GF/ARF frames

        :return: The min_gf_interval of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._min_gf_interval

    @min_gf_interval.setter
    def min_gf_interval(self, min_gf_interval):
        """Sets the min_gf_interval of this Av1VideoConfiguration.

        Minimum interval between GF/ARF frames

        :param min_gf_interval: The min_gf_interval of this Av1VideoConfiguration.
        :type: int
        """

        if min_gf_interval is not None:
            if not isinstance(min_gf_interval, int):
                raise TypeError("Invalid type for `min_gf_interval`, type has to be `int`")

            self._min_gf_interval = min_gf_interval


    @property
    def max_gf_interval(self):
        """Gets the max_gf_interval of this Av1VideoConfiguration.

        Maximum interval between GF/ARF frames

        :return: The max_gf_interval of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._max_gf_interval

    @max_gf_interval.setter
    def max_gf_interval(self, max_gf_interval):
        """Sets the max_gf_interval of this Av1VideoConfiguration.

        Maximum interval between GF/ARF frames

        :param max_gf_interval: The max_gf_interval of this Av1VideoConfiguration.
        :type: int
        """

        if max_gf_interval is not None:
            if not isinstance(max_gf_interval, int):
                raise TypeError("Invalid type for `max_gf_interval`, type has to be `int`")

            self._max_gf_interval = max_gf_interval


    @property
    def num_tile_groups(self):
        """Gets the num_tile_groups of this Av1VideoConfiguration.

        Maximum number of tile groups

        :return: The num_tile_groups of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._num_tile_groups

    @num_tile_groups.setter
    def num_tile_groups(self, num_tile_groups):
        """Sets the num_tile_groups of this Av1VideoConfiguration.

        Maximum number of tile groups

        :param num_tile_groups: The num_tile_groups of this Av1VideoConfiguration.
        :type: int
        """

        if num_tile_groups is not None:
            if not isinstance(num_tile_groups, int):
                raise TypeError("Invalid type for `num_tile_groups`, type has to be `int`")

            self._num_tile_groups = num_tile_groups


    @property
    def mtu_size(self):
        """Gets the mtu_size of this Av1VideoConfiguration.

        Maximum number of bytes in a tile group

        :return: The mtu_size of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._mtu_size

    @mtu_size.setter
    def mtu_size(self, mtu_size):
        """Sets the mtu_size of this Av1VideoConfiguration.

        Maximum number of bytes in a tile group

        :param mtu_size: The mtu_size of this Av1VideoConfiguration.
        :type: int
        """

        if mtu_size is not None:
            if not isinstance(mtu_size, int):
                raise TypeError("Invalid type for `mtu_size`, type has to be `int`")

            self._mtu_size = mtu_size

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Av1VideoConfiguration, self).to_dict()

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
            if issubclass(Av1VideoConfiguration, dict):
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
        if not isinstance(other, Av1VideoConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
