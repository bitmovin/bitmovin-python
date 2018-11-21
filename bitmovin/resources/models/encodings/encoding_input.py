from bitmovin.utils import Serializable


class EncodingInput(Serializable):

    def __init__(self, input_id, input_path=None):
        super().__init__()
        self.inputId = input_id
        self.inputPath = input_path

    @classmethod
    def parse_from_json_object(cls, json_object):
        input_id = json_object['inputId']
        input_path = json_object.get('inputPath')

        encoding_input = EncodingInput(input_id=input_id, input_path=input_path)
        return encoding_input

    def serialize(self):
        serialized = super().serialize()
        serialized['inputId'] = self.inputId
        serialized['inputPath'] = self.inputPath
        return serialized
