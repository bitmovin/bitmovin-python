# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.burn_in_subtitle_srt import BurnInSubtitleSrt
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.encodings.streams.burnInSubtitles.srt.burn_in_subtitle_srts_list_query_params import BurnInSubtitleSrtsListQueryParams


class SrtApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(SrtApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, stream_id, burn_in_subtitle_srt=None, **kwargs):
        """Burn-In SRT Subtitle into Stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/burn-in-subtitles/srt',
            burn_in_subtitle_srt,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=BurnInSubtitleSrt,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, subtitle_id, **kwargs):
        """Delete Burn-In SRT Subtitle from Stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/burn-in-subtitles/srt/{subtitle_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'subtitle_id': subtitle_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, subtitle_id, **kwargs):
        """Get Burn-In SRT Subtitle Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/burn-in-subtitles/srt/{subtitle_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'subtitle_id': subtitle_id},
            type=BurnInSubtitleSrt,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params: BurnInSubtitleSrtsListQueryParams = None, **kwargs):
        """List the Burn-In SRT subtitles of a stream"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/burn-in-subtitles/srt',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=BurnInSubtitleSrt,
            **kwargs
        )
