from bitmovin.utils import Serializable


class AutoRestartConfiguration(Serializable):
    def __init__(self, segments_written_timeout: float = None, bytes_written_timeout: float = None,
                 frames_written_timeout: float = None, hls_manifests_update_timeout: float = None,
                 dash_manifests_update_timeout: float = None, schedule_expression: str = None):
        super().__init__()
        self.segmentsWrittenTimeout = segments_written_timeout
        self.bytesWrittenTimeout = bytes_written_timeout
        self.framesWrittenTimeout = frames_written_timeout
        self.hlsManifestsUpdateTimeout = hls_manifests_update_timeout
        self.dashManifestsUpdateTimeout = dash_manifests_update_timeout
        self.scheduleExpression = schedule_expression
