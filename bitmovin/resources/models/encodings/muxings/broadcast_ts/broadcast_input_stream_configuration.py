from bitmovin.utils import Serializable
from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums.set_rai_on_au import SetRaiOnAu


class BroadcastTsInputStreamConfiguration(Serializable):

    def __init__(self, stream_id, packet_identifier=None, start_with_discontinuity_indicator=None, align_pes=None,
                 set_rai_on_au=None):
        super().__init__()
        self.streamId = stream_id
        self.packetIdentifier = packet_identifier
        self.startWithDiscontinuityIndicator = start_with_discontinuity_indicator
        self.alignPes = align_pes
        self._setRaiOnAu = None
        self.setRaiOnAu = set_rai_on_au

    @property
    def setRaiOnAu(self):
        return self._setRaiOnAu

    @setRaiOnAu.setter
    def setRaiOnAu(self, set_rai_on_au):
        if set_rai_on_au is None:
            return
        if isinstance(set_rai_on_au, str):
            self._setRaiOnAu = set_rai_on_au
        elif isinstance(set_rai_on_au, SetRaiOnAu):
            self._setRaiOnAu = set_rai_on_au.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for setRaiOnAu: must be either str or SetRaiOnAu!'.format(type(set_rai_on_au))
            )

    @classmethod
    def parse_from_json_object(cls, json_object):
        stream_id = json_object.get('streamId')
        packet_identifier = json_object.get('packetIdentifier')
        start_with_discontinuity_indicator = json_object.get('startWithDiscontinuityIndicator')
        align_pes = json_object.get('alignPes')
        set_rai_on_au = json_object.get('setRaiOnAu')

        return BroadcastTsInputStreamConfiguration(
            stream_id=stream_id, packet_identifier=packet_identifier,
            start_with_discontinuity_indicator=start_with_discontinuity_indicator,
            align_pes=align_pes, set_rai_on_au=set_rai_on_au
        )
