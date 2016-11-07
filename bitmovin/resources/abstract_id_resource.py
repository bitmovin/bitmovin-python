import abc

from .resource import Resource


class AbstractIdResource(Resource):
    __metaclass__ = abc.ABCMeta

    def __init__(self, id_=None, **kwargs):
        self.id = id_
        super().__init__(**kwargs)

    def parse_from_json_object(self, json_object):
        raise NotImplementedError()
