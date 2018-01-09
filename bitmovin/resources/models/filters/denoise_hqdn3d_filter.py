from . import AbstractFilter


class DenoiseHqdn3dFilter(AbstractFilter):

    def __init__(self, name=None, luma_spatial=None, chroma_spatial=None, luma_tmp=None, chroma_tmp=None, id_=None,
                 custom_data=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.lumaSpatial = luma_spatial
        self.chromaSpatial = chroma_spatial
        self.lumaTmp = luma_tmp
        self.chromaTmp = chroma_tmp

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        luma_spatial = json_object.get('lumaSpatial')
        chroma_spatial = json_object.get('chromaSpatial')
        luma_tmp = json_object.get('lumaTmp')
        chroma_tmp = json_object.get('chromaTmp')
        name = json_object.get('name')
        description = json_object.get('description')
        crop_filter = DenoiseHqdn3dFilter(
            luma_spatial=luma_spatial, chroma_spatial=chroma_spatial, luma_tmp=luma_tmp, chroma_tmp=chroma_tmp, id_=id_,
            name=name, description=description)
        return crop_filter
