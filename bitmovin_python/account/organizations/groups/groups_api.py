# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.group import Group
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.account.organizations.groups.tenants.tenants_api import TenantsApi
from bitmovin_python.account.organizations.groups.permissions.permissions_api import PermissionsApi


class GroupsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(GroupsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.tenants = TenantsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.permissions = PermissionsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, organization_id, group=None, **kwargs):
        """Add Group"""

        return self.api_client.post(
            '/account/organizations/{organization_id}/groups',
            group,
            path_params={'organization_id': organization_id},
            type=Group,
            **kwargs
        )

    def delete(self, organization_id, group_id, **kwargs):
        """Delete Group"""

        return self.api_client.delete(
            '/account/organizations/{organization_id}/groups/{group_id}',
            path_params={'organization_id': organization_id, 'group_id': group_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, organization_id, group_id, **kwargs):
        """Group Details"""

        return self.api_client.get(
            '/account/organizations/{organization_id}/groups/{group_id}',
            path_params={'organization_id': organization_id, 'group_id': group_id},
            type=Group,
            **kwargs
        )

    def list(self, organization_id, **kwargs):
        """List Groups"""

        return self.api_client.get(
            '/account/organizations/{organization_id}/groups',
            path_params={'organization_id': organization_id},
            pagination_response=True,
            type=Group,
            **kwargs
        )
