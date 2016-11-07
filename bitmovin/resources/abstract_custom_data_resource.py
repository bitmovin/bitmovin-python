import abc

from .resource import Resource


class AbstractCustomDataResource(Resource):
    __metaclass__ = abc.ABCMeta

    def __init__(self, custom_data=None, **kwargs):
        self.customData = custom_data
        super().__init__(**kwargs)

    def parse_from_json_object(self, json_object):
        raise NotImplementedError()
