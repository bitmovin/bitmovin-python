from bitmovin.resources import Resource
from bitmovin.errors import InvalidTypeError
from bitmovin.resources.models.encodings.muxings.information.muxing_information_audio_track import \
    MuxingInformationAudioTrack
from bitmovin.resources.models.encodings.muxings.information.muxing_information_video_track import \
    MuxingInformationVideoTrack

from bitmovin.utils import Serializable


class Mp4MuxingInformation(Resource, Serializable):

    def __init__(self, mime_type=None, file_size=None, container_format=None, container_bitrate=None,
                 duration=None, video_tracks=None, audio_tracks=None):
        super().__init__()

        self.mimeType = mime_type
        self.fileSize = file_size
        self.containerFormat = container_format
        self.containerBitrate = container_bitrate
        self.duration = duration

        self._video_tracks = None
        self._audio_tracks = None
        self.audio_tracks = audio_tracks
        self.video_tracks = video_tracks

    @classmethod
    def parse_from_json_object(cls, json_object):
        mime_type = json_object.get('mimeType')
        file_size = json_object.get('fileSize')
        container_format = json_object.get('containerFormat')
        container_bitrate = json_object.get('containerBitrate')
        duration = json_object.get('duration')

        video_tracks = json_object.get('videoTracks')
        audio_tracks = json_object.get('audioTracks')

        mp4_muxing_information = Mp4MuxingInformation(mime_type=mime_type,
                                                      file_size=file_size,
                                                      container_format=container_format,
                                                      container_bitrate=container_bitrate,
                                                      duration=duration,
                                                      video_tracks=video_tracks,
                                                      audio_tracks=audio_tracks)

        return mp4_muxing_information

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

    def serialize(self):
        serialized = super().serialize()
        serialized['videoTracks'] = self.video_tracks
        serialized['audioTracks'] = self.audio_tracks
        return serialized
