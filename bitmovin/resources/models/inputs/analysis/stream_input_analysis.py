from bitmovin.errors import BitmovinApiError
from bitmovin.resources import Resource
from .stream_analysis_details import StreamAnalysisDetails


class StreamInputAnalysis(Resource):

    def __init__(self, input_id, input_path, details):
        super().__init__()
        self._details = None
        self.inputPath = input_path
        self.inputId = input_id
        self.details = details

    @classmethod
    def parse_from_json_object(cls, json_object):
        input_id = json_object.get('inputId')
        if input_id is None:
            raise BitmovinApiError('Invalid json object: missing field \'inputId\'')

        input_path = json_object.get('inputPath')
        if input_path is None:
            raise BitmovinApiError('Invalid json object: missing field \'inputPath\'')

        details_json = json_object.get('details')
        if details_json is None:
            raise BitmovinApiError('Invalid json object: missing field \'details_json\'')

        details = StreamInputAnalysis(input_id=input_id, input_path=input_path, details=details_json)
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
