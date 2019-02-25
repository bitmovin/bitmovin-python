# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.live_encoding import LiveEncoding
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.start_live_encoding_request import StartLiveEncodingRequest


class LiveApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(LiveApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def get(self, encoding_id, **kwargs):
        """Live Encoding Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/live',
            path_params={'encoding_id': encoding_id},
            type=LiveEncoding,
            **kwargs
        )

    def getStartRequest(self, encoding_id, **kwargs):
        """Live Encoding Start Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/live/start',
            path_params={'encoding_id': encoding_id},
            type=StartLiveEncodingRequest,
            **kwargs
        )

    def restart(self, encoding_id, **kwargs):
        """Re-Start Live Encoding"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/live/restart',
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )

    def start(self, encoding_id, start_live_encoding_request=None, **kwargs):
        """Start Live Encoding"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/live/start',
            start_live_encoding_request,
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )

    def stop(self, encoding_id, **kwargs):
        """Stop Live Encoding"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/live/stop',
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )
