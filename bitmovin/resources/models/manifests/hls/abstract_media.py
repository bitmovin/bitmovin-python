from bitmovin.resources import AbstractIdResource


class AbstractMedia(AbstractIdResource):

    def __init__(self, name, group_id, language=None, assoc_language=None, is_default=None, autoselect=None,
                 characteristics=None, id_=None):
        super().__init__(id_=id_)
        self.name = name
        self.groupId = group_id
        self.language = language
        self.assocLanguage = assoc_language
        self.isDefault = is_default
        self.autoselect = autoselect
        self.characteristics = characteristics

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        name = json_object.get('name')
        group_id = json_object.get('groupId')
        language = json_object.get('language')
        assoc_language = json_object.get('assocLanguage')
        is_default = json_object.get('isDefault')
        autoselect = json_object.get('autoselect')
        characteristics = json_object.get('characteristics')

        abstract_media = AbstractMedia(id_=id_, name=name, group_id=group_id, language=language,
                                       assoc_language=assoc_language, is_default=is_default, autoselect=autoselect,
                                       characteristics=characteristics)

        return abstract_media
