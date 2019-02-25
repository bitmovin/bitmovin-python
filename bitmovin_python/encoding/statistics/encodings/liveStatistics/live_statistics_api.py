# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.live_encoding_stats import LiveEncodingStats
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.statistics.encodings.liveStatistics.events.events_api import EventsApi
from bitmovin_python.encoding.statistics.encodings.liveStatistics.streams.streams_api import StreamsApi


class LiveStatisticsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(LiveStatisticsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.events = EventsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.streams = StreamsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def get(self, encoding_id, **kwargs):
        """List Live Statistics from an Encoding"""

        return self.api_client.get(
            '/encoding/statistics/encodings/{encoding_id}/live-statistics',
            path_params={'encoding_id': encoding_id},
            type=LiveEncodingStats,
            **kwargs
        )
