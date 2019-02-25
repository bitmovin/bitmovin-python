# coding: utf-8

from bitmovin_python.models.codec_config_type import CodecConfigType
from bitmovin_python.models.color_config import ColorConfig
from bitmovin_python.models.encoding_mode import EncodingMode
from bitmovin_python.models.pixel_format import PixelFormat
from bitmovin_python.models.video_configuration import VideoConfiguration
from bitmovin_python.models.vp9_aq_mode import Vp9AqMode
from bitmovin_python.models.vp9_arnr_type import Vp9ArnrType
from bitmovin_python.models.vp9_quality import Vp9Quality
import pprint
import six
from datetime import datetime
from enum import Enum


class Vp9VideoConfiguration(VideoConfiguration):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Vp9VideoConfiguration, self).openapi_types
        types.update({
            'crf': 'int',
            'lag_in_frames': 'int',
            'tile_columns': 'int',
            'tile_rows': 'int',
            'frame_parallel': 'bool',
            'max_intra_rate': 'int',
            'qp_min': 'int',
            'qp_max': 'int',
            'rate_undershoot_pct': 'int',
            'rate_overshoot_pct': 'int',
            'noise_sensitivity': 'bool',
            'sharpness': 'int',
            'min_gop': 'int',
            'max_gop': 'int',
            'min_keyframe_interval': 'float',
            'max_keyframe_interval': 'float',
            'quality': 'Vp9Quality',
            'lossless': 'bool',
            'static_thresh': 'int',
            'aq_mode': 'Vp9AqMode',
            'arnr_max_frames': 'int',
            'arnr_strength': 'int',
            'arnr_type': 'Vp9ArnrType'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Vp9VideoConfiguration, self).attribute_map
        attributes.update({
            'crf': 'crf',
            'lag_in_frames': 'lagInFrames',
            'tile_columns': 'tileColumns',
            'tile_rows': 'tileRows',
            'frame_parallel': 'frameParallel',
            'max_intra_rate': 'maxIntraRate',
            'qp_min': 'qpMin',
            'qp_max': 'qpMax',
            'rate_undershoot_pct': 'rateUndershootPct',
            'rate_overshoot_pct': 'rateOvershootPct',
            'noise_sensitivity': 'noiseSensitivity',
            'sharpness': 'sharpness',
            'min_gop': 'minGop',
            'max_gop': 'maxGop',
            'min_keyframe_interval': 'minKeyframeInterval',
            'max_keyframe_interval': 'maxKeyframeInterval',
            'quality': 'quality',
            'lossless': 'lossless',
            'static_thresh': 'staticThresh',
            'aq_mode': 'aqMode',
            'arnr_max_frames': 'arnrMaxFrames',
            'arnr_strength': 'arnrStrength',
            'arnr_type': 'arnrType'
        })
        return attributes

    def __init__(self, crf=None, lag_in_frames=None, tile_columns=None, tile_rows=None, frame_parallel=None, max_intra_rate=None, qp_min=None, qp_max=None, rate_undershoot_pct=None, rate_overshoot_pct=None, noise_sensitivity=None, sharpness=None, min_gop=None, max_gop=None, min_keyframe_interval=None, max_keyframe_interval=None, quality=None, lossless=None, static_thresh=None, aq_mode=None, arnr_max_frames=None, arnr_strength=None, arnr_type=None, *args, **kwargs):
        super(Vp9VideoConfiguration, self).__init__(*args, **kwargs)

        self._crf = None
        self._lag_in_frames = None
        self._tile_columns = None
        self._tile_rows = None
        self._frame_parallel = None
        self._max_intra_rate = None
        self._qp_min = None
        self._qp_max = None
        self._rate_undershoot_pct = None
        self._rate_overshoot_pct = None
        self._noise_sensitivity = None
        self._sharpness = None
        self._min_gop = None
        self._max_gop = None
        self._min_keyframe_interval = None
        self._max_keyframe_interval = None
        self._quality = None
        self._lossless = None
        self._static_thresh = None
        self._aq_mode = None
        self._arnr_max_frames = None
        self._arnr_strength = None
        self._arnr_type = None
        self.discriminator = None

        if crf is not None:
            self.crf = crf
        if lag_in_frames is not None:
            self.lag_in_frames = lag_in_frames
        if tile_columns is not None:
            self.tile_columns = tile_columns
        if tile_rows is not None:
            self.tile_rows = tile_rows
        if frame_parallel is not None:
            self.frame_parallel = frame_parallel
        if max_intra_rate is not None:
            self.max_intra_rate = max_intra_rate
        if qp_min is not None:
            self.qp_min = qp_min
        if qp_max is not None:
            self.qp_max = qp_max
        if rate_undershoot_pct is not None:
            self.rate_undershoot_pct = rate_undershoot_pct
        if rate_overshoot_pct is not None:
            self.rate_overshoot_pct = rate_overshoot_pct
        if noise_sensitivity is not None:
            self.noise_sensitivity = noise_sensitivity
        if sharpness is not None:
            self.sharpness = sharpness
        if min_gop is not None:
            self.min_gop = min_gop
        if max_gop is not None:
            self.max_gop = max_gop
        if min_keyframe_interval is not None:
            self.min_keyframe_interval = min_keyframe_interval
        if max_keyframe_interval is not None:
            self.max_keyframe_interval = max_keyframe_interval
        if quality is not None:
            self.quality = quality
        if lossless is not None:
            self.lossless = lossless
        if static_thresh is not None:
            self.static_thresh = static_thresh
        if aq_mode is not None:
            self.aq_mode = aq_mode
        if arnr_max_frames is not None:
            self.arnr_max_frames = arnr_max_frames
        if arnr_strength is not None:
            self.arnr_strength = arnr_strength
        if arnr_type is not None:
            self.arnr_type = arnr_type

    @property
    def crf(self):
        """Gets the crf of this Vp9VideoConfiguration.

        Sets the constant rate factor for quality-based variable bitrate. Either bitrate or crf is required.

        :return: The crf of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._crf

    @crf.setter
    def crf(self, crf):
        """Sets the crf of this Vp9VideoConfiguration.

        Sets the constant rate factor for quality-based variable bitrate. Either bitrate or crf is required.

        :param crf: The crf of this Vp9VideoConfiguration.
        :type: int
        """

        if crf is not None:
            if crf is not None and crf > 63:
                raise ValueError("Invalid value for `crf`, must be a value less than or equal to `63`")
            if crf is not None and crf < 0:
                raise ValueError("Invalid value for `crf`, must be a value greater than or equal to `0`")
            if not isinstance(crf, int):
                raise TypeError("Invalid type for `crf`, type has to be `int`")

            self._crf = crf


    @property
    def lag_in_frames(self):
        """Gets the lag_in_frames of this Vp9VideoConfiguration.

        Number of frames to look ahead for alternate reference frame selection.

        :return: The lag_in_frames of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._lag_in_frames

    @lag_in_frames.setter
    def lag_in_frames(self, lag_in_frames):
        """Sets the lag_in_frames of this Vp9VideoConfiguration.

        Number of frames to look ahead for alternate reference frame selection.

        :param lag_in_frames: The lag_in_frames of this Vp9VideoConfiguration.
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
    def tile_columns(self):
        """Gets the tile_columns of this Vp9VideoConfiguration.

        Number of tile columns to use, log2.

        :return: The tile_columns of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._tile_columns

    @tile_columns.setter
    def tile_columns(self, tile_columns):
        """Sets the tile_columns of this Vp9VideoConfiguration.

        Number of tile columns to use, log2.

        :param tile_columns: The tile_columns of this Vp9VideoConfiguration.
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
        """Gets the tile_rows of this Vp9VideoConfiguration.

        Number of tile rows to use, log2.

        :return: The tile_rows of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._tile_rows

    @tile_rows.setter
    def tile_rows(self, tile_rows):
        """Sets the tile_rows of this Vp9VideoConfiguration.

        Number of tile rows to use, log2.

        :param tile_rows: The tile_rows of this Vp9VideoConfiguration.
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
    def frame_parallel(self):
        """Gets the frame_parallel of this Vp9VideoConfiguration.

        Enable frame parallel decodability features

        :return: The frame_parallel of this Vp9VideoConfiguration.
        :rtype: bool
        """
        return self._frame_parallel

    @frame_parallel.setter
    def frame_parallel(self, frame_parallel):
        """Sets the frame_parallel of this Vp9VideoConfiguration.

        Enable frame parallel decodability features

        :param frame_parallel: The frame_parallel of this Vp9VideoConfiguration.
        :type: bool
        """

        if frame_parallel is not None:
            if not isinstance(frame_parallel, bool):
                raise TypeError("Invalid type for `frame_parallel`, type has to be `bool`")

            self._frame_parallel = frame_parallel


    @property
    def max_intra_rate(self):
        """Gets the max_intra_rate of this Vp9VideoConfiguration.

        Maximum I-frame bitrate (percentage) 0=unlimited

        :return: The max_intra_rate of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._max_intra_rate

    @max_intra_rate.setter
    def max_intra_rate(self, max_intra_rate):
        """Sets the max_intra_rate of this Vp9VideoConfiguration.

        Maximum I-frame bitrate (percentage) 0=unlimited

        :param max_intra_rate: The max_intra_rate of this Vp9VideoConfiguration.
        :type: int
        """

        if max_intra_rate is not None:
            if not isinstance(max_intra_rate, int):
                raise TypeError("Invalid type for `max_intra_rate`, type has to be `int`")

            self._max_intra_rate = max_intra_rate


    @property
    def qp_min(self):
        """Gets the qp_min of this Vp9VideoConfiguration.

        Sets the minimum of quantization factor.

        :return: The qp_min of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._qp_min

    @qp_min.setter
    def qp_min(self, qp_min):
        """Sets the qp_min of this Vp9VideoConfiguration.

        Sets the minimum of quantization factor.

        :param qp_min: The qp_min of this Vp9VideoConfiguration.
        :type: int
        """

        if qp_min is not None:
            if qp_min is not None and qp_min > 63:
                raise ValueError("Invalid value for `qp_min`, must be a value less than or equal to `63`")
            if qp_min is not None and qp_min < 0:
                raise ValueError("Invalid value for `qp_min`, must be a value greater than or equal to `0`")
            if not isinstance(qp_min, int):
                raise TypeError("Invalid type for `qp_min`, type has to be `int`")

            self._qp_min = qp_min


    @property
    def qp_max(self):
        """Gets the qp_max of this Vp9VideoConfiguration.

        Sets the maximum of quantization factor.

        :return: The qp_max of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._qp_max

    @qp_max.setter
    def qp_max(self, qp_max):
        """Sets the qp_max of this Vp9VideoConfiguration.

        Sets the maximum of quantization factor.

        :param qp_max: The qp_max of this Vp9VideoConfiguration.
        :type: int
        """

        if qp_max is not None:
            if qp_max is not None and qp_max > 63:
                raise ValueError("Invalid value for `qp_max`, must be a value less than or equal to `63`")
            if qp_max is not None and qp_max < 0:
                raise ValueError("Invalid value for `qp_max`, must be a value greater than or equal to `0`")
            if not isinstance(qp_max, int):
                raise TypeError("Invalid type for `qp_max`, type has to be `int`")

            self._qp_max = qp_max


    @property
    def rate_undershoot_pct(self):
        """Gets the rate_undershoot_pct of this Vp9VideoConfiguration.

        Datarate undershoot (min) target (percentage).

        :return: The rate_undershoot_pct of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._rate_undershoot_pct

    @rate_undershoot_pct.setter
    def rate_undershoot_pct(self, rate_undershoot_pct):
        """Sets the rate_undershoot_pct of this Vp9VideoConfiguration.

        Datarate undershoot (min) target (percentage).

        :param rate_undershoot_pct: The rate_undershoot_pct of this Vp9VideoConfiguration.
        :type: int
        """

        if rate_undershoot_pct is not None:
            if rate_undershoot_pct is not None and rate_undershoot_pct > 100:
                raise ValueError("Invalid value for `rate_undershoot_pct`, must be a value less than or equal to `100`")
            if rate_undershoot_pct is not None and rate_undershoot_pct < 0:
                raise ValueError("Invalid value for `rate_undershoot_pct`, must be a value greater than or equal to `0`")
            if not isinstance(rate_undershoot_pct, int):
                raise TypeError("Invalid type for `rate_undershoot_pct`, type has to be `int`")

            self._rate_undershoot_pct = rate_undershoot_pct


    @property
    def rate_overshoot_pct(self):
        """Gets the rate_overshoot_pct of this Vp9VideoConfiguration.

        Datarate overshoot (max) target (percentage).

        :return: The rate_overshoot_pct of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._rate_overshoot_pct

    @rate_overshoot_pct.setter
    def rate_overshoot_pct(self, rate_overshoot_pct):
        """Sets the rate_overshoot_pct of this Vp9VideoConfiguration.

        Datarate overshoot (max) target (percentage).

        :param rate_overshoot_pct: The rate_overshoot_pct of this Vp9VideoConfiguration.
        :type: int
        """

        if rate_overshoot_pct is not None:
            if rate_overshoot_pct is not None and rate_overshoot_pct > 100:
                raise ValueError("Invalid value for `rate_overshoot_pct`, must be a value less than or equal to `100`")
            if rate_overshoot_pct is not None and rate_overshoot_pct < 0:
                raise ValueError("Invalid value for `rate_overshoot_pct`, must be a value greater than or equal to `0`")
            if not isinstance(rate_overshoot_pct, int):
                raise TypeError("Invalid type for `rate_overshoot_pct`, type has to be `int`")

            self._rate_overshoot_pct = rate_overshoot_pct


    @property
    def noise_sensitivity(self):
        """Gets the noise_sensitivity of this Vp9VideoConfiguration.

        Enable noise sensitivity on Y channel

        :return: The noise_sensitivity of this Vp9VideoConfiguration.
        :rtype: bool
        """
        return self._noise_sensitivity

    @noise_sensitivity.setter
    def noise_sensitivity(self, noise_sensitivity):
        """Sets the noise_sensitivity of this Vp9VideoConfiguration.

        Enable noise sensitivity on Y channel

        :param noise_sensitivity: The noise_sensitivity of this Vp9VideoConfiguration.
        :type: bool
        """

        if noise_sensitivity is not None:
            if not isinstance(noise_sensitivity, bool):
                raise TypeError("Invalid type for `noise_sensitivity`, type has to be `bool`")

            self._noise_sensitivity = noise_sensitivity


    @property
    def sharpness(self):
        """Gets the sharpness of this Vp9VideoConfiguration.

        Loop filter sharpness.

        :return: The sharpness of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._sharpness

    @sharpness.setter
    def sharpness(self, sharpness):
        """Sets the sharpness of this Vp9VideoConfiguration.

        Loop filter sharpness.

        :param sharpness: The sharpness of this Vp9VideoConfiguration.
        :type: int
        """

        if sharpness is not None:
            if sharpness is not None and sharpness > 7:
                raise ValueError("Invalid value for `sharpness`, must be a value less than or equal to `7`")
            if sharpness is not None and sharpness < 0:
                raise ValueError("Invalid value for `sharpness`, must be a value greater than or equal to `0`")
            if not isinstance(sharpness, int):
                raise TypeError("Invalid type for `sharpness`, type has to be `int`")

            self._sharpness = sharpness


    @property
    def min_gop(self):
        """Gets the min_gop of this Vp9VideoConfiguration.

        Minimum GOP length, the minimum distance between I-frames.

        :return: The min_gop of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._min_gop

    @min_gop.setter
    def min_gop(self, min_gop):
        """Sets the min_gop of this Vp9VideoConfiguration.

        Minimum GOP length, the minimum distance between I-frames.

        :param min_gop: The min_gop of this Vp9VideoConfiguration.
        :type: int
        """

        if min_gop is not None:
            if not isinstance(min_gop, int):
                raise TypeError("Invalid type for `min_gop`, type has to be `int`")

            self._min_gop = min_gop


    @property
    def max_gop(self):
        """Gets the max_gop of this Vp9VideoConfiguration.

        Maximum GOP length, the maximum distance between I-frames

        :return: The max_gop of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._max_gop

    @max_gop.setter
    def max_gop(self, max_gop):
        """Sets the max_gop of this Vp9VideoConfiguration.

        Maximum GOP length, the maximum distance between I-frames

        :param max_gop: The max_gop of this Vp9VideoConfiguration.
        :type: int
        """

        if max_gop is not None:
            if not isinstance(max_gop, int):
                raise TypeError("Invalid type for `max_gop`, type has to be `int`")

            self._max_gop = max_gop


    @property
    def min_keyframe_interval(self):
        """Gets the min_keyframe_interval of this Vp9VideoConfiguration.

        Minimum interval in seconds between key frames

        :return: The min_keyframe_interval of this Vp9VideoConfiguration.
        :rtype: float
        """
        return self._min_keyframe_interval

    @min_keyframe_interval.setter
    def min_keyframe_interval(self, min_keyframe_interval):
        """Sets the min_keyframe_interval of this Vp9VideoConfiguration.

        Minimum interval in seconds between key frames

        :param min_keyframe_interval: The min_keyframe_interval of this Vp9VideoConfiguration.
        :type: float
        """

        if min_keyframe_interval is not None:
            if not isinstance(min_keyframe_interval, float):
                raise TypeError("Invalid type for `min_keyframe_interval`, type has to be `float`")

            self._min_keyframe_interval = min_keyframe_interval


    @property
    def max_keyframe_interval(self):
        """Gets the max_keyframe_interval of this Vp9VideoConfiguration.

        Maximum interval in seconds between key frames

        :return: The max_keyframe_interval of this Vp9VideoConfiguration.
        :rtype: float
        """
        return self._max_keyframe_interval

    @max_keyframe_interval.setter
    def max_keyframe_interval(self, max_keyframe_interval):
        """Sets the max_keyframe_interval of this Vp9VideoConfiguration.

        Maximum interval in seconds between key frames

        :param max_keyframe_interval: The max_keyframe_interval of this Vp9VideoConfiguration.
        :type: float
        """

        if max_keyframe_interval is not None:
            if not isinstance(max_keyframe_interval, float):
                raise TypeError("Invalid type for `max_keyframe_interval`, type has to be `float`")

            self._max_keyframe_interval = max_keyframe_interval


    @property
    def quality(self):
        """Gets the quality of this Vp9VideoConfiguration.


        :return: The quality of this Vp9VideoConfiguration.
        :rtype: Vp9Quality
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this Vp9VideoConfiguration.


        :param quality: The quality of this Vp9VideoConfiguration.
        :type: Vp9Quality
        """

        if quality is not None:
            if not isinstance(quality, Vp9Quality):
                raise TypeError("Invalid type for `quality`, type has to be `Vp9Quality`")

            self._quality = quality


    @property
    def lossless(self):
        """Gets the lossless of this Vp9VideoConfiguration.

        Lossless mode

        :return: The lossless of this Vp9VideoConfiguration.
        :rtype: bool
        """
        return self._lossless

    @lossless.setter
    def lossless(self, lossless):
        """Sets the lossless of this Vp9VideoConfiguration.

        Lossless mode

        :param lossless: The lossless of this Vp9VideoConfiguration.
        :type: bool
        """

        if lossless is not None:
            if not isinstance(lossless, bool):
                raise TypeError("Invalid type for `lossless`, type has to be `bool`")

            self._lossless = lossless


    @property
    def static_thresh(self):
        """Gets the static_thresh of this Vp9VideoConfiguration.

        A change threshold on blocks below which they will be skipped by the encoder.

        :return: The static_thresh of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._static_thresh

    @static_thresh.setter
    def static_thresh(self, static_thresh):
        """Sets the static_thresh of this Vp9VideoConfiguration.

        A change threshold on blocks below which they will be skipped by the encoder.

        :param static_thresh: The static_thresh of this Vp9VideoConfiguration.
        :type: int
        """

        if static_thresh is not None:
            if static_thresh is not None and static_thresh < 0:
                raise ValueError("Invalid value for `static_thresh`, must be a value greater than or equal to `0`")
            if not isinstance(static_thresh, int):
                raise TypeError("Invalid type for `static_thresh`, type has to be `int`")

            self._static_thresh = static_thresh


    @property
    def aq_mode(self):
        """Gets the aq_mode of this Vp9VideoConfiguration.


        :return: The aq_mode of this Vp9VideoConfiguration.
        :rtype: Vp9AqMode
        """
        return self._aq_mode

    @aq_mode.setter
    def aq_mode(self, aq_mode):
        """Sets the aq_mode of this Vp9VideoConfiguration.


        :param aq_mode: The aq_mode of this Vp9VideoConfiguration.
        :type: Vp9AqMode
        """

        if aq_mode is not None:
            if not isinstance(aq_mode, Vp9AqMode):
                raise TypeError("Invalid type for `aq_mode`, type has to be `Vp9AqMode`")

            self._aq_mode = aq_mode


    @property
    def arnr_max_frames(self):
        """Gets the arnr_max_frames of this Vp9VideoConfiguration.

        altref noise reduction max frame count.

        :return: The arnr_max_frames of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._arnr_max_frames

    @arnr_max_frames.setter
    def arnr_max_frames(self, arnr_max_frames):
        """Sets the arnr_max_frames of this Vp9VideoConfiguration.

        altref noise reduction max frame count.

        :param arnr_max_frames: The arnr_max_frames of this Vp9VideoConfiguration.
        :type: int
        """

        if arnr_max_frames is not None:
            if arnr_max_frames is not None and arnr_max_frames > 15:
                raise ValueError("Invalid value for `arnr_max_frames`, must be a value less than or equal to `15`")
            if arnr_max_frames is not None and arnr_max_frames < 0:
                raise ValueError("Invalid value for `arnr_max_frames`, must be a value greater than or equal to `0`")
            if not isinstance(arnr_max_frames, int):
                raise TypeError("Invalid type for `arnr_max_frames`, type has to be `int`")

            self._arnr_max_frames = arnr_max_frames


    @property
    def arnr_strength(self):
        """Gets the arnr_strength of this Vp9VideoConfiguration.

        altref noise reduction filter strength.

        :return: The arnr_strength of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._arnr_strength

    @arnr_strength.setter
    def arnr_strength(self, arnr_strength):
        """Sets the arnr_strength of this Vp9VideoConfiguration.

        altref noise reduction filter strength.

        :param arnr_strength: The arnr_strength of this Vp9VideoConfiguration.
        :type: int
        """

        if arnr_strength is not None:
            if arnr_strength is not None and arnr_strength > 6:
                raise ValueError("Invalid value for `arnr_strength`, must be a value less than or equal to `6`")
            if arnr_strength is not None and arnr_strength < 0:
                raise ValueError("Invalid value for `arnr_strength`, must be a value greater than or equal to `0`")
            if not isinstance(arnr_strength, int):
                raise TypeError("Invalid type for `arnr_strength`, type has to be `int`")

            self._arnr_strength = arnr_strength


    @property
    def arnr_type(self):
        """Gets the arnr_type of this Vp9VideoConfiguration.


        :return: The arnr_type of this Vp9VideoConfiguration.
        :rtype: Vp9ArnrType
        """
        return self._arnr_type

    @arnr_type.setter
    def arnr_type(self, arnr_type):
        """Sets the arnr_type of this Vp9VideoConfiguration.


        :param arnr_type: The arnr_type of this Vp9VideoConfiguration.
        :type: Vp9ArnrType
        """

        if arnr_type is not None:
            if not isinstance(arnr_type, Vp9ArnrType):
                raise TypeError("Invalid type for `arnr_type`, type has to be `Vp9ArnrType`")

            self._arnr_type = arnr_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Vp9VideoConfiguration, self).to_dict()

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
            if issubclass(Vp9VideoConfiguration, dict):
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
        if not isinstance(other, Vp9VideoConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
