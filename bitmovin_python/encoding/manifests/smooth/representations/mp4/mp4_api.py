# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.smooth_streaming_representation import SmoothStreamingRepresentation
from bitmovin_python.encoding.manifests.smooth.representations.mp4.smooth_streaming_representations_list_query_params import SmoothStreamingRepresentationsListQueryParams


class Mp4Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(Mp4Api, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, manifest_id, smooth_streaming_representation=None, **kwargs):
        """Add MP4 Representation to Smooth Streaming Manifest"""

        return self.api_client.post(
            '/encoding/manifests/smooth/{manifest_id}/representations/mp4',
            smooth_streaming_representation,
            path_params={'manifest_id': manifest_id},
            type=SmoothStreamingRepresentation,
            **kwargs
        )

    def delete(self, manifest_id, representation_id, **kwargs):
        """Delete Smooth Streaming MP4 Representation"""

        return self.api_client.delete(
            '/encoding/manifests/smooth/{manifest_id}/representations/mp4/{representation_id}',
            path_params={'manifest_id': manifest_id, 'representation_id': representation_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, representation_id, **kwargs):
        """Smooth Streaming MP4 Representation Details"""

        return self.api_client.get(
            '/encoding/manifests/smooth/{manifest_id}/representations/mp4/{representation_id}',
            path_params={'manifest_id': manifest_id, 'representation_id': representation_id},
            type=SmoothStreamingRepresentation,
            **kwargs
        )

    def list(self, manifest_id, query_params: SmoothStreamingRepresentationsListQueryParams = None, **kwargs):
        """List MP4 Representation"""

        return self.api_client.get(
            '/encoding/manifests/smooth/{manifest_id}/representations/mp4',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=SmoothStreamingRepresentation,
            **kwargs
        )
