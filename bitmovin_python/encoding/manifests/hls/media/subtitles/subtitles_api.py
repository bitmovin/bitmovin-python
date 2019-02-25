# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.subtitles_media_info import SubtitlesMediaInfo
from bitmovin_python.encoding.manifests.hls.media.subtitles.subtitles_media_infos_list_query_params import SubtitlesMediaInfosListQueryParams


class SubtitlesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(SubtitlesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, manifest_id, subtitles_media_info=None, **kwargs):
        """Add Subtitles Media"""

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/media/subtitles',
            subtitles_media_info,
            path_params={'manifest_id': manifest_id},
            type=SubtitlesMediaInfo,
            **kwargs
        )

    def delete(self, manifest_id, media_id, **kwargs):
        """Delete Subtitles Media"""

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/media/subtitles/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, media_id, **kwargs):
        """Subtitles Media Details"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/subtitles/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=SubtitlesMediaInfo,
            **kwargs
        )

    def list(self, manifest_id, query_params: SubtitlesMediaInfosListQueryParams = None, **kwargs):
        """List all Subtitles Media"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/subtitles',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=SubtitlesMediaInfo,
            **kwargs
        )
