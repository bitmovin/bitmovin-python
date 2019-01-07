from bitmovin.resources.models.encodings.pertitle.per_title_configuration import PerTitleConfiguration


class VP9PerTitleConfiguration(PerTitleConfiguration):
    def __init__(self, min_bitrate=None, max_bitrate=None, min_bitrate_step_size=None,
                 max_bitrate_step_size=None, target_quality_crf=None, auto_representations=None,
				 complexity_factor=None):
        super().__init__(min_bitrate=min_bitrate, max_bitrate=max_bitrate, min_bitrate_step_size=min_bitrate_step_size,
                         max_bitrate_step_size=max_bitrate_step_size, auto_representations=auto_representations,
                         complexity_factor=complexity_factor)
        self.targetQualityCrf = target_quality_crf
