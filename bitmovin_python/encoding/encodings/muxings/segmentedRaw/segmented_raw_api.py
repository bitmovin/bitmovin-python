# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.segmented_raw_muxing import SegmentedRawMuxing
from bitmovin_python.encoding.encodings.muxings.segmentedRaw.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.muxings.segmentedRaw.segmented_raw_muxings_list_query_params import SegmentedRawMuxingsListQueryParams


class SegmentedRawApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(SegmentedRawApi, self).__init__(
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

    def create(self, encoding_id, segmented_raw_muxing=None, **kwargs):
        """Add Segmented RAW Muxing"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/segmented-raw',
            segmented_raw_muxing,
            path_params={'encoding_id': encoding_id},
            type=SegmentedRawMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        """Delete Segmented RAW Muxing"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/segmented-raw/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        """Segmented RAW Muxing Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/segmented-raw/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=SegmentedRawMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params: SegmentedRawMuxingsListQueryParams = None, **kwargs):
        """List Segmented RAW Muxings"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/segmented-raw',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=SegmentedRawMuxing,
            **kwargs
        )
