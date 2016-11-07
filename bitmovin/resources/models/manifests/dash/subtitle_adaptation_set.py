from .abstract_adaptation_set import AbstractAdaptationSet


class SubtitleAdaptationSet(AbstractAdaptationSet):

    def __init__(self, lang, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self.lang = lang

    @classmethod
    def parse_from_json_object(cls, json_object):
        adaptation_set = AbstractAdaptationSet.parse_from_json_object(json_object=json_object)
        id_ = adaptation_set.id
        custom_data = adaptation_set.customData
        lang = json_object['lang']

        audio_adaptation_set = SubtitleAdaptationSet(id_=id_, custom_data=custom_data, lang=lang)
        return audio_adaptation_set
