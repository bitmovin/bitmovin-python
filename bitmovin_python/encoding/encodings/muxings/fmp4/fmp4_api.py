# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.fmp4_muxing import Fmp4Muxing
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.encodings.muxings.fmp4.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.muxings.fmp4.drm.drm_api import DrmApi
from bitmovin_python.encoding.encodings.muxings.fmp4.captions.captions_api import CaptionsApi
from bitmovin_python.encoding.encodings.muxings.fmp4.fmp4_muxings_list_query_params import Fmp4MuxingsListQueryParams


class Fmp4Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(Fmp4Api, self).__init__(
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

        self.drm = DrmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.captions = CaptionsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, fmp4_muxing=None, **kwargs):
        """Add fMP4 Segment Muxing"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/fmp4',
            fmp4_muxing,
            path_params={'encoding_id': encoding_id},
            type=Fmp4Muxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        """Delete fMP4 Muxing"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        """fMP4 Segment Muxing Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=Fmp4Muxing,
            **kwargs
        )

    def list(self, encoding_id, query_params: Fmp4MuxingsListQueryParams = None, **kwargs):
        """List fMP4 Segment Muxings"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Fmp4Muxing,
            **kwargs
        )
