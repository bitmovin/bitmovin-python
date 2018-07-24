from bitmovin.utils import Serializable


class TimeCode(Serializable):

    def __init__(self, time_code_start):
        super().__init__()
        self.timeCodeStart = time_code_start

    @classmethod
    def parse_from_json_object(cls, json_object):
        time_code_start = json_object.get('timeCodeStart')
        time_code = TimeCode(time_code_start=time_code_start)
        return time_code

    def serialize(self):
        serialized = super().serialize()
        serialized['timeCodeStart'] = self.timeCodeStart
        return serialized
