from bitmovin.errors import InvalidTypeError
from .broadcast_ts_muxing_configuration import BroadcastTsMuxingConfiguration
from ..muxing import Muxing


class BroadcastTsMuxing(Muxing):

    def __init__(self, streams, segment_length, filename=None, configuration=None, outputs=None,
                 id_=None, custom_data=None, name=None, description=None, avg_bitrate=None, max_bitrate=None,
                 min_bitrate=None, ignored_by=None):

        super().__init__(id_=id_, custom_data=custom_data, streams=streams, outputs=outputs,
                         name=name, description=description, avg_bitrate=avg_bitrate, max_bitrate=max_bitrate,
                         min_bitrate=min_bitrate, ignored_by=ignored_by)

        self.segmentLength = segment_length
        self.filename = filename
        self._configuration = None
        self.configuration = configuration

    @property
    def configuration(self):
        return self._configuration

    @configuration.setter
    def configuration(self, new_configuration):
        if new_configuration is None:
            self._configuration = None
            return
        if isinstance(new_configuration, BroadcastTsMuxingConfiguration):
            self._configuration = new_configuration
        else:
            raise InvalidTypeError(
                'Invalid type {} for configuration: must be BroadcastTsMuxingConfiguration!'.format(
                    type(new_configuration)
                )
            )

    def serialize(self):
        serialized = super().serialize()
        serialized['configuration'] = self.configuration
        return serialized

    @classmethod
    def parse_from_json_object(cls, json_object):
        muxing = super().parse_from_json_object(json_object)

        filename = json_object['filename']

        segment_length = json_object.get('segmentLength')
        configuration_json = json_object.get('configuration')
        configuration = BroadcastTsMuxingConfiguration.parse_from_json_object(configuration_json)

        return BroadcastTsMuxing(
            filename=filename, configuration=configuration, segment_length=segment_length, outputs=muxing.outputs,
            id_=muxing.id, custom_data=muxing.customData, streams=muxing.streams, name=muxing.name,
            description=muxing.description, avg_bitrate=muxing.avgBitrate, max_bitrate=muxing.maxBitrate,
            min_bitrate=muxing.minBitrate, ignored_by=muxing.ignored_by
        )
