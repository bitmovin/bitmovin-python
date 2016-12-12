from . import AbstractFilter


class CropFilter(AbstractFilter):

    def __init__(self, name=None, left=None, right=None, top=None, bottom=None, id_=None, custom_data=None,
                 description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        left = json_object.get('left')
        right = json_object.get('right')
        top = json_object.get('top')
        bottom = json_object.get('bottom')
        name = json_object.get('name')
        description = json_object.get('description')
        crop_filter = CropFilter(
            left=left, right=right, top=top, bottom=bottom, id_=id_, name=name, description=description)
        return crop_filter
