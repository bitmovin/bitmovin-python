# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.analytics_query_request import AnalyticsQueryRequest
from bitmovin_python.models.analytics_response import AnalyticsResponse
from bitmovin_python.models.analytics_sum_query_request import AnalyticsSumQueryRequest
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError


class SumApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(SumApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, analytics_sum_query_request=None, **kwargs):
        """Sum"""

        return self.api_client.post(
            '/analytics/queries/sum',
            analytics_sum_query_request,
            type=AnalyticsResponse,
            **kwargs
        )
