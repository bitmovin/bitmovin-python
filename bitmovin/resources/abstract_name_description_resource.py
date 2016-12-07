import abc

from .resource import Resource

class AbstractNameDescriptionResource(Resource):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name=None, description=None, **kwargs):
        self.name = name
        self.description = description
        super().__init__(**kwargs)

    def parse_from_json_object(self, json_object):
        raise NotImplementedError()
