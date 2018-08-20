from bitmovin.utils import Serializable


class StreamMetadata(Serializable):

    def __init__(self, language):
        super().__init__()
        self.language = language

    @classmethod
    def parse_from_json_object(cls, json_object):
        language = json_object.get('language')
        stream_metadata = StreamMetadata(language=language)
        return stream_metadata

    def serialize(self):
        serialized = super().serialize()
        serialized['language'] = self.language
        return serialized
