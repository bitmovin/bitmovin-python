# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.muxing import Muxing
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.stream_mode import StreamMode
from bitmovin_python.encoding.encodings.muxings.fmp4.fmp4_api import Fmp4Api
from bitmovin_python.encoding.encodings.muxings.segmentedRaw.segmented_raw_api import SegmentedRawApi
from bitmovin_python.encoding.encodings.muxings.ts.ts_api import TsApi
from bitmovin_python.encoding.encodings.muxings.webm.webm_api import WebmApi
from bitmovin_python.encoding.encodings.muxings.mp3.mp3_api import Mp3Api
from bitmovin_python.encoding.encodings.muxings.mp4.mp4_api import Mp4Api
from bitmovin_python.encoding.encodings.muxings.progressiveTs.progressive_ts_api import ProgressiveTsApi
from bitmovin_python.encoding.encodings.muxings.broadcastTs.broadcast_ts_api import BroadcastTsApi
from bitmovin_python.encoding.encodings.muxings.progressiveWebm.progressive_webm_api import ProgressiveWebmApi
from bitmovin_python.encoding.encodings.muxings.progressiveMov.progressive_mov_api import ProgressiveMovApi
from bitmovin_python.encoding.encodings.muxings.muxings_list_query_params import MuxingsListQueryParams


class MuxingsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(MuxingsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.fmp4 = Fmp4Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.segmentedRaw = SegmentedRawApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.ts = TsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.webm = WebmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.mp3 = Mp3Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.mp4 = Mp4Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.progressiveTs = ProgressiveTsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.broadcastTs = BroadcastTsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.progressiveWebm = ProgressiveWebmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.progressiveMov = ProgressiveMovApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def list(self, encoding_id, query_params: MuxingsListQueryParams = None, **kwargs):
        """List All Muxings"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Muxing,
            **kwargs
        )
