from .abstract_adaptation_set import AbstractAdaptationSet


class VideoAdaptationSet(AbstractAdaptationSet):

    def __init__(self, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)

    @classmethod
    def parse_from_json_object(cls, json_object):
        adaptation_set = AbstractAdaptationSet.parse_from_json_object(json_object=json_object)
        id_ = adaptation_set.id
        custom_data = adaptation_set.customData
        audio_adaptation_set = VideoAdaptationSet(id_=id_, custom_data=custom_data)
        return audio_adaptation_set
