from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable
from .broadcast_ts_audio_stream_configuration import BroadcastTsAudioStreamConfiguration
from .broadcast_ts_program_configuration import BroadcastTsProgramConfiguration
from .broadcast_ts_transport_configuration import BroadcastTsTransportConfiguration
from .broadcast_ts_video_stream_configuration import BroadcastTsVideoStreamConfiguration


class BroadcastTsMuxingConfiguration(Serializable):

    def __init__(self, transport=None, program=None, video_streams=None, audio_streams=None):
        super().__init__()
        self.program = program

        self._transport = None
        self.transport = transport

        self._video_streams = None
        self.videoStreams = video_streams

        self._audio_streams = None
        self.audioStreams = audio_streams

    @property
    def transport(self):
        return self._transport

    @transport.setter
    def transport(self, new_transport):
        if new_transport is None:
            self._transport = None
            return

        if isinstance(new_transport, BroadcastTsTransportConfiguration):
            self._transport = new_transport
        else:
            raise InvalidTypeError(
                'Invalid type {} for transport: must be BroadcastTsTransportConfiguration!'.format(type(new_transport))
            )

    @property
    def videoStreams(self):
        return self._video_streams

    @videoStreams.setter
    def videoStreams(self, new_video_streams):
        if new_video_streams is None:
            self._video_streams = None
            return

        if not isinstance(new_video_streams, list):
            raise InvalidTypeError(
                'Invalid type {} for videoStreams: must be list!'.format(type(new_video_streams))
            )

        if all(isinstance(video_stream, BroadcastTsVideoStreamConfiguration) for video_stream in new_video_streams):
            self._video_streams = new_video_streams
        else:
            video_streams = []
            for json_object in new_video_streams:
                video_stream = BroadcastTsVideoStreamConfiguration.parse_from_json_object(json_object=json_object)
                video_streams.append(video_stream)
            self._video_streams = video_streams

    @property
    def audioStreams(self):
        return self._audio_streams

    @audioStreams.setter
    def audioStreams(self, new_audio_streams):
        if new_audio_streams is None:
            self._audio_streams = None
            return

        if not isinstance(new_audio_streams, list):
            raise InvalidTypeError(
                'Invalid type {} for audioStreams: must be list!'.format(type(new_audio_streams))
            )

        if all(isinstance(audio_stream, BroadcastTsAudioStreamConfiguration) for audio_stream in new_audio_streams):
            self._audio_streams = new_audio_streams
        else:
            audio_streams = []
            for json_object in new_audio_streams:
                audio_stream = BroadcastTsAudioStreamConfiguration.parse_from_json_object(json_object)
                audio_streams.append(audio_stream)
            self._audio_streams = audio_streams

    def serialize(self):
        serialized = super().serialize()
        serialized['transport'] = self.transport
        serialized['program'] = self.program
        serialized['videoStreams'] = self.videoStreams
        serialized['audioStreams'] = self.audioStreams
        return serialized

    @classmethod
    def parse_from_json_object(cls, json_object):
        transport_json = json_object.get('transport')
        transport = BroadcastTsTransportConfiguration.parse_from_json_object(transport_json)

        program_json = json_object.get('program')
        program = BroadcastTsProgramConfiguration.parse_from_json_object(program_json)

        video_streams = json_object.get('videoStreams')
        audio_streams = json_object.get('audioStreams')

        broadcast_ts_muxing_configuration = BroadcastTsMuxingConfiguration(transport=transport, program=program,
                                                                           video_streams=video_streams,
                                                                           audio_streams=audio_streams)
        return broadcast_ts_muxing_configuration
