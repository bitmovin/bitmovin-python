from bitmovin.resources import Resource
from bitmovin.resources.models.encodings.muxings.information import ByteRange
from bitmovin.errors import InvalidTypeError
from bitmovin.utils.serialization import Serializable

from .muxing_information_video_track import MuxingInformationVideoTrack
from .muxing_information_audio_track import MuxingInformationAudioTrack


class ProgressiveTSInformation(Resource, Serializable):

    def __init__(self, mime_type=None, file_size=None, container_format=None, container_bitrate=None, duration=None,
                 video_tracks=None, audio_tracks=None, byte_ranges=None):
        super().__init__()

        self.mime_type = mime_type
        self.file_size = file_size
        self.container_format = container_format
        self.container_bitrate = container_bitrate
        self.duration = duration

        self._video_tracks = None
        self._audio_tracks = None
        self._byte_ranges = None

        self.video_tracks = video_tracks
        self.audio_tracks = audio_tracks
        self.byte_ranges = byte_ranges

    @classmethod
    def parse_from_json_object(cls, json_object):
        mime_type = json_object.get('mimeType')
        file_size = json_object.get('fileSize')
        container_format = json_object.get('containerFormat')
        container_bitrate = json_object.get('containerBitrate')
        duration = json_object.get('duration')

        video_tracks = json_object.get('videoTracks')
        audio_tracks = json_object.get('audioTracks')
        byte_ranges = json_object.get('byteRanges')

        progressive_ts_muxing_information = ProgressiveTSInformation(mime_type=mime_type,
                                                                     file_size=file_size,
                                                                     container_format=container_format,
                                                                     container_bitrate=container_bitrate,
                                                                     duration=duration,
                                                                     video_tracks=video_tracks,
                                                                     audio_tracks=audio_tracks,
                                                                     byte_ranges=byte_ranges)

        return progressive_ts_muxing_information

    @property
    def audio_tracks(self):
        return self._audio_tracks

    @audio_tracks.setter
    def audio_tracks(self, new_audio_tracks):
        if new_audio_tracks is None:
            return

        if not isinstance(new_audio_tracks, list):
            raise InvalidTypeError('new_audio_tracks has to be a list of MuxingInformationAudioTrack objects')

        if all(isinstance(audio_track, MuxingInformationAudioTrack) for audio_track in new_audio_tracks):
            self._audio_tracks = new_audio_tracks
        else:
            audio_tracks = []
            for json_object in new_audio_tracks:
                audio_track = MuxingInformationAudioTrack.parse_from_json_object(json_object)
                audio_tracks.append(audio_track)
            self._audio_tracks = audio_tracks

    @property
    def video_tracks(self):
        return self._video_tracks

    @video_tracks.setter
    def video_tracks(self, new_video_tracks):
        if new_video_tracks is None:
            return

        if not isinstance(new_video_tracks, list):
            raise InvalidTypeError('new_video_tracks has to be a list of MuxingInformationVideoTrack objects')

        if all(isinstance(video_track, MuxingInformationVideoTrack) for video_track in new_video_tracks):
            self._video_tracks = new_video_tracks
        else:
            video_tracks = []
            for json_object in new_video_tracks:
                video_track = MuxingInformationVideoTrack.parse_from_json_object(json_object)
                video_tracks.append(video_track)
            self._video_tracks = video_tracks

    @property
    def byte_ranges(self):
        return self._byte_ranges

    @byte_ranges.setter
    def byte_ranges(self, new_value):
        if new_value is None:
            return

        if not isinstance(new_value, list):
            raise InvalidTypeError('byte_ranges has to be a list of ByteRange instances')

        if all(isinstance(output, ByteRange) for output in new_value):
            byte_ranges = []
            for item in new_value:
                byte_ranges.append(item)
            self._byte_ranges = byte_ranges
        else:
            byte_ranges = []
            for item in new_value:
                byte_ranges.append(ByteRange.parse_from_json_object(item))
            self._byte_ranges = byte_ranges

    def serialize(self):
        serialized = super().serialize()
        serialized['videoTracks'] = self.video_tracks
        serialized['audioTracks'] = self.audio_tracks
        serialized['byteRanges'] = self.byte_ranges
        return serialized
