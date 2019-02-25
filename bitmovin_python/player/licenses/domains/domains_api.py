# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.domain import Domain
from bitmovin_python.models.response_envelope import ResponseEnvelope


class DomainsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(DomainsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, license_id, domain=None, **kwargs):
        """Add Domain"""

        return self.api_client.post(
            '/player/licenses/{license_id}/domains',
            domain,
            path_params={'license_id': license_id},
            type=Domain,
            **kwargs
        )

    def delete(self, license_id, domain_id, **kwargs):
        """Delete Domain"""

        return self.api_client.delete(
            '/player/licenses/{license_id}/domains/{domain_id}',
            path_params={'license_id': license_id, 'domain_id': domain_id},
            type=BitmovinResponse,
            **kwargs
        )

    def list(self, license_id, **kwargs):
        """List allowed Domains for Player License"""

        return self.api_client.get(
            '/player/licenses/{license_id}/domains',
            path_params={'license_id': license_id},
            pagination_response=True,
            type=Domain,
            **kwargs
        )
