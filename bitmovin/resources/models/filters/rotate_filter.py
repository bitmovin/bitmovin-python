from . import AbstractFilter


class RotateFilter(AbstractFilter):

    def __init__(self, rotation=None, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self.rotation = rotation

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        rotation = json_object['rotation']
        rotate_filter = RotateFilter(rotation=rotation, id_=id_)
        return rotate_filter
