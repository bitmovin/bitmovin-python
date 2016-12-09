from .drm import DRM


class AESDRM(DRM):

    def __init__(self, name, method, key, key_file_uri, iv=None, outputs=None, id_=None, custom_data=None,
                 description=None):

        super().__init__(id_=id_, custom_data=custom_data, outputs=outputs, name=name, description=description)
        self.method = method
        self.key = key
        self.keyFileUri = key_file_uri
        self.iv = iv

    @classmethod
    def parse_from_json_object(cls, json_object):
        drm = super().parse_from_json_object(json_object=json_object)
        id_ = drm.id
        custom_data = drm.customData
        outputs = drm.outputs
        name = drm.name
        description = drm.description
        method = json_object['method']
        key = json_object['key']
        key_file_uri = json_object['keyFileUri']
        iv = json_object.get('iv')

        aes_drm = AESDRM(method=method, key=key, key_file_uri=key_file_uri, iv=iv, outputs=outputs, id_=id_,
                         custom_data=custom_data, name=name, description=description)

        return aes_drm
