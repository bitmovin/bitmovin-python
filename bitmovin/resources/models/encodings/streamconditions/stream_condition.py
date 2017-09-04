from . import AbstractStreamCondition


class StreamCondition(AbstractStreamCondition):
    def __init__(self, attribute, operator, value, type, id_=None, custom_data=None, name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        attribute = json_object.get('attribute')
        operator = json_object.get('operator')
        value = json_object.get('value')
        type = json_object.get('type')
        name = json_object.get('name')
        description = json_object.get('description')
        return StreamCondition(attribute=attribute, operator=operator, value=value, type=type, id_=id_, name=name,
                               description=description)
