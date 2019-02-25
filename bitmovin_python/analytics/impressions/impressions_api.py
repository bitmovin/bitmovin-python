# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.analytics_impression_details import AnalyticsImpressionDetails
from bitmovin_python.models.analytics_license import AnalyticsLicense
from bitmovin_python.models.response_envelope import ResponseEnvelope


class ImpressionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(ImpressionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, impression_id, analytics_license=None, **kwargs):
        """Impression Details"""

        return self.api_client.post(
            '/analytics/impressions/{impression_id}',
            analytics_license,
            path_params={'impression_id': impression_id},
            type=AnalyticsImpressionDetails,
            **kwargs
        )
