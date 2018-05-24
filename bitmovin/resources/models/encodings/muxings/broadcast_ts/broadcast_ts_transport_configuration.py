from bitmovin.utils import Serializable


class BroadcastTsTransportConfiguration(Serializable):

    def __init__(self, muxrate=None, stop_on_error=None, prevent_empty_adaptation_fields_in_video=None,
                 pat_repetition_rate_per_sec=None, pmt_repetition_rate_per_sec=None):
        super().__init__()
        self.muxrate = muxrate
        self.stopOnError = stop_on_error
        self.preventEmptyAdaptionFieldsInVideo = prevent_empty_adaptation_fields_in_video
        self.patRepetitionRatePerSec = pat_repetition_rate_per_sec
        self.pmtRepetitionRatePerSec = pmt_repetition_rate_per_sec

    @classmethod
    def parse_from_json_object(cls, json_object):
        muxrate = json_object.get('muxrate')
        stop_on_error = json_object.get('stopOnError')
        prevent_empty_adaptation_fields_in_video = json_object.get('preventEmptyAdaptionFieldsInVideo')
        pat_repetition_rate_per_sec = json_object.get('patRepetitionRatePerSec')
        pmt_repetition_rate_per_sec = json_object.get('pmtRepetitionRatePerSec')

        broadcast_ts_transport_configuration = BroadcastTsTransportConfiguration(
            muxrate=muxrate, stop_on_error=stop_on_error,
            prevent_empty_adaptation_fields_in_video=prevent_empty_adaptation_fields_in_video,
            pat_repetition_rate_per_sec=pat_repetition_rate_per_sec,
            pmt_repetition_rate_per_sec=pmt_repetition_rate_per_sec
        )
        return broadcast_ts_transport_configuration
