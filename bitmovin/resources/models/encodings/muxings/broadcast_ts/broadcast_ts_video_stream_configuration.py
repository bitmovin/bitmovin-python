from .broadcast_input_stream_configuration import BroadcastTsInputStreamConfiguration


class BroadcastTsVideoStreamConfiguration(BroadcastTsInputStreamConfiguration):

    def __init__(self, stream_id, packet_identifier=None, start_with_discontinuity_indicator=None, align_pes=None,
                 set_rai_on_au=None, insert_access_unit_delimiter_in_avc=None, max_decode_delay=None):
        super().__init__(stream_id=stream_id, packet_identifier=packet_identifier,
                         start_with_discontinuity_indicator=start_with_discontinuity_indicator, align_pes=align_pes,
                         set_rai_on_au=set_rai_on_au)

        self.insertAccessUnitDelimiterinAvc = insert_access_unit_delimiter_in_avc
        self.maxDecodeDelay = max_decode_delay

    @classmethod
    def parse_from_json_object(cls, json_object):
        input_stream_configuration = super().parse_from_json_object(json_object=json_object)

        stream_id = input_stream_configuration.streamId
        packet_identifier = input_stream_configuration.packetIdentifier
        start_with_discontinuity_indicator = input_stream_configuration.startWithDiscontinuityIndicator
        align_pes = input_stream_configuration.alignPes
        set_rai_on_au = input_stream_configuration.setRaiOnAu

        insert_access_unit_delimiter_in_avc = json_object.get('insertAccessUnitDelimiterInAvc')
        max_decode_delay = json_object.get('maxDecodeDelay')

        broadcast_ts_video_stream_configuration = BroadcastTsVideoStreamConfiguration(
            stream_id=stream_id,
            packet_identifier=packet_identifier,
            start_with_discontinuity_indicator=start_with_discontinuity_indicator,
            align_pes=align_pes,
            set_rai_on_au=set_rai_on_au,
            insert_access_unit_delimiter_in_avc=insert_access_unit_delimiter_in_avc,
            max_decode_delay=max_decode_delay
        )
        return broadcast_ts_video_stream_configuration
