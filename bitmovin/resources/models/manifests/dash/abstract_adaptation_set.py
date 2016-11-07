from bitmovin.resources.models import AbstractModel


class AbstractAdaptationSet(AbstractModel):

    def __init__(self, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        custom_data = json_object.get('customData')
        abstract_adaptation_set = AbstractAdaptationSet(id_=id_, custom_data=custom_data)
        return abstract_adaptation_set
