from bitmovin.utils import Serializable

from . import AbstractFilter


class UnsharpFilter(AbstractFilter, Serializable):

    def __init__(self,
                 name=None,
                 luma_matrix_horizontal_size=None,
                 luma_matrix_vertical_size=None,
                 luma_effect_strength=None,
                 chroma_matrix_horizontal_size=None,
                 chroma_matrix_vertical_size=None,
                 chroma_effect_strength=None,
                 id_=None,
                 custom_data=None,
                 description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.lumaMatrixHorizontalSize = luma_matrix_horizontal_size
        self.lumaMatrixVerticalSize = luma_matrix_vertical_size
        self.lumaEffectStrength = luma_effect_strength
        self.chromaMatrixHorizontalSize = chroma_matrix_horizontal_size
        self.chromaMatrixVerticalSize = chroma_matrix_vertical_size
        self.chromaEffectStrength = chroma_effect_strength

    def serialize(self):
        serialized = super().serialize()
        return serialized

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        name = json_object.get('name')
        description = json_object.get('description')
        luma_matrix_horizontal_size = json_object.get('lumaMatrixHorizontalSize')
        luma_matrix_vertical_size = json_object.get('lumaMatrixVerticalSize')
        luma_effect_strength = json_object.get('lumaEffectStrength')
        chroma_matrix_horizontal_size = json_object.get('chromaMatrixHorizontalSize')
        chroma_matrix_vertical_size = json_object.get('chromaMatrixVerticalSize')
        chroma_effect_strength = json_object.get('chromaEffectStrength')

        unsharp_filter = UnsharpFilter(
            name=name,
            id_=id_,
            description=description,
            luma_matrix_horizontal_size=luma_matrix_horizontal_size,
            luma_matrix_vertical_size=luma_matrix_vertical_size,
            luma_effect_strength=luma_effect_strength,
            chroma_matrix_horizontal_size=chroma_matrix_horizontal_size,
            chroma_matrix_vertical_size=chroma_matrix_vertical_size,
            chroma_effect_strength=chroma_effect_strength
        )

        return unsharp_filter
