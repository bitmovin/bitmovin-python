# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.cloud_region import CloudRegion
from bitmovin_python.models.encoding import Encoding
from bitmovin_python.models.reprioritize_encoding_request import ReprioritizeEncodingRequest
from bitmovin_python.models.reschedule_encoding_request import RescheduleEncodingRequest
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.start_encoding_request import StartEncodingRequest
from bitmovin_python.models.task import Task
from bitmovin_python.encoding.encodings.live.live_api import LiveApi
from bitmovin_python.encoding.encodings.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.streams.streams_api import StreamsApi
from bitmovin_python.encoding.encodings.inputStreams.input_streams_api import InputStreamsApi
from bitmovin_python.encoding.encodings.muxings.muxings_api import MuxingsApi
from bitmovin_python.encoding.encodings.subtitles.subtitles_api import SubtitlesApi
from bitmovin_python.encoding.encodings.captions.captions_api import CaptionsApi
from bitmovin_python.encoding.encodings.sidecars.sidecars_api import SidecarsApi
from bitmovin_python.encoding.encodings.keyframes.keyframes_api import KeyframesApi
from bitmovin_python.encoding.encodings.encodings_list_query_params import EncodingsListQueryParams


class EncodingsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(EncodingsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.live = LiveApi(
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

        self.streams = StreamsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.inputStreams = InputStreamsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.muxings = MuxingsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.subtitles = SubtitlesApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.captions = CaptionsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.sidecars = SidecarsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.keyframes = KeyframesApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, encoding=None, **kwargs):
        """Create Encoding"""

        return self.api_client.post(
            '/encoding/encodings',
            encoding,
            type=Encoding,
            **kwargs
        )

    def delete(self, encoding_id, **kwargs):
        """Delete Encoding"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}',
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, **kwargs):
        """Encoding Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}',
            path_params={'encoding_id': encoding_id},
            type=Encoding,
            **kwargs
        )

    def getStartRequest(self, encoding_id, **kwargs):
        """Encoding Start Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/start',
            path_params={'encoding_id': encoding_id},
            type=StartEncodingRequest,
            **kwargs
        )

    def list(self, query_params: EncodingsListQueryParams = None, **kwargs):
        """List all Encodings"""

        return self.api_client.get(
            '/encoding/encodings',
            query_params=query_params,
            pagination_response=True,
            type=Encoding,
            **kwargs
        )

    def reprioritize(self, encoding_id, reprioritize_encoding_request=None, **kwargs):
        """Reprioritize Encoding"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/reprioritize',
            reprioritize_encoding_request,
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )

    def reschedule(self, encoding_id, reschedule_encoding_request=None, **kwargs):
        """Reschedule Encoding"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/reschedule',
            reschedule_encoding_request,
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )

    def start(self, encoding_id, start_encoding_request=None, **kwargs):
        """Start Encoding"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/start',
            start_encoding_request,
            path_params={'encoding_id': encoding_id},
            type=StartEncodingRequest,
            **kwargs
        )

    def status(self, encoding_id, **kwargs):
        """Encoding Status"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/status',
            path_params={'encoding_id': encoding_id},
            type=Task,
            **kwargs
        )

    def stop(self, encoding_id, **kwargs):
        """Stop Encoding"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/stop',
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )
