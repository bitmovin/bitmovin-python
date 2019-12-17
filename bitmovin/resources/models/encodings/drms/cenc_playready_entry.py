from bitmovin.errors import InvalidTypeError
from bitmovin.resources.models.encodings.drms import PlayReadyDRMAdditionalInformation
from bitmovin.utils import Serializable


class CENCPlayReadyEntry(Serializable):

    def __init__(self, la_url=None, pssh=None, additional_information=None):
        super().__init__()
        self.laUrl = la_url
        self.pssh = pssh
        self._additional_information = None

        if additional_information is not None:
            self.additionalInformation = additional_information

    @property
    def additionalInformation(self):
        return self._additional_information

    @additionalInformation.setter
    def additionalInformation(self, new_AdditionalInformation):
        if new_AdditionalInformation is None:
            self._additional_information = None
        elif isinstance(new_AdditionalInformation, PlayReadyDRMAdditionalInformation):
            self._additional_information = new_AdditionalInformation
        else:
            raise InvalidTypeError('Invalid type {} for playReady: must be a PlayReadyDRMAdditionalInformation!'.format(
                type(new_AdditionalInformation))
            )

    @classmethod
    def parse_from_json_object(cls, json_object):
        pssh = json_object.get('pssh')
        la_url = json_object.get('laUrl')
        additional_information = None

        if json_object.get('additionalInformation') is not None:
            additional_information = PlayReadyDRMAdditionalInformation.parse_from_json_object(
                json_object.get('additionalInformation'))

        cenc_playready_entry = CENCPlayReadyEntry(la_url, pssh, additional_information=additional_information)
        return cenc_playready_entry

    def serialize(self):
        serialized = super().serialize()
        serialized['pssh'] = self.pssh
        serialized['laUrl'] = self.laUrl
        serialized['additionalInformation'] = self.additionalInformation
        return serialized
