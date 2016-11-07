import abc

from bitmovin.resources import AbstractCustomDataResource, AbstractIdResource


class AbstractModel(AbstractCustomDataResource, AbstractIdResource):
    __metaclass__ = abc.ABCMeta

    def __init__(self, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)

    def parse_from_json_object(self, json_object):
        raise NotImplementedError()
