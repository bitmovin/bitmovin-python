from bitmovin import MVPredictionMode, BAdapt, H264CodecConfiguration
from bitmovin.resources.enums.h264_Preset import H264Preset
from bitmovin.resources.enums.h264_motion_estimation_method import H264MotionEstimationMethod
from bitmovin.resources.enums.h264_partition import H264Partition
from bitmovin.resources.enums.h264_sub_me import H264SubMe


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

        if preset == H264Preset.FAST:
            self.setFastPreset(config)

        return config

    def setFastPreset(self, config):
        config.refFrames=2
        config.mvPredictionMode=MVPredictionMode.SPATIAL
        config.rc_lookahead=30
        config.sub_me=H264SubMe.RD_IP
        config.motion_estimation_method=H264MotionEstimationMethod.HEX
        config.b_adapt=BAdapt.FAST
        config.partitions=[H264Partition.I4X4, H264Partition.I8X8, H264Partition.P8X8, H264Partition.B8X8]