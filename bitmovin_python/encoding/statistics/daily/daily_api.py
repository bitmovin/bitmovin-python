# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.daily_statistics import DailyStatistics
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.statistics.daily.daily_statisticss_list_by_date_range_query_params import DailyStatisticssListByDateRangeQueryParams
from bitmovin_python.encoding.statistics.daily.daily_statisticss_list_query_params import DailyStatisticssListQueryParams


class DailyApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(DailyApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def list(self, query_params: DailyStatisticssListQueryParams = None, **kwargs):
        """List Daily Statistics"""

        return self.api_client.get(
            '/encoding/statistics/daily',
            query_params=query_params,
            pagination_response=True,
            type=DailyStatistics,
            **kwargs
        )

    def list(self, _from, to, query_params: DailyStatisticssListByDateRangeQueryParams = None, **kwargs):
        """List daily statistics within specific dates"""

        return self.api_client.get(
            '/encoding/statistics/daily/{from}/{to}',
            path_params={'_from': _from, 'to': to},
            query_params=query_params,
            pagination_response=True,
            type=DailyStatistics,
            **kwargs
        )
