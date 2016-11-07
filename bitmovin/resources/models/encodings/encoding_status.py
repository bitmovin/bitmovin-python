from bitmovin.resources import AbstractIdResource


class EncodingStatus(AbstractIdResource):

    def __init__(self, status, number_of_segments=None, id_=None):
        super().__init__(id_=id_)

        self.status = status
        self.numberOfSegments = number_of_segments

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        status = json_object['status']
        number_of_segments = json_object.get('numberOfSegments')

        encoding_status = EncodingStatus(status=status, number_of_segments=number_of_segments, id_=id_)
        return encoding_status
