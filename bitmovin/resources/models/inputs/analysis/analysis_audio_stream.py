from .analysis_stream import AnalysisStream


class AnalysisAudioStream(AnalysisStream):

    def __init__(self, id_, position, duration, codec, sample_rate, bitrate, channel_format, language,
                 hearing_impaired):
        super().__init__(id_=id_, position=position, duration=duration, codec=codec)
        self.sampleRate = sample_rate
        self.bitrate = bitrate
        self.channelFormat = channel_format
        self.language = language
        self.hearingImpaired = hearing_impaired

    @classmethod
    def parse_from_json_object(cls, json_object):
        analysis_stream = AnalysisStream.parse_from_json_object(json_object=json_object)
        sample_rate = json_object.get('sampleRate')
        bitrate = json_object.get('bitrate')
        channel_format = json_object.get('channelFormat')
        language = json_object.get('language')
        hearing_impaired = json_object.get('hearingImpaired')

        analysis_audio_stream = AnalysisAudioStream(id_=analysis_stream.id, position=analysis_stream.position,
                                                    duration=analysis_stream.duration, codec=analysis_stream.codec,
                                                    sample_rate=sample_rate, bitrate=bitrate,
                                                    channel_format=channel_format, language=language,
                                                    hearing_impaired=hearing_impaired)

        return analysis_audio_stream
