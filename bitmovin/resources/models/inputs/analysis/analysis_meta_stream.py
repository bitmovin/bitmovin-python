from .analysis_stream import AnalysisStream


class AnalysisMetaStream(AnalysisStream):

    def __init__(self, id_, position, duration, codec):
        super().__init__(id_=id_, position=position, duration=duration, codec=codec)

    @classmethod
    def parse_from_json_object(cls, json_object):
        analysis_stream = AnalysisStream.parse_from_json_object(json_object=json_object)
        analysis_meta_stream = AnalysisMetaStream(id_=analysis_stream.id, position=analysis_stream.position,
                                                  duration=analysis_stream.duration, codec=analysis_stream.codec)
        return analysis_meta_stream
