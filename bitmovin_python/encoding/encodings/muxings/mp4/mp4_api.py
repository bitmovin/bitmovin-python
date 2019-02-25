# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.mp4_muxing import Mp4Muxing
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.encodings.muxings.mp4.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.muxings.mp4.information.information_api import InformationApi
from bitmovin_python.encoding.encodings.muxings.mp4.drm.drm_api import DrmApi
from bitmovin_python.encoding.encodings.muxings.mp4.mp4_muxings_list_query_params import Mp4MuxingsListQueryParams


class Mp4Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(Mp4Api, self).__init__(
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

        self.information = InformationApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.drm = DrmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, encoding_id, mp4_muxing=None, **kwargs):
        """Add MP4 Muxing"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/mp4',
            mp4_muxing,
            path_params={'encoding_id': encoding_id},
            type=Mp4Muxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        """Delete MP4 Muxing"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        """MP4 Segment Muxing Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=Mp4Muxing,
            **kwargs
        )

    def list(self, encoding_id, query_params: Mp4MuxingsListQueryParams = None, **kwargs):
        """List MP4 Muxings"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mp4',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Mp4Muxing,
            **kwargs
        )
