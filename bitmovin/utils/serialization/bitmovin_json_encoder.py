import copy
from json import JSONEncoder
from bitmovin.resources import Resource
from .serializable import Serializable


class BitmovinJSONEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, Serializable):
            serialized_object = o.serialize()
            return self._remove_none_values(serialized_object)
        if isinstance(o, Resource):
            copied = copy.deepcopy(o.__dict__)
            copied = self._remove_none_values(copied)
            return copied
        else:
            copied = copy.deepcopy(o.__dict__)
            return copied

    @classmethod
    def _remove_none_values(cls, o):
        empty_keys = []
        for key in o.keys():
            if o.get(key) is None:
                empty_keys.append(key)
        for empty_key in empty_keys:
            o.pop(empty_key)
        return o
