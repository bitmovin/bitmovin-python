# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.player_license import PlayerLicense
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.player.licenses.domains.domains_api import DomainsApi
from bitmovin_python.player.licenses.thirdPartyLicensing.third_party_licensing_api import ThirdPartyLicensingApi
from bitmovin_python.player.licenses.player_licenses_list_query_params import PlayerLicensesListQueryParams


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

        self.thirdPartyLicensing = ThirdPartyLicensingApi(
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
            '/player/licenses/{license_id}',
            path_params={'license_id': license_id},
            type=PlayerLicense,
            **kwargs
        )

    def list(self, query_params: PlayerLicensesListQueryParams = None, **kwargs):
        """List Player Licenses"""

        return self.api_client.get(
            '/player/licenses',
            query_params=query_params,
            pagination_response=True,
            type=PlayerLicense,
            **kwargs
        )
