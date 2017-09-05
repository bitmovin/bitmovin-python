from bitmovin.errors import InvalidTypeError
from bitmovin.resources import Resource
from .analysis_audio_stream import AnalysisAudioStream
from .analysis_video_stream import AnalysisVideoStream


class StreamAnalysisDetails(Resource):

    def __init__(self, audio_streams, video_streams):
        super().__init__()
        self._audioStreams = None
        self._videoStreams = None

        self.audioStreams = audio_streams
        self.videoStreams = video_streams

    @classmethod
    def parse_from_json_object(cls, json_object):
        audio_streams = json_object.get('audioStreams')
        video_streams = json_object.get('videoStreams')
        details = StreamAnalysisDetails(audio_streams=audio_streams, video_streams=video_streams)
        return details

    @property
    def audioStreams(self):
        return self._audioStreams

    @audioStreams.setter
    def audioStreams(self, new_audio_streams):
        if new_audio_streams is None:
            return

        if not isinstance(new_audio_streams, list):
            raise InvalidTypeError('audioStreams has to be a list')

        if all(isinstance(audio_stream, AnalysisAudioStream) for audio_stream in new_audio_streams):
            self._audioStreams = new_audio_streams
        else:
            audio_streams = []
            for json_message in new_audio_streams:
                audio_stream = AnalysisAudioStream.parse_from_json_object(json_message)
                audio_streams.append(audio_stream)
            self._audioStreams = audio_streams

    @property
    def videoStreams(self):
        return self._videoStreams

    @videoStreams.setter
    def videoStreams(self, new_video_streams):
        if new_video_streams is None:
            return

        if not isinstance(new_video_streams, list):
            raise InvalidTypeError('videoStreams has to be a list')

        if all(isinstance(video_stream, AnalysisVideoStream) for video_stream in new_video_streams):
            self._videoStreams = new_video_streams
        else:
            video_streams = []
            for json_message in new_video_streams:
                video_stream = AnalysisVideoStream.parse_from_json_object(json_message)
                video_streams.append(video_stream)
            self._videoStreams = video_streams
