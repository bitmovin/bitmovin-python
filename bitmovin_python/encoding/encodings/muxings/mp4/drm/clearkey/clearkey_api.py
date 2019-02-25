# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.clear_key_drm import ClearKeyDrm
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.encodings.muxings.mp4.drm.clearkey.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.muxings.mp4.drm.clearkey.clear_key_drms_list_query_params import ClearKeyDrmsListQueryParams


class ClearkeyApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(ClearkeyApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, clear_key_drm=None, **kwargs):
        """Add ClearKey DRM to MP4"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/clearkey',
            clear_key_drm,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=ClearKeyDrm,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, drm_id, **kwargs):
        """Delete ClearKey DRM from MP4"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/clearkey/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        """ClearKey DRM Details of MP4"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/clearkey/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=ClearKeyDrm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params: ClearKeyDrmsListQueryParams = None, **kwargs):
        """List ClearKey DRMs of MP4"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/clearkey',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=ClearKeyDrm,
            **kwargs
        )
