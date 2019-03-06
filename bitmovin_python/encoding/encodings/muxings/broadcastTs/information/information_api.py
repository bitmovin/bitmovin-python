# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.broadcast_ts_muxing_information import BroadcastTsMuxingInformation
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError


class InformationApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(InformationApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        """Broadcast TS Muxing Information"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/broadcast-ts/{muxing_id}/information',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BroadcastTsMuxingInformation,
            **kwargs
        )
