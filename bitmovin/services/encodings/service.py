from bitmovin.bitmovin_object import BitmovinObject
from .encoding_service import Encoding
from .stream_service import Stream
from .muxing_service import MuxingService
from .keyframe_service import KeyframeService
from .input_analysis_service import InputAnalysisService
from .ingest_input_stream_service import IngestInputStream
from .concatenation_input_stream_service import ConcatenationInputStream
from .time_based_trimming_input_stream_service import TimeBasedTrimmingInputStream
from .time_code_track_trimming_input_stream_service import TimeCodeTrackTrimmingInputStream
from .h264_picture_timing_trimming_input_stream_service import H264PictureTimingTrimmingInputStream


class EncodingService(BitmovinObject):
    def __init__(self, http_client):
        super().__init__()
        self.http_client = http_client
        self.Encoding = Encoding(http_client=self.http_client)
        self.Stream = Stream(http_client=self.http_client)
        self.Muxing = MuxingService(http_client=self.http_client)
        self.Keyframe = KeyframeService(http_client=self.http_client)
        self.InputAnalysis = InputAnalysisService(http_client=self.http_client)
        self.IngestInputStream = IngestInputStream(http_client=self.http_client)
        self.ConcatenationInputStream = ConcatenationInputStream(http_client=self.http_client)
        self.TimeBasedTrimmingInputStream = TimeBasedTrimmingInputStream(http_client=self.http_client)
        self.TimeCodeTrackTrimmingInputStream = TimeCodeTrackTrimmingInputStream(http_client=self.http_client)
        self.H264PictureTimingTrimmingInputStream = H264PictureTimingTrimmingInputStream(http_client=self.http_client)
