# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.aes_encryption_drm import AesEncryptionDrm
from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.encodings.muxings.ts.drm.aes.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.muxings.ts.drm.aes.aes_encryption_drms_list_query_params import AesEncryptionDrmsListQueryParams


class AesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(AesApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, aes_encryption_drm=None, **kwargs):
        """Add AES Encryption to TS Segment"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/drm/aes',
            aes_encryption_drm,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=AesEncryptionDrm,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, drm_id, **kwargs):
        """Delete AES Encryption from TS Segment"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/drm/aes/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        """AES Encryption Details of TS Segment"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/drm/aes/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=AesEncryptionDrm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params: AesEncryptionDrmsListQueryParams = None, **kwargs):
        """List AES Encryption of TS Segment"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/drm/aes',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=AesEncryptionDrm,
            **kwargs
        )
