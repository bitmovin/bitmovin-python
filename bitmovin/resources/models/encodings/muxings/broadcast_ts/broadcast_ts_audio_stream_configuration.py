from .broadcast_input_stream_configuration import BroadcastTsInputStreamConfiguration


class BroadcastTsAudioStreamConfiguration(BroadcastTsInputStreamConfiguration):

    def __init__(self, stream_id, packet_identifier=None, start_with_discontinuity_indicator=None, align_pes=None,
                 set_rai_on_au=None, use_atsc_buffer_model=None, language=None):
        super().__init__(stream_id=stream_id, packet_identifier=packet_identifier,
                         start_with_discontinuity_indicator=start_with_discontinuity_indicator,
                         align_pes=align_pes,
                         set_rai_on_au=set_rai_on_au)

        self.useATSCBufferModel = use_atsc_buffer_model
        self.language = language

    @classmethod
    def parse_from_json_object(cls, json_object):
        input_stream_configuration = super().parse_from_json_object(json_object=json_object)

        use_atsc_buffer_model = json_object.get('useATSCBufferModel')
        language = json_object.get('language')

        return BroadcastTsAudioStreamConfiguration(
            stream_id=input_stream_configuration.streamId,
            packet_identifier=input_stream_configuration.packetIdentifier,
            start_with_discontinuity_indicator=input_stream_configuration.startWithDiscontinuityIndicator,
            align_pes=input_stream_configuration.alignPes,
            set_rai_on_au=input_stream_configuration.setRaiOnAu,
            use_atsc_buffer_model=use_atsc_buffer_model,
            language=language
        )
