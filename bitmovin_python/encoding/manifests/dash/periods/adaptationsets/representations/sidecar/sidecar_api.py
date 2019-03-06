# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.dash_sidecar_representation import DashSidecarRepresentation
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.representations.sidecar.dash_sidecar_representations_list_query_params import DashSidecarRepresentationsListQueryParams


class SidecarApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(SidecarApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, period_id, adaptationset_id, dash_sidecar_representation=None, **kwargs):
        """Add Sidecar Representation"""

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/sidecar',
            dash_sidecar_representation,
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=DashSidecarRepresentation,
            **kwargs
        )

    def delete(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        """Delete Sidecar Representation"""

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/sidecar/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        """Sidecar Representation Details"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/sidecar/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=DashSidecarRepresentation,
            **kwargs
        )

    def list(self, manifest_id, period_id, adaptationset_id, query_params: DashSidecarRepresentationsListQueryParams = None, **kwargs):
        """List all Sidecar Representations"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/sidecar',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            query_params=query_params,
            pagination_response=True,
            type=DashSidecarRepresentation,
            **kwargs
        )
