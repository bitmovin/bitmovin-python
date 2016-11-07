from . import AbstractModel


class MinimalModel(AbstractModel):

    def __init__(self, id_):
        super().__init__(id_=id_)

    @classmethod
    def parse_from_json_object(cls, json_object):
        minimal_model = MinimalModel(id_=json_object.get('id'))
        return minimal_model
