# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.web_vtt_extract import WebVttExtract
from bitmovin_python.encoding.encodings.captions.webvtt.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.captions.webvtt.web_vtt_extracts_list_query_params import WebVttExtractsListQueryParams


class WebvttApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(WebvttApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, encoding_id, web_vtt_extract=None, **kwargs):
        """Extract WebVtt Captions"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/captions/webvtt',
            web_vtt_extract,
            path_params={'encoding_id': encoding_id},
            type=WebVttExtract,
            **kwargs
        )

    def delete(self, encoding_id, captions_id, **kwargs):
        """Delete Extract WebVtt Captions"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/captions/webvtt/{captions_id}',
            path_params={'encoding_id': encoding_id, 'captions_id': captions_id},
            type=WebVttExtract,
            **kwargs
        )

    def get(self, encoding_id, captions_id, **kwargs):
        """Get Extract WebVtt Captions Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/webvtt/{captions_id}',
            path_params={'encoding_id': encoding_id, 'captions_id': captions_id},
            type=WebVttExtract,
            **kwargs
        )

    def list(self, encoding_id, query_params: WebVttExtractsListQueryParams = None, **kwargs):
        """List Extract WebVtt Captions"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/webvtt',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=WebVttExtract,
            **kwargs
        )
