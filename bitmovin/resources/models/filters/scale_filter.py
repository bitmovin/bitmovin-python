from bitmovin.utils import Serializable

from bitmovin.errors import InvalidTypeError

from bitmovin.resources.enums import ScalingAlgorithm
from . import AbstractFilter


class ScaleFilter(AbstractFilter, Serializable):

    def __init__(self, name=None, width=None, height=None, scaling_algorithm=None, id_=None, custom_data=None,
                 description=None, sample_aspect_ratio_numerator=None, sample_aspect_ratio_denominator=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.width = width
        self.height = height
        self._scaling_algorithm = None
        self.scalingAlgorithm = scaling_algorithm
        self.sampleAspectRatioNumerator = sample_aspect_ratio_numerator
        self.sampleAspectRatioDenominator = sample_aspect_ratio_denominator

    @property
    def scalingAlgorithm(self):
        return self._scaling_algorithm

    @scalingAlgorithm.setter
    def scalingAlgorithm(self, new_value):
        if new_value is None:
            self._scaling_algorithm = None
            return
        if isinstance(new_value, str):
            self._scaling_algorithm = new_value
        elif isinstance(new_value, ScalingAlgorithm):
            self._scaling_algorithm = new_value.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for scalingAlgorithm: ' +
                'must be either str or ScalingAlgorithm!'.format(type(new_value)))

    def serialize(self):
        serialized = super().serialize()
        serialized['scalingAlgorithm'] = self.scalingAlgorithm
        return serialized

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        scaling_algorithm = json_object.get('scalingAlgorithm')
        width = json_object.get('width')
        height = json_object.get('height')
        name = json_object.get('name')
        description = json_object.get('description')
        sample_aspect_ratio_numerator = json_object.get('sampleAspectRatioNumerator')
        sample_aspect_ratio_denominator = json_object.get('sampleAspectRatioDenominator')
        scale_filter = ScaleFilter(
            name=name,
            width=width,
            height=height,
            scaling_algorithm=scaling_algorithm,
            id_=id_,
            description=description,
            sample_aspect_ratio_numerator=sample_aspect_ratio_numerator,
            sample_aspect_ratio_denominator=sample_aspect_ratio_denominator
        )
        return scale_filter
