from bitmovin.resources.models.encodings.pertitle.per_title_configuration import PerTitleConfiguration


class H265PerTitleConfiguration(PerTitleConfiguration):
    def __init__(self, min_bitrate=None, max_bitrate=None, min_bitrate_step_size=None,
                 max_bitrate_step_size=None, target_quality_crf=None, auto_representations=None,
                 codec_min_bitrate_factor=None, codec_max_bitrate_factor=None, codec_bufsize_factor=None):
        super().__init__(min_bitrate=min_bitrate, max_bitrate=max_bitrate, min_bitrate_step_size=min_bitrate_step_size,
                         max_bitrate_step_size=max_bitrate_step_size, auto_representations=auto_representations)
        self.targetQualityCrf = target_quality_crf
        self.codecMinBitrateFactor = codec_min_bitrate_factor
        self.codecMaxBitrateFactor = codec_max_bitrate_factor 
        self.codecBufsizeFactor = codec_bufsize_factor 
