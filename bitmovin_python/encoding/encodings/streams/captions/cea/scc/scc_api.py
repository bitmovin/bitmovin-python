# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.models.scc_caption import SccCaption
from bitmovin_python.encoding.encodings.streams.captions.cea.scc.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.streams.captions.cea.scc.scc_captions_list_query_params import SccCaptionsListQueryParams


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

    def create(self, encoding_id, stream_id, scc_caption=None, **kwargs):
        """Embed SCC captions as 608/708 into Stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/captions/608-708/scc',
            scc_caption,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=SccCaption,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, captions_id, **kwargs):
        """Delete SCC captions as 608/708 from Stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/captions/608-708/scc/{captions_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'captions_id': captions_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, captions_id, **kwargs):
        """Embed SCC captions as 608/708 Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/captions/608-708/scc/{captions_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'captions_id': captions_id},
            type=SccCaption,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params: SccCaptionsListQueryParams = None, **kwargs):
        """List SCC captions as 608/708 from Stream"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/captions/608-708/scc',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=SccCaption,
            **kwargs
        )
