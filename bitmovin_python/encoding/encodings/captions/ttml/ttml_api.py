# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.ttml_extract import TtmlExtract
from bitmovin_python.encoding.encodings.captions.ttml.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.captions.ttml.ttml_extracts_list_query_params import TtmlExtractsListQueryParams


class TtmlApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(TtmlApi, self).__init__(
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

    def create(self, encoding_id, ttml_extract=None, **kwargs):
        """Extract TTML Captions"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/captions/ttml',
            ttml_extract,
            path_params={'encoding_id': encoding_id},
            type=TtmlExtract,
            **kwargs
        )

    def delete(self, encoding_id, captions_id, **kwargs):
        """Delete TTML Extract Captions"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/captions/ttml/{captions_id}',
            path_params={'encoding_id': encoding_id, 'captions_id': captions_id},
            type=TtmlExtract,
            **kwargs
        )

    def get(self, encoding_id, captions_id, **kwargs):
        """TTML Extract Captions Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/ttml/{captions_id}',
            path_params={'encoding_id': encoding_id, 'captions_id': captions_id},
            type=TtmlExtract,
            **kwargs
        )

    def list(self, encoding_id, query_params: TtmlExtractsListQueryParams = None, **kwargs):
        """List TTML Extract Captions"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/ttml',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=TtmlExtract,
            **kwargs
        )
