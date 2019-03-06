# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.dash_mp4_representation import DashMp4Representation
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.representations.mp4.drm.drm_api import DrmApi
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.representations.mp4.dash_mp4_representations_list_query_params import DashMp4RepresentationsListQueryParams


class Mp4Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(Mp4Api, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.drm = DrmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, period_id, adaptationset_id, dash_mp4_representation=None, **kwargs):
        """Add MP4 Representation"""

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/mp4',
            dash_mp4_representation,
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=DashMp4Representation,
            **kwargs
        )

    def delete(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        """Delete MP4 Representation"""

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/mp4/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        """MP4 Representation Details"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/mp4/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=DashMp4Representation,
            **kwargs
        )

    def list(self, manifest_id, period_id, adaptationset_id, query_params: DashMp4RepresentationsListQueryParams = None, **kwargs):
        """List all MP4 Representations"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/mp4',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            query_params=query_params,
            pagination_response=True,
            type=DashMp4Representation,
            **kwargs
        )
