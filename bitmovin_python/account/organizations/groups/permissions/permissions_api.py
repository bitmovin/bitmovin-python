# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.acl import Acl
from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError


class PermissionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(PermissionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, organization_id, group_id, acl=None, **kwargs):
        """Set Group Permissions"""

        return self.api_client.post(
            '/account/organizations/{organization_id}/groups/{group_id}/permissions',
            acl,
            path_params={'organization_id': organization_id, 'group_id': group_id},
            type=Acl,
            **kwargs
        )

    def delete(self, organization_id, group_id, permission_id, **kwargs):
        """Delete Permission"""

        return self.api_client.delete(
            '/account/organizations/{organization_id}/groups/{group_id}/permissions/{permission_id}',
            path_params={'organization_id': organization_id, 'group_id': group_id, 'permission_id': permission_id},
            type=BitmovinResponse,
            **kwargs
        )

    def list(self, organization_id, group_id, **kwargs):
        """Get Group Permissions"""

        return self.api_client.get(
            '/account/organizations/{organization_id}/groups/{group_id}/permissions',
            path_params={'organization_id': organization_id, 'group_id': group_id},
            pagination_response=True,
            type=Acl,
            **kwargs
        )
