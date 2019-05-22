from bitmovin import MVPredictionMode, BAdapt, H264CodecConfiguration
from bitmovin.resources.enums.h264_Preset import H264Preset
from bitmovin.resources.enums.h264_motion_estimation_method import H264MotionEstimationMethod
from bitmovin.resources.enums.h264_partition import H264Partition
from bitmovin.resources.enums.h264_sub_me import H264SubMe
from bitmovin.resources.enums.h264_trellis import H264Trellis


class H264CodecConfigurationFactory():

    def createH264CodecConfiguration(self,
                                     name,
                                     bitrate,
                                     rate,
                                     profile,
                                     preset):

        if preset is not None:
            if not isinstance(preset, H264Preset):
                raise "preset must be of type H264Preset"

        config = H264CodecConfiguration(name, bitrate, rate, profile)

        if preset == H264Preset.PLACEBO:
            self.setPlaceboPreset(config)
        elif preset == H264Preset.VERYSLOW:
            self.setVerySlowPreset(config)
        elif preset == H264Preset.SLOWER:
            self.setSlowerPreset(config)
        elif preset == H264Preset.SLOW:
            self.setSlowPreset(config)
        elif preset == H264Preset.MEDIUM:
            self.setMediumPreset(config)
        elif preset == H264Preset.FAST:
            self.setFastPreset(config)
        elif preset == H264Preset.FASTER:
            self.setFasterPreset(config)
        elif preset == H264Preset.VERYFAST:
            self.setVeryFastPreset(config)
        elif preset == H264Preset.SUPERFAST:
            self.setSuperFastPreset(config)
        elif preset == H264Preset.ULTRAFAST:
            self.setUltraFastPreset(config)

        return config

    def setPlaceboPreset(self, config):
        #merange = mvsearchrange
        config.b_adapt = BAdapt.FULL
        config.bframes = 16
        config.mvSearchRangeMax = 24
        config.mvPredictionMode = MVPredictionMode.AUTO
        config.motion_estimation_method = H264MotionEstimationMethod.UMH
        config.cabac = True
        config.rc_lookahead = 60
        config.refFrames = 16
        config.sub_me = H264SubMe.RD_REF_ALL
        config.trellis = H264Trellis.ENABLED_ALL
        config.partitions = [H264Partition.ALL]

    def setVerySlowPreset(self, config):
        config.b_adapt = BAdapt.FULL
        config.bframes = 8
        config.mvSearchRangeMax = 24
        config.mvPredictionMode = MVPredictionMode.AUTO
        config.motion_estimation_method = H264MotionEstimationMethod.UMH
        config.cabac = True
        config.rc_lookahead = 60
        config.refFrames = 16
        config.sub_me = H264SubMe.RD_REF_ALL
        config.trellis = H264Trellis.ENABLED_ALL
        config.partitions = [H264Partition.ALL]

    def setSlowerPreset(self, config):
        config.b_adapt = BAdapt.FULL
        config.bframes = 3
        config.mvSearchRangeMax = 16
        config.mvPredictionMode = MVPredictionMode.AUTO
        config.motion_estimation_method = H264MotionEstimationMethod.UMH
        config.cabac = True
        config.rc_lookahead = 60
        config.refFrames = 8
        config.sub_me = H264SubMe.RD_REF_ALL
        config.trellis = H264Trellis.ENABLED_ALL
        config.partitions = [H264Partition.ALL]

    def setSlowPreset(self, config):
        config.b_adapt = BAdapt.FULL
        config.bframes = 3
        config.mvSearchRangeMax = 16
        config.mvPredictionMode = MVPredictionMode.AUTO
        config.motion_estimation_method = H264MotionEstimationMethod.UMH
        config.cabac = True
        config.rc_lookahead = 50
        config.refFrames = 5
        config.sub_me = H264SubMe.RD_REF_IP
        config.trellis = H264Trellis.ENABLED_ALL
        config.partitions = [H264Partition.ALL]

    def setMediumPreset(self, config):
        config.b_adapt = BAdapt.FAST
        config.bframes = 3
        config.mvSearchRangeMax = 16
        config.mvPredictionMode = MVPredictionMode.SPATIAL
        config.motion_estimation_method = H264MotionEstimationMethod.HEX
        config.cabac = True
        config.rc_lookahead = 40
        config.refFrames = 3
        config.sub_me = H264SubMe.RD_ALL
        config.trellis = H264Trellis.ENABLED_ALL
        config.partitions = [H264Partition.I4X4, H264Partition.I8X8, H264Partition.P8X8, H264Partition.B8X8]

    def setFastPreset(self, config):
        config.b_adapt = BAdapt.FAST
        config.bframes = 3
        config.mvSearchRangeMax = 16
        config.mvPredictionMode = MVPredictionMode.SPATIAL
        config.motion_estimation_method = H264MotionEstimationMethod.HEX
        config.cabac = True
        config.rc_lookahead = 30
        config.refFrames = 2
        config.sub_me = H264SubMe.RD_IP
        config.trellis = H264Trellis.ENABLED_FINAL_MB
        config.partitions = [H264Partition.I4X4, H264Partition.I8X8, H264Partition.P8X8, H264Partition.B8X8]

    def setFasterPreset(self, config):
        config.b_adapt = BAdapt.FAST
        config.bframes = 3
        config.mvSearchRangeMax = 16
        config.mvPredictionMode = MVPredictionMode.SPATIAL
        config.motion_estimation_method = H264MotionEstimationMethod.HEX
        config.cabac = True
        config.rc_lookahead = 20
        config.refFrames = 2
        config.sub_me = H264SubMe.QPEL4
        config.trellis = H264Trellis.ENABLED_FINAL_MB
        config.partitions = [H264Partition.I4X4, H264Partition.I8X8, H264Partition.P8X8, H264Partition.B8X8]

    def setVeryFastPreset(self, config):
        config.b_adapt = BAdapt.FAST
        config.bframes = 3
        config.mvSearchRangeMax = 16
        config.mvPredictionMode = MVPredictionMode.SPATIAL
        config.motion_estimation_method = H264MotionEstimationMethod.HEX
        config.cabac = True
        config.rc_lookahead = 10
        config.refFrames = 1
        config.sub_me = H264SubMe.SATD
        config.trellis = H264Trellis.ENABLED_FINAL_MB
        config.partitions = [H264Partition.I4X4, H264Partition.I8X8, H264Partition.P8X8, H264Partition.B8X8]

    def setSuperFastPreset(self, config):
        config.b_adapt = BAdapt.FAST
        config.bframes = 3
        config.mvSearchRangeMax = 16
        config.mvPredictionMode = MVPredictionMode.SPATIAL
        config.motion_estimation_method = H264MotionEstimationMethod.DIA
        config.cabac = True
        config.rc_lookahead = 0
        config.refFrames = 1
        config.sub_me = H264SubMe.SAD
        config.trellis = H264Trellis.ENABLED_FINAL_MB
        config.partitions = [H264Partition.I4X4, H264Partition.I8X8]

    def setUltraFastPreset(self, config):
        config.b_adapt = BAdapt.NONE
        config.bframes = 0
        config.mvSearchRangeMax = 16
        config.mvPredictionMode = MVPredictionMode.SPATIAL
        config.motion_estimation_method = H264MotionEstimationMethod.DIA
        config.cabac = False
        config.rc_lookahead = 0
        config.refFrames = 1
        config.sub_me = H264SubMe.FULLPEL
        config.trellis = H264Trellis.DISABLED
        config.partitions = [H264Partition.NONE]

