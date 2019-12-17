from bitmovin.utils import Serializable


class PlayReadyDRMAdditionalInformation(Serializable):

    def __init__(self, wrm_header_custom_attributes=None):
        super().__init__()
        self.wrmHeaderCustomAttributes = wrm_header_custom_attributes

    @classmethod
    def parse_from_json_object(cls, json_object):
        wrm_header_custom_attributes = json_object.get('wrmHeaderCustomAttributes')

        playready_drm_additional_information = PlayReadyDRMAdditionalInformation(
            wrm_header_custom_attributes=wrm_header_custom_attributes)

        return playready_drm_additional_information
