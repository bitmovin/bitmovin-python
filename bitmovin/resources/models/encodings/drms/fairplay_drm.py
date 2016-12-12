from .drm import DRM


class FairPlayDRM(DRM):

    def __init__(self, key, iv=None, uri=None, outputs=None, id_=None, custom_data=None, name=None, description=None):

        super().__init__(id_=id_, custom_data=custom_data, outputs=outputs, name=name, description=description)
        self.key = key
        self.iv = iv
        self.uri = uri

    @classmethod
    def parse_from_json_object(cls, json_object):
        drm = super().parse_from_json_object(json_object=json_object)
        id_ = drm.id
        custom_data = drm.customData
        outputs = drm.outputs
        name = drm.name
        description = drm.description
        key = json_object['key']
        iv = json_object.get('iv')
        uri = json_object.get('uri')

        fairplay_drm = FairPlayDRM(key=key, iv=iv, uri=uri, outputs=outputs, id_=id_, custom_data=custom_data,
                                   name=name, description=description)

        return fairplay_drm
