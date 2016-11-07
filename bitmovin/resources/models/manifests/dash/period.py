from bitmovin.resources.models import AbstractModel


class Period(AbstractModel):

    def __init__(self, start=None, duration=None, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self.start = start
        self.duration = duration

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        custom_data = json_object.get('customData')
        start = json_object.get('start')
        duration = json_object.get('duration')
        period = Period(
            id_=id_, custom_data=custom_data, start=start, duration=duration)
        return period
