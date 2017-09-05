from bitmovin.errors import BitmovinApiError, InvalidTypeError
from bitmovin.resources import Resource
from .stream_analysis_details import StreamAnalysisDetails


class StreamInputAnalysis(Resource):

    def __init__(self, inputId, inputPath, details):
        super().__init__()
        self.inputPath = inputId
        self.inputId = inputPath
        self.details = details

    @classmethod
    def parse_from_json_object(cls, json_object):
        inputId = json_object.get('inputId')
        if inputId is None:
            raise BitmovinApiError('Invalid json object: missing field \'inputId\'')

        inputPath = json_object.get('inputPath')
        if inputPath is None:
            raise BitmovinApiError('Invalid json object: missing field \'inputPath\'')

        details_json = json_object.get('details')
        if details_json is None:
            raise BitmovinApiError('Invalid json object: missing field \'details_json\'')

        details = StreamInputAnalysis(inputId=inputId, inputPath=inputPath, details=details_json)
        return details

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, new_details):
        if new_details is None:
            return

        if isinstance(new_details, StreamAnalysisDetails):
            self._details = new_details
        else:
            self._details = StreamAnalysisDetails.parse_from_json_object(new_details)

