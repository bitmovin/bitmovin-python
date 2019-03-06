# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.encoding_statistics_live import EncodingStatisticsLive
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.statistics.encodings.live.encoding_statistics_lives_list_by_date_range_query_params import EncodingStatisticsLivesListByDateRangeQueryParams
from bitmovin_python.encoding.statistics.encodings.live.encoding_statistics_lives_list_query_params import EncodingStatisticsLivesListQueryParams


class LiveApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(LiveApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params: EncodingStatisticsLivesListQueryParams = None, **kwargs):
        """List Live Encoding Statistics"""

        return self.api_client.get(
            '/encoding/statistics/encodings/live',
            query_params=query_params,
            pagination_response=True,
            type=EncodingStatisticsLive,
            **kwargs
        )

    def list(self, _from, to, query_params: EncodingStatisticsLivesListByDateRangeQueryParams = None, **kwargs):
        """List live encoding statistics within specific dates"""

        return self.api_client.get(
            '/encoding/statistics/encodings/live/{from}/{to}',
            path_params={'_from': _from, 'to': to},
            query_params=query_params,
            pagination_response=True,
            type=EncodingStatisticsLive,
            **kwargs
        )
