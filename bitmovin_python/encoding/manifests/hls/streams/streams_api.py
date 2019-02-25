# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.stream_info import StreamInfo
from bitmovin_python.encoding.manifests.hls.streams.customTag.custom_tag_api import CustomTagApi
from bitmovin_python.encoding.manifests.hls.streams.iframe.iframe_api import IframeApi
from bitmovin_python.encoding.manifests.hls.streams.stream_infos_list_query_params import StreamInfosListQueryParams


class StreamsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(StreamsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.customTag = CustomTagApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.iframe = IframeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, manifest_id, stream_info=None, **kwargs):
        """Add Variant Stream"""

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/streams',
            stream_info,
            path_params={'manifest_id': manifest_id},
            type=StreamInfo,
            **kwargs
        )

    def delete(self, manifest_id, stream_id, **kwargs):
        """Delete Variant Stream"""

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}',
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, stream_id, **kwargs):
        """Variant Stream Details"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}',
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id},
            type=StreamInfo,
            **kwargs
        )

    def list(self, manifest_id, query_params: StreamInfosListQueryParams = None, **kwargs):
        """List all Variant Streams"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/streams',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=StreamInfo,
            **kwargs
        )
