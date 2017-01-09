from . import AbstractFilter


class RotateFilter(AbstractFilter):

    def __init__(self, name=None, rotation=None, id_=None, custom_data=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.rotation = rotation

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        rotation = json_object['rotation']
        name = json_object.get('name')
        description = json_object.get('description')
        rotate_filter = RotateFilter(rotation=rotation, id_=id_, name=name, description=description)
        return rotate_filter
