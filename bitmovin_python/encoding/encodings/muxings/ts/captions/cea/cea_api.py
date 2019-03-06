# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.captions_embed_cea import CaptionsEmbedCea
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.encodings.muxings.ts.captions.cea.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.muxings.ts.captions.cea.captions_embed_ceas_list_query_params import CaptionsEmbedCeasListQueryParams


class CeaApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(CeaApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, captions_embed_cea=None, **kwargs):
        """TS Embed CEA 608/708 Captions"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/captions/cea',
            captions_embed_cea,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=CaptionsEmbedCea,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, captions_id, **kwargs):
        """Delete Embedded CEA 608/708 Captions"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/captions/cea/{captions_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'captions_id': captions_id},
            type=CaptionsEmbedCea,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, captions_id, **kwargs):
        """Embedded CEA 608/708 Captions Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/captions/cea/{captions_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'captions_id': captions_id},
            type=CaptionsEmbedCea,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params: CaptionsEmbedCeasListQueryParams = None, **kwargs):
        """List TS Embedded CEA 608/708 Captions"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/captions/cea',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=CaptionsEmbedCea,
            **kwargs
        )
