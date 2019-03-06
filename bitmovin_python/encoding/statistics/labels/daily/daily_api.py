# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.daily_statistics_per_label import DailyStatisticsPerLabel
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.statistics.labels.daily.daily_statistics_per_labels_list_query_params import DailyStatisticsPerLabelsListQueryParams
from bitmovin_python.encoding.statistics.labels.daily.daily_statistics_per_labels_list_by_date_range_query_params import DailyStatisticsPerLabelsListByDateRangeQueryParams


class DailyApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DailyApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params: DailyStatisticsPerLabelsListQueryParams = None, **kwargs):
        """Get Daily Statistics per Label"""

        return self.api_client.get(
            '/encoding/statistics/labels/daily',
            query_params=query_params,
            pagination_response=True,
            type=DailyStatisticsPerLabel,
            **kwargs
        )

    def list(self, _from, to, query_params: DailyStatisticsPerLabelsListByDateRangeQueryParams = None, **kwargs):
        """Get daily statistics per label within specific dates"""

        return self.api_client.get(
            '/encoding/statistics/labels/daily/{from}/{to}',
            path_params={'_from': _from, 'to': to},
            query_params=query_params,
            pagination_response=True,
            type=DailyStatisticsPerLabel,
            **kwargs
        )
