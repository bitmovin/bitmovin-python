from bitmovin.errors import BitmovinApiError, InvalidTypeError
from bitmovin.resources import Resource
from .analysis_audio_stream import AnalysisAudioStream
from .analysis_video_stream import AnalysisVideoStream
from .analysis_meta_stream import AnalysisMetaStream
from .analysis_subtitle_stream import AnalysisSubtitleStream
from .analysis_message import AnalysisMessage


class AnalysisDetails(Resource):

    def __init__(self, id_, path, cloud_region, audio_streams, video_streams, meta_streams, subtitle_streams, messages,
                 meta_data):
        super().__init__()
        self._audioStreams = None
        self._videoStreams = None
        self._metaStreams = None
        self._subtitleStreams = None
        self._messages = None

        self.id = id_
        self.path = path
        self.cloudRegion = cloud_region
        self.audioStreams = audio_streams
        self.videoStreams = video_streams
        self.metaStreams = meta_streams
        self.subtitleStreams = subtitle_streams
        self.messages = messages
        self.metaData = meta_data

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        if id_ is None:
            raise BitmovinApiError('Invalid json object: missing field \'id\'')
        path = json_object.get('path')
        if path is None:
            raise BitmovinApiError('Invalid json object: missing field \'path\'')
        cloud_region = json_object.get('cloudRegion')
        messages = json_object.get('messages')
        audio_streams = json_object.get('audioStreams')
        video_streams = json_object.get('videoStreams')
        meta_streams = json_object.get('metaStreams')
        subtitle_streams = json_object.get('subtitleStreams')
        meta_data = json_object.get('metaData')
        details = AnalysisDetails(
            id_=id, path=path, cloud_region=cloud_region, audio_streams=audio_streams, video_streams=video_streams,
            meta_streams=meta_streams, subtitle_streams=subtitle_streams, messages=messages, meta_data=meta_data
        )
        return details

    @property
    def audioStreams(self):
        return self._audioStreams

    @audioStreams.setter
    def audioStreams(self, new_audio_streams):
        if new_audio_streams is None:
            return

        if not isinstance(new_audio_streams, list):
            raise InvalidTypeError('messages has to be a list of Message objects')

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
            raise InvalidTypeError('messages has to be a list of Message objects')

        if all(isinstance(video_stream, AnalysisVideoStream) for video_stream in new_video_streams):
            self._videoStreams = new_video_streams
        else:
            video_streams = []
            for json_message in new_video_streams:
                video_stream = AnalysisVideoStream.parse_from_json_object(json_message)
                video_streams.append(video_stream)
            self._videoStreams = video_streams
            
    @property
    def metaStreams(self):
        return self._metaStreams

    @metaStreams.setter
    def metaStreams(self, new_meta_streams):
        if new_meta_streams is None:
            return

        if not isinstance(new_meta_streams, list):
            raise InvalidTypeError('messages has to be a list of Message objects')

        if all(isinstance(meta_stream, AnalysisMetaStream) for meta_stream in new_meta_streams):
            self._metaStreams = new_meta_streams
        else:
            meta_streams = []
            for json_message in new_meta_streams:
                meta_stream = AnalysisMetaStream.parse_from_json_object(json_message)
                meta_streams.append(meta_stream)
            self._metaStreams = meta_streams

    @property
    def subtitleStreams(self):
        return self._subtitleStreams

    @subtitleStreams.setter
    def subtitleStreams(self, new_subtitle_streams):
        if new_subtitle_streams is None:
            return
    
        if not isinstance(new_subtitle_streams, list):
            raise InvalidTypeError('messages has to be a list of Message objects')
    
        if all(isinstance(subtitle_stream, AnalysisSubtitleStream) for subtitle_stream in new_subtitle_streams):
            self._subtitleStreams = new_subtitle_streams
        else:
            subtitle_streams = []
            for json_message in new_subtitle_streams:
                subtitle_stream = AnalysisSubtitleStream.parse_from_json_object(json_message)
                subtitle_streams.append(subtitle_stream)
            self._subtitleStreams = subtitle_streams

    @property
    def messages(self):
        return self._messages

    @messages.setter
    def messages(self, new_messages):
        if new_messages is None:
            return

        if not isinstance(new_messages, list):
            raise InvalidTypeError('messages has to be a list of Message objects')

        if all(isinstance(message, AnalysisMessage) for message in new_messages):
            self._messages = new_messages
        else:
            messages = []
            for json_message in new_messages:
                message = AnalysisMessage.parse_from_json_object(json_message)
                messages.append(message)
            self._messages = messages
