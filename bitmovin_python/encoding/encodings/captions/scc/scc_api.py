# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.convert_scc_caption import ConvertSccCaption
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.encodings.captions.scc.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.captions.scc.convert_scc_captions_list_query_params import ConvertSccCaptionsListQueryParams


class SccApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(SccApi, self).__init__(
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

    def create(self, encoding_id, convert_scc_caption=None, **kwargs):
        """Convert SCC captions"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/captions/scc',
            convert_scc_caption,
            path_params={'encoding_id': encoding_id},
            type=ConvertSccCaption,
            **kwargs
        )

    def delete(self, encoding_id, captions_id, **kwargs):
        """Delete Convert SCC captions"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/captions/scc/{captions_id}',
            path_params={'encoding_id': encoding_id, 'captions_id': captions_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, captions_id, **kwargs):
        """Convert SCC captions Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/scc/{captions_id}',
            path_params={'encoding_id': encoding_id, 'captions_id': captions_id},
            type=ConvertSccCaption,
            **kwargs
        )

    def list(self, encoding_id, query_params: ConvertSccCaptionsListQueryParams = None, **kwargs):
        """List Convert SCC captions"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/scc',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ConvertSccCaption,
            **kwargs
        )
