# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.statistics import Statistics
from bitmovin_python.encoding.statistics.daily.daily_api import DailyApi
from bitmovin_python.encoding.statistics.encodings.encodings_api import EncodingsApi
from bitmovin_python.encoding.statistics.labels.labels_api import LabelsApi
from bitmovin_python.encoding.statistics.statisticss_list_query_params import StatisticssListQueryParams


class StatisticsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(StatisticsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.daily = DailyApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.encodings = EncodingsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.labels = LabelsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def get(self, **kwargs):
        """Show Overall Statistics"""

        return self.api_client.get(
            '/encoding/statistics',
            type=Statistics,
            **kwargs
        )

    def list(self, _from, to, query_params: StatisticssListQueryParams = None, **kwargs):
        """Show Overall Statistics Within Specific Dates"""

        return self.api_client.get(
            '/encoding/statistics/{from}/{to}',
            path_params={'_from': _from, 'to': to},
            query_params=query_params,
            pagination_response=True,
            type=Statistics,
            **kwargs
        )
