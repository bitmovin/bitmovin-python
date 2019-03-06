# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.progressive_ts_muxing import ProgressiveTsMuxing
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.encodings.muxings.progressiveTs.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.muxings.progressiveTs.information.information_api import InformationApi
from bitmovin_python.encoding.encodings.muxings.progressiveTs.id3.id3_api import Id3Api
from bitmovin_python.encoding.encodings.muxings.progressiveTs.drm.drm_api import DrmApi
from bitmovin_python.encoding.encodings.muxings.progressiveTs.progressive_ts_muxings_list_query_params import ProgressiveTsMuxingsListQueryParams


class ProgressiveTsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ProgressiveTsApi, self).__init__(
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

        self.id3 = Id3Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.drm = DrmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, progressive_ts_muxing=None, **kwargs):
        """Add Progressive TS Muxing"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts',
            progressive_ts_muxing,
            path_params={'encoding_id': encoding_id},
            type=ProgressiveTsMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        """Delete Progressive TS Muxing"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        """Progressive TS Muxing Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=ProgressiveTsMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params: ProgressiveTsMuxingsListQueryParams = None, **kwargs):
        """List Progressive TS Muxings"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ProgressiveTsMuxing,
            **kwargs
        )
