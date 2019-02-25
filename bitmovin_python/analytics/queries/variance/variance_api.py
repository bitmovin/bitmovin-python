# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.analytics_query_request import AnalyticsQueryRequest
from bitmovin_python.models.analytics_response import AnalyticsResponse
from bitmovin_python.models.analytics_variance_query_request import AnalyticsVarianceQueryRequest
from bitmovin_python.models.response_envelope import ResponseEnvelope


class VarianceApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(VarianceApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, analytics_variance_query_request=None, **kwargs):
        """Variance"""

        return self.api_client.post(
            '/analytics/queries/variance',
            analytics_variance_query_request,
            type=AnalyticsResponse,
            **kwargs
        )
