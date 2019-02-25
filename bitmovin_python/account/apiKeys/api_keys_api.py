# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.account_api_key import AccountApiKey
from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope


class ApiKeysApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(ApiKeysApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, **kwargs):
        """Create Api Key"""

        return self.api_client.post(
            '/account/api-keys',
            type=AccountApiKey,
            **kwargs
        )

    def delete(self, api_key_id, **kwargs):
        """Delete Api Key"""

        return self.api_client.delete(
            '/account/api-keys/{api_key_id}',
            path_params={'api_key_id': api_key_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, api_key_id, **kwargs):
        """Get Api Key"""

        return self.api_client.get(
            '/account/api-keys/{api_key_id}',
            path_params={'api_key_id': api_key_id},
            type=AccountApiKey,
            **kwargs
        )

    def list(self, **kwargs):
        """List Api Keys"""

        return self.api_client.get(
            '/account/api-keys',
            pagination_response=True,
            type=AccountApiKey,
            **kwargs
        )
