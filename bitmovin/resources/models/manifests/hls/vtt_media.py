from .abstract_media import AbstractMedia


class VttMedia(AbstractMedia):

    def __init__(self, name, group_id, vtt_url, language=None, assoc_language=None, is_default=None, autoselect=None,
                 characteristics=None, uri=None, id_=None):
        super().__init__(id_=id_, name=name, group_id=group_id, language=language, assoc_language=assoc_language,
                         is_default=is_default, autoselect=autoselect, characteristics=characteristics)
        self.vttUrl = vtt_url
        self.uri = uri

    @classmethod
    def parse_from_json_object(cls, json_object):
        media = super().parse_from_json_object(json_object=json_object)
        id_ = media.id
        name = media.name
        group_id = media.groupId
        language = media.language
        assoc_language = media.assocLanguage
        is_default = media.isDefault
        autoselect = media.autoselect
        characteristics = media.characteristics
        vtt_url = json_object.get('vttUrl')
        uri = json_object.get('uri')

        vtt_media = VttMedia(id_=id_, name=name, group_id=group_id, language=language, assoc_language=assoc_language,
                             is_default=is_default, autoselect=autoselect, characteristics=characteristics,
                             vtt_url=vtt_url, uri=uri)

        return vtt_media
