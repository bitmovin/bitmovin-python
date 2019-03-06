# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.keyframe import Keyframe
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.encodings.keyframes.keyframes_list_query_params import KeyframesListQueryParams


class KeyframesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(KeyframesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, keyframe=None, **kwargs):
        """Create Keyframes"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/keyframes',
            keyframe,
            path_params={'encoding_id': encoding_id},
            type=Keyframe,
            **kwargs
        )

    def delete(self, encoding_id, keyframe_id, **kwargs):
        """Delete Keyframe"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/keyframes/{keyframe_id}',
            path_params={'encoding_id': encoding_id, 'keyframe_id': keyframe_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, keyframe_id, **kwargs):
        """Keyframe Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/keyframes/{keyframe_id}',
            path_params={'encoding_id': encoding_id, 'keyframe_id': keyframe_id},
            type=Keyframe,
            **kwargs
        )

    def list(self, encoding_id, query_params: KeyframesListQueryParams = None, **kwargs):
        """List all Keyframes"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/keyframes',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Keyframe,
            **kwargs
        )
