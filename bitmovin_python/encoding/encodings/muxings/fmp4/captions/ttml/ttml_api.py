# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.models.ttml_embed import TtmlEmbed
from bitmovin_python.encoding.encodings.muxings.fmp4.captions.ttml.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.muxings.fmp4.captions.ttml.ttml_embeds_list_query_params import TtmlEmbedsListQueryParams


class TtmlApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(TtmlApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, muxing_id, ttml_embed=None, **kwargs):
        """FMP4 Embed TTML Captions"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/captions/ttml',
            ttml_embed,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=TtmlEmbed,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, captions_id, **kwargs):
        """Delete TTML Embed Captions"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/captions/ttml/{captions_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'captions_id': captions_id},
            type=TtmlEmbed,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, captions_id, **kwargs):
        """TTML Embed Captions Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/captions/ttml/{captions_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'captions_id': captions_id},
            type=TtmlEmbed,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params: TtmlEmbedsListQueryParams = None, **kwargs):
        """List TTML Embed Captions"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/captions/ttml',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=TtmlEmbed,
            **kwargs
        )
