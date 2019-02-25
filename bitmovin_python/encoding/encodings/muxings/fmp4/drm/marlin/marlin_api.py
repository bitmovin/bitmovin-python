# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.marlin_drm import MarlinDrm
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.encodings.muxings.fmp4.drm.marlin.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.muxings.fmp4.drm.marlin.marlin_drms_list_query_params import MarlinDrmsListQueryParams


class MarlinApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(MarlinApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, marlin_drm=None, **kwargs):
        """Add Marlin DRM to fMP4"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/marlin',
            marlin_drm,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=MarlinDrm,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, drm_id, **kwargs):
        """Delete Marlin DRM from fMP4"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/marlin/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        """Marlin DRM Details of fMP4"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/marlin/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=MarlinDrm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params: MarlinDrmsListQueryParams = None, **kwargs):
        """List Marlin DRMs of fMP4"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/marlin',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=MarlinDrm,
            **kwargs
        )
