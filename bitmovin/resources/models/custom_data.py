from bitmovin.resources import AbstractCustomDataResource


class CustomData(AbstractCustomDataResource):

    def __init__(self, created_at, modified_at, custom_data):
        super().__init__(custom_data=custom_data)
        self.createdAt = created_at
        self.modifiedAt = modified_at

    @classmethod
    def parse_from_json_object(cls, json_object):
        created_at = json_object.get('createdAt')
        modified_at = json_object.get('modifiedAt')
        data = json_object.get('customData')
        custom_data = CustomData(created_at=created_at, modified_at=modified_at, custom_data=data)
        return custom_data
