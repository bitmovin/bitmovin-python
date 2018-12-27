from .abstract_trimming_input_stream import AbstractTrimmingInputStream


class TimeBasedTrimmingInputStream(AbstractTrimmingInputStream):

    def __init__(self, input_stream_id, offset=None, duration=None, id_=None, custom_data=None, name=None,
                 description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description,
                         input_stream_id=input_stream_id)

        self.inputStreamId = input_stream_id
        self.offset = offset
        self.duration = duration

    @classmethod
    def parse_from_json_object(cls, json_object):
        trimming_input_stream = AbstractTrimmingInputStream.parse_from_json_object(json_object=json_object)

        input_stream_id = trimming_input_stream.inputStreamId
        id_ = trimming_input_stream.id
        custom_data = trimming_input_stream.customData
        name = trimming_input_stream.name
        description = trimming_input_stream.description
        offset = json_object.get('offset')
        duration = json_object.get('duration')

        time_based_trimming_input_stream = TimeBasedTrimmingInputStream(
            input_stream_id=input_stream_id,
            offset=offset,
            duration=duration,
            id_=id_,
            custom_data=custom_data,
            name=name,
            description=description
        )

        return time_based_trimming_input_stream
