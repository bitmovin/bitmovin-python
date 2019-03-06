# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.models.widevine_drm import WidevineDrm
from bitmovin_python.encoding.encodings.muxings.mp4.drm.widevine.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.muxings.mp4.drm.widevine.widevine_drms_list_query_params import WidevineDrmsListQueryParams


class WidevineApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(WidevineApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, widevine_drm=None, **kwargs):
        """Add Widevine DRM to MP4"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/widevine',
            widevine_drm,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=WidevineDrm,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, drm_id, **kwargs):
        """Delete Widevine DRM from MP4"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/widevine/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        """Widevine DRM Details of MP4"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/widevine/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=WidevineDrm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params: WidevineDrmsListQueryParams = None, **kwargs):
        """List Widevine DRMs of MP4"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/widevine',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=WidevineDrm,
            **kwargs
        )
