# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.fair_play_drm import FairPlayDrm
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.encodings.muxings.fmp4.drm.fairplay.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.muxings.fmp4.drm.fairplay.fair_play_drms_list_query_params import FairPlayDrmsListQueryParams


class FairplayApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(FairplayApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, fair_play_drm=None, **kwargs):
        """Add FairPlay DRM to fMP4"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/fairplay',
            fair_play_drm,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=FairPlayDrm,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, drm_id, **kwargs):
        """Delete FairPlay DRM from fMP4"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/fairplay/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        """FairPlay DRM Details of fMP4"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/fairplay/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=FairPlayDrm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params: FairPlayDrmsListQueryParams = None, **kwargs):
        """List FairPlay DRMs of fMP4"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/fairplay',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=FairPlayDrm,
            **kwargs
        )
