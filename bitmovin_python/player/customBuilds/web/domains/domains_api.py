# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.custom_web_player_build_domain import CustomWebPlayerBuildDomain
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError


class DomainsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DomainsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, custom_web_player_build_domain=None, **kwargs):
        """Add Domain"""

        return self.api_client.post(
            '/player/custom-builds/web/domains',
            custom_web_player_build_domain,
            type=CustomWebPlayerBuildDomain,
            **kwargs
        )

    def delete(self, domain_id, **kwargs):
        """Delete Domain"""

        return self.api_client.delete(
            '/player/custom-builds/web/domains/{domain_id}',
            path_params={'domain_id': domain_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, domain_id, **kwargs):
        """Get Domain Details"""

        return self.api_client.get(
            '/player/custom-builds/web/domains/{domain_id}',
            path_params={'domain_id': domain_id},
            type=CustomWebPlayerBuildDomain,
            **kwargs
        )

    def list(self, **kwargs):
        """List Domain Details"""

        return self.api_client.get(
            '/player/custom-builds/web/domains',
            pagination_response=True,
            type=CustomWebPlayerBuildDomain,
            **kwargs
        )
