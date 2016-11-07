from .analysis_stream import AnalysisStream


class AnalysisSubtitleStream(AnalysisStream):

    def __init__(self, id_, position, duration, codec, language, hearing_impaired):
        super().__init__(id_=id_, position=position, duration=duration, codec=codec)
        self.language = language
        self.hearingImpaired = hearing_impaired

    @classmethod
    def parse_from_json_object(cls, json_object):
        analysis_stream = AnalysisStream.parse_from_json_object(json_object=json_object)
        language = json_object.get('language')
        hearing_impaired = json_object.get('hearingImpaired')

        analysis_subtitle_stream = AnalysisSubtitleStream(id_=analysis_stream.id, position=analysis_stream.position,
                                                          duration=analysis_stream.duration,
                                                          codec=analysis_stream.codec, language=language,
                                                          hearing_impaired=hearing_impaired)
        return analysis_subtitle_stream
