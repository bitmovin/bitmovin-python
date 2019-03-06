# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.encoding_stats import EncodingStats
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.statistics.encodings.live.live_api import LiveApi
from bitmovin_python.encoding.statistics.encodings.vod.vod_api import VodApi
from bitmovin_python.encoding.statistics.encodings.liveStatistics.live_statistics_api import LiveStatisticsApi


class EncodingsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(EncodingsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.live = LiveApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.vod = VodApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.liveStatistics = LiveStatisticsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, **kwargs):
        """Get Statistics from an Encoding"""

        return self.api_client.get(
            '/encoding/statistics/encodings/{encoding_id}',
            path_params={'encoding_id': encoding_id},
            type=EncodingStats,
            **kwargs
        )
