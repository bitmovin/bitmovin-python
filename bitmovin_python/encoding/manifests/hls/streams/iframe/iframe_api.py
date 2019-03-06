# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.i_frame_playlist import IFramePlaylist
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.manifests.hls.streams.iframe.i_frame_playlists_list_query_params import IFramePlaylistsListQueryParams


class IframeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(IframeApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, stream_id, i_frame_playlist=None, **kwargs):
        """Add I-frame playlist to variant stream"""

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}/iframe',
            i_frame_playlist,
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id},
            type=IFramePlaylist,
            **kwargs
        )

    def delete(self, manifest_id, stream_id, iframe_id, **kwargs):
        """Delete I-frame playlist"""

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}/iframe/{iframe_id}',
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id, 'iframe_id': iframe_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, stream_id, iframe_id, **kwargs):
        """I-frame playlist Details"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}/iframe/{iframe_id}',
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id, 'iframe_id': iframe_id},
            type=IFramePlaylist,
            **kwargs
        )

    def list(self, manifest_id, stream_id, query_params: IFramePlaylistsListQueryParams = None, **kwargs):
        """List all I-frame playlists of a variant stream"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}/iframe',
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=IFramePlaylist,
            **kwargs
        )
