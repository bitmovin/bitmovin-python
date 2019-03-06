# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.progressive_mov_muxing import ProgressiveMovMuxing
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.encodings.muxings.progressiveMov.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.muxings.progressiveMov.information.information_api import InformationApi
from bitmovin_python.encoding.encodings.muxings.progressiveMov.progressive_mov_muxings_list_query_params import ProgressiveMovMuxingsListQueryParams


class ProgressiveMovApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ProgressiveMovApi, self).__init__(
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

        self.information = InformationApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, progressive_mov_muxing=None, **kwargs):
        """Add Progressive MOV Muxing"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/progressive-mov',
            progressive_mov_muxing,
            path_params={'encoding_id': encoding_id},
            type=ProgressiveMovMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        """Delete Progressive MOV Muxing"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/progressive-mov/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        """Progressive MOV Muxing Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-mov/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=ProgressiveMovMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params: ProgressiveMovMuxingsListQueryParams = None, **kwargs):
        """List Progressive MOV Muxings"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-mov',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ProgressiveMovMuxing,
            **kwargs
        )
