# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.custom_tag import CustomTag
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.manifests.hls.streams.customTag.custom_tags_list_query_params import CustomTagsListQueryParams


class CustomTagApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(CustomTagApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, stream_id, custom_tag=None, **kwargs):
        """Add Custom Tag to Variant Stream"""

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}/custom-tag',
            custom_tag,
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id},
            type=CustomTag,
            **kwargs
        )

    def delete(self, manifest_id, stream_id, custom_tag_id, **kwargs):
        """Delete Custom Tag"""

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}/custom-tag/{custom_tag_id}',
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id, 'custom_tag_id': custom_tag_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, stream_id, custom_tag_id, **kwargs):
        """Custom Tag Details"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}/custom-tag/{custom_tag_id}',
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id, 'custom_tag_id': custom_tag_id},
            type=CustomTag,
            **kwargs
        )

    def list(self, manifest_id, stream_id, query_params: CustomTagsListQueryParams = None, **kwargs):
        """List all Custom Tags of a Variant Stream"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}/custom-tag',
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=CustomTag,
            **kwargs
        )
