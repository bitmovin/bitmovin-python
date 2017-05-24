from . import AbstractOutput


class LocalOutput(AbstractOutput):

    def __init__(self, path, id_=None, custom_data=None, name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.path = path

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        path = json_object['path']
        name = json_object.get('name')
        description = json_object.get('description')
        local_output = LocalOutput(path=path, id_=id_, name=name, description=description)
        return local_output
