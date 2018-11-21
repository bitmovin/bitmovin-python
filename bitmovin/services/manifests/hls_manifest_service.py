from bitmovin.resources import HlsManifest
from bitmovin.services.manifests.generic_manifest_service import GenericManifestService

from .manifest_control_service import ManifestControlService

from .video_media_service import Video
from .audio_media_service import Audio
from .subtitles_media_service import Subtitles
from .vtt_media_service import Vtt
from .closed_captions_media_service import ClosedCaptions
from .variant_stream_service import VariantStreamService


class HLS(GenericManifestService, ManifestControlService):
    manifest_type = 'hls'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, manifest_type=self.manifest_type, resource_class=HlsManifest)

        self.VideoMedia = Video(http_client=http_client)
        self.AudioMedia = Audio(http_client=http_client)
        self.SubtitlesMedia = Subtitles(http_client=http_client)
        self.VttMedia = Vtt(http_client=http_client)
        self.ClosedCaptionsMedia = ClosedCaptions(http_client=http_client)
        self.VariantStream = VariantStreamService(http_client=http_client)
