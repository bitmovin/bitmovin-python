# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.analytics_license import AnalyticsLicense
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.analytics.licenses.domains.domains_api import DomainsApi


class LicensesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(LicensesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.domains = DomainsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def get(self, license_id, **kwargs):
        """Get License"""

        return self.api_client.get(
            '/analytics/licenses/{license_id}',
            path_params={'license_id': license_id},
            type=AnalyticsLicense,
            **kwargs
        )

    def list(self, **kwargs):
        """List Analytics Licenses"""

        return self.api_client.get(
            '/analytics/licenses',
            pagination_response=True,
            type=AnalyticsLicense,
            **kwargs
        )
