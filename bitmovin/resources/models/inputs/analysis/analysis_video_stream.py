from .analysis_stream import AnalysisStream


class AnalysisVideoStream(AnalysisStream):

    def __init__(self, id_, position, duration, codec, fps, bitrate, width, height):
        super().__init__(id_=id_, position=position, duration=duration, codec=codec)
        self.fps = fps
        self.bitrate = bitrate
        self.width = width
        self.height = height

    @classmethod
    def parse_from_json_object(cls, json_object):
        analysis_stream = AnalysisStream.parse_from_json_object(json_object=json_object)
        fps = json_object.get('fps')
        bitrate = json_object.get('bitrate')
        width = json_object.get('width')
        height = json_object.get('height')

        analysis_video_stream = AnalysisVideoStream(id_=analysis_stream.id, position=analysis_stream.position,
                                                    duration=analysis_stream.duration, codec=analysis_stream.codec,
                                                    fps=fps, bitrate=bitrate, width=width, height=height)

        return analysis_video_stream
