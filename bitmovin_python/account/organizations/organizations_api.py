# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.organization import Organization
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.account.organizations.groups.groups_api import GroupsApi


class OrganizationsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(OrganizationsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.groups = GroupsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, organization=None, **kwargs):
        """Add Organization"""

        return self.api_client.post(
            '/account/organizations',
            organization,
            type=Organization,
            **kwargs
        )

    def delete(self, organization_id, **kwargs):
        """Delete Organization"""

        return self.api_client.delete(
            '/account/organizations/{organization_id}',
            path_params={'organization_id': organization_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, organization_id, **kwargs):
        """Organization Details"""

        return self.api_client.get(
            '/account/organizations/{organization_id}',
            path_params={'organization_id': organization_id},
            type=Organization,
            **kwargs
        )

    def list(self, **kwargs):
        """List Organizations"""

        return self.api_client.get(
            '/account/organizations',
            pagination_response=True,
            type=Organization,
            **kwargs
        )
